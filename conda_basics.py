#  창 띄우기, 어플리케이션 아이콘 넣기, 창 닫기, 툴팁 나타내기
# import sys
# from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QToolTip #기본적인 UI 구성요소를 제공하는 위젯
# from PyQt5.QtCore import QCoreApplication
# from PyQt5.QtGui import QIcon
# from PyQt5.QtGui import QFont


# class MyApp(QWidget):

#     def __init__(self):
#         super().__init__()
#         self.initUI()

#     def initUI(self):
#         self.setWindowTitle("JW's First Application") #타이틀바에 나타나는 창의 제목

#         QToolTip.setFont(QFont('SansSerif', 10)) #툴팁 폰트 설정
#         self.setToolTip('This is a <b>QWidget</b> widget')

#         btn = QPushButton('Quit', self) #푸시버튼 생성(첫번째 파라미터 : 버튼에 표시될 텍스트, 두번째 파라미터 : 버튼이 위치할 부모 위젯)
#         btn.setToolTip('This is a <b>QPushButton</b> widget')
#         btn.move(50, 50)
#         btn.resize(btn.sizeHint()) #sizeHint() : 버튼을 적절한 크기로 설정
#         btn.clicked.connect(QCoreApplication.instance().quit)
        
#         # self.move(500, 500) #위젯 위치 설정
#         # self.resize(500, 300) #위젯의 크기(너비, 높이) 설정
#         self.setWindowIcon(QIcon('web.png')) #어플리케이션 아이콘 설정(다른 폴더에 저장했을 경우 경로까지 입력해야 함)
#         self.setGeometry(300, 300, 300, 200) #위젯 위치 및 크기 설정(move(), resize()와 같음)
#         self.show() #위젯을 스크린에 보여줌


# if __name__ == '__main__':

#    app = QApplication(sys.argv) #모든 PyQt5 어플리케이션은 어플리케이션 객체를 생성해야 함
#    ex = MyApp()
#    sys.exit(app.exec_())


# ---------------------------------------------------------------------------------------------------------------------------


# 상태바 만들기
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


# 메뉴바 만들기
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, qApp
from PyQt5.QtGui import QIcon


class MyApp(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        exitAction = QAction(QIcon('exit.png'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q') # 동작에 대한 단축키 설정
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(qApp.quit) # 생성된 (triggered) 시그널이 QApplication 위젯의 quit() 메서드에 연결되고, 어플리케이션을 종료시키게 됩니다.

        self.statusBar()

        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        filemenu = menubar.addMenu('&File')
        filemenu.addAction(exitAction)

        self.setWindowTitle('Menubar')
        self.setGeometry(300, 300, 300, 200)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())