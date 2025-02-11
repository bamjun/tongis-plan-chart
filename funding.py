import matplotlib.pyplot as plt
import pandas as pd

# 한글 폰트 설정
# Windows의 경우
plt.rc('font', family='Malgun Gothic')

# Data for the funding allocation
categories = [
    "Equipment",
    "Operating Expenses",
    "Outsourcing",
    "Mentoring",
    "Advertising",
    "Office Rent",
    "Personnel Costs"
]

government_funding = [5000000, 5000000, 35000000, 5000000, 20000000, 10000000, 20000000]
counter_cash = [1428571, 1428571, 1428571, 1428571, 1428571, 1428571, 1428574]
counter_in_kind = [2857143, 2857143, 2857143, 2857143, 2857143, 2857143, 2857142]

# Dates for the timeline (based on 2025-04 to 2025-12)
dates = pd.date_range(start="2025-04-01", end="2025-12-31", freq="M")

# Create cumulative funding arrays for each funding type
cumulative_gov = [sum(government_funding[:i+1]) for i in range(len(government_funding))]
cumulative_cash = [sum(counter_cash[:i+1]) for i in range(len(counter_cash))]
cumulative_in_kind = [sum(counter_in_kind[:i+1]) for i in range(len(counter_in_kind))]

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(dates[:len(cumulative_gov)], cumulative_gov, marker='o', linestyle='-', color='b', label='정부지원금')
plt.plot(dates[:len(cumulative_cash)], cumulative_cash, marker='o', linestyle='--', color='g', label='대응금(현금)')
plt.plot(dates[:len(cumulative_in_kind)], cumulative_in_kind, marker='o', linestyle='-.', color='r', label='대응금(혀물)')

# Customize the plot
plt.title('자금 계획표 (Apr 2025 - Dec 2025)')
plt.xlabel('Time')
plt.ylabel('Cumulative Amount (KRW)')
plt.xticks(rotation=45)
plt.legend()
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()

# Show the plot
plt.show()
