

import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtWidgets import QMessageBox


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('http://google.com'))
        self.setCentralWidget(self.browser)
        self.showMaximized()
        
        self.sub_window = SubWindow()
       

        # navbar
        navbar = QToolBar()
        self.addToolBar(navbar)

        back_btn = QAction('Back', self)
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)

        forward_btn = QAction('Forward', self)
        forward_btn.triggered.connect(self.browser.forward)
        navbar.addAction(forward_btn)

        reload_btn = QAction('Reload', self)
        reload_btn.triggered.connect(self.browser.reload)
        navbar.addAction(reload_btn)

        home_btn = QAction('Home', self)
        home_btn.triggered.connect(self.navigate_home)
        navbar.addAction(home_btn)

       
        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.url_bar)

        ads_btn = QAction('Ads', self)
        ads_btn.triggered.connect(self.sub_window.show)
        navbar.addAction(ads_btn)

        
        
        acc = QAction('Account', self)
        acc.triggered.connect(self.show_popup)
        navbar.addAction(acc)          
       
          


        self.browser.urlChanged.connect(self.update_url)

    def navigate_home(self):
        self.browser.setUrl(QUrl('http://google.com'))

    def navigate_to_url(self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))

    def update_url(self, q):
        self.url_bar.setText(q.toString())

    def show_popup(self):
        msg = QMessageBox()
        msg.setWindowTitle("Red") 
        msg.setText("Account details here")
        msg.setDetailedText("details")

        x = msg.exec_()

      
        


class SubWindow(QWidget):
     def __init__(self):
         super(SubWindow, self).__init__()
         self.resize(400, 300)

         # Label
         self.label = QLabel(self)
         self.label.setGeometry(0, 0, 400, 300)
         self.label.setText('View Ads here')
         self.label.setAlignment(Qt.AlignCenter)
         self.label.setStyleSheet('font-size:40px')
 


app = QApplication(sys.argv)
QApplication.setApplicationName('Red')
window = MainWindow()
app.exec_()

