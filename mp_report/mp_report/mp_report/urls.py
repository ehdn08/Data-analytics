# mp_report/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', include('reports.urls')),  # 'home/' 경로를 reports 앱의 URL 설정으로 리디렉션
]