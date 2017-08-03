import pandas as pd

code_list = pd.read_csv('/home/david/桌面/沪深300.csv')

l = []

for c in code_list['code']:#获取300只股票代码存放于l
    c = str(c)
    c = c.zfill(6)
    l.append(c)

train = pd.DataFrame(columns=('C/O_1', 'C/H_1', 'C/L_1', 'C/M5_1', 'C/M10_1', 'C/M20_1', 'Pchange_1', 'V/V5_1', 'V/V10_1', 'V/V20_1',
                              'C/O_2', 'C/H_2', 'C/L_2', 'C/M5_2', 'C/M10_2', 'C/M20_2', 'Pchange_2', 'V/V5_2', 'V/V10_2', 'V/V20_2',
                              'C/O_3', 'C/H_3', 'C/L_3', 'C/M5_3', 'C/M10_3', 'C/M20_3', 'Pchange_3', 'V/V5_3', 'V/V10_3', 'V/V20_3',

                              'label'
                              ))

long = 0

for li in l:
    print(li)
    csv = pd.read_csv('/home/david/tushare300/' + li + '.csv')
    print(len(list(pd.Series(csv['date']))))
    temp = len(list(pd.Series(csv['date'])))
    while temp > 4:
        a = dict(csv[temp - 1:temp])
        b = dict(csv[temp - 2:temp - 1])
        c = dict(csv[temp - 3:temp - 2])
        d = dict(csv[temp - 4:temp - 3])
        #print(temp)
        if float(d['p_change']) > 0:
            label = True
        else:label = False

        newraw = pd.DataFrame([[
                                float(c['close'] / c['open']), float(c['close'] / c['high']), float(c['close'] / c['low']), float(c['close'] / c['ma5']), float(c['close'] / c['ma10']), float(c['close'] / c['ma20']), float(c['p_change']), float(c['volume'] / c['v_ma5']), float(c['volume'] / c['v_ma10']), float(c['volume'] / c['v_ma20']),

                                float(b['close'] / b['open']), float(b['close'] / b['high']), float(b['close'] / b['low']), float(b['close'] / b['ma5']), float(b['close'] / b['ma10']), float(b['close'] / b['ma20']), float(b['p_change']), float(b['volume'] / b['v_ma5']), float(b['volume'] / b['v_ma10']), float(b['volume'] / b['v_ma20']),

                                float(a['close'] / a['open']), float(a['close'] / a['high']), float(a['close'] / a['low']), float(a['close'] / a['ma5']), float(a['close'] / a['ma10']), float(a['close'] / a['ma20']), float(a['p_change']), float(a['volume'] / a['v_ma5']), float(a['volume'] / a['v_ma10']), float(a['volume'] / a['v_ma20']),



                                label
        ]],

                     columns=('C/O_1', 'C/H_1', 'C/L_1', 'C/M5_1', 'C/M10_1', 'C/M20_1', 'Pchange_1', 'V/V5_1', 'V/V10_1', 'V/V20_1',
                              'C/O_2', 'C/H_2', 'C/L_2', 'C/M5_2', 'C/M10_2', 'C/M20_2', 'Pchange_2', 'V/V5_2', 'V/V10_2', 'V/V20_2',
                              'C/O_3', 'C/H_3', 'C/L_3', 'C/M5_3', 'C/M10_3', 'C/M20_3', 'Pchange_3', 'V/V5_3', 'V/V10_3', 'V/V20_3',

                              'label'
                              ))
        train = train.append(newraw,ignore_index=True)
        temp -= 1

    train.to_csv('/home/david/桌面/train.csv')

