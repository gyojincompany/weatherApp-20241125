import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic  # QT Designer에서 만든 ui를 불러오는 모듈
from PyQt5.QtCore import Qt

from os import environ
import multiprocessing as mp

form_class = uic.loadUiType("ui/weather.ui")[0]
# QT Designer에서 만든 외부 ui 불러오기

class WeatherApp(QMainWindow, form_class):
    def __init__(self):
        super().__init__()  # 부모 클래스의 생성자 호출
        self.setupUi(self)  # 불러온 ui 파일을 연결

        self.setWindowTitle("구글 한줄 번역기")  # 윈도우 제목 설정
        self.setWindowIcon(QIcon("img/weather_icon.png"))  # 윈도우 아이콘 설정
        self.statusBar().showMessage("네이버 날씨 앱 v0.5")  # 윈도우 상태 표시줄 설정
        self.setWindowFlag(Qt.WindowStaysOnTopHint)  # 항상위에 옵션



def suppress_qt_warnings():  # 해상도별 글자크기 강제 고정하는 함수
    environ["QT_DEVICE_PIXEL_RATIO"] = "0"
    environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    environ["QT_SCREEN_SCALE_FACTORS"] = "1"
    environ["QT_SCALE_FACTOR"] = "1"


# 해상도 고정 함수 호출
suppress_qt_warnings()
mp.freeze_support()

app = QApplication(sys.argv)
Win = WeatherApp()
Win.show()
sys.exit(app.exec_())