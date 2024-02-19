# Generated by Django 4.2.6 on 2024-02-15 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0007_userreport_job'),
    ]

    operations = [
        migrations.CreateModel(
            name='ScamRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=100)),
                ('scam_detail', models.TextField()),
                ('report_date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='userreport',
            name='job',
            field=models.CharField(choices=[('초보자', '초보자'), ('검사', '검사'), ('파이터', '파이터'), ('크루세이더', '크루세이더'), ('히어로', '히어로'), ('페이지', '페이지'), ('나이트', '나이트'), ('팔라딘', '팔라딘'), ('스피어맨', '스피어맨'), ('드래곤나이트', '드래곤나이트'), ('매지션', '매지션'), ('위자드 (불,독)', '위자드 (불,독)'), ('메이지 (불,독)', '메이지 (불,독)'), ('아크메이지 (불,독)', '아크메이지 (불,독)'), ('위자드 (얼음,번개)', '위자드 (얼음,번개)'), ('메이지 (얼음,번개)', '메이지 (얼음,번개)'), ('아크메이지 (얼음,번개)', '아크메이지 (얼음,번개)'), ('클레릭', '클레릭'), ('프리스트', '프리스트'), ('비숍', '비숍'), ('아처', '아처'), ('헌터', '헌터'), ('레인저', '레인저'), ('보우마스터', '보우마스터'), ('사수', '사수'), ('저격수', '저격수'), ('신궁', '신궁'), ('로그', '로그'), ('어쌔신', '어쌔신'), ('허밋', '허밋'), ('나이트로드', '나이트로드'), ('시프', '시프'), ('시프마스터', '시프마스터'), ('새도어', '새도어')], default='초보자', max_length=50),
        ),
    ]
