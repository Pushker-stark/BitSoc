import csv
import pandas as pd
import numpy as np
df=pd.read_csv('mempool1.csv')

# df.to_dict()
# pk=df.set_index('tx_id').T.to_dict('list')
# # print(pk)
# for x in pk:
#     for l in range(len(pk[x])):
#         # print(x[l])
#         if x[l]==';':
#             x[l]=[x[l].split(";")]
#             print(x[l])
#     # if isinstance(pk[x],str)==False :
    #     print(pk[x])






# df=df.sort_values('fee',ascending=False)
# print(df['fee'])
pt=df['parents'].to_list()
wt=df['weight'].to_numpy()
fe=df['fee'].to_numpy()
tx=df['tx_id'].to_list()
for
# for l in pt:
#     if isinstance(l, str):
#         if l in pt:
#             print(l)

for p in pt:
    if p in tx:
        print(p)


# maxwt=4000000
# weigt=0
# for i in range(1,len(wt)):
#     if (weigt<=maxwt):
#         weigt+=wt[i]
#         print(wt[i])
# print(weigt)
# def func(x):
#     a=x.split(";")
#     return ",".join(a)
# bt=bt['parents'].apply(func,axis=1)
# # with open('mempool.csv') as file:
#     reader = csv.reader(file)
#     tx = [];wt = [];fe = [];pt=[[]]
#     for row in reader:
#         # tx += [row[0]]
#         # fe += [row[1]]
#         # wt +=
#         a=""
#         for l in row[3]:
#             a+=l
#             if(l==';'):
#                 pt+=[[a]]
#                 a=""

        # pt+=[[row[3]]]


# print(bt.head(5))