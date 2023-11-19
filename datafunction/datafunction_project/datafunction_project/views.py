import requests
import json
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from datafunction_app.models import Board, Post
from .forms import BoardForm, PostForm
from social_django.models import UserSocialAuth
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.http import JsonResponse
from django.http import HttpResponseNotFound

# Common --- START

@login_required
def home(request):
    return render(request, 'home.html')

def login(request):
    return render(request, 'login.html')

def google_authenticate(request):
    # 구글 리디렉션 Oauth login URL
    return redirect('social:begin', 'google-oauth2')

# Common --- END


# Function Project --- START

def board(request):
    post_list = Board.objects.all()

    # 페이지당 보여줄 게시물 수
    items_per_page = 5

    paginator = Paginator(post_list, items_per_page)
    page = request.GET.get('page')

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # 페이지 번호가 정수가 아닌 경우, 첫 번째 페이지를 보여줍니다.
        posts = paginator.page(1)
    except EmptyPage:
        # 페이지가 비어있는 경우, 마지막 페이지를 보여줍니다.
        posts = paginator.page(paginator.num_pages)

    return render(request, 'board.html', {'posts': posts})

def memo(request):
    return render(request, 'memo.html')

def create_post(request):
    if request.method == 'POST':
        form = BoardForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('board')  # 글 목록으로 이동하는 URL로 수정
    else:
        form = BoardForm()
    return render(request, 'create_post.html', {'form': form})

def delete_post(request, post_id):
    try:
        # 해당 post_id로 게시물을 찾습니다.
        post = Board.objects.get(pk=post_id)  # Board 모델명으로 변경합니다.
        
        # 게시물을 삭제합니다.
        post.delete()
        
        # 게시판 페이지로 리디렉션합니다.
        return redirect('board')  # 'board'는 게시판 페이지의 URL 패턴 이름입니다. 필요에 따라 변경해주세요.

    except Board.DoesNotExist:  # Board 모델명으로 변경합니다.
        return HttpResponseNotFound("해당 게시물을 찾을 수 없습니다.")  # 게시물이 존재하지 않는 경우 에러 메시지를 반환합니다
    
def post_detail(request, post_id):
    post = get_object_or_404(Board, pk=post_id)
    return render(request, 'post_detail.html', {'post': post})

def edit_post(request, post_id):
    post = get_object_or_404(Board, id=post_id)
    if request.method == 'POST':
        form = BoardForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', post_id=post_id)
    else:
        form = BoardForm(instance=post)
    return render(request, 'edit_post.html', {'form': form})
    

# Function Project --- END



# Data Crawling Project --- START

def weather_data(request):
    apikey = "d3216f4e854d05aaaa5b748eb069cad1"

    city_list = ["Seoul, KR", "Tokyo, JP", "New York, US"]
    weather_info = []  # 도시별 날씨 정보를 담을 리스트

    # API 지정
    api = "http://api.openweathermap.org/data/2.5/weather?q={city}&APPID={key}"

    # 켈빈 온도를 섭씨 온도로 변환하는 함수
    k2C = lambda k: k - 273.15

    # 각 도시의 정보를 추출하기
    for name in city_list:
        # API의 URL 구성하기
        url = api.format(city=name, key=apikey)

        # API 요청을 보내 날씨 정보를 가져오기
        res = requests.get(url)

        # JSON 형식의 데이터를 파이썬으로 변환
        data = json.loads(res.text)

        # 날씨 정보를 딕셔너리로 만들어 리스트에 추가
        city_weather = {
            'city_name': data["name"], #city name
            'weather_description': data["weather"][0]["description"], # weather 1
            'min_temp': round(k2C(data["main"]["temp_min"]), 2), #최저온도
            'max_temp': round(k2C(data["main"]["temp_max"]), 2), #최고온도
            'humidity': data["main"]["humidity"], #습도
            'pressure': data["main"]["pressure"], #기압
            'wind_deg': data["wind"]["deg"], #풍향
            'wind_speed': data["wind"]["speed"] #풍속
        }
        weather_info.append(city_weather)

    context = {
        'city_weather_list': weather_info
    }

    return render(request, 'weather.html', context)



# Data Crawling Project --- END