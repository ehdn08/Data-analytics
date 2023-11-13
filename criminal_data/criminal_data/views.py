import requests
import pandas as pd
from django.shortcuts import render
import urllib.parse

api_url = 'https://api.odcloud.kr/api/3074462/v1/uddi:f046e6e5-58f2-4716-8b74-be62f1a6c6fc_201910221520?page=1&perPage=10&serviceKey=3sAHAp7Jxn%2Bm8MNGaUsDJPtg9WVUOXtevUba75gofwYXjZlmIF2maUdGpBLVBOHZKJcnU6gZV1F2gNiJnAZudw%3D%3D'
encoding_key = '3sAHAp7Jxn%2Bm8MNGaUsDJPtg9WVUOXtevUba75gofwYXjZlmIF2maUdGpBLVBOHZKJcnU6gZV1F2gNiJnAZudw%3D%3D' 
decoding_key = '3sAHAp7Jxn+m8MNGaUsDJPtg9WVUOXtevUba75gofwYXjZlmIF2maUdGpBLVBOHZKJcnU6gZV1F2gNiJnAZudw=='

decoded_key = urllib.parse.unquote(encoding_key)

# API 요청을 보내기 위한 헤더 설정
headers = {
    'Authorization': f'Bearer {decoded_key}'
}

response = requests.get(api_url, headers=headers)

if response.status_code == 200:
    data = response.json()
    print(data)  # API 응답 출력
else:
    print('API 요청 실패:', response.status_code)

def api_data(request):
    api_url = 'https://api.odcloud.kr/api/3074462/v1/uddi:f046e6e5-58f2-4716-8b74-be62f1a6c6fc_201910221520?page=1&perPage=10'
    response = requests.get(api_url)

    if response.status_code == 200:
        data = response.json()
        api_data = data.get('data', [])
        
        # 데이터 프레임 생성
        if api_data:
            df = pd.DataFrame(api_data)
            
            # df에 있는 데이터를 context로 전달
            return render(request, 'main.html', {'df': df})
        else:
            error_message = 'Error: No data available'
            return render(request, 'error_template.html', {'error_message': error_message})
    else:
        error_message = 'Error: Unable to fetch data from the API'
        return render(request, 'error_template.html', {'error_message': error_message})
    
def main(request):

    return render(request, 'main.html')  # main.html 템플릿을 렌더링