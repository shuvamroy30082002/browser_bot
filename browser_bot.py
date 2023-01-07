from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import *
import sys
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtCore import *

class MainWIndow(QMainWindow):
    def __init__(self): 
        super(MainWIndow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('http://google.com'))
        self.setCentralWidget(self.browser)
        self.showMaximized()


        navbar = QToolBar()
        self.addToolBar(navbar)


        back_botton = QAction('back', self)
        back_botton.triggered.connect(self.browser.back)
        navbar.addAction(back_botton)

        Forward_botton = QAction('Forword', self)
        Forward_botton.triggered.connect(self.browser.forward)
        navbar.addAction(Forward_botton)

        Reload = QAction('Reload', self)
        Reload.triggered.connect(self.browser.reload)
        navbar.addAction(Reload)

        Home = QAction('Home', self)
        Home.triggered.connect(self.nevigate_home)
        navbar.addAction(Home)

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.connect_to_url)
        navbar.addWidget(self.url_bar)


        self.browser.urlChanged.connect(self.update_Url)  

    def nevigate_home(self):
        self.browser.setUrl(QUrl('http://google.com'))

    def connect_to_url(self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))


    def update_Url(self, q):
        self.url_bar.setText(q. toString())      

app = QApplication(sys.argv)
QApplication.setApplicationName('crome bot')
window = MainWIndow()
app.exec_()