import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# import matplotlib
# matplotlib.use('macosx')
# matplotlib.use('module://backend_integrate')
# pdf = pd.DataFrame([[1, 2, 3]], columns=['a', 'b', 'c'])
# print(pdf)
# x = np.arange(0, 4*np.pi, 0.1)   # start,stop,step
# y = np.sin(x)
# plt.plot(x, y)
# plt.show()
# I tested this on vscode
Industry = ['Bank', 'Bank', 'Bank',
            'Tech', 'Tech', 'Tech',
            'Ecomm', 'Ecomm']
SIC_Code = ['300', '400', '100',
            '1100', '1200', '1300', 
            '10', '20']
cnt = [10, 12, 15,
       40, 30, 20,
       100, 150]

test = pd.DataFrame({'Industry':Industry,
                     'SIC_Code':SIC_Code,
                     'cnt':cnt})
#print(test)

test["rank"] = test.groupby("Industry")["cnt"].rank(method="dense", ascending=False)
print(test)
tmp = test.loc[test['rank']==1.0]
print(tmp)
service_pdf = pd.read_csv('../data/311-service-requests.csv')
print(service_pdf.head())
print(sorted(service_pdf.columns))
