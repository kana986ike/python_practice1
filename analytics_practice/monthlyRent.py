import pandas as pd
allData = pd.read_csv('monthlyRent.csv')
allData

import matplotlib.pyplot as plt
%matplotlib inline
plt.scatter(allData['人口密度'],allData['家賃'])
plt.xlabel('PopulationDensity')
plt.ylabel('MonthlyRent')


from sklearn.linear_model import LinearRegression
model1 = LinearRegression()
a = allData[['人口密度']]
b = allData['家賃']
model1.fit(a , b)

plt.scatter(allData['人口密度'],allData['家賃'])
plt.xlabel('PopulationDensity')
plt.ylabel('MonthlyRent')
plt.plot(a, model1.predict(a))

model1.predict(4000)

print(model1.coef_)
print(model1.intercept_)
print(model1.score(a, b))

c = allData['家賃']
c = allData.drop(['都道府県', '家賃'], axis=1)
c.head()
c = LinearRegression()
c.fit(a, b)
print(pd.DataFrame({'係数名':a.columns, '係数値':c.coef_}))
print(c.intercept_)
print(c.score(a, b))

X_pred = pd.DataFrame([[4000, 50000, 100000, 1000, 14000, 140]])
c.predict(X_pred)
