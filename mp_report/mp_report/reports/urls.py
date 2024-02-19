# reports/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('search/', views.search_results, name='search_results'),  # search_results 뷰에 대한 URL 패턴 추가
    path('report_user/<int:user_id>/', views.report_user, name='report_user'),  # 신고 기능을 위한 URL 패턴
    path('report/', views.report, name='report'),  # 신고하기 페이지 URL
    path('scam-records/<int:user_id>/', views.scam_records, name='scam_records'),  # Import scam_records from views
]