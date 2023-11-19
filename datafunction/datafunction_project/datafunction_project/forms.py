from django import forms
from datafunction_app.models import Board, Post

class BoardForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = ['title', 'content']  # 필드는 적절히 수정해서 사용해주세요

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']  # 필요한 필드들을 여기에 추가해주세요