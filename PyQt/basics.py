""" 창 띄우기, 어플리케이션 아이콘 넣기, 창 닫기, 툴팁 나타내기 """
# import sys
# from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QToolTip, QDesktopWidget #기본적인 UI 구성요소를 제공하는 위젯
# from PyQt5.QtCore import QCoreApplication
# from PyQt5.QtGui import QIcon
# from PyQt5.QtGui import QFont


# class MyApp(QWidget):

#     def __init__(self):
#         super().__init__()
#         self.initUI()

#     def initUI(self):
#         self.setWindowTitle("JW's First Application") # 타이틀바에 나타나는 창의 제목

#         QToolTip.setFont(QFont('SansSerif', 10)) # 툴팁 폰트 설정
#         self.setToolTip('This is a <b>QWidget</b> widget')

#         btn = QPushButton('Quit', self) # 푸시버튼 생성(첫번째 파라미터 : 버튼에 표시될 텍스트, 두번째 파라미터 : 버튼이 위치할 부모 위젯)
#         btn.setToolTip('This is a <b>QPushButton</b> widget')
#         # btn.move(50, 50)
#         btn.resize(btn.sizeHint()) # sizeHint() : 버튼을 적절한 크기로 설정
#         btn.clicked.connect(QCoreApplication.instance().quit)
        
#         # self.move(500, 500) #위젯 위치 설정
#         # self.resize(500, 300) #위젯의 크기(너비, 높이) 설정
#         self.setWindowIcon(QIcon('web.png')) # 어플리케이션 아이콘 설정(다른 폴더에 저장했을 경우 경로까지 입력해야 함)
#         self.setGeometry(300, 300, 300, 200) # 위젯 위치 및 크기 설정(move(), resize()와 같음)
#         self.center() # 창을 화면 중앙에 위치시킴
#         self.show() # 위젯을 스크린에 보여줌

#     def center(self):
#         qr = self.frameGeometry() # 창의 위치와 크기 정보를 가져옴
#         cp = QDesktopWidget().availableGeometry().center() # 사용하는 모니터 화면의 가운데 위치를 파악함
#         qr.moveCenter(cp) # 창의 직사각형 위치를 화면의 중심의 위치로 이동함
#         self.move(qr.topLeft()) # 현재 창을, 화면의 중심으로 이동했던 직사각형(qr)의 위치로 이동시킴. 결과적으로 현재 창의 중심이 화면의 중심과 일치하게 돼서 창이 가운데에 나타나게 됨


# if __name__ == '__main__':

#    app = QApplication(sys.argv) # 모든 PyQt5 어플리케이션은 어플리케이션 객체를 생성해야 함
#    ex = MyApp()
#    sys.exit(app.exec_())


# ---------------------------------------------------------------------------------------------------------------------------


""" 상태바 만들기 """
# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow


# class MyApp(QMainWindow):

#     def __init__(self):
#         super().__init__()
#         self.initUI()

#     def initUI(self):
#         self.statusBar().showMessage('Ready') # 상태바 생성

#         self.setWindowTitle('Statusbar')
#         self.setGeometry(300, 300, 300, 200)
#         self.show()


# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = MyApp()
#     sys.exit(app.exec_())


# ---------------------------------------------------------------------------------------------------------------------------


""" 메뉴바 만들기 """
# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, qApp
# from PyQt5.QtGui import QIcon


# class MyApp(QMainWindow):

#     def __init__(self):
#         super().__init__()
#         self.initUI()

#     def initUI(self):
#         exitAction = QAction(QIcon('exit.png'), 'Exit', self)
#         exitAction.setShortcut('Ctrl+Q') # 동작에 대한 단축키 설정
#         exitAction.setStatusTip('Exit application')
#         exitAction.triggered.connect(qApp.quit) # 생성된 (triggered) 시그널이 QApplication 위젯의 quit() 메서드에 연결되고, 어플리케이션을 종료시키게 됩니다.

#         self.statusBar()

#         self.toolbar = self.addToolBar('Exit')
#         self.toolbar.addAction(exitAction)

#         menubar = self.menuBar()
#         menubar.setNativeMenuBar(False)
#         filemenu = menubar.addMenu('&File')
#         filemenu.addAction(exitAction)

#         self.setWindowTitle('PyQt5 Practice')
#         self.setGeometry(300, 300, 300, 200)
#         self.show()


# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = MyApp()
#     sys.exit(app.exec_())


# ---------------------------------------------------------------------------------------------------------------------------


""" 날짜와 시간 표시하기 """
# from PyQt5.QtCore import QDate, Qt, QTime, QDateTime


# now = QDate.currentDate() # 현재 날짜 반환
# print(now.toString()) # 현재 날짜를 문자열로 출력

# # 날짜 format 설정
# print(now.toString('d.M.yy'))
# print(now.toString('dd.MM.yyyy'))
# print(now.toString('ddd.MMMM.yyyy'))
# print(now.toString(Qt.ISODate)) # ISO 표준 형식
# print(now.toString(Qt.DefaultLocaleLongDate)) # 어플리케이션의 기본 설정

# time = QTime.currentTime() # 현재 시간 반환
# print(time.toString())

# # 시간 format 설정
# print(time.toString('h.m.s'))
# print(time.toString('hh.mm.ss'))
# print(time.toString('hh.mm.ss.zzz')) # 'z' : 1000분의 1초
# print(time.toString(Qt.DefaultLocaleLongDate))
# print(time.toString(Qt.DefaultLocaleShortDate))

# datetime = QDateTime.currentDateTime() # 현재 날짜와 시간을 반환
# print(datetime.toString())

# # 날짜, 시간 format 설정
# datetime = QDateTime.currentDateTime()
# print(datetime.toString('d.M.yy hh:mm:ss'))
# print(datetime.toString('dd.MM.yyyy, hh:mm:ss'))
# print(datetime.toString(Qt.DefaultLocaleLongDate))
# print(datetime.toString(Qt.DefaultLocaleShortDate))


""" 상태 표시줄에 날짜 표시하기 """
# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow
# from PyQt5.QtCore import QDate, Qt


# class MyApp(QMainWindow):

#     def __init__(self):
#         super().__init__()
#         self.date = QDate.currentDate()
#         self.initUI()

#     def initUI(self):
#         self.statusBar().showMessage(self.date.toString(Qt.DefaultLocaleLongDate))

#         self.setWindowTitle('Date')
#         self.setGeometry(300, 300, 400, 200)
#         self.show()


# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = MyApp()
#     sys.exit(app.exec_())


# ---------------------------------------------------------------------------------------------------------------------------


""" 스타일 꾸미기 """
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        lbl_red = QLabel('Red')
        lbl_green = QLabel('Green')
        lbl_blue = QLabel('Blue')

        lbl_red.setStyleSheet("color: red;"
                             "border-style: solid;"
                             "border-width: 2px;"
                             "border-color: #FA8072;"
                             "border-radius: 3px")
        lbl_green.setStyleSheet("color: green;"
                               "background-color: #7FFFD4")
        lbl_blue.setStyleSheet("color: blue;"
                              "background-color: #87CEFA;"
                              "border-style: dashed;"
                              "border-width: 3px;"
                              "border-color: #1E90FF")

        vbox = QVBoxLayout()
        vbox.addWidget(lbl_red)
        vbox.addWidget(lbl_green)
        vbox.addWidget(lbl_blue)

        self.setLayout(vbox)

        self.setWindowTitle('Stylesheet')
        self.setGeometry(300, 300, 300, 200)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())