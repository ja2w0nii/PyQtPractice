import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QCheckBox, QRadioButton, QComboBox
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
        # cb = QCheckBox('Show title', self)
        # cb.move(20, 20)
        # cb.toggle()
        # cb.stateChanged.connect(self.changeTitle) # 체크박스의 상태가 바뀔 때 발생하는 시그널 (stateChanged)을 changeTitle() 메서드에 연결


        """ Radio Button """ # 기본적으로 autoExclusive로 설정되어 있음 (하나의 버튼을 선택하면 나머지 버튼들은 선택 해제)
        # rbtn1 = QRadioButton('First Button', self)
        # rbtn1.move(50, 50)
        # rbtn1.setChecked(True)

        # rbtn2 = QRadioButton(self)
        # rbtn2.move(50, 70)
        # rbtn2.setText('Second Button')


        """ Combo Box """
        self.lbl = QLabel('Option1', self)
        self.lbl.move(50, 150)

        cb = QComboBox(self)
        cb.addItem('Option1')
        cb.addItem('Option2')
        cb.addItem('Option3')
        cb.addItem('Option4')
        cb.move(50, 50)

        cb.activated[str].connect(self.onActivated) # 옵션을 선택하면 onActivated() 메서드 호출됨

        self.setWindowTitle('PyQt5 Widget Practice')
        self.setGeometry(300, 300, 300, 200)
        self.show()


        """ Line Edit: 한 줄의 문자열을 입력하고 수정할 수 있도록 하는 위젯 """




    # 체크박스의 체크 여부에 따라 타이틀바 텍스트 변경
    def changeTitle(self, state): 
        if state == Qt.Checked:
            self.setWindowTitle('QCheckBox')
        else:
            self.setWindowTitle(' ')

    def onActivated(self, text):
        self.lbl.setText(text) # 선택한 항목의 텍스트가 라벨에 나타남
        self.lbl.adjustSize() # 라벨의 크기를 자동으로 조절




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

"""
QLineEdit.Normal / 0: 입력된 문자를 표시합니다. (기본값)
QLineEdit.NoEcho / 1: 문자열을 표시하지 않습니다. 이 설정은 비밀번호의 글자수도 공개하지 않을 때 유용합니다.
QLineEdit.Password / 2: 입력된 문자 대신 비밀번호 가림용 문자를 표시합니다.
QLineEdit.PasswordEchoOnEdit / 3: 입력할 때만 문자를 표시하고, 수정 중에는 다른 문자를 표시합니다.
"""