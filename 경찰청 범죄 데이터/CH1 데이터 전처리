
import pandas as pd

# CSV 파일 경로 설정
csv_file = '경찰청_범죄_통계_데이터.csv'

# CSV 파일을 읽어 데이터프레임으로 불러오기
data = pd.read_csv(csv_file, encoding='utf-8')

# 데이터 전처리를 수행
# 예를 들어, '발생지역' 컬럼을 기준으로 그룹화하고 합계를 계산
crime_by_area = data.groupby('발생지역')['범죄발생건수'].sum().reset_index()

# 결과를 CSV 파일로 저장
crime_by_area.to_csv('범죄_지역별_통계.csv', index=False)
