from django.shortcuts import get_object_or_404, redirect, render
from .models import UserReport, Tag, ScamRecord
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from django.utils.dateparse import parse_date
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.db.models import Count

from django.core.paginator import Paginator #데이터테이블 페이징 home참조

def index(request):
    return HttpResponse("Hello, world. This is the reports index.")

def home_view(request):
    user_reports = UserReport.objects.annotate(scam_report_count=Count('scam_records')).order_by('-scam_report_count')
    paginator = Paginator(user_reports, 5)  # 페이지당 5개의 아이템을 보여줍니다.
    
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'home.html', {'page_obj': page_obj})

def search_results(request):
    query = request.GET.get('query', '')
    if query:
        results = UserReport.objects.filter(nickname__icontains=query).prefetch_related('scam_records', 'tags')
    else:
        results = UserReport.objects.none()
    return render(request, 'search_results.html', {'results': results})

def scam_records(request, user_id):
    user = get_object_or_404(UserReport, pk=user_id)
    scam_records = user.scam_records.all()
    return render(request, 'scam_records.html', {'user': user, 'scam_records': scam_records})


def ranking(request):
    ranking_list = UserReport.objects.order_by('-report_count')[:10] # 상위 10명
    return render(request, 'ranking.html', {'ranking_list': ranking_list})

@require_POST  # POST 요청만 허용
def report_user(request):
    if request.method == 'POST':
        # 폼 데이터 수집
        nickname = request.POST.get('nickname')
        discord_nickname = request.POST.get('discord_nickname', '')
        report_date = request.POST.get('report_date')
        scam_detail = request.POST.get('scam_detail', '')

        # UserReport 인스턴스 생성 및 저장
        user_report = UserReport.objects.create(
            nickname=nickname,
            discord_nickname=discord_nickname,
            report_date=report_date,
            scam_detail=scam_detail
        )

        # 선택된 단일 태그 처리
        selected_tag_name = request.POST.get('selectedTag')
        if selected_tag_name:
            tag, created = Tag.objects.get_or_create(name=selected_tag_name)
            user_report.tags.add(tag)

        return JsonResponse({'message': '신고가 성공적으로 접수되었습니다.'})


@require_http_methods(["GET", "POST"])
def report(request):
    if request.method == "POST":
        nickname = request.POST.get('nickname')
        discord_nickname = request.POST.get('discord_nickname', '')  
        report_date = request.POST.get('report_date')
        scam_detail = request.POST.get('scam_detail', '')  
        selected_tag = request.POST.get('selectedTag')  
        level = int(request.POST.get('level', 1))
        job = request.POST.get('job', '')

        # UserReport 인스턴스 조회 또는 생성
        user_report, created = UserReport.objects.get_or_create(
            nickname=nickname,
            defaults={
                'discord_nickname': discord_nickname,
                'level': level,
                'job': job,
                'report_date': report_date,
            }
        )

        if not created:
            # Update the existing user report if it already exists
            user_report.discord_nickname = discord_nickname
            user_report.level = level
            user_report.job = job
            user_report.report_date = report_date
            user_report.save()
            message = '신고된 유저가 존재합니다. 데이터를 업데이트하였습니다.'
        else:
            message = '신고가 성공적으로 접수되었습니다.'

        # Handle tags for both new and existing reports
        if selected_tag:
            tag, _ = Tag.objects.get_or_create(name=selected_tag.strip())
            user_report.tags.add(tag)

        # ScamRecord 인스턴스 생성, 여기서 nickname 대신 user_report 사용
        ScamRecord.objects.create(
            user_report=user_report,  # 수정: user_report 인스턴스를 참조하도록 변경
            scam_detail=scam_detail,
            report_date=report_date if report_date else None  # 날짜 유효성 검사 추가
        )

        return JsonResponse({'message': message})
    else:
        # Render the form with job choices
        return render(request, 'report.html', {'job_choices': UserReport.JOB_CHOICES})
    