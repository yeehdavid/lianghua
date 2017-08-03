import pandas as pd

train = pd.read_csv('/home/david/train.csv')

test = train.iloc[160000:]


bianzhun = test['label']
bianzhun.to_csv('/home/david/biaozhun.csv')

test = test.drop('label',axis = 1)

test.to_csv('/home/david/test.csv')





train = train.iloc[0:160000]

train.to_csv('/home/david/train.csv')

