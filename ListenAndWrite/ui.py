# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\uploadfile\Anaconda\Lib\site-packages\PyQt5-tools\designer\re_words.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
import sys
import random

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):


    def retranslateUi(self, MainWindow):
        list_prefix = [('a-', '否', 'asymmetry（不对称)'),
                       ('an-', '否', 'anhydrous（无水的）'),
                       ('dis-', '否', ' dishonest'),
                       ('in-', '否', 'incapable inability'),
                       ('il-', '否', 'illegal'),
                       ('ig-', '否', 'ignoble'),
                       ('im-', '否', 'impossible immoral'),
                       ('ir-', '否', 'irregular'),
                       ('ne-', '否', ' never'),
                       ('n- ', '否', 'neither'),
                       ('non-', '否', 'none '),
                       ('neg-', '否', 'neglect'),
                       ('un-', '否', 'unable'),
                       ('male-', '错误', ''),
                       ('mal-', '错误', 'malfunction  失调 '),
                       ('mis-', '错误', 'mistake '),
                       ('pseudo-', '错误', 'pseudonym假名 '),
                       ('de- ', '反动作', 'demodulation解调 '),
                       ('dis-', '反动作', 'disarm '),
                       ('un- ', '反动作', 'unload '),
                       ('anti-', ' 相反', ' antiforeign 排外的  '),
                       ('ant- ', '相反', ' antiknock 防震 '),
                       ('contra-', ' 相反', 'contradiction'),
                       ('contre-', ' 相反', ''),
                       ('contro-', ' 相反 ', 'controflow 逆流 '),
                       ('counter- ', '相反', 'counterreaction '),
                       ('ob-', '相反', '  object'),
                       ('oc-', '相反', '  occupy '),
                       ('of-', '相反  ', ''),
                       ('op- ', '相反', ' oppose '),
                       ('with-', ' 相反', ' withdraw '),
                       ('a- ', '’’表示“ 在??之上” ，“向??”', ' aboard aside '),
                       ('by-', ' 表示“附近，邻近，边侧 ”', ' bypath bypass弯路 '),
                       ('circum-', ' 表示“周围，环绕，回转 ”', ' circumstance circuit '),
                       ('circu- ', '表示“周围，环绕，回转 ”', ' circumstance circuit '),
                       ('de-', ' 表示“在下，向下 ”', ' descend degrade '),
                       ('en- ', '表示“在内，进入 ”', ' encage（禁闭）  enbed上床 '),
                       ('ex- ec- es-', ' 表示“外部，外 ”', ' exit eclipse expand export '),
                       ('extra-', ' 表示“额外”', ' extraction （提取）'),
                       ('fore- ', '表示“在前面”', ' forehead foreground '),
                       ('in- il- im- ir- ', '表示“向内，在内，背于 ” ', 'inland invade inside import '),
                       ('inter- intel- ', '表示“在??间，相互 ” ', 'international interaction internet '),
                       ('intro-', ' 表示“向内，在内，内侧 ”', ' introduce introduce '),
                       ('medi- med- mid- ', '表示“中，中间 ” ', 'Mediterranean midposition '),
                       ('out- ', '表示“在上面，在外部，在外 ” ', 'outline outside outward '),
                       ('over- ', '表示“在上面，在外部，向上 ”', ' overlook overhead overboard '),
                       ('post-', ' 表示"向后，在后边，次 ” ', 'postscript附言，'),
                       ('pre-', ' 表示"在前”在前面” ', 'prefix preface preposition '),
                       ('pro- ', '表示“在前，向前 ” ', 'progress proceed '),
                       ('sub- suc- suf- sug- sum- sup- sur- sus- ', '表示“在下面，下 ”',
                        'subway submarine suffix suppress supplement'),
                       ('trans- ', '表示“移上，转上，在那一边 ”', ' translate transform transoceanic '),
                       ('under- ', '表示“在?下面，下的 ” ', 'underline underground underwater '),
                       ('up- ', '表示“向上，向上面，在上 ” ', 'upward uphold uphill上坡 '),
                       ('ante- anti- ', '表示“先前，早于，预先 ”', 'antecedent anticipate '),
                       ('ex-', ' 表示“先，故，旧 ”', 'expresident exhusband '),
                       ('fore-', ' 表示“在前面，先前，前面 ”', 'foreward dorecast foretell预言 '),
                       ('mid- medi- ', '表示“中，中间 ”', 'midnight midsummer '),
                       ('post-', '"表示“在后，后 ”', 'postwar '),
                       ('by-', ' 表示“副，次要的 ”', 'byproduct bywork副业 '),
                       ('extra-', '表示“超越，额外 ”', 'extraordinary '),
                       ('hyper-', ' 表示“超过，极度 ”', 'hypersonic超声波  hypertesion高血压  '),
                       ('out-', '表示“超过，过分 ”', 'outdo超过 outbid出价过高的人  '),
                       ('over-', '，表示 “超过，过度，太 ”', 'overeat overdress oversleep '),
                       ('sub- suc- sur-', '   表示“低，次，副，亚 ”', 'subeditor subordinate subtropical亚热带'),
                       ('super- sur-', ' 表示“超过”', 'Supernature  superpower  surplus  surpass '),
                       ('under-', '表示“低劣，低下 ”', 'undersize undergrown underproduction生产不足  '),
                       ('pre- pri-', ' 表示“在前，事先，预先 ”', 'preheat prewar prehistory '),
                       ('pro- ', '表示“在前，先，前 ”', 'prologue 序幕，prophet预言家 '),
                       ('re- ', '表示“再一次，重新 ”', 'retell rewrite '),
                       ('vice- ', '表示“副，次 ”', 'vicepresident vicechairman'),
                       ('com- cop- con- cor- co- ', '表示“共同，一起 ” 。',
                        'connect combine collect combat coexist co-operate '),
                       ('syn- syl-sym-', '表示“同，共，和，类 ”', 'symmetry sympathy synthesis合成 '),
                       ('al-', ' 表示“完整，完全 ”', 'alone almost '),
                       ('over-', '表示“完全，全 ”', 'overall overflow充满 '),
                       ('pan-', '表示“全，总，万 ”', 'panentheism泛神论 ，panorama'),
                       ('a- ab- abs-', '表示“分离，离开 ”', ' away apart abstract abstain '),
                       ('de-', ' 表示“离去，处去 ”', 'depart decolour '),
                       ('dis- di- dif- ', '表示“分离，离开 ”', ' divorce disarm缴械 '),
                       ('ex- e-', ' 表示“离开，分离 ”', 'expel exclude expatriate驱出国外  '),
                       ('for-', ' 表示“离开，脱离 ”', 'forget forgive '),
                       ('re-', '表示“离开”', 'release resolve '),
                       ('se-', '表示“分离，隔离 ”', 'separate seduce select '),
                       ('dia-', '表示“通过，横过 ”', 'diameter diagram '),
                       ('per- pel- ', '表示“通，总，遍 ”', 'perfect perform pervade浸透 '),
                       ('trans-', ' 表示“横过，贯通 ”', 'transparent transmit transport '),
                       ('a-', ' 加强', 'arouse ashamed '),
                       ('ad-', ' 加强', 'adjoin adhere 粘着 '),
                       ('be- ', '变换词类作用', 'befriend '),
                       ('en- ', '变换词类作用', 'enslave enable enrich '),
                       ('ad-', '变换词类作用', 'adapt'),
                       ('ac-', ' 变换词类作用', 'accord '),
                       ('af- ', '变换词类作用', 'affix'),
                       ('ag- ', '变换词类作用', 'aggression arrive'),
                       ('an-', '变换词类作用', ''),
                       ('ap- ', '变换词类作用', ''),
                       ('ar-', '变换词类作用', 'arrange '),
                       ('as-', '变换词类作用', 'assist assign委派'),
                       ('at-', '变换词类作用', 'attend attract '),
                       ('mono-', '单', 'monotone单调'),
                       ('mon- ', '单', ' monarch '),
                       ('uni-', '单', ' uniform'),
                       ('un-', '单 ', ' unicellular单细胞  '),
                       ('ambi-', '双', ' ambiguous amphibian两栖类  '),
                       ('bi-', '双', ' bicycle '),
                       ('bin- ', '双', ''),
                       ('di-', '双', ' diode二级管 ，'),
                       ('twi- ', '双', 'twilight '),
                       ('deca -', '“十”', ' decade '),
                       ('deco- ', '“十”', ''),
                       ('dec-', '“十”', ' decade '),
                       ('deci-', '“十”', 'decimals '),
                       ('hecto-', '百，百分子一', ' hect- hectometer '),
                       ('centi- ', '百，百分子一', 'centimeter '),
                       ('kilo- ', '千，千分子一', ' kilometer '),
                       ('myria- ', '万，万分子一', 'myriametre'),
                       ('myri- ', '万，万分子一', 'myriametre '),
                       ('mega-', ' 万，万分子一', 'megabyte '),
                       ('meg- ', '万，万分子一', ' megabyte '),
                       ('micro- ', '万，万分子一', ' microvolt 微伏特  '),
                       ('multi-', ' 许多', 'multipmetre 万用表'),
                       ('mult- ', '许多', 'multipmetre 万用表  '),
                       ('poly- ', '许多', ' polysyllable '),
                       ('hemi- ', '一半', 'hemisphere '),
                       ('demi-', ' 一半', ' demiofficial '),
                       ('semi-', ' 一半', ' semiconductor semitransparent '),
                       ('pene-', ' 一半 ”', ''),
                       ('pen-  ', '一半', ' peninsula '),
                       ('arch- ', '表示“首位，第一的，主要的 ”', 'architect archbishop '),
                       ('auto-', ' 表示“自己，独立，自动 ”', 'automobile autobiography '),
                       ('bene- ', '表示“善，福”', 'benefit '),
                       ('eu- ', '表示“优，美好 ”', 'eugenics优生学 ，euphemism '),
                       ('male-', '表示“恶，不良 ”', 'maltreatment malodor '),
                       ('mal- ', '表示“恶，不良 ”', 'maltreatment malodor '),
                       ('macro- ', '表示“大，宏大 ”', 'macroscopic宏观 '),
                       ('magni- ', '表示“ 大”', 'magnificent '),
                       ('micro- ', '表示“微”', 'microscope '),
                       ('aud-', ' 表示“听，声”', 'audience '),
                       ('bio-', ' 表示“生命，生物 ”', 'biography传记 '),
                       ('ge- ', '表示“地球，大地 ”', 'geography '),
                       ('phon-', ' 表示“声，音调 ”', 'phonograph '),
                       ('tele- ', '表示“远离”', 'television telephone '),
                       ]
