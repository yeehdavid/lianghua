import xgboost as xgb
import tushare as ts
from PyQt5 import QtCore
import datetime  # 导入日期时间模块
import time
class Get_One_Prob(QtCore.QThread):
    def __init__(self, parent=None):
        super(Get_One_Prob, self).__init__(parent)

    code = None#用于存储股票代码
    _signal_ = QtCore.pyqtSignal(str)#定义一个str信号

    def run(self):
        model = xgb.Booster()
        model.load_model('softprob.model')#加载得到训练完成的Xgboost模型

        today = start = datetime.date.today()  # 获得今天的日期
        temp = 7
        while temp:
            start = start - datetime.timedelta(days=1)  # 用今天日期减掉时间差，参数为1天，获得昨天的日期
            temp = temp - 1
        df = ts.get_hist_data(self.code, start=str(start), end=str(today))

        df = df.head(3)
        d1 = df[0:1]
        d2 = df[1:2]
        d3 = df[2:3]
        if df.index.size != 3:
            return 0



        l = []  ####获取所需的交易信息
        l.append(float(d1['close'] / d1['open']))
        l.append(float(d1['close'] / d1['high']))
        l.append(float(d1['close'] / d1['low']))
        l.append(float(d1['close'] / d1['ma5']))
        l.append(float(d1['close'] / d1['ma10']))
        l.append(float(d1['close'] / d1['ma20']))
        l.append(float(d1['p_change']))
        l.append(float(d1['volume'] / d1['v_ma5']))
        l.append(float(d1['volume'] / d1['v_ma10']))
        l.append(float(d1['volume'] / d1['v_ma20']))

        l.append(float(d2['close'] / d2['open']))
        l.append(float(d2['close'] / d2['high']))
        l.append(float(d2['close'] / d2['low']))
        l.append(float(d2['close'] / d2['ma5']))
        l.append(float(d2['close'] / d2['ma10']))
        l.append(float(d2['close'] / d2['ma20']))
        l.append(float(d2['p_change']))
        l.append(float(d2['volume'] / d2['v_ma5']))
        l.append(float(d2['volume'] / d2['v_ma10']))
        l.append(float(d2['volume'] / d2['v_ma20']))

        l.append(float(d3['close'] / d3['open']))
        l.append(float(d3['close'] / d3['high']))
        l.append(float(d3['close'] / d3['low']))
        l.append(float(d3['close'] / d3['ma5']))
        l.append(float(d3['close'] / d3['ma10']))
        l.append(float(d3['close'] / d3['ma20']))
        l.append(float(d3['p_change']))
        l.append(float(d3['volume'] / d3['v_ma5']))
        l.append(float(d3['volume'] / d3['v_ma10']))
        l.append(float(d3['volume'] / d3['v_ma20']))

        test = xgb.DMatrix(l)#讲要处理的数据加载为Xgboost的数据形式
        pre = model.predict(test)#得到预测结果

        self._signal_.emit(str(pre[0][1]))#通过信号讲预测结果发送给主线程
        time.sleep(0)



def Get_Code_Price(self,Code):

    df = ts.get_realtime_quotes(str(Code))  # 得到实时数据
    self.company_name.setText('   '+str(df.name[0]))
    print(df)
    if float(df.high) == 0:
        return 0
    self.a_5_m_Edit.setText(str((df.a5_v)))
    self.a_4_m_Edit.setText(str((df.a4_v)))
    self.a_3_m_Edit.setText(str((df.a3_v)))
    self.a_2_m_Edit.setText(str((df.a2_v)))
    self.a_1_m_Edit.setText(str((df.a1_v)))
    self.b_1_m_Edit.setText(str((df.b1_v)))
    self.b_2_m_Edit.setText(str((df.b2_v)))
    self.b_3_m_Edit.setText(str((df.b3_v)))
    self.b_4_m_Edit.setText(str((df.b4_v)))
    self.b_5_m_Edit.setText(str((df.b5_v)))

    self.a_5_p_Edit.setText(str((df.a5_p)))
    self.a_4_p_Edit.setText(str((df.a4_p)))
    self.a_3_p_Edit.setText(str((df.a3_p)))
    self.a_2_p_Edit.setText(str((df.a2_p)))
    self.a_1_p_Edit.setText(str((df.a1_p)))
    self.b_1_p_Edit.setText(str((df.b1_p)))
    self.b_2_p_Edit.setText(str((df.b2_p)))
    self.b_3_p_Edit.setText(str((df.b3_p)))
    self.b_4_p_Edit.setText(str((df.b4_p)))
    self.b_5_p_Edit.setText(str((df.b5_p)))


    self.price_now_Edit.setText(str(float(df.price)))
    self.pre_clos_Edit.setText(str(float(df.pre_close)))
    self.open_Edit.setText(str(float(df.open)))
    self.high_Edit.setText(str(float(df.high)))
    self.low_Edit.setText(str(float(df.low)))
    self.volume_Edit.setText(str(float(df.volume)))
    self.amount_Edit.setText(str(float(df.amount)))






