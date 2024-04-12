# How to swap two DataFrame columns in Pandas

import pandas as pd


df = pd.DataFrame({
    'name': ['Alice', 'Bobby', 'Carl', 'Dan'],
    'age': [29, 30, 31, 32],
    'salary': [175.1, 180.2, 190.3, 205.4],
})

print(df)

column_names = ['name', 'salary', 'age']

df = df.reindex(columns=column_names)

print('-' * 50)

print(df)