# 函数1
        choice = []   #待选项
        rad_A = random.randint(1,160)
        choice.append(list_prefix[rad_A])
        answer = list_prefix[rad_A][1]
        for i in range(3):
            rad = random.randint(1,160)
            choice.append(list_prefix[rad])
        choice.sort()
        print(choice)
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Button_correct.setText(_translate("MainWindow", "确认"))
        self.Button_last.setText(_translate("MainWindow", "上一个"))
        self.Button_Choice.setText(_translate("MainWindow", "前缀为： "+str(choice[0][0])))
        self.Button_A.setText(_translate("MainWindow", str(choice[0][1])))
        self.Button_B.setText(_translate("MainWindow", str(choice[1][1])))
        self.Button_C.setText(_translate("MainWindow", str(choice[2][1])))
        self.Button_D.setText(_translate("MainWindow", str(choice[3][1])))

        #choice = []

    def judge(self,choice,answer):
        if choice==answer:
            MainWindow.destroy()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1101, 811)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Button_correct = QtWidgets.QPushButton(self.centralwidget)
        self.Button_correct.setGeometry(QtCore.QRect(680, 440, 111, 61))
        self.Button_correct.setObjectName("Button_correct")
        self.Button_last = QtWidgets.QPushButton(self.centralwidget)
        self.Button_last.setGeometry(QtCore.QRect(250, 440, 121, 61))
        self.Button_last.setObjectName("Button_last")
        self.Button_Choice = QtWidgets.QPushButton(self.centralwidget)
        self.Button_Choice.setGeometry(QtCore.QRect(250, 100, 701, 71))  # (左边，上边，右边，下边
        self.Button_Choice.setObjectName("Button_A")
        self.Button_A = QtWidgets.QPushButton(self.centralwidget)
        self.Button_A.setGeometry(QtCore.QRect(250, 190, 701, 41))
        self.Button_A.setObjectName("Button_A")
        self.Button_B = QtWidgets.QPushButton(self.centralwidget)
        self.Button_B.setGeometry(QtCore.QRect(250, 250, 701, 41))
        self.Button_B.setObjectName("Button_B")
        self.Button_C = QtWidgets.QPushButton(self.centralwidget)
        self.Button_C.setGeometry(QtCore.QRect(250, 310, 701, 41))
        self.Button_C.setObjectName("Button_C")
        self.Button_D = QtWidgets.QPushButton(self.centralwidget)
        self.Button_D.setGeometry(QtCore.QRect(250, 370, 701, 41))
        self.Button_D.setObjectName("Button_D")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1101, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()

    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())