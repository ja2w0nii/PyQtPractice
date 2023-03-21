import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QCheckBox
from PyQt5.QtCore import Qt


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        """ Push Button """
        # btn1 = QPushButton('&Button1', self) # 첫번째 파라미터: 버튼에 나타날 텍스트, 두번째 파라미터: 버튼이 속할 부모 클래스
        # btn1.setCheckable(True) # 선택되거나 선택되지 않은 상태를 유지
        # btn1.toggle() # 프로그램이 시작될 때 선택되어 있음

        # btn2 = QPushButton(self)
        # btn2.setText('Button&2')

        # btn3 = QPushButton('Button3', self)
        # btn3.setEnabled(False) # 버튼을 사용할 수 없음

        # vbox = QVBoxLayout()
        # vbox.addWidget(btn1)
        # vbox.addWidget(btn2)
        # vbox.addWidget(btn3)
        # self.setLayout(vbox)


        """ Label """
        # label1 = QLabel('First Label', self)
        # label1.setAlignment(Qt.AlignCenter) # 수평, 수직 방향 모두 가운데로 설정

        # label2 = QLabel('Second Label', self)
        # label2.setAlignment(Qt.AlignVCenter) # 수직 방향으로만 가운데로 설정 (수평 방향 가운데: Qt.AlignHCenter)

        # font1 = label1.font()
        # font1.setPointSize(20)

        # font2 = label2.font()
        # font2.setFamily('Times New Roman')
        # font2.setBold(True) # 폰트 크기 디폴트: 13

        # label1.setFont(font1)
        # label2.setFont(font2)

        # layout = QVBoxLayout()
        # layout.addWidget(label1)
        # layout.addWidget(label2)

        # self.setLayout(layout)


        """ Check Box """
        cb = QCheckBox('Show title', self)
        cb.move(20, 20)
        cb.toggle()
        cb.stateChanged.connect(self.changeTitle) # 체크박스의 상태가 바뀔 때 발생하는 시그널 (stateChanged)을 changeTitle() 메서드에 연결

        self.setWindowTitle('PyQt5 Widget Practice')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    # 체크박스의 체크 여부에 따라 타이틀바 텍스트 변경
    def changeTitle(self, state): 
        if state == Qt.Checked:
            self.setWindowTitle('QCheckBox')
        else:
            self.setWindowTitle(' ')




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())


# ---------------------------------------------------------------------------------------------------------------------------



"""
자주 쓰이는 메서드
setCheckable() : True 설정 시, 누른 상태와 그렇지 않은 상태를 구분합니다.
toggle() : 상태를 바꿉니다.
setIcon() : 버튼의 아이콘을 설정합니다.
setEnabled() : False 설정 시, 버튼을 사용할 수 없습니다.
isChecked() : 선택 여부를 반환합니다.
setText() : 표시될 텍스트를 설정합니다.
text() : 표시된 텍스트를 반환합니다.
checkState() : 상태를 반환합니다.

자주 쓰이는 시그널
clicked() : 클릭할 때 발생합니다.
pressed() : 눌렸을 때 발생합니다.
released() : 눌렀다 뗄 때 발생합니다.
toggled() : 상태가 바뀔 때 발생합니다.
stateChanged() : 상태가 바뀔 때 발생합니다.
"""