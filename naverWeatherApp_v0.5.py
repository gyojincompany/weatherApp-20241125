# v0.5

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic  # QT Designer에서 만든 ui를 불러오는 모듈
from PyQt5.QtCore import Qt

from os import environ
import multiprocessing as mp

import requests
from bs4 import BeautifulSoup


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

        self.weather_btn.clicked.connect(self.weather_search)  # 날씨 조회 버튼 클릭시 weather_search 메소드 호출

    def weather_search(self):  # 날씨 조회 메소드
        inputArea = self.area_input_edit.text()  # 사용자가 입력한 지역명 텍스트 가져오기

        html = requests.get(f"https://search.naver.com/search.naver?query={inputArea}+날씨")
        soup = BeautifulSoup(html.text, "html.parser")
        # print(soup.prettify())
        nowTemperText = soup.find("div", {"class":"temperature_text"}).text.strip()  # 현재 온도
        nowTemperText = nowTemperText[5:]
        print(nowTemperText)
        areaText = soup.find("h2",{"class":"title"}).text.strip()  # 날씨 조회 지역이름
        print(areaText)
        weatherText = soup.find("span",{"class":"weather before_slash"}).text.strip()  # 오늘 날씨 텍스트
        print(weatherText)
        yesterdayTempText = soup.find("p",{"class":"summary"}).text.strip()  # 어제와의 날씨 비교
        # print(yesterdayTempText[:15].strip())
        yesterdayTempText = yesterdayTempText[:15].strip()
        print(yesterdayTempText)
        senseTemperText = soup.find("dd",{"class":"desc"}).text.strip()  # 체감온도
        print(senseTemperText)
        todayWeatherInfo = soup.select("ul.today_chart_list>li")  # 리스트 형태로 반환->미세먼지,초미세먼지,자외선,일몰
        # print(todayWeatherInfo)
        dustInfo1 = todayWeatherInfo[0].find("span",{"class":"txt"}).text.strip()  # 미세먼지 정보
        dustInfo2 = todayWeatherInfo[1].find("span", {"class": "txt"}).text.strip()  # 초미세먼지 정보
        print(dustInfo1)
        print(dustInfo2)

        # ui 해당 label에 크롤링한 텍스트 출력
        self.weather_area_label.setText(areaText)
        self.now_temper_label.setText(nowTemperText)
        self.weather_image_label.setText(weatherText)
        self.yester_temper_label.setText(yesterdayTempText)
        self.sense_temper_label.setText(senseTemperText)
        self.dust1_info_label.setText(dustInfo1)
        self.dust2_info_label.setText(dustInfo2)


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