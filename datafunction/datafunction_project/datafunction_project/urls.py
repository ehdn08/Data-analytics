# datafunction_app/urls.py
from django.urls import path, include
from .views import home, login, memo, google_authenticate, weather_data, board, create_post, delete_post, post_detail, edit_post
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('home/', home, name='home'),
    path('login/', login, name='login'),
    path('memo/', memo, name='memo'),
    path('board/', board, name='board'),
    path('create/', create_post, name='create_post'),
    path('delete_post/<int:post_id>/', delete_post, name='delete_post'),
    path('edit_post/<int:post_id>/', edit_post, name='edit_post'),
    path('board/<int:post_id>/', post_detail, name='post_detail'),
    path('google-auth/', google_authenticate, name='google-auth'),
    path('weather/', weather_data, name='weather'),
    path('social/', include('social_django.urls', namespace='social')),  # Social Auth 앱의 URL 패턴 등록

    # 필요에 따라 다른 URL 패턴들 추가
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)