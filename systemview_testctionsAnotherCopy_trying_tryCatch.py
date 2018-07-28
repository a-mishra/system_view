# -*- coding: utf-8 -*-
#
# Form implementation generated from reading ui file 'system-view.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# Author: Ashutosh Mishra
#
# Creation Date : 19/May/2019
#
# CheckPoint : 20/May/2019 ; changes column header and adjusted columnWidth to fill whole area
#
# CheckPoint : 22/May/2019 ; Unavailable agents tab is activated; trying try except for all db commands
#
# NextMilestone : History Tab
#
# Vulnerablity : If Agent is lodded in multiple campaigns are selection, foe each campaign there is a different session_id this will adrupt al the count and whole thing will blow to bits, count available will be destroyed and row count of unavailable will be blown to bits. Possible solution : create a postprocessor for available the will delete not count any of the repeted entries according to agent is, will apdate available and will then everything be at peace. 


from PyQt5 import QtCore, QtGui, QtWidgets, QtTest
import time
import psycopg2
import unicodedata
from datetime import datetime

dbIp = "192.168.56.24"
dbUser = "postgres"
dbName = "ameyodb"
dbPass = ""
dbPort = "5432"
dbconnection = 1
available = 0
autocall = 0
total = 1
tableData= [('0','0')]
tableData_2= [('0','0')]
allAgents = [('0','0')]

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.ApplicationModal)
        MainWindow.resize(582, 551)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Ameyo3.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(30, 29, 521, 71))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lcdNumber = QtWidgets.QLCDNumber(self.horizontalLayoutWidget)
        self.lcdNumber.setProperty("intValue", 26)
        self.lcdNumber.setObjectName("lcdNumber")
        self.horizontalLayout.addWidget(self.lcdNumber)
        self.lcdNumber_2 = QtWidgets.QLCDNumber(self.horizontalLayoutWidget)
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        self.horizontalLayout.addWidget(self.lcdNumber_2)
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(30, 100, 258, 23))
        self.progressBar.setMouseTracking(False)
        self.progressBar.setFocusPolicy(QtCore.Qt.NoFocus)
        self.progressBar.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.progressBar.setAutoFillBackground(False)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.progressBar_2 = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_2.setGeometry(QtCore.QRect(294, 100, 258, 23))
        self.progressBar_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.progressBar_2.setProperty("value", 24)
        self.progressBar_2.setInvertedAppearance(False)
        self.progressBar_2.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.progressBar_2.setObjectName("progressBar_2")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(20, 150, 541, 391))
        self.tabWidget.setFocusPolicy(QtCore.Qt.TabFocus)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setDocumentMode(True)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setTabBarAutoHide(True)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.frame = QtWidgets.QFrame(self.tab)
        self.frame.setGeometry(QtCore.QRect(0, 9, 541, 341))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.scrollArea = QtWidgets.QScrollArea(self.frame)
        self.scrollArea.setGeometry(QtCore.QRect(9, 9, 521, 321))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 519, 319))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.tableWidget = QtWidgets.QTableWidget(self.scrollAreaWidgetContents)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 521, 321))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.frame_2 = QtWidgets.QFrame(self.tab_2)
        self.frame_2.setGeometry(QtCore.QRect(0, 9, 541, 341))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.scrollArea_2 = QtWidgets.QScrollArea(self.frame_2)
        self.scrollArea_2.setGeometry(QtCore.QRect(10, 10, 521, 321))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 519, 319))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.scrollAreaWidgetContents_2)
        self.tableWidget_2.setGeometry(QtCore.QRect(0, 0, 521, 321))
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(0)
        self.tableWidget_2.setRowCount(0)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.tabWidget.addTab(self.tab_2, "")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 10, 62, 20))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(294, 10, 62, 20))
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "System View"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Available"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Unavailable"))
        self.label_2.setText(_translate("MainWindow", "Available"))
        self.label_3.setText(_translate("MainWindow", "Autocall"))



