# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

# 한글 폰트 설정
# Windows의 경우
plt.rc('font', family='Malgun Gothic')

# Mac의 경우
# plt.rc('font', family='AppleGothic')

# 마이너스 폰트 깨짐 방지
plt.rcParams['axes.unicode_minus'] = False

tasks = [
    "",  # 빈 데이터 추가
    "디스코드 클랜 광고 서비스 개발 (MVP 개발완료 고도화 예정)",
    "디스코드 클랜 관리 봇 및 대시보드 개발",
    "배틀그라운드 전적 검색 및 클랜 순위 관리",
    "MVP 개발 (디스코드 봇, 전적 조회 서비스 개발)",
    "마케팅 및 고도화",
    "서비스 확장 및 글로벌 진출",
    "글로벌 광고"
]

start_dates = [
    pd.NaT,  # 빈 데이터는 NaT로 설정
    pd.to_datetime("2024-10-20"),
    pd.to_datetime("2024-11-20"),
    pd.to_datetime("2025-03-10"),
    pd.to_datetime("2025-04-01"),
    pd.to_datetime("2025-06-01"),
    pd.to_datetime("2025-08-01"),
    pd.to_datetime("2025-10-01")
]

end_dates = [
    pd.NaT,  # 빈 데이터는 NaT로 설정
    pd.to_datetime("2024-11-20"),
    pd.to_datetime("2025-03-10"),
    pd.to_datetime("2025-04-20"),
    pd.to_datetime("2025-05-31"),
    pd.to_datetime("2025-07-31"),
    pd.to_datetime("2025-09-30"),
    pd.to_datetime("2025-12-31")
]

# Create the plot with thicker lines
plt.figure(figsize=(12, 10))

# y축 위치를 일정한 간격으로 설정
y_positions = [3 + i * 1.5 for i in range(len(tasks))]  # 기본 간격 1.5로 설정
y_positions = [pos + 1 if i >= 1 else pos for i, pos in enumerate(y_positions)]  # 첫 번째 빈 데이터 이후 모두 1만큼 위로

for i, (task, start, end) in enumerate(zip(tasks, start_dates, end_dates)):
    if pd.notna(start) and pd.notna(end):  # NaT가 아닌 경우에만 그래프 그리기
        plt.plot([start, end], [y_positions[i], y_positions[i]], 
                 linestyle='-', color='b', linewidth=8, 
                 label='' if i > 0 else 'Development Duration')
        
        if task:  # 빈 문자열이 아닌 경우에만 텍스트 표시
            plt.text(start + (end - start)/2, y_positions[i] - 0.4, f'{task}', 
                     va='top', ha='center', fontsize=9, color='black')

# y축 눈금 조정
plt.yticks(y_positions, [''] * len(tasks))

# Customize the plot
plt.grid(axis='x', linestyle='--', alpha=0.7)

# 여백 조정
plt.subplots_adjust(left=0.1, right=0.95, top=0.95, bottom=0.3)

# x축 레이블과 제목을 아래쪽에 배치
plt.xlabel('Time')
plt.title('Development and Business Timeline (2024-2025)', y=-0.3)

plt.show()
