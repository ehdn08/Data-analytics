from django.shortcuts import render
import requests
from django.conf import settings

# 소환사 정보 호출 함수
def search_summoner(request):
    context = {'current_game_data': None, 'error_message': None, 'opponent_tier_data': {}}  # 현재 게임 정보 및 상대방 티어 데이터 변수 초기화

    if request.method == 'POST':
        summoner_name = request.POST.get('summoner_name')
        
        # Riot Games API를 호출해서 소환사 정보를 가져오는 코드
        api_key = settings.RIOT_API_KEY
        region = "KR"  # region 설정

        url = f"https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-name/{summoner_name}"

        headers = {
            "X-Riot-Token": api_key,
        }
        
        response = requests.get(url, headers=headers)
        
        # 성공 시 소환사 정보를 summoner_data에 저장
        if response.status_code == 200:
            summoner_data = response.json()

            # 현재 게임 정보 변수 초기화
            current_game_data = None

            # 현재 게임 정보 API 엔드포인트
            current_game_url = f"https://kr.api.riotgames.com/lol/spectator/v4/active-games/by-summoner/{summoner_data['id']}"
            current_game_response = requests.get(current_game_url, headers=headers)

            if current_game_response.status_code == 200:
                current_game_data = current_game_response.json()
                # 현재 게임 정보를 불러왔으므로 이제 current_game_data 변수에 값이 할당됩니다.

                # 상대방 티어 정보 가져오기
                for player in current_game_data['participants']:
                    summoner_id = player['summonerId']
                    league_url = f"https://kr.api.riotgames.com/lol/league/v4/entries/by-summoner/{summoner_id}"
                    league_response = requests.get(league_url, headers=headers)

                    if league_response.status_code == 200:
                        league_data = league_response.json()
                        print(f"Summoner ID: {summoner_id}, League Data: {league_data}")

                        if league_data:
                            tier_info = {
                                'tier': league_data[0]['tier'],
                                'rank': league_data[0]['rank'],
                                'leaguePoints': league_data[0]['leaguePoints'],
                            }
                            context['opponent_tier_data'][summoner_id] = tier_info
                        else:
                            context['opponent_tier_data'][summoner_id] = {'tier': 'UNRANKED', 'rank': '', 'leaguePoints': 0}
                    else:
                        print(f"Failed to fetch league data for Summoner ID: {summoner_id}")


            # 리그 정보 API 엔드포인트
            league_url = f"https://kr.api.riotgames.com/lol/league/v4/entries/by-summoner/{summoner_data['id']}"
            league_response = requests.get(league_url, headers=headers)
            
            if league_response.status_code == 200:
                league_data = league_response.json()

                # 티어 이미지 파일 경로 추가
                for league in league_data:
                    if league['tier'] == 'BRONZE':
                        league['tier_image_path'] = 'bronze.png'
                    # ...

                # 템플릿에 전달할 context 생성
                context.update({
                    'summoner_data': summoner_data,
                    'league_data': league_data,
                    'current_game_data': current_game_data,  # 현재 게임 정보 추가
                })

                # 검색 결과 페이지로 이동
                return render(request, 'summoner_search/result.html', context)
        else:
            # API 요청이 실패한 경우
            context['error_message'] = "소환사 정보를 가져올 수 없습니다."
     
    # POST 요청이 아니거나 요청 실패 시 검색 페이지로 이동
    return render(request, 'summoner_search/search.html', context)