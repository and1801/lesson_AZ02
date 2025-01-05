import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# dates = pd.date_range(start='2022-07-26', periods=10, freq = 'D')
#
# values = np.random.rand(10)
#
# df = pd.DataFrame({'Date' : dates, 'Value' : values})
#
# df.set_index('Date', inplace=True)
#
# print(df)
#
# month = df.resample('M').mean()
#
# print(month)

data = {
    'value' : [1, 2, 2, 3, 3, 3, 4, 4, 5, 6, 7, 8, 9, 10, 55]
}
df = pd.DataFrame(data)

df.boxplot(column='value')
plt.show()

Q1 = df['value'].quantile(0.25)
Q3 = df['value'].quantile(0.75)
IQR = Q3 - Q1

downside = Q1 - 1.5 * IQR
upside = Q3 + 1.5 * IQR

df_new = df[(df['value'] >= downside)&(df['value'] <= upside)]

print(df_new)
df_new.boxplot(column='value')
plt.show()
