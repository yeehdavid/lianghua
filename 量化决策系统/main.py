from PyQt5 import QtWidgets, QtCore, QtGui
from MainWindow import Ui_MainWindow
import sys
import One_Prob_thread as one_prob_thread

class MainWindow(Ui_MainWindow):
    def __init__(self,parent = None):
        super(MainWindow,self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("                          面向散户的量化投资决策系统  V0.1")

        self.Search_Button.clicked.connect(lambda :self.Search_Button_Clicked(Flag=0))
        self.get_top_eight.clicked.connect(lambda :self.Get_Eight_Clicked())
        self.top_1.clicked.connect(lambda :self.Search_Button_Clicked(Flag=1))
        self.top_2.clicked.connect(lambda: self.Search_Button_Clicked(Flag=2))
        self.top_3.clicked.connect(lambda: self.Search_Button_Clicked(Flag=3))
        self.top_4.clicked.connect(lambda: self.Search_Button_Clicked(Flag=4))
        self.top_5.clicked.connect(lambda: self.Search_Button_Clicked(Flag=5))
        self.top_6.clicked.connect(lambda: self.Search_Button_Clicked(Flag=6))
        self.top_7.clicked.connect(lambda: self.Search_Button_Clicked(Flag=7))
        self.top_8.clicked.connect(lambda: self.Search_Button_Clicked(Flag=8))

    def Search_Button_Clicked(self,Flag):
        if Flag == 0:
            code  = self.Insert_Code.text()
        else:
            if Flag == 1:
                code = self.top_1.text()
                self.Insert_Code.setText(code)
            elif Flag == 2:
                code = self.top_2.text()
                self.Insert_Code.setText(code)
            elif Flag == 3:
                code = self.top_3.text()
                self.Insert_Code.setText(code)
            elif Flag == 4:
                code = self.top_4.text()
                self.Insert_Code.setText(code)
            elif Flag == 5:
                code = self.top_5.text()
                self.Insert_Code.setText(code)
            elif Flag == 6:
                code = self.top_6.text()
                self.Insert_Code.setText(code)
            elif Flag == 7:
                code = self.top_7.text()
                self.Insert_Code.setText(code)
            elif Flag == 8:
                code = self.top_8.text()
                self.Insert_Code.setText(code)

        one_prob_thread.Get_Code_Price(self,code)

        self.Get_One_Prob_Thread = one_prob_thread.Get_One_Prob()
        self.Get_One_Prob_Thread._signal_.connect(self.Put_One_Prob)
        self.Get_One_Prob_Thread.code = code
        self.Get_One_Prob_Thread.start()

    def Get_Eight_Clicked(self):
        self.thread = Top_Eight_thread()
        self.thread._signal_.connect(self.Put_Eight_Info)
        self.thread.start()

    def Put_Eight_Info(self,mes):
        if len(mes) == 1:
            self.progressBar.setValue(int(mes['value']) / 3)
        else:
            keys = mes.keys()
            key = list(keys)
            self.top_1.setText(str(key[0]))
            self.Top1_label.setText(str(mes[key[0]])[0:5])
            self.top_2.setText(str(key[1]))
            self.Top2_label.setText(str(mes[key[1]])[0:5])
            self.top_3.setText(str(key[2]))
            self.Top3_label.setText(str(mes[key[2]])[0:5])
            self.top_4.setText(str(key[3]))
            self.Top4_label.setText(str(mes[key[3]])[0:5])
            self.top_5.setText(str(key[4]))
            self.Top5_label.setText(str(mes[key[4]])[0:5])
            self.top_6.setText(str(key[5]))
            self.Top6_label.setText(str(mes[key[5]])[0:5])
            self.top_7.setText(str(key[6]))
            self.Top7_label.setText(str(mes[key[6]])[0:5])
            self.top_8.setText(str(key[7]))
            self.Top8_label.setText(str(mes[key[7]])[0:5])
            self.progressBar.setValue(100)

    def Put_One_Prob(self,prob):
        self.prob_up_Edit.setText(str(prob))


if __name__ == "__main__":



    app = QtWidgets.QApplication(sys.argv)

    from Top_Eight_thread import Top_Eight_thread

    mainwindow = MainWindow()
    mainwindow.show()




    sys.exit(app.exec_())
