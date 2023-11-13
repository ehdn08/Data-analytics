import requests
from django.conf import settings

def get_summoner_data(summoner_name):
    # Riot Games API를 호출해서 소환사 정보를 가져오는 코드
    api_key = settings.RIOT_API_KEY
    region = "KR"  # region 설정

    url = f"https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-name/{summoner_name}"

    headers = {
        "X-Riot-Token": api_key,
    }
    
    response = requests.get(url, headers=headers)

    # 성공 시 소환사 정보를 반환
    if response.status_code == 200:
        summoner_data = response.json()
        return summoner_data
    else:
        # 실패 시 None 반환
        return None

def get_league_data(summoner_id):
    # Riot Games API를 호출해서 리그 정보를 가져오는 코드
    api_key = settings.RIOT_API_KEY
    region = "KR"  # region 설정

    url = f"https://kr.api.riotgames.com/lol/league/v4/entries/by-summoner/{summoner_id}"

    headers = {
        "X-Riot-Token": api_key,
    }
    
    response = requests.get(url, headers=headers)

    # 성공 시 리그 정보를 반환
    if response.status_code == 200:
        league_data = response.json()
        return league_data
    else:
        # 실패 시 None 반환
        return None