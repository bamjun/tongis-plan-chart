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
    "디스코드 클랜 광고 서비스 개발 (MVP 개발완료 고도화 예정)",
    "디스코드 클랜 관리 봇 및 대시보드 개발",
    "배틀그라운드 전적 검색 및 클랜 순위 관리",
    "MVP 개발 (디스코드 봇, 전적 조회 서비스 개발)",
    "마케팅 및 고도화",
    "서비스 확장 및 글로벌 진출",
    "글로벌 광고"
]

start_dates = pd.to_datetime([
    "2024-10-20", "2024-11-20", "2024-12-20",
    "2025-04-01", "2025-06-01", "2025-08-01", "2025-10-01"
])

end_dates = [
    pd.to_datetime("2024-11-20"), pd.to_datetime("2025-03-10"), pd.to_datetime("2025-04-20"),
    pd.to_datetime("2025-05-31"), pd.to_datetime("2025-07-31"), pd.to_datetime("2025-09-30"), pd.to_datetime("2025-12-31")
]

# Create the plot with thicker lines
plt.figure(figsize=(12, 8))
for i, (task, start, end) in enumerate(zip(tasks, start_dates, end_dates)):
    plt.plot([start, end], [i, i], linestyle='-', color='b', linewidth=8, label='' if i > 0 else 'Development Duration')
    # start 날짜에서 10일을 뺀 위치에 텍스트 배치
    text_position = start - pd.Timedelta(days=10)
    plt.text(text_position, i, f'{task}', va='center', ha='right', fontsize=9, color='black')

# Customize the plot
plt.yticks(range(len(tasks)), [''] * len(tasks))  # Hide y-tick labels since tasks are annotated
plt.title('Development and Business Timeline (2024-2025)')
plt.xlabel('Time')
plt.grid(axis='x', linestyle='--', alpha=0.7)

# 여백 조정
plt.subplots_adjust(left=0.4)  # 왼쪽 여백을 40%로 설정

# Show the plot
plt.show()
