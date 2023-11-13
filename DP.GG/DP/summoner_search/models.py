from django.db import models


    #데이터 모델 정의 (소환사 정보를 저장할 수 있는 함수)
class Summoner(models.Model):
    name = models.CharField(max_length=255)
    summonerLevel = models.IntegerField(default=0)
    tier = models.CharField(max_length=255, blank=True, null=True)  # 티어 정보 저장

    def __str__(self):
        return self.name
    
class Tier(models.Model):
    name = models.CharField(max_length=255)  # 티어 이름 (예: Bronze, Silver, Gold, ...)
    image_path = models.CharField(max_length=255)  # 티어 이미지 파일 경로 (예: "bronze.png", "silver.png", "gold.png", ...)

    def __str__(self):
        return self.name


