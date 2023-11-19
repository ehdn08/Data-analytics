from django.contrib import admin
from .models import Board

@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')  # 보여지는 필드 지정
    search_fields = ('title',)             # 검색 기능 추가