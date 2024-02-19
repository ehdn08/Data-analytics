from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class UserReport(models.Model):
    JOB_CHOICES = [
        ('초보자', '초보자'),    
        ('검사', '검사'),
        ('파이터', '파이터'),
        ('크루세이더', '크루세이더'),
        ('히어로', '히어로'),
        ('페이지', '페이지'),
        ('나이트', '나이트'),
        ('팔라딘', '팔라딘'),
        ('스피어맨', '스피어맨'),
        ('드래곤나이트', '드래곤나이트'),
        ('매지션', '매지션'),
        ('위자드 (불,독)', '위자드 (불,독)'),
        ('메이지 (불,독)', '메이지 (불,독)'),
        ('아크메이지 (불,독)', '아크메이지 (불,독)'),
        ('위자드 (썬,콜)', '위자드 (썬,콜)'),
        ('메이지 (썬,콜)', '메이지 (썬,콜)'),
        ('아크메이지 (썬,콜)', '아크메이지 (썬,콜)'),
        ('클레릭', '클레릭'),
        ('프리스트', '프리스트'),
        ('비숍', '비숍'),
        ('아처', '아처'),
        ('헌터', '헌터'),
        ('레인저', '레인저'),
        ('보우마스터', '보우마스터'),
        ('사수', '사수'),
        ('저격수', '저격수'),
        ('신궁', '신궁'),
        ('로그', '로그'),
        ('어쌔신', '어쌔신'),
        ('허밋', '허밋'),
        ('나이트로드', '나이트로드'),
        ('시프', '시프'),
        ('시프마스터', '시프마스터'),
        ('새도어', '새도어'),
    ]
    nickname = models.CharField(max_length=100)
    discord_nickname = models.CharField(max_length=100, blank=True, null=True)
    report_date = models.DateField()
    report_count = models.IntegerField(default=0)
    tags = models.ManyToManyField(Tag, related_name='user_reports')
    level = models.PositiveSmallIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(200)])
    job = models.CharField(max_length=50, choices=JOB_CHOICES, default='초보자')

    def __str__(self):
        return self.nickname
    
# ScamRecord 모델 수정
class ScamRecord(models.Model):
    user_report = models.ForeignKey(UserReport, on_delete=models.CASCADE, related_name='scam_records')
    scam_detail = models.TextField(blank=True, null=True)
    report_date = models.DateField()

    def __str__(self):
        return f"{self.user_report.nickname} - {self.report_date}"