class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent=parent)
        self.setupUi(self)

    def setit(self):
        self.lcdNumber.setProperty("intValue", available)
        self.progressBar.setProperty("value", (((available)/total)*100))
        self.lcdNumber_2.setProperty("intValue", autocall)
        self.progressBar_2.setProperty("value", (((autocall)/total)*100))
    
    def setTable(self):
        rowCount = 0
        columnCount = 0
        rowCount = len(tableData)
        if rowCount > 0:
            columnCount = len(tableData[0])
        self.tableWidget.setRowCount(rowCount)
        self.tableWidget.setColumnCount(columnCount)
        self.tableWidget.setHorizontalHeaderLabels(("Campaign;UserID;UserName;Ready-Start-Time;").split(";"))
        self.tableWidget.setColumnWidth(0, 150)
        self.tableWidget.setColumnWidth(1, 100)
        self.tableWidget.setColumnWidth(2, 100)
        self.tableWidget.setColumnWidth(3, 155)
        i=0
        for row in tableData:
            j = 0
            red = 1
            for m in tableData_2:
                if row[1]==m[0]:
                    red = 0
                    break
            for cell in row:
                if type(cell) == datetime:
                    cell = datetime.strftime(cell,'%b %d, %Y - %H:%M') 
                self.tableWidget.setItem(i,j, QtWidgets.QTableWidgetItem(cell))
                if red == 0:
                    self.tableWidget.item(i, j).setBackground(QtGui.QColor(204,255,229))
                else:
                    self.tableWidget.item(i, j).setBackground(QtGui.QColor(255,204,204))   
                j+=1
            i+=1




    def setTable_2(self):
        rowCount = 0
        columnCount = 0
        rowCount = len(allAgents)-len(tableData)
        if rowCount > 0:
            columnCount = len(allAgents[0])
        self.tableWidget_2.setRowCount(rowCount)
        self.tableWidget_2.setColumnCount(columnCount)
        self.tableWidget_2.setHorizontalHeaderLabels(("UserID;UserName;").split(";"))
        self.tableWidget_2.setColumnWidth(0, 240)
        self.tableWidget_2.setColumnWidth(1, 243)
        i=0
        for row in allAgents:
            j = 0
            red = 1
            show = 1
            for m in tableData:
                if row[0]==m[1]:
                    show = 0
                    break
            for cell in row:
                if show == 1:
                    self.tableWidget_2.setItem(i,j, QtWidgets.QTableWidgetItem(cell))
                    if red == 0:
                        self.tableWidget_2.item(i, j).setBackground(QtGui.QColor(204,255,229))
                    else:
                        self.tableWidget_2.item(i, j).setBackground(QtGui.QColor(255,204,204))   
                j+=1
            if show == 1:
                i+=1





def connection():
	global dbconnection
	dbconnection = 1
	try:
		conn = psycopg2.connect(database=dbName, user = dbUser, password = dbPass, host = dbIp, port = dbPort)
	except:
		dbconnection = 0
		print ("Could not connect to database")
	if dbconnection == 1:
		print ("Connected to database")


def resetdata():
	global dbconnection
	global available
	global autocall
	global total
	global tableData
	global tableData_2

	dbconnection = 1
	available = 0
	autocall = 0
	total = 1
	tableData= [('0','0')]
	tableData_2= [('0','0')]


def numberOfAgents():
	global dbconnection
	dbconnection = 1
	try:	
		conn = psycopg2.connect(database=dbName, user = dbUser, password = dbPass, host = dbIp, port = dbPort)
		cur = conn.cursor()
		cur.execute("SELECT user_id, username from users where user_type ilike '%pro%' or user_type ilike '%exe%'")
		global allAgents	
		allAgents = cur.fetchall()
		global total
		total = len(allAgents)
		conn.close()
	except:
		dbconnection = 0
		print ("Could not connect to database")
	#if dbconnection == 1:
	#	print ("Connected to database")


def availableAgents():
	global dbconnection
	dbconnection = 1
	try:
		conn = psycopg2.connect(database=dbName, user = dbUser, password = dbPass, host = dbIp, port = dbPort)
		cur = conn.cursor()
		cur.execute("select t5.name, t5.user_id, users.username, t5.ready_start_time from (select t4.name, t3.user_id, t3.ready_start_time from (select  t1.session_id, t1.campaign_id, t2.user_id, t1.ready_start_time from (select * from campaign_user_ready_history  where ready_end_time is null order by ready_start_time desc) as t1 inner join (select * from user_session_history where logout_time is null order by login_time desc) as t2 on t1.session_id = t2.session_id) as t3 left join campaign_context as t4 on t3.campaign_id = t4.id) as t5 left join users on users.user_id = t5.user_id")
		global tableData
		tableData = cur.fetchall()
		global available
		available = len(tableData)
		conn.close()
	except:
		dbconnection = 0
		print ("Could not connect to database")
	#if dbconnection == 1:
	#	print ("Connected to database")


def autocallAgents():
	global dbconnection
	dbconnection = 1
	try:
		conn = psycopg2.connect(database=dbName, user = dbUser, password = dbPass, host = dbIp, port = dbPort)
		cur = conn.cursor()
		cur.execute("select  t2.user_id from (select * from campaign_user_autocall_history  where auto_call_on_end_time is null order by auto_call_on_end_time desc) as t1 inner join (select * from user_session_history where logout_time is null order by login_time desc) as t2 on t1.session_id = t2.session_id")
		global tableData_2
		tableData_2 = cur.fetchall()
		global autocall
		autocall = len(tableData_2)
		conn.close()
	except:
		dbconnection = 0
		print ("Could not connect to database")
	#if dbconnection == 1:
	#	print ("Connected to database")



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    connection()
    testVar = 0
    while True:
    	testVar += 1
    	if testVar >= 10:
    		testVar = 0
    	#	connection()
    	#	if dbconnection == 0:
    	#		resetdata()
    	if dbconnection == 0:
    		resetdata()
    	numberOfAgents()
    	autocallAgents()
    	availableAgents()
    	w.setit()
    	w.setTable()
    	w.setTable_2()
    	QtTest.QTest.qWait(5000)
    
    sys.exit(app.exec_())
