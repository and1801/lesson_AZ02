import pandas as pd

data = {
    'Имя' : ['Алексей', 'Борис', 'Виктория', 'Галина', 'Дмитрий', 'Елена', 'Иван', 'Ксения', 'Мария', 'Николай'],
    'Математика' : [5, 5, 4, 3, 3, 3, 4, 5, 3, 5],
    'Физика' : [5, 5, 4, 3, 4, 3, 5, 3, 3, 5],
    'Химия' : [5, 4, 5, 5, 4, 5, 5, 4, 5, 3],
    'История' : [5, 3, 5, 5, 5, 5, 4, 5, 4, 3],
    'Литература' : [5, 3, 5, 5, 3, 5, 4, 5, 3, 5]
}

df = pd.DataFrame(data)

print(df.head())

print(f'средняя оценка по математике - {df['Математика'].mean()}')
print(f'средняя оценка по Физике - {df['Физика'].mean()}')
print(f'средняя оценка по химии - {df['Химия'].mean()}')
print(f'средняя оценка по истории - {df['История'].mean()}')
print(f'средняя оценка по литературе - {df['Литература'].mean()}')

print(f'медианная оценка по математике - {df['Математика'].median()}')
print(f'медианная оценка по Физике - {df['Физика'].median()}')
print(f'медианная оценка по химии - {df['Химия'].median()}')
print(f'медианная оценка по истории - {df['История'].median()}')
print(f'медианная оценка по литературе - {df['Литература'].median()}')

Q1_math = df['Математика'].quantile(0.25)
Q3_math = df['Математика'].quantile(0.75)

IQR = Q3_math - Q1_math

print(Q1_math, Q3_math, IQR)

print(f'стандартное отклонение по математике - {df['Математика'].std()}')
print(f'стандартное отклонение по Физике - {df['Физика'].std()}')
print(f'стандартное отклонение по химии - {df['Химия'].std()}')
print(f'стандартное отклонение по истории - {df['История'].std()}')
print(f'стандартное отклонение по литературе - {df['Литература'].std()}')