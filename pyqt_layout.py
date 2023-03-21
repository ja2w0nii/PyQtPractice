# 절대적 배치
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QHBoxLayout, QVBoxLayout


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        label1 = QLabel('Label1', self) # 라벨 생성
        label1.move(20, 20) # 라벨 위치 설정
        label2 = QLabel('Label2', self)
        label2.move(20, 60)

        btn1 = QPushButton('Button1', self) # 버튼 생성
        btn1.move(80, 13) # 버튼 위치 설정
        btn2 = QPushButton('Button2', self)
        btn2.move(80, 53)

        okButton = QPushButton('OK')
        cancelButton = QPushButton('Cancel')

        hbox = QHBoxLayout() # 수평 박스 생성
        hbox.addStretch(1) # 신축성있는 빈 공간 추가 (stretch facter 조절)
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)
        hbox.addStretch(1)

        vbox = QVBoxLayout()
        vbox.addStretch(3)
        vbox.addLayout(hbox) # 수평 박스를 수직 박스에 넣음
        vbox.addStretch(1)
        # 수평 박스 위:아래=3:1

        self.setLayout(vbox) # 수직 박스를 창의 메인 레이아웃으로 설정

        self.setWindowTitle('PyQt5 Layout Practice')
        self.setGeometry(300, 300, 400, 200)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())


# ---------------------------------------------------------------------------------------------------------------------------