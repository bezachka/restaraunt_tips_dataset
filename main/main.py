import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("data.csv")

print("=== ОСНОВНАЯ ИНФОРМАЦИЯ О ДАТАСЕТЕ ===")
print(f"Количество строк: {len(data)}")
print(f"Количество столбцов: {len(data.columns)}")
print("\nНазвания столбцов:")
for col in data.columns:
    print(f"  - {col}")

print("\n=== ТИПЫ ДАННЫХ ===")
print(data.dtypes)

print("\n=== ПЕРВЫЕ 5 СТРОК ===")
print(data.head())

print("\n=== КРАТКОЕ ОПИСАНИЕ ДАТАСЕТА ===")
print("""
Датасет 'Tips' содержит информацию о заказах в ресторане:
- total_bill: общая сумма счёта ($)
- tip: размер чаевых ($)
- sex: пол плательщика (Male/Female)
- smoker: курят ли (Yes/No)
- day: день недели (Thur, Fri, Sat, Sun)
- time: время приёма пищи (Lunch/Dinner)
- size: размер компании (1-4 человек)

Данные часто используются для анализа поведения клиентов
и предсказания размера чаевых.
""")

def sorting(dat, type):

    sort_data = data[data[type] == dat]

    chay = sort_data[["tip", "total_bill"]].sort_values(["tip", "total_bill"])

    tip, cost = list(chay["tip"]), list(chay["total_bill"])

    procent = []

    for i in range(len(cost)):
        proc = round(tip[i])
        procent.append(proc)

    return round(sum(procent))

fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(10, 8))

x = [1, 2, 3, 4]
y = []

for i in x:
    y.append(sorting(type = "size", dat=i))

axes[0, 0].bar(x, y)
axes[0, 0].set_title('Кол-во Гостей')
axes[0, 0].grid(True)

x1 = ["Male", "Female"]
y1 = []

for i in x1:
    y1.append(sorting(type = "sex", dat=i))

axes[0, 1].bar(x1, y1)
axes[0, 1].set_title('Пол')
axes[0, 1].grid(True)


x2 = ["Thur", "Fri", "Sat", "Sun"]
y2 = []

for i in x2:
    y2.append(sorting(type = "day", dat=i))

axes[1, 0].bar(x2, y2)
axes[1, 0].set_title('День недели')
axes[1, 0].grid(True)


x3 = ["Lunch", "Dinner"]
y3 = []

for i in x3:
    y3.append(sorting(type = "time", dat=i))

axes[1, 1].bar(x3, y3)
axes[1, 1].set_title('Время')
axes[1, 1].grid(True)



plt.suptitle('Кол-во чаевых оставленное за все время', fontsize=16)
plt.tight_layout()  # Автоматическое расположение
plt.show()