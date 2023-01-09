from supervision import *

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *

from PyQt5 import QtWidgets, QtCore, QtGui

from Custom_Widgets.Widgets import QCustomSlideMenu
from Custom_Widgets.Widgets import QCustomStackedWidget

import resources_rc

from netmiko import ConnectHandler

class Router():
    def __init__(self, device_type,ip,username='', password='', secret=''):
        self.device={'device_type':device_type,
               'host':ip,
               'username':username,
               'password':password,
               'secret':secret
            }
    def interfaceInfo(self):
       net_connect = ConnectHandler(**self.device)
       net_connect.enable()
       output= net_connect.send_command("sh ip int brief")
       return output

    def routeTable(self):
        net_connect = ConnectHandler(**self.device)
        net_connect.enable()
        output=net_connect.send_command("sh ip route")
        return output

    def enableInterface(self,interface):
        net_connect= ConnectHandler(**self.device)
        net_connect.enable()
        config=["interface GigabitEthernet 0/"+str(interface),
        "no shutdown",
         "exit"] 
        output =net_connect.send_config_set(config)     
        return output

    def disableInterface(self,interface): 
        net_connect= ConnectHandler(**self.device)
        net_connect.enable()
        config=["interface GigabitEthernet 0/"+str(interface),
        "shutdown",
         "exit"] 
        output =net_connect.send_config_set(config)     
        return output

    def affecteripint(self,interface,ip_address,mask):
        net_connect= ConnectHandler(**self.device)
        net_connect.enable()
        config=["interface GigabitEthernet 0/"+str(interface),
         "ip address " +str(ip_address)+" "+str(mask),
         'exit']
        output = net_connect.send_config_set(config)
        return output

testRt=Router('cisco_ios_telnet','192.168.3.1','iccn5','ICCN',"ICCN")


class switch():
    def __init__(self,device_type,ip,username,password):
        self.device={
        "device_type":device_type,
        "host":ip,
        "username":username,
        "password":password}

    def affectationdesport(self,n,m,t):
        net_connect= ConnectHandler(**self.device)
        net_connect.enable()
        config=["configure terminal","vlan"+" "+str(m)+" "+str(t)+" "+str(n)]
        output = net_connect.send_config_set(config)
        return output

    def enablePort(self,port):
        net_connect= ConnectHandler(**self.device)
        net_connect.enable()
        config=["configure terminal",
         "interface "+str(port),
         "enable",
         'exit'] 
        output =net_connect.send_config_set(config)
        return output

    def disablePort(self,port):
        net_connect= ConnectHandler(**self.device)
        net_connect.enable()
        config=["configure terminal",
         "interface "+str(port),
        "disable",
        'exit'] 
        output = net_connect.send_config_set(config)
        return output

    def creerVlan(self,n,ip_address,masque):
            net_connect= ConnectHandler(**self.device)
            net_connect.enable()
            config=["configure terminal",
            "vlan"+" "+str(n),
            "ip address"+" "+ip_address +" "+masque] 
            output = net_connect.send_config_set(config)     
            return output

    def supprimerVlan(self,n):
            net_connect= ConnectHandler(**self.device)
            net_connect.enable()
            config=["configure terminal",
            " no vlan"+" "+str(n)] 
            output = net_connect.send_config_set(config)     
            return output

    def tablemac(self):
            net_connect= ConnectHandler(**self.device)
            net_connect.enable()
            output=net_connect.send_command("sh mac")
            return output


    def configinfo(self):
        net_connect= ConnectHandler(**self.device)
        net_connect.enable()
        output=net_connect.send_command("sh running-config")
        return output

    def affectationdesport(self,n,m,t):
        net_connect= ConnectHandler(**self.device)
        net_connect.enable()
        config=["configure terminal","vlan"+" "+str(m)+" "+str(t)+" "+str(n)]
        output = net_connect.send_config_set(config)
        return output

    def removePortFromVlan(self,n,m,t):
        net_connect= ConnectHandler(**self.device)
        net_connect.enable()
        config=["no vlan "+" "+str(m)+" "+str(t)+" "+str(n),
        'exit']
        output = net_connect.send_config_set(config)
        return output

testsw1=switch('hp_procurve_telnet','192.168.1.200','sw1','ICCN')
testsw2=switch('hp_procurve_telnet','192.168.2.200','sw2','ICCN')


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1115, 724)
        MainWindow.setMaximumSize(QSize(1677215, 16777215))
        MainWindow.setStyleSheet(u"*{\n"
"	border: none;\n"
"	background-color: transparent;\n"
"	background: none;\n"
"	padding: 0;\n"
"	margin: 0;\n"
"	color: #fff;\n"
"}\n"
"#centralwidget{\n"
"  background-color:#1f232a;\n"
"}\n"
"#leftmenusub{\n"
"  background-color:#16191d;\n"
"}\n"
"#leftmenusub QPushButton{\n"
"	text-align: left;\n"
"	padding:5px 10px;\n"
"	border-top-left-radius: 10px;\n"
"	border-bottom-left-radius: 10px;\n"
"}\n"
"#headerContainer{\n"
"background-color:#1a1b1e;\n"
"}\n"
"#machinesBtn, #routerBtn, #switchBtn, #rapportBtn, #performenceBtn{\n"
"background-color:#16191d;\n"
"}\n"
"#machinesBtn:hover, #routerBtn:hover, #switchBtn:hover, #rapportBtn:hover, #performenceBtn:hover, #homeBtn:hover, #profilBtn:hover{\n"
"background-color:#2c313c;\n"
"}\n"
"#machinesBtn:checked, #routerBtn:checked, #switchBtn:checked, #rapportBtn:checked, #performenceBtn:checked, #homeBtn:checked, #profilBtn:checked{\n"
"background-color:#2c313c;\n"
"}\n"
"#machinesBtn:pressed, #routerBtn:pressed, #switchBtn:pressed, #rapportBtn:pressed, #perfor"
                        "menceBtn:pressed, #homeBtn:pressed, #profilBtn:pressed{\n"
"background-color:#2c313c;\n"
"}\n"
"\n"
"\n"
"#machinesBtn:released, #routerBtn:released, #switchBtn:released, #rapportBtn:released, #performenceBtn:released, #homeBtn:released, #profilBtn:released{\n"
"background-color:#2c313c;\n"
"}\n"
"#machinesBtn:focus:pressed, #routerBtn:focus:pressed, #switchBtn:focus:pressed, #rapportBtn:focus:pressed, #performenceBtn:focus:pressed, #homeBtn:focus:pressed, #profilBtn:focus:pressed{\n"
"background-color:#2c313c;\n"
"}\n"
"\n"
"#switch1Btn{background-color:#16191d;}\n"
"#switch1Btn:hover{background-color:#2c313c;}\n"
"#switch1Btn:checked{background-color:#2c313c;}\n"
"#switch1Btn:pressed{background-color:#2c313c;}\n"
"#switch1Btn:focus{background-color:#2c313c;}\n"
"#switch1Btn:released{background-color:#2c313c;}\n"
"#switch1Btn:focus:pressed{background-color:#2c313c;}")
        self.go = go
        self.went = went
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.leftmenu = QCustomSlideMenu(self.centralwidget)
        self.leftmenu.setObjectName(u"leftmenu")
        self.leftmenu.setMaximumSize(QSize(55, 16777215))
        self.verticalLayout = QVBoxLayout(self.leftmenu)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.leftmenusub = QWidget(self.leftmenu)
        self.leftmenusub.setObjectName(u"leftmenusub")
        self.verticalLayout_2 = QVBoxLayout(self.leftmenusub)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.leftmenusub)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.menuButton = QPushButton(self.frame)
        self.menuButton.setObjectName(u"menuButton")
        icon = QIcon()
        icon.addFile(u":/icons/icons/align-justify.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.menuButton.setIcon(icon)
        self.menuButton.setIconSize(QSize(35, 35))

        self.verticalLayout_3.addWidget(self.menuButton)


        self.verticalLayout_2.addWidget(self.frame)

        self.frame_2 = QFrame(self.leftmenusub)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 10, 0, 0)
        self.devicesBtn = QPushButton(self.frame_2)
        self.devicesBtn.setObjectName(u"devicesBtn")
        font = QFont()
        font.setPointSize(18)
        self.devicesBtn.setFont(font)
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/codesandbox.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.devicesBtn.setIcon(icon1)
        self.devicesBtn.setIconSize(QSize(35, 35))

        self.verticalLayout_4.addWidget(self.devicesBtn)

        self.switchBtn = QPushButton(self.frame_2)
        self.switchBtn.setObjectName(u"switchBtn")
        font1 = QFont()
        font1.setPointSize(13)
        self.switchBtn.setFont(font1)
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/server.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.switchBtn.setIcon(icon2)
        self.switchBtn.setIconSize(QSize(33, 33))

        self.verticalLayout_4.addWidget(self.switchBtn, 0, Qt.AlignRight)

        self.routerBtn = QPushButton(self.frame_2)
        self.routerBtn.setObjectName(u"routerBtn")
        self.routerBtn.setFont(font1)
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/hard-drive.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.routerBtn.setIcon(icon3)
        self.routerBtn.setIconSize(QSize(33, 33))

        self.verticalLayout_4.addWidget(self.routerBtn, 0, Qt.AlignRight)

        self.machinesBtn = QPushButton(self.frame_2)
        self.machinesBtn.setObjectName(u"machinesBtn")
        self.machinesBtn.setFont(font1)
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/box.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.machinesBtn.setIcon(icon4)
        self.machinesBtn.setIconSize(QSize(33, 33))

        self.verticalLayout_4.addWidget(self.machinesBtn, 0, Qt.AlignRight)


        self.verticalLayout_2.addWidget(self.frame_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.frame_3 = QFrame(self.leftmenusub)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_3)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 35)
        self.rapportBtn = QPushButton(self.frame_3)
        self.rapportBtn.setObjectName(u"rapportBtn")
        self.rapportBtn.setFont(font1)
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/book-open.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.rapportBtn.setIcon(icon5)
        self.rapportBtn.setIconSize(QSize(33, 33))

        self.verticalLayout_5.addWidget(self.rapportBtn, 0, Qt.AlignRight)

        self.performenceBtn = QPushButton(self.frame_3)
        self.performenceBtn.setObjectName(u"performenceBtn")
        self.performenceBtn.setFont(font1)
        icon6 = QIcon()
        icon6.addFile(u":/icons/icons/activity.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.performenceBtn.setIcon(icon6)
        self.performenceBtn.setIconSize(QSize(33, 33))

        self.verticalLayout_5.addWidget(self.performenceBtn, 0, Qt.AlignRight)


        self.verticalLayout_2.addWidget(self.frame_3)


        self.verticalLayout.addWidget(self.leftmenusub, 0, Qt.AlignLeft)


        self.horizontalLayout.addWidget(self.leftmenu)

        self.main = QWidget(self.centralwidget)
        self.main.setObjectName(u"main")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.main.sizePolicy().hasHeightForWidth())
        self.main.setSizePolicy(sizePolicy1)
        self.main.setStyleSheet(u"")
        self.verticalLayout_6 = QVBoxLayout(self.main)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.headerContainer = QWidget(self.main)
        self.headerContainer.setObjectName(u"headerContainer")
        self.horizontalLayout_3 = QHBoxLayout(self.headerContainer)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.headerContainer)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame_4)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(39, 39))
        self.label.setMaximumSize(QSize(39, 39))
        font2 = QFont()
        font2.setPointSize(24)
        font2.setBold(True)
        font2.setWeight(75)
        self.label.setFont(font2)
        self.label.setStyleSheet(u"border-image: url(:/logo/logonn.png);")

        self.horizontalLayout_4.addWidget(self.label)

        self.label_2 = QLabel(self.frame_4)
        self.label_2.setObjectName(u"label_2")
        font3 = QFont()
        font3.setFamily(u"Bahnschrift SemiLight SemiConde")
        font3.setPointSize(24)
        font3.setBold(False)
        font3.setWeight(50)
        self.label_2.setFont(font3)

        self.horizontalLayout_4.addWidget(self.label_2)


        self.horizontalLayout_3.addWidget(self.frame_4, 0, Qt.AlignLeft)

        self.frame_5 = QFrame(self.headerContainer)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_20.setSpacing(0)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.homeBtn = QPushButton(self.frame_5)
        self.homeBtn.setObjectName(u"homeBtn")
        self.homeBtn.setMinimumSize(QSize(39, 39))
        self.homeBtn.setMaximumSize(QSize(39, 39))
        icon7 = QIcon()
        icon7.addFile(u":/icons/icons/home.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.homeBtn.setIcon(icon7)
        self.homeBtn.setIconSize(QSize(32, 32))

        self.horizontalLayout_20.addWidget(self.homeBtn)


        self.horizontalLayout_3.addWidget(self.frame_5, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.frame_6 = QFrame(self.headerContainer)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.minimizeBtn = QPushButton(self.frame_6)
        self.minimizeBtn.setObjectName(u"minimizeBtn")
        icon8 = QIcon()
        icon8.addFile(u":/icons/icons/minus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeBtn.setIcon(icon8)
        self.minimizeBtn.setIconSize(QSize(35, 35))

        self.horizontalLayout_2.addWidget(self.minimizeBtn)

        self.restoreBtn = QPushButton(self.frame_6)
        self.restoreBtn.setObjectName(u"restoreBtn")
        icon9 = QIcon()
        icon9.addFile(u":/icons/icons/square.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.restoreBtn.setIcon(icon9)
        self.restoreBtn.setIconSize(QSize(30, 30))

        self.horizontalLayout_2.addWidget(self.restoreBtn)

        self.closeBtn = QPushButton(self.frame_6)
        self.closeBtn.setObjectName(u"closeBtn")
        icon10 = QIcon()
        icon10.addFile(u":/icons/icons/x.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.closeBtn.setIcon(icon10)
        self.closeBtn.setIconSize(QSize(35, 35))

        self.horizontalLayout_2.addWidget(self.closeBtn)


        self.horizontalLayout_3.addWidget(self.frame_6, 0, Qt.AlignRight)


        self.verticalLayout_6.addWidget(self.headerContainer)

        self.mainBodyContent = QWidget(self.main)
        self.mainBodyContent.setObjectName(u"mainBodyContent")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.mainBodyContent.sizePolicy().hasHeightForWidth())
        self.mainBodyContent.setSizePolicy(sizePolicy2)
        self.mainBodyContent.setStyleSheet(u"background-color: rgb(44, 49, 60);")
        self.verticalLayout_7 = QVBoxLayout(self.mainBodyContent)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.mainPages = QCustomStackedWidget(self.mainBodyContent)
        self.mainPages.setObjectName(u"mainPages")
        self.mainPages.setStyleSheet(u"")
        self.Home = QWidget()
        self.Home.setObjectName(u"Home")
        self.horizontalLayout_19 = QHBoxLayout(self.Home)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.widget_37 = QWidget(self.Home)
        self.widget_37.setObjectName(u"widget_37")
        self.verticalLayout_37 = QVBoxLayout(self.widget_37)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.label_28 = QLabel(self.widget_37)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setMaximumSize(QSize(16777215, 100))
        font4 = QFont()
        font4.setFamily(u"Mongolian Baiti")
        font4.setPointSize(60)
        font4.setBold(True)
        font4.setWeight(75)
        self.label_28.setFont(font4)
        self.label_28.setAlignment(Qt.AlignCenter)

        self.verticalLayout_37.addWidget(self.label_28)

        self.label_29 = QLabel(self.widget_37)
        self.label_29.setObjectName(u"label_29")
        sizePolicy.setHeightForWidth(self.label_29.sizePolicy().hasHeightForWidth())
        self.label_29.setSizePolicy(sizePolicy)
        self.label_29.setMaximumSize(QSize(16777215, 100))
        font5 = QFont()
        font5.setFamily(u"Mongolian Baiti")
        font5.setPointSize(20)
        font5.setStrikeOut(False)
        font5.setKerning(True)
        self.label_29.setFont(font5)
        self.label_29.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.verticalLayout_37.addWidget(self.label_29)


        self.horizontalLayout_19.addWidget(self.widget_37)

        self.mainPages.addWidget(self.Home)
        self.Switch = QWidget()
        self.Switch.setObjectName(u"Switch")
        sizePolicy.setHeightForWidth(self.Switch.sizePolicy().hasHeightForWidth())
        self.Switch.setSizePolicy(sizePolicy)
        self.verticalLayout_8 = QVBoxLayout(self.Switch)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.widget = QWidget(self.Switch)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(1000, 120))
        self.widget.setMaximumSize(QSize(3500, 120))
        self.widget.setStyleSheet(u"background-color:#21252d;\n"
"border-color:1px solid grey;\n"
"border-radius: 8px;\n"
"")
        self.horizontalLayout_7 = QHBoxLayout(self.widget)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy3)
        font6 = QFont()
        font6.setPointSize(30)
        font6.setBold(True)
        font6.setItalic(False)
        font6.setWeight(75)
        self.label_4.setFont(font6)
        self.label_4.setStyleSheet(u"background-color:#16191d;")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.label_4)


        self.verticalLayout_8.addWidget(self.widget, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.widget_2 = QWidget(self.Switch)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy3.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy3)
        self.widget_2.setMinimumSize(QSize(1000, 500))
        self.widget_2.setStyleSheet(u"background-color:#2c313c;\n"
"border-color:1px solid grey;\n"
"border-radius: 8px;")
        self.horizontalLayout_6 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.widget_3 = QWidget(self.widget_2)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setStyleSheet(u"border-color:1px solid grey;\n"
"border-radius: 15px;\n"
"background-color:#2c313c;")
        self.verticalLayout_10 = QVBoxLayout(self.widget_3)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(9, 0, 9, 0)
        self.switch1Btn = QPushButton(self.widget_3)
        self.switch1Btn.setObjectName(u"switch1Btn")
        self.switch1Btn.setMinimumSize(QSize(500, 150))
        self.switch1Btn.setMaximumSize(QSize(500, 150))
        font7 = QFont()
        font7.setPointSize(30)
        font7.setBold(True)
        font7.setWeight(75)
        self.switch1Btn.setFont(font7)
        self.switch1Btn.setStyleSheet(u"QPushButton{background-color:#16191d;}\n"
"\n"
"QPushButton:hover{background-color:#21252d;}\n"
"QPushButton:checked{background-color:#21252d;}\n"
"QPushButton:pressed{background-color:#21252d;}\n"
"QPushButton:released{background-color:#21252d;}\n"
"QPushButton:focus:pressed{background-color:#21252d;}\n"
"\n"
"")
        icon11 = QIcon()
        icon11.addFile(u":/images/network-switch.png", QSize(), QIcon.Normal, QIcon.Off)
        self.switch1Btn.setIcon(icon11)
        self.switch1Btn.setIconSize(QSize(150, 150))

        self.verticalLayout_10.addWidget(self.switch1Btn, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.horizontalLayout_6.addWidget(self.widget_3)

        self.widget_4 = QWidget(self.widget_2)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setStyleSheet(u"background-color:#2c313c;\n"
"border-color:1px solid grey;\n"
"border-radius: 15px;")
        self.verticalLayout_9 = QVBoxLayout(self.widget_4)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(9, 0, 9, 0)
        self.switch2Btn = QPushButton(self.widget_4)
        self.switch2Btn.setObjectName(u"switch2Btn")
        self.switch2Btn.setMinimumSize(QSize(500, 150))
        self.switch2Btn.setMaximumSize(QSize(500, 150))
        self.switch2Btn.setFont(font7)
        self.switch2Btn.setStyleSheet(u"QPushButton{background-color:#16191d;}\n"
"\n"
"QPushButton:hover{background-color:#21252d;}\n"
"QPushButton:checked{background-color:#21252d;}\n"
"QPushButton:pressed{background-color:#21252d;}\n"
"\n"
"QPushButton:released{background-color:#21252d;}\n"
"QPushButton:focus:pressed{background-color:#21252d;}")
        self.switch2Btn.setIcon(icon11)
        self.switch2Btn.setIconSize(QSize(150, 150))

        self.verticalLayout_9.addWidget(self.switch2Btn, 0, Qt.AlignHCenter)


        self.horizontalLayout_6.addWidget(self.widget_4)


        self.verticalLayout_8.addWidget(self.widget_2, 0, Qt.AlignVCenter)

        self.mainPages.addWidget(self.Switch)
        self.Switch1 = QWidget()
        self.Switch1.setObjectName(u"Switch1")
        self.verticalLayout_20 = QVBoxLayout(self.Switch1)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.widget_5 = QWidget(self.Switch1)
        self.widget_5.setObjectName(u"widget_5")
        self.verticalLayout_22 = QVBoxLayout(self.widget_5)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.widget_7 = QWidget(self.widget_5)
        self.widget_7.setObjectName(u"widget_7")
        self.widget_7.setMinimumSize(QSize(123, 250))
        self.widget_7.setMaximumSize(QSize(16777215, 250))
        self.widget_7.setStyleSheet(u"background-color: rgb(44, 49, 60);")
        self.verticalLayout_21 = QVBoxLayout(self.widget_7)
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.widget_7)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setEnabled(True)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        font8 = QFont()
        font8.setPointSize(25)
        font8.setBold(True)
        font8.setWeight(75)
        self.label_3.setFont(font8)

        self.verticalLayout_21.addWidget(self.label_3, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.widget_8 = QWidget(self.widget_7)
        self.widget_8.setObjectName(u"widget_8")
        self.widget_8.setMinimumSize(QSize(780, 0))
        self.widget_8.setMaximumSize(QSize(16777215, 120))
        self.widget_8.setAutoFillBackground(False)
        self.widget_8.setStyleSheet(u"border: 1px solid black;\n"
"border-radius:20px;\n"
"background-color: rgb(208, 208, 208);")
        self.pushButton_49 = QPushButton(self.widget_8)
        self.pushButton_49.setObjectName(u"pushButton_49")
        self.pushButton_49.setGeometry(QRect(10, 10, 51, 49))
        self.pushButton_49.setCheckable(True)
        self.pushButton_49.clicked.connect(self.stat1)
        self.pushButton_49.setStyleSheet(u"QPushButton {background-color: green;\n"
"border-radius:15px;}\n"
"QPushButton:checked{background-color: red;} \n"
"QPushButton:pressed {background-color: red;}\n"
"QPushButton:focus:pressed{ background-color: black; }\n"
"QPushButton:focus{ background-color:red; }\n"
"QPushButton:hover{ background-color:rgb(85, 255, 0); }\n"
"QPushButton:released{background-color:green;}\n"
"\n"
"")
        self.pushButton_50 = QPushButton(self.widget_8)
        self.pushButton_50.setObjectName(u"pushButton_50")
        self.pushButton_50.setGeometry(QRect(70, 10, 51, 49))
        self.pushButton_50.setCheckable(True)
        self.pushButton_50.clicked.connect(self.stat2)
        self.pushButton_50.setStyleSheet(u"QPushButton {background-color: green;\n"
"border-radius:15px;}\n"
"QPushButton:checked{background-color: red;} \n"
"QPushButton:pressed {background-color: red;}\n"
"QPushButton:focus:pressed{ background-color: black; }\n"
"QPushButton:focus{ background-color:red; }\n"
"QPushButton:hover{ background-color:rgb(52, 247, 18); }\n"
"QPushButton:released{background-color:green;}\n"
"")
        self.pushButton_51 = QPushButton(self.widget_8)
        self.pushButton_51.setObjectName(u"pushButton_51")
        self.pushButton_51.setGeometry(QRect(10, 60, 51, 50))
        self.pushButton_51.setCheckable(True)
        self.pushButton_51.clicked.connect(self.stat3)
        self.pushButton_51.setStyleSheet(u"QPushButton {background-color: green;\n"
"border-radius:15px;}\n"
"QPushButton:checked{background-color: red;} \n"
"QPushButton:pressed {background-color: red;}\n"
"QPushButton:focus:pressed{ background-color: black; }\n"
"QPushButton:focus{ background-color:red; }\n"
"QPushButton:hover{ background-color:rgb(52, 247, 18); }\n"
"QPushButton:released{background-color:green;}")
        self.pushButton_52 = QPushButton(self.widget_8)
        self.pushButton_52.setObjectName(u"pushButton_52")
        self.pushButton_52.setGeometry(QRect(70, 60, 51, 50))
        self.pushButton_52.setCheckable(True)
        self.pushButton_52.clicked.connect(self.stat4)
        self.pushButton_52.setStyleSheet(u"QPushButton {background-color: green;\n"
"border-radius:15px;}\n"
"QPushButton:checked{background-color: red;} \n"
"QPushButton:pressed {background-color: red;}\n"
"QPushButton:focus:pressed{ background-color: black; }\n"
"QPushButton:focus{ background-color:red; }\n"
"QPushButton:hover{ background-color:rgb(52, 247, 18); }\n"
"QPushButton:released{background-color:green;}")
        self.pushButton_52.setAutoExclusive(False)
        self.pushButton_52.setAutoDefault(False)
        self.pushButton_52.setFlat(False)
        self.pushButton_53 = QPushButton(self.widget_8)
        self.pushButton_53.setObjectName(u"pushButton_53")
        self.pushButton_53.setCheckable(True)
        self.pushButton_53.setGeometry(QRect(200, 10, 51, 49))
        self.pushButton_53.clicked.connect(self.stat5)
        self.pushButton_53.setStyleSheet(u"QPushButton {background-color: green;\n"
"border-radius:15px;}\n"
"QPushButton:checked{background-color: red;} \n"
"QPushButton:pressed {background-color: red;}\n"
"QPushButton:focus:pressed{ background-color: black; }\n"
"QPushButton:focus{ background-color:red; }\n"
"QPushButton:hover{ background-color:rgb(52, 247, 18); }\n"
"QPushButton:released{background-color:green;}")
        self.pushButton_54 = QPushButton(self.widget_8)
        self.pushButton_54.setObjectName(u"pushButton_54")
        self.pushButton_54.setGeometry(QRect(140, 10, 51, 49))
        self.pushButton_54.setCheckable(True)
        self.pushButton_54.clicked.connect(self.stat6)
        self.pushButton_54.setStyleSheet(u"QPushButton {background-color: green;\n"
"border-radius:15px;}\n"
"QPushButton:checked{background-color: red;} \n"
"QPushButton:pressed {background-color: red;}\n"
"QPushButton:focus:pressed{ background-color: black; }\n"
"QPushButton:focus{ background-color:red; }\n"
"QPushButton:hover{ background-color:rgb(52, 247, 18); }\n"
"QPushButton:released{background-color:green;}")
        self.pushButton_55 = QPushButton(self.widget_8)
        self.pushButton_55.setObjectName(u"pushButton_55")
        self.pushButton_55.setGeometry(QRect(140, 60, 51, 50))
        self.pushButton_55.setCheckable(True)
        self.pushButton_55.clicked.connect(self.stat7)
        self.pushButton_55.setStyleSheet(u"QPushButton {background-color: green;\n"
"border-radius:15px;}\n"
"QPushButton:checked{background-color: red;} \n"
"QPushButton:pressed {background-color: red;}\n"
"QPushButton:focus:pressed{ background-color: black; }\n"
"QPushButton:focus{ background-color:red; }\n"
"QPushButton:hover{ background-color:rgb(52, 247, 18); }\n"
"QPushButton:released{background-color:green;}")
        self.pushButton_56 = QPushButton(self.widget_8)
        self.pushButton_56.setObjectName(u"pushButton_56")
        self.pushButton_56.setGeometry(QRect(200, 60, 51, 50))
        self.pushButton_56.setCheckable(True)
        self.pushButton_56.clicked.connect(self.stat8)
        self.pushButton_56.setStyleSheet(u"QPushButton {background-color: green;\n"
"border-radius:15px;}\n"
"QPushButton:checked{background-color: red;} \n"
"QPushButton:pressed {background-color: red;}\n"
"QPushButton:focus:pressed{ background-color: black; }\n"
"QPushButton:focus{ background-color:red; }\n"
"QPushButton:hover{ background-color:rgb(52, 247, 18); }\n"
"QPushButton:released{background-color:green;}")
        self.pushButton_57 = QPushButton(self.widget_8)
        self.pushButton_57.setObjectName(u"pushButton_57")
        self.pushButton_57.setGeometry(QRect(270, 10, 51, 49))
        self.pushButton_57.setCheckable(True)
        self.pushButton_57.clicked.connect(self.stat9)
        self.pushButton_57.setStyleSheet(u"QPushButton {background-color: green;\n"
"border-radius:15px;}\n"
"QPushButton:checked{background-color: red;} \n"
"QPushButton:pressed {background-color: red;}\n"
"QPushButton:focus:pressed{ background-color: black; }\n"
"QPushButton:focus{ background-color:red; }\n"
"QPushButton:hover{ background-color:rgb(52, 247, 18); }\n"
"QPushButton:released{background-color:green;}")
        self.pushButton_58 = QPushButton(self.widget_8)
        self.pushButton_58.setObjectName(u"pushButton_58")
        self.pushButton_58.setGeometry(QRect(330, 10, 51, 49))
        self.pushButton_58.setCheckable(True)
        self.pushButton_58.clicked.connect(self.stat10)
        self.pushButton_58.setStyleSheet(u"QPushButton {background-color: green;\n"
"border-radius:15px;}\n"
"QPushButton:checked{background-color: red;} \n"
"QPushButton:pressed {background-color: red;}\n"
"QPushButton:focus:pressed{ background-color: black; }\n"
"QPushButton:focus{ background-color:red; }\n"
"QPushButton:hover{ background-color:rgb(52, 247, 18); }\n"
"QPushButton:released{background-color:green;}")
        self.pushButton_59 = QPushButton(self.widget_8)
        self.pushButton_59.setObjectName(u"pushButton_59")
        self.pushButton_59.setGeometry(QRect(270, 60, 51, 50))
        self.pushButton_59.setCheckable(True)
        self.pushButton_59.clicked.connect(self.stat11)
        self.pushButton_59.setStyleSheet(u"QPushButton {background-color: green;\n"
"border-radius:15px;}\n"
"QPushButton:checked{background-color: red;} \n"
"QPushButton:pressed {background-color: red;}\n"
"QPushButton:focus:pressed{ background-color: black; }\n"
"QPushButton:focus{ background-color:red; }\n"
"QPushButton:hover{ background-color:rgb(52, 247, 18); }\n"
"QPushButton:released{background-color:green;}")
        self.pushButton_60 = QPushButton(self.widget_8)
        self.pushButton_60.setObjectName(u"pushButton_60")
        self.pushButton_60.setGeometry(QRect(330, 60, 51, 50))
        self.pushButton_60.setCheckable(True)
        self.pushButton_60.clicked.connect(self.stat12)
        self.pushButton_60.setStyleSheet(u"QPushButton {background-color: green;\n"
"border-radius:15px;}\n"
"QPushButton:checked{background-color: red;} \n"
"QPushButton:pressed {background-color: red;}\n"
"QPushButton:focus:pressed{ background-color: black; }\n"
"QPushButton:focus{ background-color:red; }\n"
"QPushButton:hover{ background-color:rgb(52, 247, 18); }\n"
"QPushButton:released{background-color:green;}")
        self.pushButton_61 = QPushButton(self.widget_8)
        self.pushButton_61.setObjectName(u"pushButton_61")
        self.pushButton_61.setGeometry(QRect(400, 10, 51, 49))
        self.pushButton_61.setCheckable(True)
        self.pushButton_61.clicked.connect(self.stat13)
        self.pushButton_61.setStyleSheet(u"QPushButton {background-color: green;\n"
"border-radius:15px;}\n"
"QPushButton:checked{background-color: red;} \n"
"QPushButton:pressed {background-color: red;}\n"
"QPushButton:focus:pressed{ background-color: black; }\n"
"QPushButton:focus{ background-color:red; }\n"
"QPushButton:hover{ background-color:rgb(52, 247, 18); }\n"
"QPushButton:released{background-color:green;}")
        self.pushButton_62 = QPushButton(self.widget_8)
        self.pushButton_62.setObjectName(u"pushButton_62")
        self.pushButton_62.setGeometry(QRect(460, 10, 51, 49))
        self.pushButton_62.setCheckable(True)
        self.pushButton_62.clicked.connect(self.stat14)
        self.pushButton_62.setStyleSheet(u"QPushButton {background-color: green;\n"
"border-radius:15px;}\n"
"QPushButton:checked{background-color: red;} \n"
"QPushButton:pressed {background-color: red;}\n"
"QPushButton:focus:pressed{ background-color: black; }\n"
"QPushButton:focus{ background-color:red; }\n"
"QPushButton:hover{ background-color:rgb(52, 247, 18); }\n"
"QPushButton:released{background-color:green;}")
        self.pushButton_63 = QPushButton(self.widget_8)
        self.pushButton_63.setObjectName(u"pushButton_63")
        self.pushButton_63.setGeometry(QRect(400, 60, 51, 50))
        self.pushButton_63.setCheckable(True)
        self.pushButton_63.clicked.connect(self.stat15)
        self.pushButton_63.setStyleSheet(u"QPushButton {background-color: green;\n"
"border-radius:15px;}\n"
"QPushButton:checked{background-color: red;} \n"
"QPushButton:pressed {background-color: red;}\n"
"QPushButton:focus:pressed{ background-color: black; }\n"
"QPushButton:focus{ background-color:red; }\n"
"QPushButton:hover{ background-color:rgb(52, 247, 18); }\n"
"QPushButton:released{background-color:green;}")
        self.pushButton_64 = QPushButton(self.widget_8)
        self.pushButton_64.setObjectName(u"pushButton_64")
        self.pushButton_64.setGeometry(QRect(460, 60, 51, 50))
        self.pushButton_64.setCheckable(True)
        self.pushButton_64.clicked.connect(self.stat16)
        self.pushButton_64.setStyleSheet(u"QPushButton {background-color: green;\n"
"border-radius:15px;}\n"
"QPushButton:checked{background-color: red;} \n"
"QPushButton:pressed {background-color: red;}\n"
"QPushButton:focus:pressed{ background-color: black; }\n"
"QPushButton:focus{ background-color:red; }\n"
"QPushButton:hover{ background-color:rgb(52, 247, 18); }\n"
"QPushButton:released{background-color:green;}")
        self.pushButton_65 = QPushButton(self.widget_8)
        self.pushButton_65.setObjectName(u"pushButton_65")
        self.pushButton_65.setGeometry(QRect(530, 10, 51, 49))
        self.pushButton_65.setCheckable(True)
        self.pushButton_65.clicked.connect(self.stat17)
        self.pushButton_65.setStyleSheet(u"QPushButton {background-color: green;\n"
"border-radius:15px;}\n"
"QPushButton:checked{background-color: red;} \n"
"QPushButton:pressed {background-color: red;}\n"
"QPushButton:focus:pressed{ background-color: black; }\n"
"QPushButton:focus{ background-color:red; }\n"
"QPushButton:hover{ background-color:rgb(52, 247, 18); }\n"
"QPushButton:released{background-color:green;}")
        self.pushButton_66 = QPushButton(self.widget_8)
        self.pushButton_66.setObjectName(u"pushButton_66")
        self.pushButton_66.setGeometry(QRect(590, 10, 51, 49))
        self.pushButton_66.setCheckable(True)
        self.pushButton_66.clicked.connect(self.stat18)
        self.pushButton_66.setStyleSheet(u"QPushButton {background-color: green;\n"
"border-radius:15px;}\n"
"QPushButton:checked{background-color: red;} \n"
"QPushButton:pressed {background-color: red;}\n"
"QPushButton:focus:pressed{ background-color: black; }\n"
"QPushButton:focus{ background-color:red; }\n"
"QPushButton:hover{ background-color:rgb(52, 247, 18); }\n"
"QPushButton:released{background-color:green;}")
        self.pushButton_67 = QPushButton(self.widget_8)
        self.pushButton_67.setObjectName(u"pushButton_67")
        self.pushButton_67.setGeometry(QRect(530, 60, 51, 50))
        self.pushButton_67.setCheckable(True)
        self.pushButton_67.clicked.connect(self.stat19)
        self.pushButton_67.setStyleSheet(u"QPushButton {background-color: green;\n"
"border-radius:15px;}\n"
"QPushButton:checked{background-color: red;} \n"
"QPushButton:pressed {background-color: red;}\n"
"QPushButton:focus:pressed{ background-color: black; }\n"
"QPushButton:focus{ background-color:red; }\n"
"QPushButton:hover{ background-color:rgb(52, 247, 18); }\n"
"QPushButton:released{background-color:green;}")
        self.pushButton_68 = QPushButton(self.widget_8)
        self.pushButton_68.setObjectName(u"pushButton_68")
        self.pushButton_68.setGeometry(QRect(590, 60, 51, 50))
        self.pushButton_68.setCheckable(True)
        self.pushButton_68.clicked.connect(self.stat20)
        self.pushButton_68.setStyleSheet(u"QPushButton {background-color: green;\n"
"border-radius:15px;}\n"
"QPushButton:checked{background-color: red;} \n"
"QPushButton:pressed {background-color: red;}\n"
"QPushButton:focus:pressed{ background-color: black; }\n"
"QPushButton:focus{ background-color:red; }\n"
"QPushButton:hover{ background-color:rgb(52, 247, 18); }\n"
"QPushButton:released{background-color:green;}")
        self.pushButton_69 = QPushButton(self.widget_8)
        self.pushButton_69.setObjectName(u"pushButton_69")
        self.pushButton_69.setGeometry(QRect(660, 10, 51, 49))
        self.pushButton_69.setCheckable(True)
        self.pushButton_69.clicked.connect(self.stat21)
        self.pushButton_69.setStyleSheet(u"QPushButton {background-color: green;\n"
"border-radius:15px;}\n"
"QPushButton:checked{background-color: red;} \n"
"QPushButton:pressed {background-color: red;}\n"
"QPushButton:focus:pressed{ background-color: black; }\n"
"QPushButton:focus{ background-color:red; }\n"
"QPushButton:hover{ background-color:rgb(52, 247, 18); }\n"
"QPushButton:released{background-color:green;}")
        self.pushButton_70 = QPushButton(self.widget_8)
        self.pushButton_70.setObjectName(u"pushButton_70")
        self.pushButton_70.setGeometry(QRect(720, 10, 51, 49))
        self.pushButton_70.setCheckable(True)
        self.pushButton_70.clicked.connect(self.stat22)
        self.pushButton_70.setStyleSheet(u"QPushButton {background-color: green;\n"
"border-radius:15px;}\n"
"QPushButton:checked{background-color: red;} \n"
"QPushButton:pressed {background-color: red;}\n"
"QPushButton:focus:pressed{ background-color: black; }\n"
"QPushButton:focus{ background-color:red; }\n"
"QPushButton:hover{ background-color:rgb(52, 247, 18); }\n"
"QPushButton:released{background-color:green;}")
        self.pushButton_71 = QPushButton(self.widget_8)
        self.pushButton_71.setObjectName(u"pushButton_71")
        self.pushButton_71.setCheckable(True)
        self.pushButton_71.clicked.connect(self.stat23)
        self.pushButton_71.setGeometry(QRect(660, 60, 51, 50))
        self.pushButton_71.setStyleSheet(u"QPushButton {background-color: green;\n"
"border-radius:15px;}\n"
"QPushButton:checked{background-color: red;} \n"
"QPushButton:pressed {background-color: red;}\n"
"QPushButton:focus:pressed{ background-color: black; }\n"
"QPushButton:focus{ background-color:red; }\n"
"QPushButton:hover{ background-color:rgb(52, 247, 18); }\n"
"QPushButton:released{background-color:green;}")
        self.pushButton_72 = QPushButton(self.widget_8)
        self.pushButton_72.setObjectName(u"pushButton_72")
        self.pushButton_72.setGeometry(QRect(720, 60, 51, 50))
        self.pushButton_72.setCheckable(True)
        self.pushButton_72.clicked.connect(self.stat24)
        self.pushButton_72.setStyleSheet(u"QPushButton {background-color: green;\n"
"border-radius:15px;}\n"
"QPushButton:checked{background-color: red;} \n"
"QPushButton:pressed {background-color: red;}\n"
"QPushButton:focus:pressed{ background-color: black; }\n"
"QPushButton:focus{ background-color:red; }\n"
"QPushButton:hover{ background-color:rgb(52, 247, 18); }\n"
"QPushButton:released{background-color:green;}")

        self.verticalLayout_21.addWidget(self.widget_8, 0, Qt.AlignHCenter)


        self.verticalLayout_22.addWidget(self.widget_7)

        self.widget_11 = QWidget(self.widget_5)
        self.widget_11.setObjectName(u"widget_11")
        self.widget_11.setMaximumSize(QSize(16777215, 300))
        self.widget_11.setAutoFillBackground(False)
        self.widget_11.setStyleSheet(u"background-color: rgb(44, 49, 60);\n"
"border-color:1px solid grey;\n"
"border-radius: 15px;\n"
"background-color:#2c313c;")
        self.horizontalLayout_10 = QHBoxLayout(self.widget_11)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.vlan1confBtn = QPushButton(self.widget_11)
        self.vlan1confBtn.setObjectName(u"vlan1confBtn")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.vlan1confBtn.sizePolicy().hasHeightForWidth())
        self.vlan1confBtn.setSizePolicy(sizePolicy4)
        self.vlan1confBtn.setMinimumSize(QSize(500, 100))
        self.vlan1confBtn.setMaximumSize(QSize(500, 100))
        font9 = QFont()
        font9.setPointSize(19)
        font9.setBold(True)
        font9.setWeight(75)
        self.vlan1confBtn.setFont(font9)
        self.vlan1confBtn.setStyleSheet(u"QPushButton{background-color:#16191d;}\n"
"\n"
"QPushButton:hover{background-color:#21252d;}\n"
"QPushButton:checked{background-color:#21252d;}\n"
"QPushButton:pressed{background-color:#21252d;}\n"
"\n"
"QPushButton:released{background-color:#21252d;}\n"
"QPushButton:focus:pressed{background-color:#21252d;}")

        self.horizontalLayout_10.addWidget(self.vlan1confBtn)

        self.infoSwt1Btn = QPushButton(self.widget_11)
        self.infoSwt1Btn.setObjectName(u"infoSwt1Btn")
        self.infoSwt1Btn.setMinimumSize(QSize(500, 100))
        self.infoSwt1Btn.setMaximumSize(QSize(500, 100))
        self.infoSwt1Btn.setFont(font9)
        self.infoSwt1Btn.setStyleSheet(u"QPushButton{background-color:#16191d;}\n"
"\n"
"QPushButton:hover{background-color:#21252d;}\n"
"QPushButton:checked{background-color:#21252d;}\n"
"QPushButton:pressed{background-color:#21252d;}\n"
"\n"
"QPushButton:released{background-color:#21252d;}\n"
"QPushButton:focus:pressed{background-color:#21252d;}\n"
"")

        self.horizontalLayout_10.addWidget(self.infoSwt1Btn)


        self.verticalLayout_22.addWidget(self.widget_11)


        self.verticalLayout_20.addWidget(self.widget_5)

        self.mainPages.addWidget(self.Switch1)
        self.vlan1 = QWidget()
        self.vlan1.setObjectName(u"vlan1")
        self.verticalLayout_15 = QVBoxLayout(self.vlan1)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.widget_6 = QWidget(self.vlan1)
        self.widget_6.setObjectName(u"widget_6")
        self.verticalLayout_18 = QVBoxLayout(self.widget_6)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.return1 = QPushButton(self.widget_6)
        self.return1.setObjectName(u"return1")
        self.return1.setMinimumSize(QSize(25, 25))
        self.return1.setMaximumSize(QSize(25, 25))
        self.return1.setStyleSheet(u"background-color:#21252d;\n"
"")
        icon12 = QIcon()
        icon12.addFile(u":/icons/icons/chevron-left.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.return1.setIcon(icon12)

        self.verticalLayout_18.addWidget(self.return1)

        self.widget_19 = QWidget(self.widget_6)
        self.widget_19.setObjectName(u"widget_19")
        self.widget_19.setMinimumSize(QSize(600, 100))
        self.widget_19.setMaximumSize(QSize(950, 100))
        self.widget_19.setStyleSheet(u"background-color:#21252d;\n"
"border-color:1px solid grey;\n"
"border-radius: 15px;\n"
"")
        self.verticalLayout_19 = QVBoxLayout(self.widget_19)
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.label_11 = QLabel(self.widget_19)
        self.label_11.setObjectName(u"label_11")
        font10 = QFont()
        font10.setPointSize(20)
        font10.setBold(True)
        font10.setWeight(75)
        self.label_11.setFont(font10)
        self.label_11.setAlignment(Qt.AlignCenter)

        self.verticalLayout_19.addWidget(self.label_11)


        self.verticalLayout_18.addWidget(self.widget_19, 0, Qt.AlignHCenter)

        self.widget_18 = QWidget(self.widget_6)
        self.widget_18.setObjectName(u"widget_18")
        self.widget_18.setMinimumSize(QSize(950, 200))
        self.widget_18.setMaximumSize(QSize(1000, 200))
        self.widget_18.setStyleSheet(u"background-color:#21252d;\n"
"border-color:1px solid grey;\n"
"border-radius: 15px;")
        self.horizontalLayout_13 = QHBoxLayout(self.widget_18)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.widget_27 = QWidget(self.widget_18)
        self.widget_27.setObjectName(u"widget_27")
        self.verticalLayout_33 = QVBoxLayout(self.widget_27)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.widget_29 = QWidget(self.widget_27)
        self.widget_29.setObjectName(u"widget_29")
        self.widget_29.setMaximumSize(QSize(16777215, 45))
        self.horizontalLayout_15 = QHBoxLayout(self.widget_29)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_21 = QLabel(self.widget_29)
        self.label_21.setObjectName(u"label_21")
        font11 = QFont()
        font11.setPointSize(15)
        self.label_21.setFont(font11)
        self.label_21.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_15.addWidget(self.label_21)

        self.label_22 = QLabel(self.widget_29)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setFont(font11)
        self.label_22.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_15.addWidget(self.label_22)

        self.label_23 = QLabel(self.widget_29)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setFont(font11)
        self.label_23.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_15.addWidget(self.label_23)


        self.verticalLayout_33.addWidget(self.widget_29)

        self.widget_30 = QWidget(self.widget_27)
        self.widget_30.setObjectName(u"widget_30")
        self.horizontalLayout_14 = QHBoxLayout(self.widget_30)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.spinBox = QSpinBox(self.widget_30)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setMinimumSize(QSize(200, 40))
        self.spinBox.setMaximumSize(QSize(200, 40))
        self.spinBox.setFont(font)
        self.spinBox.setStyleSheet(u"background-color:#2c313c;\n"
"border-radius: 5px;")
        self.spinBox.setMaximum(100)
        self.spinBox.setSingleStep(10)

        self.horizontalLayout_14.addWidget(self.spinBox, 0, Qt.AlignTop)

        self.lineEdit = QLineEdit(self.widget_30)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(200, 40))
        self.lineEdit.setMaximumSize(QSize(200, 40))
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet(u"background-color:#2c313c;\n"
"border-radius: 5px;")

        self.horizontalLayout_14.addWidget(self.lineEdit, 0, Qt.AlignTop)

        self.lineEdit_2 = QLineEdit(self.widget_30)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMinimumSize(QSize(200, 40))
        self.lineEdit_2.setMaximumSize(QSize(200, 40))
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet(u"background-color:#2c313c;\n"
"border-radius: 5px;")

        self.horizontalLayout_14.addWidget(self.lineEdit_2, 0, Qt.AlignTop)


        self.verticalLayout_33.addWidget(self.widget_30)


        self.horizontalLayout_13.addWidget(self.widget_27)

        self.widget_28 = QWidget(self.widget_18)
        self.widget_28.setObjectName(u"widget_28")
        self.widget_28.setMinimumSize(QSize(250, 0))
        self.widget_28.setMaximumSize(QSize(250, 16777215))
        self.verticalLayout_32 = QVBoxLayout(self.widget_28)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.pushButton_2 = QPushButton(self.widget_28)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(200, 40))
        self.pushButton_2.setMaximumSize(QSize(200, 40))
        self.pushButton_2.clicked.connect(self.addvlan)
        self.pushButton_2.clicked.connect(self.addtobox)
        self.pushButton_2.setStyleSheet(u"QPushButton{background-color:#2c313c;}\n"
"\n"
"QPushButton:hover{background-color:#16191d;}\n"
"QPushButton:checked{background-color:#16191d;}\n"
"QPushButton:pressed{background-color:#16191d;}\n"
"\n"
"QPushButton:released{background-color:#16191d;}\n"
"QPushButton:focus:pressed{background-color:#16191d;}")

        self.verticalLayout_32.addWidget(self.pushButton_2, 0, Qt.AlignRight)

        self.pushButton_3 = QPushButton(self.widget_28)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(200, 40))
        self.pushButton_3.setMaximumSize(QSize(200, 40))
        self.pushButton_3.clicked.connect(self.delvlan)
        self.pushButton_3.clicked.connect(self.removefrombox)
        self.pushButton_3.setStyleSheet(u"QPushButton{background-color:#2c313c;}\n"
"\n"
"QPushButton:hover{background-color:#16191d;}\n"
"\n"
"QPushButton:pressed{background-color:#16191d;}\n"
"\n"
"QPushButton:checked{background-color:#16191d;}\n"
"\n"
"QPushButton:focus:pressed{background-color:#16191d;}\n"
"\n"
"\n"
"QPushButton:released{background-color:#2c313c;}\n"
"\n"
"")

        self.verticalLayout_32.addWidget(self.pushButton_3, 0, Qt.AlignRight)

        self.pushButton_8 = QPushButton(self.widget_28)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setMinimumSize(QSize(200, 40))
        self.pushButton_8.setMaximumSize(QSize(200, 40))
        self.pushButton_8.setStyleSheet(u"QPushButton{background-color:#2c313c;}\n"
"\n"
"QPushButton:hover{background-color:#16191d;}\n"
"QPushButton:checked{background-color:#16191d;}\n"
"QPushButton:pressed{background-color:#16191d;}\n"
"\n"
"QPushButton:released{background-color:#16191d;}\n"
"QPushButton:focus:pressed{background-color:#16191d;}")

        self.verticalLayout_32.addWidget(self.pushButton_8, 0, Qt.AlignRight)


        self.horizontalLayout_13.addWidget(self.widget_28)


        self.verticalLayout_18.addWidget(self.widget_18, 0, Qt.AlignHCenter)

        self.widget_17 = QWidget(self.widget_6)
        self.widget_17.setObjectName(u"widget_17")
        self.widget_17.setMinimumSize(QSize(600, 100))
        self.widget_17.setMaximumSize(QSize(950, 100))
        self.widget_17.setStyleSheet(u"background-color:#21252d;\n"
"border-color:1px solid grey;\n"
"border-radius: 15px;\n"
"")
        self.verticalLayout_31 = QVBoxLayout(self.widget_17)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.label_10 = QLabel(self.widget_17)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font10)
        self.label_10.setAlignment(Qt.AlignCenter)

        self.verticalLayout_31.addWidget(self.label_10)


        self.verticalLayout_18.addWidget(self.widget_17, 0, Qt.AlignHCenter)

        self.widget_12 = QWidget(self.widget_6)
        self.widget_12.setObjectName(u"widget_12")
        self.widget_12.setMinimumSize(QSize(950, 200))
        self.widget_12.setMaximumSize(QSize(1000, 200))
        self.widget_12.setStyleSheet(u"background-color:#21252d;\n"
"border-color:1px solid grey;\n"
"border-radius: 15px;")
        self.verticalLayout_26 = QVBoxLayout(self.widget_12)
        self.verticalLayout_26.setSpacing(5)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(12, 0, 12, 3)
        self.widget_21 = QWidget(self.widget_12)
        self.widget_21.setObjectName(u"widget_21")
        self.widget_21.setMaximumSize(QSize(650, 50))
        self.horizontalLayout_8 = QHBoxLayout(self.widget_21)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_12 = QLabel(self.widget_21)
        self.label_12.setObjectName(u"label_12")
        font12 = QFont()
        font12.setPointSize(12)
        font12.setBold(True)
        font12.setWeight(75)
        self.label_12.setFont(font12)

        self.horizontalLayout_8.addWidget(self.label_12, 0, Qt.AlignHCenter)

        self.label_13 = QLabel(self.widget_21)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font12)

        self.horizontalLayout_8.addWidget(self.label_13, 0, Qt.AlignHCenter)

        self.label_15 = QLabel(self.widget_21)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font12)

        self.horizontalLayout_8.addWidget(self.label_15, 0, Qt.AlignHCenter)


        self.verticalLayout_26.addWidget(self.widget_21)

        self.widget_20 = QWidget(self.widget_12)
        self.widget_20.setObjectName(u"widget_20")
        self.widget_20.setMaximumSize(QSize(16777215, 150))
        self.horizontalLayout_5 = QHBoxLayout(self.widget_20)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.widget_50 = QWidget(self.widget_20)
        self.widget_50.setObjectName(u"widget_50")
        self.widget_50.setMinimumSize(QSize(0, 80))
        self.widget_50.setMaximumSize(QSize(16777215, 80))
        self.horizontalLayout_28 = QHBoxLayout(self.widget_50)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.comboBox_1 = QComboBox(self.widget_50)
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.setObjectName(u"comboBox_1")
        self.comboBox_1.setMinimumSize(QSize(180, 42))
        self.comboBox_1.setMaximumSize(QSize(180, 42))
        self.comboBox_1.setFont(font11)
        self.comboBox_1.setStyleSheet(u"background-color:#2c313c;\n"
"")

        self.horizontalLayout_28.addWidget(self.comboBox_1)

        self.comboBox_2 = QComboBox(self.widget_50)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setMinimumSize(QSize(180, 42))
        self.comboBox_2.setMaximumSize(QSize(180, 42))
        self.comboBox_2.setFont(font11)
        self.comboBox_2.setStyleSheet(u"background-color:#2c313c;\n"
"")

        self.horizontalLayout_28.addWidget(self.comboBox_2)

        self.comboBox_4 = QComboBox(self.widget_50)
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.setObjectName(u"comboBox_4")
        self.comboBox_4.setMinimumSize(QSize(200, 42))
        self.comboBox_4.setMaximumSize(QSize(200, 42))
        self.comboBox_4.setFont(font11)
        self.comboBox_4.setStyleSheet(u"background-color:#2c313c;\n"
"")

        self.horizontalLayout_28.addWidget(self.comboBox_4)


        self.horizontalLayout_5.addWidget(self.widget_50, 0, Qt.AlignTop)

        self.widget_49 = QWidget(self.widget_20)
        self.widget_49.setObjectName(u"widget_49")
        self.widget_49.setMinimumSize(QSize(250, 100))
        self.widget_49.setMaximumSize(QSize(250, 16777215))
        self.verticalLayout_47 = QVBoxLayout(self.widget_49)
        self.verticalLayout_47.setObjectName(u"verticalLayout_47")
        self.selectBtn = QPushButton(self.widget_49)
        self.selectBtn.setObjectName(u"selectBtn")
        self.selectBtn.setMinimumSize(QSize(200, 40))
        self.selectBtn.setMaximumSize(QSize(200, 40))
        font13 = QFont()
        font13.setFamily(u"Arial")
        font13.setPointSize(8)
        font13.setBold(False)
        font13.setUnderline(False)
        font13.setWeight(50)
        font13.setStrikeOut(False)
        font13.setKerning(True)
        self.selectBtn.setFont(font13)
        self.selectBtn.clicked.connect(self.getvlan)
        self.selectBtn.setStyleSheet(u"QPushButton{background-color:#2c313c;}\n"
"\n"
"QPushButton:hover{background-color:#16191d;}\n"
"QPushButton:checked{background-color:#16191d;}\n"
"QPushButton:pressed{background-color:#16191d;}\n"
"QPushButton:released{background-color:#16191d;}\n"
"QPushButton:focus:pressed{background-color:#16191d;}\n"
"")

        self.verticalLayout_47.addWidget(self.selectBtn, 0, Qt.AlignHCenter)

        self.delport1 = QPushButton(self.widget_49)
        self.delport1.setObjectName(u"delport1")
        self.delport1.setMinimumSize(QSize(200, 40))
        self.delport1.setMaximumSize(QSize(200, 40))
        self.delport1.clicked.connect(self.delport)
        self.delport1.setStyleSheet(u"QPushButton{background-color:#2c313c;}\n"
"\n"
"QPushButton:hover{background-color:#16191d;}\n"
"\n"
"QPushButton:pressed{background-color:#16191d;}\n"
"\n"
"QPushButton:checked{background-color:#16191d;}\n"
"\n"
"QPushButton:focus:pressed{background-color:#16191d;}\n"
"\n"
"\n"
"QPushButton:released{background-color:#2c313c;}\n"
"\n"
"")

        self.verticalLayout_47.addWidget(self.delport1, 0, Qt.AlignHCenter)


        self.horizontalLayout_5.addWidget(self.widget_49)


        self.verticalLayout_26.addWidget(self.widget_20)


        self.verticalLayout_18.addWidget(self.widget_12, 0, Qt.AlignHCenter)


        self.verticalLayout_15.addWidget(self.widget_6)

        self.mainPages.addWidget(self.vlan1)
        self.InfoSwitch1 = QWidget()
        self.InfoSwitch1.setObjectName(u"InfoSwitch1")
        self.verticalLayout_38 = QVBoxLayout(self.InfoSwitch1)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.widget_38 = QWidget(self.InfoSwitch1)
        self.widget_38.setObjectName(u"widget_38")
        self.verticalLayout_27 = QVBoxLayout(self.widget_38)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.return2 = QPushButton(self.widget_38)
        self.return2.setObjectName(u"return2")
        self.return2.setMinimumSize(QSize(25, 25))
        self.return2.setMaximumSize(QSize(25, 25))
        self.return2.setStyleSheet(u"background-color:#21252d;\n"
"")
        self.return2.setIcon(icon12)

        self.verticalLayout_27.addWidget(self.return2)

        self.widget_40 = QWidget(self.widget_38)
        self.widget_40.setObjectName(u"widget_40")
        self.widget_40.setMinimumSize(QSize(0, 80))
        self.widget_40.setMaximumSize(QSize(16777215, 80))
        self.widget_40.setStyleSheet(u"border-radius: 15px;")
        self.horizontalLayout_21 = QHBoxLayout(self.widget_40)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.label_30 = QLabel(self.widget_40)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setMinimumSize(QSize(800, 60))
        self.label_30.setMaximumSize(QSize(800, 60))
        font14 = QFont()
        font14.setPointSize(20)
        self.label_30.setFont(font14)
        self.label_30.setStyleSheet(u"background-color:#21252d;\n"
"border-radius: 15px;")
        self.label_30.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_21.addWidget(self.label_30)

        self.getmactable1Btn = QPushButton(self.widget_40)
        self.getmactable1Btn.setObjectName(u"getmactable1Btn")
        self.getmactable1Btn.setMinimumSize(QSize(150, 60))
        self.getmactable1Btn.setMaximumSize(QSize(150, 50))
        self.getmactable1Btn.setFont(font11)
        self.getmactable1Btn.clicked.connect(self.table1)
        self.getmactable1Btn.setStyleSheet(u"\n"
"\n"
"QPushButton{background-color:#21252d;}\n"
"\n"
"QPushButton:hover{background-color:#16191d;}\n"
"QPushButton:checked{background-color:#16191d;}\n"
"QPushButton:pressed{background-color:#16191d;}\n"
"\n"
"QPushButton:released{background-color:#16191d;}\n"
"QPushButton:focus:pressed{background-color:#16191d;}\n"
"\n"
"")

        self.horizontalLayout_21.addWidget(self.getmactable1Btn, 0, Qt.AlignTop)


        self.verticalLayout_27.addWidget(self.widget_40)

        self.widget_39 = QWidget(self.widget_38)
        self.widget_39.setObjectName(u"widget_39")
        self.widget_39.setMinimumSize(QSize(0, 80))
        self.widget_39.setMaximumSize(QSize(1677215, 80))
        self.widget_39.setStyleSheet(u"border-radius: 15px;")
        self.horizontalLayout_22 = QHBoxLayout(self.widget_39)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.label_31 = QLabel(self.widget_39)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setMinimumSize(QSize(800, 60))
        self.label_31.setMaximumSize(QSize(800, 60))
        self.label_31.setFont(font14)
        self.label_31.setStyleSheet(u"background-color:#21252d;\n"
"border-radius: 15px;")
        self.label_31.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_22.addWidget(self.label_31, 0, Qt.AlignTop)

        self.getconf1Btn = QPushButton(self.widget_39)
        self.getconf1Btn.setObjectName(u"getconf1Btn")
        self.getconf1Btn.setMinimumSize(QSize(150, 60))
        self.getconf1Btn.setMaximumSize(QSize(150, 60))
        self.getconf1Btn.setFont(font11)
        self.getconf1Btn.clicked.connect(self.conf1)
        self.getconf1Btn.setStyleSheet(u"\n"
"\n"
"QPushButton{background-color:#21252d;}\n"
"\n"
"QPushButton:hover{background-color:#16191d;}\n"
"QPushButton:checked{background-color:#16191d;}\n"
"QPushButton:pressed{background-color:#16191d;}\n"
"\n"
"QPushButton:released{background-color:#16191d;}\n"
"QPushButton:focus:pressed{background-color:#16191d;}\n"
"\n"
"")

        self.horizontalLayout_22.addWidget(self.getconf1Btn, 0, Qt.AlignTop)


        self.verticalLayout_27.addWidget(self.widget_39)

        self.pushButton_6 = QPushButton(self.widget_38)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.verticalLayout_27.addWidget(self.pushButton_6)

        self.pushButton_5 = QPushButton(self.widget_38)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.verticalLayout_27.addWidget(self.pushButton_5)


        self.verticalLayout_38.addWidget(self.widget_38)

        self.mainPages.addWidget(self.InfoSwitch1)
        self.tablemac1 = QWidget()
        self.tablemac1.setObjectName(u"tablemac1")
        self.horizontalLayout_24 = QHBoxLayout(self.tablemac1)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.widget_45 = QWidget(self.tablemac1)
        self.widget_45.setObjectName(u"widget_45")
        self.verticalLayout_40 = QVBoxLayout(self.widget_45)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.return3 = QPushButton(self.widget_45)
        self.return3.setObjectName(u"return3")
        self.return3.setMinimumSize(QSize(25, 25))
        self.return3.setMaximumSize(QSize(25, 25))
        self.return3.setStyleSheet(u"background-color:#21252d;\n"
"")
        self.return3.setIcon(icon12)

        self.verticalLayout_40.addWidget(self.return3)

        self.label_33 = QLabel(self.widget_45)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setMinimumSize(QSize(800, 60))
        self.label_33.setMaximumSize(QSize(800, 60))
        self.label_33.setFont(font10)
        self.label_33.setStyleSheet(u"background-color:#21252d;\n"
"border-radius: 15px;")
        self.label_33.setAlignment(Qt.AlignCenter)

        self.verticalLayout_40.addWidget(self.label_33, 0, Qt.AlignHCenter)

        self.textEdit = QTextEdit(self.widget_45)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMinimumSize(QSize(900, 500))
        self.textEdit.setMaximumSize(QSize(900, 500))
        font15 = QFont()
        font15.setFamily(u"Terminal")
        font15.setPointSize(18)
        font15.setBold(True)
        font15.setWeight(75)
        self.textEdit.setFont(font15)
        self.textEdit.setStyleSheet(u"background-color:#21252d;\n"
"border-radius: 15px;")
        self.textEdit.setReadOnly(True)

        self.verticalLayout_40.addWidget(self.textEdit, 0, Qt.AlignHCenter)


        self.horizontalLayout_24.addWidget(self.widget_45)

        self.mainPages.addWidget(self.tablemac1)
        self.configuration1 = QWidget()
        self.configuration1.setObjectName(u"configuration1")
        self.horizontalLayout_25 = QHBoxLayout(self.configuration1)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.widget_46 = QWidget(self.configuration1)
        self.widget_46.setObjectName(u"widget_46")
        self.verticalLayout_41 = QVBoxLayout(self.widget_46)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.return4 = QPushButton(self.widget_46)
        self.return4.setObjectName(u"return4")
        self.return4.setMinimumSize(QSize(25, 25))
        self.return4.setMaximumSize(QSize(25, 25))
        self.return4.setStyleSheet(u"background-color:#21252d;\n"
"")
        self.return4.setIcon(icon12)

        self.verticalLayout_41.addWidget(self.return4)

        self.label_34 = QLabel(self.widget_46)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setMinimumSize(QSize(800, 60))
        self.label_34.setMaximumSize(QSize(800, 60))
        self.label_34.setFont(font10)
        self.label_34.setStyleSheet(u"background-color:#21252d;\n"
"border-radius: 15px;")
        self.label_34.setAlignment(Qt.AlignCenter)

        self.verticalLayout_41.addWidget(self.label_34, 0, Qt.AlignHCenter)

        self.textEdit_4 = QTextEdit(self.widget_46)
        self.textEdit_4.setObjectName(u"textEdit_4")
        self.textEdit_4.setMinimumSize(QSize(950, 500))
        self.textEdit_4.setMaximumSize(QSize(950, 500))
        font16 = QFont()
        font16.setFamily(u"Terminal")
        font16.setPointSize(15)
        self.textEdit_4.setFont(font16)
        self.textEdit_4.setStyleSheet(u"background-color:#21252d;\n"
"border-radius: 15px;")

        self.verticalLayout_41.addWidget(self.textEdit_4, 0, Qt.AlignHCenter)


        self.horizontalLayout_25.addWidget(self.widget_46)

        self.mainPages.addWidget(self.configuration1)
        self.Switch2 = QWidget()
        self.Switch2.setObjectName(u"Switch2")
        self.verticalLayout_23 = QVBoxLayout(self.Switch2)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.widget_13 = QWidget(self.Switch2)
        self.widget_13.setObjectName(u"widget_13")
        self.verticalLayout_24 = QVBoxLayout(self.widget_13)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.widget_14 = QWidget(self.widget_13)
        self.widget_14.setObjectName(u"widget_14")
        self.widget_14.setMinimumSize(QSize(123, 250))
        self.widget_14.setMaximumSize(QSize(16777215, 250))
        self.widget_14.setStyleSheet(u"background-color: rgb(44, 49, 60);")
        self.verticalLayout_25 = QVBoxLayout(self.widget_14)
        self.verticalLayout_25.setSpacing(0)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.widget_14)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setEnabled(True)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setFont(font8)

        self.verticalLayout_25.addWidget(self.label_5, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.widget_15 = QWidget(self.widget_14)
        self.widget_15.setObjectName(u"widget_15")
        self.widget_15.setMinimumSize(QSize(780, 0))
        self.widget_15.setMaximumSize(QSize(16777215, 120))
        self.widget_15.setAutoFillBackground(False)
        self.widget_15.setStyleSheet(u"border: 1px solid black;\n"
"border-radius:20px;\n"
"background-color: rgb(208, 208, 208);")
        self.pushButton_73 = QPushButton(self.widget_15)
        self.pushButton_73.setObjectName(u"pushButton_73")
        self.pushButton_73.setGeometry(QRect(10, 10, 51, 49))
        self.pushButton_73.setCheckable(True)
        self.pushButton_73.clicked.connect(self.stat25)
        self.pushButton_73.setStyleSheet(u"QPushButton {background-color: green;\n"
"border-radius:15px;}\n"
"QPushButton:checked{background-color: red;} \n"
"QPushButton:pressed {background-color: red;}\n"
"QPushButton:focus:pressed{ background-color: black; }\n"
"QPushButton:focus{ background-color:red; }\n"
"QPushButton:hover{ background-color:rgb(85, 255, 0); }\n"
"QPushButton:released{background-color:green;}\n"
"\n"
"")
        self.pushButton_74 = QPushButton(self.widget_15)
        self.pushButton_74.setObjectName(u"pushButton_74")
        self.pushButton_74.setGeometry(QRect(70, 10, 51, 49))
        self.pushButton_74.setCheckable(True)
        self.pushButton_74.clicked.connect(self.stat26)
        self.pushButton_74.setStyleSheet(u"QPushButton {background-color: green;\n"
"border-radius:15px;}\n"
"QPushButton:checked{background-color: red;} \n"
"QPushButton:pressed {background-color: red;}\n"
"QPushButton:focus:pressed{ background-color: black; }\n"
"QPushButton:focus{ background-color:red; }\n"
"QPushButton:hover{ background-color:rgb(52, 247, 18); }\n"
"QPushButton:released{background-color:green;}\n"
"")
        self.pushButton_75 = QPushButton(self.widget_15)
        self.pushButton_75.setObjectName(u"pushButton_75")
        self.pushButton_75.setGeometry(QRect(10, 60, 51, 50))
        self.pushButton_75.setCheckable(True)
        self.pushButton_75.clicked.connect(self.stat27)
        self.pushButton_75.setStyleSheet(u"QPushButton {background-color: green;\n"
"border-radius:15px;}\n"
"QPushButton:checked{background-color: red;} \n"
"QPushButton:pressed {background-color: red;}\n"
"QPushButton:focus:pressed{ background-color: black; }\n"
"QPushButton:focus{ background-color:red; }\n"
"QPushButton:hover{ background-color:rgb(52, 247, 18); }\n"
"QPushButton:released{background-color:green;}")
        self.pushButton_76 = QPushButton(self.widget_15)
        self.pushButton_76.setObjectName(u"pushButton_76")
        self.pushButton_76.setGeometry(QRect(70, 60, 51, 50))
        self.pushButton_76.setCheckable(True)
        self.pushButton_76.clicked.connect(self.stat28)
        self.pushButton_76.setStyleSheet(u"QPushButton {background-color: green;\n"
"border-radius:15px;}\n"
"QPushButton:checked{background-color: red;} \n"
"QPushButton:pressed {background-color: red;}\n"
"QPushButton:focus:pressed{ background-color: black; }\n"
"QPushButton:focus{ background-color:red; }\n"
"QPushButton:hover{ background-color:rgb(52, 247, 18); }\n"
"QPushButton:released{background-color:green;}")
        self.pushButton_76.setAutoExclusive(False)
        self.pushButton_76.setAutoDefault(False)
        self.pushButton_76.setFlat(False)
        self.pushButton_77 = QPushButton(self.widget_15)
        self.pushButton_77.setObjectName(u"pushButton_77")
        self.pushButton_77.setGeometry(QRect(200, 10, 51, 49))
        self.pushButton_77.setCheckable(True)
        self.pushButton_77.clicked.connect(self.stat29)
        self.pushButton_77.setStyleSheet(u"QPushButton {background-color: green;\n"
"border-radius:15px;}\n"
"QPushButton:checked{background-color: red;} \n"
"QPushButton:pressed {background-color: red;}\n"
"QPushButton:focus:pressed{ background-color: black; }\n"
"QPushButton:focus{ background-color:red; }\n"
"QPushButton:hover{ background-color:rgb(52, 247, 18); }\n"
"QPushButton:released{background-color:green;}")
        self.pushButton_78 = QPushButton(self.widget_15)
        self.pushButton_78.setObjectName(u"pushButton_78")
        self.pushButton_78.setGeometry(QRect(140, 10, 51, 49))
        self.pushButton_78.setCheckable(True)
        self.pushButton_78.clicked.connect(self.stat30)
        self.pushButton_78.setStyleSheet(u"QPushButton {background-color: green;\n"
"border-radius:15px;}\n"
"QPushButton:checked{background-color: red;} \n"
"QPushButton:pressed {background-color: red;}\n"
"QPushButton:focus:pressed{ background-color: black; }\n"
"QPushButton:focus{ background-color:red; }\n"
"QPushButton:hover{ background-color:rgb(52, 247, 18); }\n"
"QPushButton:released{background-color:green;}")
        self.pushButton_79 = QPushButton(self.widget_15)
        self.pushButton_79.setObjectName(u"pushButton_79")
        self.pushButton_79.setGeometry(QRect(140, 60, 51, 50))
        self.pushButton_79.setCheckable(True)
        self.pushButton_79.clicked.connect(self.stat31)
        self.pushButton_79.setStyleSheet(u"QPushButton {background-color: green;\n"
"border-radius:15px;}\n"
"QPushButton:checked{background-color: red;} \n"
"QPushButton:pressed {background-color: red;}\n"
"QPushButton:focus:pressed{ background-color: black; }\n"
"QPushButton:focus{ background-color:red; }\n"
"QPushButton:hover{ background-color:rgb(52, 247, 18); }\n"
"QPushButton:released{background-color:green;}")
        self.pushButton_80 = QPushButton(self.widget_15)
        self.pushButton_80.setObjectName(u"pushButton_80")
        self.pushButton_80.setGeometry(QRect(200, 60, 51, 50))
        self.pushButton_80.setCheckable(True)
        self.pushButton_80.clicked.connect(self.stat32)
        self.pushButton_80.setStyleSheet(u"QPushButton {background-color: green;\n"
"border-radius:15px;}\n"
"QPushButton:checked{background-color: red;} \n"
"QPushButton:pressed {background-color: red;}\n"
"QPushButton:focus:pressed{ background-color: black; }\n"
"QPushButton:focus{ background-color:red; }\n"
"QPushButton:hover{ background-color:rgb(52, 247, 18); }\n"
"QPushButton:released{background-color:green;}")
        self.pushButton_81 = QPushButton(self.widget_15)
        self.pushButton_81.setObjectName(u"pushButton_81")
        self.pushButton_81.setGeometry(QRect(270, 10, 51, 49))
        self.pushButton_81.setCheckable(True)
        self.pushButton_81.clicked.connect(self.stat33)
        self.pushButton_81.setStyleSheet(u"QPushButton {background-color: green;\n"
"border-radius:15px;}\n"
"QPushButton:checked{background-color: red;} \n"
"QPushButton:pressed {background-color: red;}\n"
"QPushButton:focus:pressed{ background-color: black; }\n"
"QPushButton:focus{ background-color:red; }\n"
"QPushButton:hover{ background-color:rgb(52, 247, 18); }\n"
"QPushButton:released{background-color:green;}")
        self.pushButton_82 = QPushButton(self.widget_15)
        self.pushButton_82.setObjectName(u"pushButton_82")
        self.pushButton_82.setGeometry(QRect(330, 10, 51, 49))
        self.pushButton_82.setCheckable(True)
        self.pushButton_82.clicked.connect(self.stat34)
        self.pushButton_82.setStyleSheet(u"QPushButton {background-color: green;\n"
"border-radius:15px;}\n"
"QPushButton:checked{background-color: red;} \n"
"QPushButton:pressed {background-color: red;}\n"
"QPushButton:focus:pressed{ background-color: black; }\n"
"QPushButton:focus{ background-color:red; }\n"
"QPushButton:hover{ background-color:rgb(52, 247, 18); }\n"
"QPushButton:released{background-color:green;}")
        self.pushButton_83 = QPushButton(self.widget_15)
        self.pushButton_83.setObjectName(u"pushButton_83")
        self.pushButton_83.setGeometry(QRect(270, 60, 51, 50))
        self.pushButton_83.setCheckable(True)
        self.pushButton_83.clicked.connect(self.stat35)
        self.pushButton_83.setStyleSheet(u"QPushButton {background-color: green;\n"
"border-radius:15px;}\n"
"QPushButton:checked{background-color: red;} \n"
"QPushButton:pressed {background-color: red;}\n"
"QPushButton:focus:pressed{ background-color: black; }\n"
"QPushButton:focus{ background-color:red; }\n"
"QPushButton:hover{ background-color:rgb(52, 247, 18); }\n"
"QPushButton:released{background-color:green;}")
        self.pushButton_84 = QPushButton(self.widget_15)
        self.pushButton_84.setObjectName(u"pushButton_84")
        self.pushButton_84.setGeometry(QRect(330, 60, 51, 50))
        self.pushButton_84.setCheckable(True)
        self.pushButton_84.clicked.connect(self.stat36)
        self.pushButton_84.setStyleSheet(u"QPushButton {background-color: green;\n"
"border-radius:15px;}\n"
"QPushButton:checked{background-color: red;} \n"
"QPushButton:pressed {background-color: red;}\n"
"QPushButton:focus:pressed{ background-color: black; }\n"
"QPushButton:focus{ background-color:red; }\n"
"QPushButton:hover{ background-color:rgb(52, 247, 18); }\n"
"QPushButton:released{background-color:green;}")
        self.pushButton_85 = QPushButton(self.widget_15)
        self.pushButton_85.setObjectName(u"pushButton_85")
        self.pushButton_85.setGeometry(QRect(400, 10, 51, 49))
        self.pushButton_85.setCheckable(True)
        self.pushButton_85.clicked.connect(self.stat37)
        self.pushButton_85.setStyleSheet(u"QPushButton {background-color: green;\n"
"border-radius:15px;}\n"
"QPushButton:checked{background-color: red;} \n"
"QPushButton:pressed {background-color: red;}\n"
"QPushButton:focus:pressed{ background-color: black; }\n"
"QPushButton:focus{ background-color:red; }\n"
"QPushButton:hover{ background-color:rgb(52, 247, 18); }\n"
"QPushButton:released{background-color:green;}")
        self.pushButton_86 = QPushButton(self.widget_15)
        self.pushButton_86.setObjectName(u"pushButton_86")
        self.pushButton_86.setGeometry(QRect(460, 10, 51, 49))
        self.pushButton_86.setCheckable(True)
        self.pushButton_86.clicked.connect(self.stat38)
        self.pushButton_86.setStyleSheet(u"QPushButton {background-color: green;\n"
"border-radius:15px;}\n"
"QPushButton:checked{background-color: red;} \n"
"QPushButton:pressed {background-color: red;}\n"
"QPushButton:focus:pressed{ background-color: black; }\n"
"QPushButton:focus{ background-color:red; }\n"
"QPushButton:hover{ background-color:rgb(52, 247, 18); }\n"
"QPushButton:released{background-color:green;}")
        self.pushButton_87 = QPushButton(self.widget_15)
        self.pushButton_87.setObjectName(u"pushButton_87")
        self.pushButton_87.setGeometry(QRect(400, 60, 51, 50))
        self.pushButton_87.setCheckable(True)
        self.pushButton_87.clicked.connect(self.stat39)
        self.pushButton_87.setStyleSheet(u"QPushButton {background-color: green;\n"
"border-radius:15px;}\n"
"QPushButton:checked{background-color: red;} \n"
"QPushButton:pressed {background-color: red;}\n"
"QPushButton:focus:pressed{ background-color: black; }\n"
"QPushButton:focus{ background-color:red; }\n"
"QPushButton:hover{ background-color:rgb(52, 247, 18); }\n"
"QPushButton:released{background-color:green;}")
        self.pushButton_88 = QPushButton(self.widget_15)
        self.pushButton_88.setObjectName(u"pushButton_88")
        self.pushButton_88.setGeometry(QRect(460, 60, 51, 50))
        self.pushButton_88.setCheckable(True)
        self.pushButton_88.clicked.connect(self.stat40)
        self.pushButton_88.setStyleSheet(u"QPushButton {background-color: green;\n"
"border-radius:15px;}\n"
"QPushButton:checked{background-color: red;} \n"
"QPushButton:pressed {background-color: red;}\n"
"QPushButton:focus:pressed{ background-color: black; }\n"
"QPushButton:focus{ background-color:red; }\n"
"QPushButton:hover{ background-color:rgb(52, 247, 18); }\n"
"QPushButton:released{background-color:green;}")
        self.pushButton_89 = QPushButton(self.widget_15)
        self.pushButton_89.setObjectName(u"pushButton_89")
        self.pushButton_89.setGeometry(QRect(530, 10, 51, 49))
        self.pushButton_89.setCheckable(True)
        self.pushButton_89.clicked.connect(self.stat41)
        self.pushButton_89.setStyleSheet(u"QPushButton {background-color: green;\n"
"border-radius:15px;}\n"
"QPushButton:checked{background-color: red;} \n"
"QPushButton:pressed {background-color: red;}\n"
"QPushButton:focus:pressed{ background-color: black; }\n"
"QPushButton:focus{ background-color:red; }\n"
"QPushButton:hover{ background-color:rgb(52, 247, 18); }\n"
"QPushButton:released{background-color:green;}")
        self.pushButton_90 = QPushButton(self.widget_15)
        self.pushButton_90.setObjectName(u"pushButton_90")
        self.pushButton_90.setGeometry(QRect(590, 10, 51, 49))
        self.pushButton_90.setCheckable(True)
        self.pushButton_90.clicked.connect(self.stat42)
        self.pushButton_90.setStyleSheet(u"QPushButton {background-color: green;\n"
"border-radius:15px;}\n"
"QPushButton:checked{background-color: red;} \n"
"QPushButton:pressed {background-color: red;}\n"
"QPushButton:focus:pressed{ background-color: black; }\n"
"QPushButton:focus{ background-color:red; }\n"
"QPushButton:hover{ background-color:rgb(52, 247, 18); }\n"
"QPushButton:released{background-color:green;}")
        self.pushButton_91 = QPushButton(self.widget_15)
        self.pushButton_91.setObjectName(u"pushButton_91")
        self.pushButton_91.setGeometry(QRect(530, 60, 51, 50))
        self.pushButton_91.setCheckable(True)
        self.pushButton_91.setStyleSheet(u"QPushButton {background-color: green;\n"
"border-radius:15px;}\n"
"QPushButton:checked{background-color: red;} \n"
"QPushButton:pressed {background-color: red;}\n"
"QPushButton:focus:pressed{ background-color: black; }\n"
"QPushButton:focus{ background-color:red; }\n"
"QPushButton:hover{ background-color:rgb(52, 247, 18); }\n"
"QPushButton:released{background-color:green;}")
        self.pushButton_92 = QPushButton(self.widget_15)
        self.pushButton_92.setObjectName(u"pushButton_92")
        self.pushButton_92.setGeometry(QRect(590, 60, 51, 50))
        self.pushButton_92.setCheckable(True)
        self.pushButton_92.setStyleSheet(u"QPushButton {background-color: green;\n"
"border-radius:15px;}\n"
"QPushButton:checked{background-color: red;} \n"
"QPushButton:pressed {background-color: red;}\n"
"QPushButton:focus:pressed{ background-color: black; }\n"
"QPushButton:focus{ background-color:red; }\n"
"QPushButton:hover{ background-color:rgb(52, 247, 18); }\n"
"QPushButton:released{background-color:green;}")
        self.pushButton_93 = QPushButton(self.widget_15)
        self.pushButton_93.setObjectName(u"pushButton_93")
        self.pushButton_93.setGeometry(QRect(660, 10, 51, 49))
        self.pushButton_93.setCheckable(True)
        self.pushButton_93.setStyleSheet(u"QPushButton {background-color: green;\n"
"border-radius:15px;}\n"
"QPushButton:checked{background-color: red;} \n"
"QPushButton:pressed {background-color: red;}\n"
"QPushButton:focus:pressed{ background-color: black; }\n"
"QPushButton:focus{ background-color:red; }\n"
"QPushButton:hover{ background-color:rgb(52, 247, 18); }\n"
"QPushButton:released{background-color:green;}")
        self.pushButton_94 = QPushButton(self.widget_15)
        self.pushButton_94.setObjectName(u"pushButton_94")
        self.pushButton_94.setGeometry(QRect(720, 10, 51, 49))
        self.pushButton_94.setCheckable(True)
        self.pushButton_94.setStyleSheet(u"QPushButton {background-color: green;\n"
"border-radius:15px;}\n"
"QPushButton:checked{background-color: red;} \n"
"QPushButton:pressed {background-color: red;}\n"
"QPushButton:focus:pressed{ background-color: black; }\n"
"QPushButton:focus{ background-color:red; }\n"
"QPushButton:hover{ background-color:rgb(52, 247, 18); }\n"
"QPushButton:released{background-color:green;}")
        self.pushButton_95 = QPushButton(self.widget_15)
        self.pushButton_95.setObjectName(u"pushButton_95")
        self.pushButton_95.setGeometry(QRect(660, 60, 51, 50))
        self.pushButton_95.setCheckable(True)
        self.pushButton_95.setStyleSheet(u"QPushButton {background-color: green;\n"
"border-radius:15px;}\n"
"QPushButton:checked{background-color: red;} \n"
"QPushButton:pressed {background-color: red;}\n"
"QPushButton:focus:pressed{ background-color: black; }\n"
"QPushButton:focus{ background-color:red; }\n"
"QPushButton:hover{ background-color:rgb(52, 247, 18); }\n"
"QPushButton:released{background-color:green;}")
        self.pushButton_96 = QPushButton(self.widget_15)
        self.pushButton_96.setObjectName(u"pushButton_96")
        self.pushButton_96.setGeometry(QRect(720, 60, 51, 50))
        self.pushButton_96.setCheckable(True)
        self.pushButton_96.setStyleSheet(u"QPushButton {background-color: green;\n"
"border-radius:15px;}\n"
"QPushButton:checked{background-color: red;} \n"
"QPushButton:pressed {background-color: red;}\n"
"QPushButton:focus:pressed{ background-color: black; }\n"
"QPushButton:focus{ background-color:red; }\n"
"QPushButton:hover{ background-color:rgb(52, 247, 18); }\n"
"QPushButton:released{background-color:green;}")

        self.verticalLayout_25.addWidget(self.widget_15, 0, Qt.AlignHCenter)


        self.verticalLayout_24.addWidget(self.widget_14)

        self.widget_16 = QWidget(self.widget_13)
        self.widget_16.setObjectName(u"widget_16")
        self.widget_16.setMaximumSize(QSize(16777215, 300))
        self.widget_16.setAutoFillBackground(False)
        self.widget_16.setStyleSheet(u"background-color: rgb(44, 49, 60);\n"
"border-color:1px solid grey;\n"
"border-radius: 15px;\n"
"background-color:#2c313c;")
        self.horizontalLayout_11 = QHBoxLayout(self.widget_16)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.vlan2confBtn = QPushButton(self.widget_16)
        self.vlan2confBtn.setObjectName(u"vlan2confBtn")
        sizePolicy4.setHeightForWidth(self.vlan2confBtn.sizePolicy().hasHeightForWidth())
        self.vlan2confBtn.setSizePolicy(sizePolicy4)
        self.vlan2confBtn.setMinimumSize(QSize(500, 100))
        self.vlan2confBtn.setMaximumSize(QSize(500, 100))
        self.vlan2confBtn.setFont(font9)
        self.vlan2confBtn.setStyleSheet(u"QPushButton{background-color:#16191d;}\n"
"\n"
"QPushButton:hover{background-color:#21252d;}\n"
"QPushButton:checked{background-color:#21252d;}\n"
"QPushButton:pressed{background-color:#21252d;}\n"
"\n"
"QPushButton:released{background-color:#21252d;}\n"
"QPushButton:focus:pressed{background-color:#21252d;}")

        self.horizontalLayout_11.addWidget(self.vlan2confBtn)

        self.infoSwt2Btn = QPushButton(self.widget_16)
        self.infoSwt2Btn.setObjectName(u"infoSwt2Btn")
        self.infoSwt2Btn.setMinimumSize(QSize(500, 100))
        self.infoSwt2Btn.setMaximumSize(QSize(500, 100))
        self.infoSwt2Btn.setFont(font9)
        self.infoSwt2Btn.setStyleSheet(u"QPushButton{background-color:#16191d;}\n"
"\n"
"QPushButton:hover{background-color:#21252d;}\n"
"QPushButton:checked{background-color:#21252d;}\n"
"QPushButton:pressed{background-color:#21252d;}\n"
"\n"
"QPushButton:released{background-color:#21252d;}\n"
"QPushButton:focus:pressed{background-color:#21252d;}\n"
"")

        self.horizontalLayout_11.addWidget(self.infoSwt2Btn)


        self.verticalLayout_24.addWidget(self.widget_16)


        self.verticalLayout_23.addWidget(self.widget_13)

        self.mainPages.addWidget(self.Switch2)
        self.vlan2 = QWidget()
        self.vlan2.setObjectName(u"vlan2")
        self.verticalLayout_30 = QVBoxLayout(self.vlan2)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.widget_22 = QWidget(self.vlan2)
        self.widget_22.setObjectName(u"widget_22")
        self.verticalLayout_63 = QVBoxLayout(self.widget_22)
        self.verticalLayout_63.setObjectName(u"verticalLayout_63")
        self.return5 = QPushButton(self.widget_22)
        self.return5.setObjectName(u"return5")
        self.return5.setMinimumSize(QSize(25, 25))
        self.return5.setMaximumSize(QSize(25, 25))
        self.return5.setStyleSheet(u"background-color:#21252d;\n"
"")
        self.return5.setIcon(icon12)

        self.verticalLayout_63.addWidget(self.return5)

        self.widget_65 = QWidget(self.widget_22)
        self.widget_65.setObjectName(u"widget_65")
        self.widget_65.setMinimumSize(QSize(600, 100))
        self.widget_65.setMaximumSize(QSize(950, 100))
        self.widget_65.setStyleSheet(u"background-color:#21252d;\n"
"border-color:1px solid grey;\n"
"border-radius: 15px;\n"
"")
        self.verticalLayout_64 = QVBoxLayout(self.widget_65)
        self.verticalLayout_64.setSpacing(0)
        self.verticalLayout_64.setObjectName(u"verticalLayout_64")
        self.verticalLayout_64.setContentsMargins(0, 0, 0, 0)
        self.label_44 = QLabel(self.widget_65)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setFont(font10)
        self.label_44.setAlignment(Qt.AlignCenter)

        self.verticalLayout_64.addWidget(self.label_44)


        self.verticalLayout_63.addWidget(self.widget_65, 0, Qt.AlignHCenter)

        self.widget_66 = QWidget(self.widget_22)
        self.widget_66.setObjectName(u"widget_66")
        self.widget_66.setMinimumSize(QSize(950, 200))
        self.widget_66.setMaximumSize(QSize(1000, 200))
        self.widget_66.setStyleSheet(u"background-color:#21252d;\n"
"border-color:1px solid grey;\n"
"border-radius: 15px;")
        self.horizontalLayout_32 = QHBoxLayout(self.widget_66)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.widget_67 = QWidget(self.widget_66)
        self.widget_67.setObjectName(u"widget_67")
        self.verticalLayout_65 = QVBoxLayout(self.widget_67)
        self.verticalLayout_65.setObjectName(u"verticalLayout_65")
        self.widget_68 = QWidget(self.widget_67)
        self.widget_68.setObjectName(u"widget_68")
        self.widget_68.setMaximumSize(QSize(16777215, 45))
        self.horizontalLayout_33 = QHBoxLayout(self.widget_68)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.label_45 = QLabel(self.widget_68)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setFont(font11)
        self.label_45.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_33.addWidget(self.label_45)

        self.label_46 = QLabel(self.widget_68)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setFont(font11)
        self.label_46.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_33.addWidget(self.label_46)

        self.label_47 = QLabel(self.widget_68)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setFont(font11)
        self.label_47.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_33.addWidget(self.label_47)


        self.verticalLayout_65.addWidget(self.widget_68)

        self.widget_69 = QWidget(self.widget_67)
        self.widget_69.setObjectName(u"widget_69")
        self.horizontalLayout_34 = QHBoxLayout(self.widget_69)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.spinBox_4 = QSpinBox(self.widget_69)
        self.spinBox_4.setObjectName(u"spinBox_4")
        self.spinBox_4.setMinimumSize(QSize(200, 40))
        self.spinBox_4.setMaximumSize(QSize(200, 40))
        self.spinBox_4.setFont(font)
        self.spinBox_4.setStyleSheet(u"background-color:#2c313c;\n"
"border-radius: 5px;")
        self.spinBox_4.setMaximum(100)
        self.spinBox_4.setSingleStep(10)

        self.horizontalLayout_34.addWidget(self.spinBox_4, 0, Qt.AlignTop)

        self.lineEdit_7 = QLineEdit(self.widget_69)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setMinimumSize(QSize(200, 40))
        self.lineEdit_7.setMaximumSize(QSize(200, 40))
        self.lineEdit_7.setFont(font)
        self.lineEdit_7.setStyleSheet(u"background-color:#2c313c;\n"
"border-radius: 5px;")

        self.horizontalLayout_34.addWidget(self.lineEdit_7, 0, Qt.AlignTop)

        self.lineEdit_8 = QLineEdit(self.widget_69)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        self.lineEdit_8.setMinimumSize(QSize(200, 40))
        self.lineEdit_8.setMaximumSize(QSize(200, 40))
        self.lineEdit_8.setFont(font)
        self.lineEdit_8.setStyleSheet(u"background-color:#2c313c;\n"
"border-radius: 5px;")

        self.horizontalLayout_34.addWidget(self.lineEdit_8, 0, Qt.AlignTop)


        self.verticalLayout_65.addWidget(self.widget_69)


        self.horizontalLayout_32.addWidget(self.widget_67)

        self.widget_70 = QWidget(self.widget_66)
        self.widget_70.setObjectName(u"widget_70")
        self.widget_70.setMinimumSize(QSize(250, 0))
        self.widget_70.setMaximumSize(QSize(250, 16777215))
        self.verticalLayout_66 = QVBoxLayout(self.widget_70)
        self.verticalLayout_66.setObjectName(u"verticalLayout_66")
        self.pushButton_15 = QPushButton(self.widget_70)
        self.pushButton_15.setObjectName(u"pushButton_15")
        self.pushButton_15.setMinimumSize(QSize(200, 40))
        self.pushButton_15.setMaximumSize(QSize(200, 40))
        self.pushButton_15.clicked.connect(self.addvlan2)
        self.pushButton_15.clicked.connect(self.addtobox2)
        self.pushButton_15.setStyleSheet(u"QPushButton{background-color:#2c313c;}\n"
"\n"
"QPushButton:hover{background-color:#16191d;}\n"
"QPushButton:checked{background-color:#16191d;}\n"
"QPushButton:pressed{background-color:#16191d;}\n"
"\n"
"QPushButton:released{background-color:#16191d;}\n"
"QPushButton:focus:pressed{background-color:#16191d;}")

        self.verticalLayout_66.addWidget(self.pushButton_15, 0, Qt.AlignRight)

        self.pushButton_16 = QPushButton(self.widget_70)
        self.pushButton_16.setObjectName(u"pushButton_16")
        self.pushButton_16.setMinimumSize(QSize(200, 40))
        self.pushButton_16.setMaximumSize(QSize(200, 40))
        self.pushButton_16.clicked.connect(self.delvlan2)
        self.pushButton_16.clicked.connect(self.removefrombox2)
        self.pushButton_16.setStyleSheet(u"QPushButton{background-color:#2c313c;}\n"
"\n"
"QPushButton:hover{background-color:#16191d;}\n"
"\n"
"QPushButton:pressed{background-color:#16191d;}\n"
"\n"
"QPushButton:checked{background-color:#16191d;}\n"
"\n"
"QPushButton:focus:pressed{background-color:#16191d;}\n"
"\n"
"\n"
"QPushButton:released{background-color:#2c313c;}\n"
"\n"
"")

        self.verticalLayout_66.addWidget(self.pushButton_16, 0, Qt.AlignRight)

        self.pushButton_17 = QPushButton(self.widget_70)
        self.pushButton_17.setObjectName(u"pushButton_17")
        self.pushButton_17.setMinimumSize(QSize(200, 40))
        self.pushButton_17.setMaximumSize(QSize(200, 40))
        self.pushButton_17.setStyleSheet(u"QPushButton{background-color:#2c313c;}\n"
"\n"
"QPushButton:hover{background-color:#16191d;}\n"
"QPushButton:checked{background-color:#16191d;}\n"
"QPushButton:pressed{background-color:#16191d;}\n"
"\n"
"QPushButton:released{background-color:#16191d;}\n"
"QPushButton:focus:pressed{background-color:#16191d;}")

        self.verticalLayout_66.addWidget(self.pushButton_17, 0, Qt.AlignRight)


        self.horizontalLayout_32.addWidget(self.widget_70)


        self.verticalLayout_63.addWidget(self.widget_66, 0, Qt.AlignHCenter)

        self.widget_71 = QWidget(self.widget_22)
        self.widget_71.setObjectName(u"widget_71")
        self.widget_71.setMinimumSize(QSize(600, 100))
        self.widget_71.setMaximumSize(QSize(950, 100))
        self.widget_71.setStyleSheet(u"background-color:#21252d;\n"
"border-color:1px solid grey;\n"
"border-radius: 15px;\n"
"")
        self.verticalLayout_67 = QVBoxLayout(self.widget_71)
        self.verticalLayout_67.setObjectName(u"verticalLayout_67")
        self.label_48 = QLabel(self.widget_71)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setFont(font10)
        self.label_48.setAlignment(Qt.AlignCenter)

        self.verticalLayout_67.addWidget(self.label_48)


        self.verticalLayout_63.addWidget(self.widget_71, 0, Qt.AlignHCenter)

        self.widget_72 = QWidget(self.widget_22)
        self.widget_72.setObjectName(u"widget_72")
        self.widget_72.setMinimumSize(QSize(950, 200))
        self.widget_72.setMaximumSize(QSize(1000, 200))
        self.widget_72.setStyleSheet(u"background-color:#21252d;\n"
"border-color:1px solid grey;\n"
"border-radius: 15px;")
        self.verticalLayout_68 = QVBoxLayout(self.widget_72)
        self.verticalLayout_68.setSpacing(5)
        self.verticalLayout_68.setObjectName(u"verticalLayout_68")
        self.verticalLayout_68.setContentsMargins(12, 0, 12, 3)
        self.widget_73 = QWidget(self.widget_72)
        self.widget_73.setObjectName(u"widget_73")
        self.widget_73.setMaximumSize(QSize(650, 50))
        self.horizontalLayout_35 = QHBoxLayout(self.widget_73)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.label_49 = QLabel(self.widget_73)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setFont(font12)

        self.horizontalLayout_35.addWidget(self.label_49, 0, Qt.AlignHCenter)

        self.label_50 = QLabel(self.widget_73)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setFont(font12)

        self.horizontalLayout_35.addWidget(self.label_50, 0, Qt.AlignHCenter)

        self.label_51 = QLabel(self.widget_73)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setFont(font12)

        self.horizontalLayout_35.addWidget(self.label_51, 0, Qt.AlignHCenter)


        self.verticalLayout_68.addWidget(self.widget_73)

        self.widget_74 = QWidget(self.widget_72)
        self.widget_74.setObjectName(u"widget_74")
        self.widget_74.setMaximumSize(QSize(16777215, 150))
        self.horizontalLayout_36 = QHBoxLayout(self.widget_74)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.widget_75 = QWidget(self.widget_74)
        self.widget_75.setObjectName(u"widget_75")
        self.widget_75.setMinimumSize(QSize(0, 80))
        self.widget_75.setMaximumSize(QSize(16777215, 80))
        self.horizontalLayout_37 = QHBoxLayout(self.widget_75)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.comboBox_3 = QComboBox(self.widget_75)
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.setObjectName(u"comboBox_3")
        self.comboBox_3.setMinimumSize(QSize(180, 42))
        self.comboBox_3.setMaximumSize(QSize(180, 42))
        self.comboBox_3.setFont(font11)
        self.comboBox_3.setStyleSheet(u"background-color:#2c313c;\n"
"")

        self.horizontalLayout_37.addWidget(self.comboBox_3)

        self.comboBox_9 = QComboBox(self.widget_75)
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.setObjectName(u"comboBox_9")
        self.comboBox_9.setMinimumSize(QSize(180, 42))
        self.comboBox_9.setMaximumSize(QSize(180, 42))
        self.comboBox_9.setFont(font11)
        self.comboBox_9.setStyleSheet(u"background-color:#2c313c;\n"
"")

        self.horizontalLayout_37.addWidget(self.comboBox_9)

        self.comboBox_10 = QComboBox(self.widget_75)
        self.comboBox_10.addItem("")
        self.comboBox_10.addItem("")
        self.comboBox_10.setObjectName(u"comboBox_10")
        self.comboBox_10.setMinimumSize(QSize(200, 42))
        self.comboBox_10.setMaximumSize(QSize(200, 42))
        self.comboBox_10.setFont(font11)
        self.comboBox_10.setStyleSheet(u"background-color:#2c313c;\n"
"")

        self.horizontalLayout_37.addWidget(self.comboBox_10)


        self.horizontalLayout_36.addWidget(self.widget_75, 0, Qt.AlignTop)

        self.widget_76 = QWidget(self.widget_74)
        self.widget_76.setObjectName(u"widget_76")
        self.widget_76.setMinimumSize(QSize(250, 100))
        self.widget_76.setMaximumSize(QSize(250, 16777215))
        self.verticalLayout_69 = QVBoxLayout(self.widget_76)
        self.verticalLayout_69.setObjectName(u"verticalLayout_69")
        self.selectBtn_3 = QPushButton(self.widget_76)
        self.selectBtn_3.setObjectName(u"selectBtn_3")
        self.selectBtn_3.setMinimumSize(QSize(200, 40))
        self.selectBtn_3.setMaximumSize(QSize(200, 40))
        self.selectBtn_3.setFont(font13)
        self.selectBtn_3.clicked.connect(self.getvlan2)
        self.selectBtn_3.setStyleSheet(u"QPushButton{background-color:#2c313c;}\n"
"\n"
"QPushButton:hover{background-color:#16191d;}\n"
"QPushButton:checked{background-color:#16191d;}\n"
"QPushButton:pressed{background-color:#16191d;}\n"
"QPushButton:released{background-color:#16191d;}\n"
"QPushButton:focus:pressed{background-color:#16191d;}\n"
"")

        self.verticalLayout_69.addWidget(self.selectBtn_3, 0, Qt.AlignHCenter)

        self.delport1_2 = QPushButton(self.widget_76)
        self.delport1_2.setObjectName(u"delport1_2")
        self.delport1_2.setMinimumSize(QSize(200, 40))
        self.delport1_2.setMaximumSize(QSize(200, 40))
        self.delport1_2.clicked.connect(self.delport2)
        self.delport1_2.setStyleSheet(u"QPushButton{background-color:#2c313c;}\n"
"\n"
"QPushButton:hover{background-color:#16191d;}\n"
"\n"
"QPushButton:pressed{background-color:#16191d;}\n"
"\n"
"QPushButton:checked{background-color:#16191d;}\n"
"\n"
"QPushButton:focus:pressed{background-color:#16191d;}\n"
"\n"
"\n"
"QPushButton:released{background-color:#2c313c;}\n"
"\n"
"")

        self.verticalLayout_69.addWidget(self.delport1_2, 0, Qt.AlignHCenter)


        self.horizontalLayout_36.addWidget(self.widget_76)


        self.verticalLayout_68.addWidget(self.widget_74)


        self.verticalLayout_63.addWidget(self.widget_72, 0, Qt.AlignHCenter)


        self.verticalLayout_30.addWidget(self.widget_22)

        self.mainPages.addWidget(self.vlan2)
        self.InfoSwitch2 = QWidget()
        self.InfoSwitch2.setObjectName(u"InfoSwitch2")
        self.verticalLayout_82 = QVBoxLayout(self.InfoSwitch2)
        self.verticalLayout_82.setObjectName(u"verticalLayout_82")
        self.widget_41 = QWidget(self.InfoSwitch2)
        self.widget_41.setObjectName(u"widget_41")
        self.verticalLayout_42 = QVBoxLayout(self.widget_41)
        self.verticalLayout_42.setSpacing(0)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.verticalLayout_42.setContentsMargins(0, 0, 0, 0)
        self.return6 = QPushButton(self.widget_41)
        self.return6.setObjectName(u"return6")
        self.return6.setMinimumSize(QSize(25, 25))
        self.return6.setMaximumSize(QSize(25, 25))
        self.return6.setStyleSheet(u"background-color:#21252d;\n"
"")
        self.return6.setIcon(icon12)

        self.verticalLayout_42.addWidget(self.return6)

        self.widget_42 = QWidget(self.widget_41)
        self.widget_42.setObjectName(u"widget_42")
        self.widget_42.setMinimumSize(QSize(0, 80))
        self.widget_42.setMaximumSize(QSize(16777215, 80))
        self.widget_42.setStyleSheet(u"border-radius: 15px;")
        self.horizontalLayout_23 = QHBoxLayout(self.widget_42)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.label_35 = QLabel(self.widget_42)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setMinimumSize(QSize(800, 60))
        self.label_35.setMaximumSize(QSize(800, 60))
        self.label_35.setFont(font14)
        self.label_35.setStyleSheet(u"background-color:#21252d;\n"
"border-radius: 15px;")
        self.label_35.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_23.addWidget(self.label_35)

        self.getmactable2Btn = QPushButton(self.widget_42)
        self.getmactable2Btn.setObjectName(u"getmactable2Btn")
        self.getmactable2Btn.setMinimumSize(QSize(150, 60))
        self.getmactable2Btn.setMaximumSize(QSize(150, 50))
        self.getmactable2Btn.setFont(font11)
        self.getmactable2Btn.clicked.connect(self.table2)
        self.getmactable2Btn.setStyleSheet(u"\n"
"\n"
"QPushButton{background-color:#21252d;}\n"
"\n"
"QPushButton:hover{background-color:#16191d;}\n"
"QPushButton:checked{background-color:#16191d;}\n"
"QPushButton:pressed{background-color:#16191d;}\n"
"\n"
"QPushButton:released{background-color:#16191d;}\n"
"QPushButton:focus:pressed{background-color:#16191d;}\n"
"\n"
"")

        self.horizontalLayout_23.addWidget(self.getmactable2Btn, 0, Qt.AlignTop)


        self.verticalLayout_42.addWidget(self.widget_42)

        self.widget_43 = QWidget(self.widget_41)
        self.widget_43.setObjectName(u"widget_43")
        self.widget_43.setMinimumSize(QSize(0, 80))
        self.widget_43.setMaximumSize(QSize(1677215, 80))
        self.widget_43.setStyleSheet(u"border-radius: 15px;")
        self.horizontalLayout_27 = QHBoxLayout(self.widget_43)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.label_36 = QLabel(self.widget_43)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setMinimumSize(QSize(800, 60))
        self.label_36.setMaximumSize(QSize(800, 60))
        self.label_36.setFont(font14)
        self.label_36.setStyleSheet(u"background-color:#21252d;\n"
"border-radius: 15px;")
        self.label_36.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_27.addWidget(self.label_36, 0, Qt.AlignTop)

        self.getconf2Btn = QPushButton(self.widget_43)
        self.getconf2Btn.setObjectName(u"getconf2Btn")
        self.getconf2Btn.setMinimumSize(QSize(150, 60))
        self.getconf2Btn.setMaximumSize(QSize(150, 60))
        self.getconf2Btn.setFont(font11)
        self.getconf2Btn.clicked.connect(self.conf2)
        self.getconf2Btn.setStyleSheet(u"\n"
"\n"
"QPushButton{background-color:#21252d;}\n"
"\n"
"QPushButton:hover{background-color:#16191d;}\n"
"QPushButton:checked{background-color:#16191d;}\n"
"QPushButton:pressed{background-color:#16191d;}\n"
"\n"
"QPushButton:released{background-color:#16191d;}\n"
"QPushButton:focus:pressed{background-color:#16191d;}\n"
"\n"
"")

        self.horizontalLayout_27.addWidget(self.getconf2Btn, 0, Qt.AlignTop)


        self.verticalLayout_42.addWidget(self.widget_43)

        self.pushButton_7 = QPushButton(self.widget_41)
        self.pushButton_7.setObjectName(u"pushButton_7")

        self.verticalLayout_42.addWidget(self.pushButton_7)

        self.pushButton_9 = QPushButton(self.widget_41)
        self.pushButton_9.setObjectName(u"pushButton_9")

        self.verticalLayout_42.addWidget(self.pushButton_9)


        self.verticalLayout_82.addWidget(self.widget_41)

        self.mainPages.addWidget(self.InfoSwitch2)
        self.tablemac2 = QWidget()
        self.tablemac2.setObjectName(u"tablemac2")
        self.horizontalLayout_26 = QHBoxLayout(self.tablemac2)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.widget_47 = QWidget(self.tablemac2)
        self.widget_47.setObjectName(u"widget_47")
        self.verticalLayout_43 = QVBoxLayout(self.widget_47)
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.return7 = QPushButton(self.widget_47)
        self.return7.setObjectName(u"return7")
        self.return7.setMinimumSize(QSize(25, 25))
        self.return7.setMaximumSize(QSize(25, 25))
        font17 = QFont()
        font17.setPointSize(4)
        self.return7.setFont(font17)
        self.return7.setStyleSheet(u"background-color:#21252d;\n"
"")
        self.return7.setIcon(icon12)

        self.verticalLayout_43.addWidget(self.return7)

        self.label_37 = QLabel(self.widget_47)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setMinimumSize(QSize(800, 60))
        self.label_37.setMaximumSize(QSize(800, 60))
        self.label_37.setFont(font10)
        self.label_37.setStyleSheet(u"background-color:#21252d;\n"
"border-radius: 15px;")
        self.label_37.setAlignment(Qt.AlignCenter)

        self.verticalLayout_43.addWidget(self.label_37, 0, Qt.AlignHCenter)

        self.textEdit_2 = QTextEdit(self.widget_47)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setMinimumSize(QSize(900, 500))
        self.textEdit_2.setMaximumSize(QSize(900, 500))
        self.textEdit_2.setFont(font)
        self.textEdit_2.setStyleSheet(u"background-color:#21252d;\n"
"border-radius: 15px;")

        self.verticalLayout_43.addWidget(self.textEdit_2, 0, Qt.AlignHCenter)


        self.horizontalLayout_26.addWidget(self.widget_47)

        self.mainPages.addWidget(self.tablemac2)
        self.configuration2 = QWidget()
        self.configuration2.setObjectName(u"configuration2")
        self.verticalLayout_44 = QVBoxLayout(self.configuration2)
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.widget_48 = QWidget(self.configuration2)
        self.widget_48.setObjectName(u"widget_48")
        self.verticalLayout_45 = QVBoxLayout(self.widget_48)
        self.verticalLayout_45.setObjectName(u"verticalLayout_45")
        self.return8 = QPushButton(self.widget_48)
        self.return8.setObjectName(u"return8")
        self.return8.setMinimumSize(QSize(25, 25))
        self.return8.setMaximumSize(QSize(25, 25))
        font18 = QFont()
        font18.setPointSize(6)
        self.return8.setFont(font18)
        self.return8.setStyleSheet(u"background-color:#21252d;\n"
"")
        self.return8.setIcon(icon12)

        self.verticalLayout_45.addWidget(self.return8)

        self.label_38 = QLabel(self.widget_48)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setMinimumSize(QSize(800, 60))
        self.label_38.setMaximumSize(QSize(800, 60))
        self.label_38.setFont(font10)
        self.label_38.setStyleSheet(u"background-color:#21252d;\n"
"border-radius: 15px;")
        self.label_38.setAlignment(Qt.AlignCenter)

        self.verticalLayout_45.addWidget(self.label_38, 0, Qt.AlignHCenter)

        self.textEdit_3 = QTextEdit(self.widget_48)
        self.textEdit_3.setObjectName(u"textEdit_3")
        self.textEdit_3.setMinimumSize(QSize(950, 500))
        self.textEdit_3.setMaximumSize(QSize(950, 500))
        self.textEdit_3.setStyleSheet(u"background-color:#21252d;\n"
"border-radius: 15px;")

        self.verticalLayout_45.addWidget(self.textEdit_3, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_44.addWidget(self.widget_48)

        self.mainPages.addWidget(self.configuration2)
        self.Router = QWidget()
        self.Router.setObjectName(u"Router")
        self.verticalLayout_16 = QVBoxLayout(self.Router)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.widget_9 = QWidget(self.Router)
        self.widget_9.setObjectName(u"widget_9")
        self.widget_9.setMinimumSize(QSize(1000, 120))
        self.widget_9.setMaximumSize(QSize(3500, 120))
        self.widget_9.setStyleSheet(u"background-color:#16191d;\n"
"border-color:1px solid grey;\n"
"border-radius: 8px;\n"
"")
        self.verticalLayout_17 = QVBoxLayout(self.widget_9)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.label_9 = QLabel(self.widget_9)
        self.label_9.setObjectName(u"label_9")
        sizePolicy3.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy3)
        self.label_9.setMinimumSize(QSize(0, 0))
        self.label_9.setFont(font6)
        self.label_9.setAlignment(Qt.AlignCenter)

        self.verticalLayout_17.addWidget(self.label_9)


        self.verticalLayout_16.addWidget(self.widget_9)

        self.widget_10 = QWidget(self.Router)
        self.widget_10.setObjectName(u"widget_10")
        self.widget_10.setMinimumSize(QSize(0, 0))
        self.widget_10.setMaximumSize(QSize(16777215, 500))
        self.widget_10.setStyleSheet(u"border-color:1px solid grey;\n"
"border-radius: 15px;\n"
"background-color:#2c313c;")
        self.verticalLayout_11 = QVBoxLayout(self.widget_10)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.routerciscoBtn = QPushButton(self.widget_10)
        self.routerciscoBtn.setObjectName(u"routerciscoBtn")
        self.routerciscoBtn.setMinimumSize(QSize(600, 150))
        self.routerciscoBtn.setMaximumSize(QSize(600, 150))
        self.routerciscoBtn.setFont(font7)
        self.routerciscoBtn.setStyleSheet(u"QPushButton{background-color:#16191d;}\n"
"QPushButton:hover{background-color:#21252d;}\n"
"QPushButton:checked{background-color:#21252d;}\n"
"QPushButton:pressed{background-color:#21252d;}\n"
"QPushButton:released{background-color:#21252d;}\n"
"QPushButton:focus:pressed{background-color:#21252d;}\n"
"")
        icon13 = QIcon()
        icon13.addFile(u":/images/router.png", QSize(), QIcon.Normal, QIcon.Off)
        self.routerciscoBtn.setIcon(icon13)
        self.routerciscoBtn.setIconSize(QSize(150, 150))

        self.verticalLayout_11.addWidget(self.routerciscoBtn, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_16.addWidget(self.widget_10)

        self.mainPages.addWidget(self.Router)
        self.router = QWidget()
        self.router.setObjectName(u"router")
        self.verticalLayout_46 = QVBoxLayout(self.router)
        self.verticalLayout_46.setObjectName(u"verticalLayout_46")
        self.widget_44 = QWidget(self.router)
        self.widget_44.setObjectName(u"widget_44")
        self.verticalLayout_48 = QVBoxLayout(self.widget_44)
        self.verticalLayout_48.setObjectName(u"verticalLayout_48")
        self.widget_51 = QWidget(self.widget_44)
        self.widget_51.setObjectName(u"widget_51")
        self.widget_51.setMinimumSize(QSize(800, 70))
        self.widget_51.setMaximumSize(QSize(800, 70))
        self.widget_51.setStyleSheet(u"background-color:#21252d;\n"
"border-radius: 15px;")
        self.verticalLayout_50 = QVBoxLayout(self.widget_51)
        self.verticalLayout_50.setObjectName(u"verticalLayout_50")
        self.label_14 = QLabel(self.widget_51)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font7)

        self.verticalLayout_50.addWidget(self.label_14, 0, Qt.AlignHCenter)


        self.verticalLayout_48.addWidget(self.widget_51, 0, Qt.AlignHCenter)

        self.widget_52 = QWidget(self.widget_44)
        self.widget_52.setObjectName(u"widget_52")
        self.widget_52.setMinimumSize(QSize(950, 500))
        self.widget_52.setMaximumSize(QSize(950, 500))
        self.widget_52.setStyleSheet(u"background-color:#21252d;\n"
"border-radius: 15px;")
        self.verticalLayout_49 = QVBoxLayout(self.widget_52)
        self.verticalLayout_49.setObjectName(u"verticalLayout_49")
        self.tableroutageBtn = QPushButton(self.widget_52)
        self.tableroutageBtn.setObjectName(u"tableroutageBtn")
        self.tableroutageBtn.setMinimumSize(QSize(500, 60))
        self.tableroutageBtn.setMaximumSize(QSize(500, 60))
        self.tableroutageBtn.setFont(font14)
        self.tableroutageBtn.clicked.connect(self.tableRt)
        self.tableroutageBtn.setStyleSheet(u"QPushButton{background-color:#2c313c;}\n"
"\n"
"QPushButton:hover{background-color:#16191d;}\n"
"QPushButton:checked{background-color:#16191d;}\n"
"QPushButton:pressed{background-color:#16191d;}\n"
"QPushButton:released{background-color:#16191d;}\n"
"QPushButton:focus:pressed{background-color:#16191d;}")

        self.verticalLayout_49.addWidget(self.tableroutageBtn, 0, Qt.AlignHCenter)

        self.gestionBtn = QPushButton(self.widget_52)
        self.gestionBtn.setObjectName(u"gestionBtn")
        self.gestionBtn.setMinimumSize(QSize(500, 60))
        self.gestionBtn.setMaximumSize(QSize(500, 60))
        self.gestionBtn.setFont(font14)
        self.gestionBtn.setStyleSheet(u"QPushButton{background-color:#2c313c;}\n"
"\n"
"QPushButton:hover{background-color:#16191d;}\n"
"QPushButton:checked{background-color:#16191d;}\n"
"QPushButton:pressed{background-color:#16191d;}\n"
"QPushButton:released{background-color:#16191d;}\n"
"QPushButton:focus:pressed{background-color:#16191d;}")

        self.verticalLayout_49.addWidget(self.gestionBtn, 0, Qt.AlignHCenter)

        self.etatinfBtn = QPushButton(self.widget_52)
        self.etatinfBtn.setObjectName(u"etatinfBtn")
        self.etatinfBtn.setMinimumSize(QSize(500, 60))
        self.etatinfBtn.setMaximumSize(QSize(500, 60))
        self.etatinfBtn.setFont(font14)
        self.etatinfBtn.clicked.connect(self.intinfo)
        self.etatinfBtn.setStyleSheet(u"QPushButton{background-color:#2c313c;}\n"
"\n"
"QPushButton:hover{background-color:#16191d;}\n"
"QPushButton:checked{background-color:#16191d;}\n"
"QPushButton:pressed{background-color:#16191d;}\n"
"QPushButton:released{background-color:#16191d;}\n"
"QPushButton:focus:pressed{background-color:#16191d;}")

        self.verticalLayout_49.addWidget(self.etatinfBtn, 0, Qt.AlignHCenter)


        self.verticalLayout_48.addWidget(self.widget_52, 0, Qt.AlignHCenter)


        self.verticalLayout_46.addWidget(self.widget_44)

        self.mainPages.addWidget(self.router)
        self.tableroutage = QWidget()
        self.tableroutage.setObjectName(u"tableroutage")
        self.verticalLayout_51 = QVBoxLayout(self.tableroutage)
        self.verticalLayout_51.setObjectName(u"verticalLayout_51")
        self.widget_53 = QWidget(self.tableroutage)
        self.widget_53.setObjectName(u"widget_53")
        self.verticalLayout_54 = QVBoxLayout(self.widget_53)
        self.verticalLayout_54.setObjectName(u"verticalLayout_54")
        self.return9 = QPushButton(self.widget_53)
        self.return9.setObjectName(u"return9")
        self.return9.setMinimumSize(QSize(25, 25))
        self.return9.setMaximumSize(QSize(25, 25))
        self.return9.setStyleSheet(u"background-color:#21252d;\n"
"")
        self.return9.setIcon(icon12)

        self.verticalLayout_54.addWidget(self.return9)

        self.widget_54 = QWidget(self.widget_53)
        self.widget_54.setObjectName(u"widget_54")
        self.widget_54.setMinimumSize(QSize(800, 70))
        self.widget_54.setMaximumSize(QSize(800, 70))
        self.widget_54.setStyleSheet(u"background-color:#21252d;\n"
"border-radius: 15px;")
        self.verticalLayout_52 = QVBoxLayout(self.widget_54)
        self.verticalLayout_52.setObjectName(u"verticalLayout_52")
        self.label_32 = QLabel(self.widget_54)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setFont(font7)

        self.verticalLayout_52.addWidget(self.label_32, 0, Qt.AlignHCenter)


        self.verticalLayout_54.addWidget(self.widget_54, 0, Qt.AlignHCenter)

        self.textEdit_5 = QTextEdit(self.widget_53)
        self.textEdit_5.setObjectName(u"textEdit_5")
        self.textEdit_5.setMinimumSize(QSize(950, 500))
        self.textEdit_5.setMaximumSize(QSize(950, 500))
        self.textEdit_5.setFont(font16)
        self.textEdit_5.setStyleSheet(u"background-color:#21252d;\n"
"border-radius: 15px;")

        self.verticalLayout_54.addWidget(self.textEdit_5, 0, Qt.AlignHCenter)


        self.verticalLayout_51.addWidget(self.widget_53)

        self.mainPages.addWidget(self.tableroutage)
        self.gestionintf = QWidget()
        self.gestionintf.setObjectName(u"gestionintf")
        self.verticalLayout_56 = QVBoxLayout(self.gestionintf)
        self.verticalLayout_56.setObjectName(u"verticalLayout_56")
        self.widget_55 = QWidget(self.gestionintf)
        self.widget_55.setObjectName(u"widget_55")
        self.verticalLayout_55 = QVBoxLayout(self.widget_55)
        self.verticalLayout_55.setObjectName(u"verticalLayout_55")
        self.return10 = QPushButton(self.widget_55)
        self.return10.setObjectName(u"return10")
        self.return10.setMinimumSize(QSize(25, 25))
        self.return10.setMaximumSize(QSize(25, 25))
        font19 = QFont()
        font19.setPointSize(7)
        self.return10.setFont(font19)
        self.return10.setStyleSheet(u"background-color:#21252d;\n"
"")
        self.return10.setIcon(icon12)

        self.verticalLayout_55.addWidget(self.return10)

        self.widget_56 = QWidget(self.widget_55)
        self.widget_56.setObjectName(u"widget_56")
        self.widget_56.setMinimumSize(QSize(800, 70))
        self.widget_56.setMaximumSize(QSize(800, 70))
        self.widget_56.setStyleSheet(u"background-color:#21252d;\n"
"border-radius: 15px;")
        self.verticalLayout_53 = QVBoxLayout(self.widget_56)
        self.verticalLayout_53.setObjectName(u"verticalLayout_53")
        self.label_39 = QLabel(self.widget_56)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setFont(font7)

        self.verticalLayout_53.addWidget(self.label_39, 0, Qt.AlignHCenter)


        self.verticalLayout_55.addWidget(self.widget_56, 0, Qt.AlignHCenter)

        self.widget_59 = QWidget(self.widget_55)
        self.widget_59.setObjectName(u"widget_59")
        self.widget_59.setMinimumSize(QSize(950, 500))
        self.widget_59.setMaximumSize(QSize(950, 500))
        self.widget_59.setStyleSheet(u"background-color:#21252d;\n"
"border-radius: 15px;")
        self.horizontalLayout_29 = QHBoxLayout(self.widget_59)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.widget_60 = QWidget(self.widget_59)
        self.widget_60.setObjectName(u"widget_60")
        self.verticalLayout_61 = QVBoxLayout(self.widget_60)
        self.verticalLayout_61.setObjectName(u"verticalLayout_61")
        self.widget_63 = QWidget(self.widget_60)
        self.widget_63.setObjectName(u"widget_63")
        self.widget_63.setMinimumSize(QSize(0, 200))
        self.widget_63.setMaximumSize(QSize(16777215, 200))
        self.horizontalLayout_31 = QHBoxLayout(self.widget_63)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.label_41 = QLabel(self.widget_63)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setFont(font11)
        self.label_41.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_31.addWidget(self.label_41, 0, Qt.AlignBottom)

        self.label_42 = QLabel(self.widget_63)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setFont(font11)
        self.label_42.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_31.addWidget(self.label_42, 0, Qt.AlignBottom)

        self.label_43 = QLabel(self.widget_63)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setFont(font11)
        self.label_43.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_31.addWidget(self.label_43, 0, Qt.AlignBottom)


        self.verticalLayout_61.addWidget(self.widget_63)

        self.widget_62 = QWidget(self.widget_60)
        self.widget_62.setObjectName(u"widget_62")
        self.horizontalLayout_30 = QHBoxLayout(self.widget_62)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.spinBox_3 = QSpinBox(self.widget_62)
        self.spinBox_3.setObjectName(u"spinBox_3")
        self.spinBox_3.setMinimumSize(QSize(200, 40))
        self.spinBox_3.setMaximumSize(QSize(200, 40))
        self.spinBox_3.setFont(font11)
        self.spinBox_3.setStyleSheet(u"background-color:#2c313c;\n"
"border-radius: 5px;")
        self.spinBox_3.setMaximum(1)

        self.horizontalLayout_30.addWidget(self.spinBox_3, 0, Qt.AlignTop)

        self.lineEdit_6 = QLineEdit(self.widget_62)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setMinimumSize(QSize(200, 40))
        self.lineEdit_6.setMaximumSize(QSize(200, 40))
        self.lineEdit_6.setFont(font)
        self.lineEdit_6.setStyleSheet(u"background-color:#2c313c;\n"
"border-radius: 5px;")

        self.horizontalLayout_30.addWidget(self.lineEdit_6, 0, Qt.AlignTop)

        self.lineEdit_5 = QLineEdit(self.widget_62)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setMinimumSize(QSize(200, 40))
        self.lineEdit_5.setMaximumSize(QSize(200, 40))
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setStyleSheet(u"background-color:#2c313c;\n"
"border-radius: 5px;")

        self.horizontalLayout_30.addWidget(self.lineEdit_5, 0, Qt.AlignTop)


        self.verticalLayout_61.addWidget(self.widget_62)


        self.horizontalLayout_29.addWidget(self.widget_60)

        self.widget_61 = QWidget(self.widget_59)
        self.widget_61.setObjectName(u"widget_61")
        self.widget_61.setMinimumSize(QSize(230, 250))
        self.widget_61.setMaximumSize(QSize(230, 250))
        self.verticalLayout_60 = QVBoxLayout(self.widget_61)
        self.verticalLayout_60.setObjectName(u"verticalLayout_60")
        self.activerintBtn = QPushButton(self.widget_61)
        self.activerintBtn.setObjectName(u"activerintBtn")
        self.activerintBtn.setMinimumSize(QSize(200, 50))
        self.activerintBtn.setMaximumSize(QSize(200, 50))
        font20 = QFont()
        font20.setPointSize(10)
        self.activerintBtn.setFont(font20)
        self.activerintBtn.clicked.connect(self.activerint)
        self.activerintBtn.setStyleSheet(u"QPushButton{background-color:#2c313c;}\n"
"\n"
"QPushButton:hover{background-color:#16191d;}\n"
"QPushButton:checked{background-color:#16191d;}\n"
"QPushButton:pressed{background-color:#16191d;}\n"
"QPushButton:released{background-color:#16191d;}\n"
"QPushButton:focus:pressed{background-color:#16191d;}")

        self.verticalLayout_60.addWidget(self.activerintBtn, 0, Qt.AlignHCenter)

        self.desactiverintBtn = QPushButton(self.widget_61)
        self.desactiverintBtn.setObjectName(u"desactiverintBtn")
        self.desactiverintBtn.setMinimumSize(QSize(200, 50))
        self.desactiverintBtn.setMaximumSize(QSize(200, 50))
        self.desactiverintBtn.setFont(font20)
        self.desactiverintBtn.clicked.connect(self.desactiverint)
        self.desactiverintBtn.setStyleSheet(u"QPushButton{background-color:#2c313c;}\n"
"\n"
"QPushButton:hover{background-color:#16191d;}\n"
"QPushButton:checked{background-color:#16191d;}\n"
"QPushButton:pressed{background-color:#16191d;}\n"
"QPushButton:released{background-color:#16191d;}\n"
"QPushButton:focus:pressed{background-color:#16191d;}")

        self.verticalLayout_60.addWidget(self.desactiverintBtn, 0, Qt.AlignHCenter)

        self.IpBtn = QPushButton(self.widget_61)
        self.IpBtn.setObjectName(u"IpBtn")
        self.IpBtn.setMinimumSize(QSize(200, 50))
        self.IpBtn.setMaximumSize(QSize(200, 50))
        self.IpBtn.setFont(font20)
        self.IpBtn.clicked.connect(self.afectip)
        self.IpBtn.setStyleSheet(u"QPushButton{background-color:#2c313c;}\n"
"\n"
"QPushButton:hover{background-color:#16191d;}\n"
"QPushButton:checked{background-color:#16191d;}\n"
"QPushButton:pressed{background-color:#16191d;}\n"
"QPushButton:released{background-color:#16191d;}\n"
"QPushButton:focus:pressed{background-color:#16191d;}")

        self.verticalLayout_60.addWidget(self.IpBtn, 0, Qt.AlignHCenter)


        self.horizontalLayout_29.addWidget(self.widget_61)


        self.verticalLayout_55.addWidget(self.widget_59, 0, Qt.AlignHCenter)


        self.verticalLayout_56.addWidget(self.widget_55)

        self.mainPages.addWidget(self.gestionintf)
        self.etatintf = QWidget()
        self.etatintf.setObjectName(u"etatintf")
        self.verticalLayout_59 = QVBoxLayout(self.etatintf)
        self.verticalLayout_59.setObjectName(u"verticalLayout_59")
        self.widget_57 = QWidget(self.etatintf)
        self.widget_57.setObjectName(u"widget_57")
        self.verticalLayout_57 = QVBoxLayout(self.widget_57)
        self.verticalLayout_57.setObjectName(u"verticalLayout_57")
        self.return11 = QPushButton(self.widget_57)
        self.return11.setObjectName(u"return11")
        self.return11.setMinimumSize(QSize(25, 25))
        self.return11.setMaximumSize(QSize(25, 25))
        font21 = QFont()
        font21.setPointSize(5)
        self.return11.setFont(font21)
        self.return11.setStyleSheet(u"background-color:#21252d;\n"
"")
        self.return11.setIcon(icon12)

        self.verticalLayout_57.addWidget(self.return11)

        self.widget_58 = QWidget(self.widget_57)
        self.widget_58.setObjectName(u"widget_58")
        self.widget_58.setMinimumSize(QSize(800, 70))
        self.widget_58.setMaximumSize(QSize(800, 70))
        self.widget_58.setStyleSheet(u"background-color:#21252d;\n"
"border-radius: 15px;")
        self.verticalLayout_58 = QVBoxLayout(self.widget_58)
        self.verticalLayout_58.setObjectName(u"verticalLayout_58")
        self.label_40 = QLabel(self.widget_58)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setFont(font7)

        self.verticalLayout_58.addWidget(self.label_40, 0, Qt.AlignHCenter)


        self.verticalLayout_57.addWidget(self.widget_58, 0, Qt.AlignHCenter)

        self.textEdit_7 = QTextEdit(self.widget_57)
        self.textEdit_7.setObjectName(u"textEdit_7")
        self.textEdit_7.setMinimumSize(QSize(950, 500))
        self.textEdit_7.setMaximumSize(QSize(950, 500))
        self.textEdit_7.setFont(font16)
        self.textEdit_7.setStyleSheet(u"background-color:#21252d;\n"
"border-radius: 15px;")

        self.verticalLayout_57.addWidget(self.textEdit_7, 0, Qt.AlignHCenter)


        self.verticalLayout_59.addWidget(self.widget_57)

        self.mainPages.addWidget(self.etatintf)
        self.Rapport = QWidget()
        self.Rapport.setObjectName(u"Rapport")
        self.verticalLayout_12 = QVBoxLayout(self.Rapport)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.widget_64 = QWidget(self.Rapport)
        self.widget_64.setObjectName(u"widget_64")
        self.widget_64.setStyleSheet(u"border-radius: 15px;")
        self.verticalLayout_62 = QVBoxLayout(self.widget_64)
        self.verticalLayout_62.setObjectName(u"verticalLayout_62")
        self.label_6 = QLabel(self.widget_64)
        self.label_6.setObjectName(u"label_6")
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setMinimumSize(QSize(0, 100))
        self.label_6.setMaximumSize(QSize(16777215, 100))
        self.label_6.setFont(font8)
        self.label_6.setStyleSheet(u"background-color:#21252d;\n"
"border-radius: 15px;")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_62.addWidget(self.label_6)

        self.pdfBtn = QPushButton(self.widget_64)
        self.pdfBtn.setObjectName(u"pdfBtn")
        self.pdfBtn.setMinimumSize(QSize(350, 70))
        self.pdfBtn.setMaximumSize(QSize(350, 70))
        self.pdfBtn.setFont(font10)
        self.pdfBtn.clicked.connect(self.went)
        self.pdfBtn.setStyleSheet(u"QPushButton{background-color:#21252d;}\n"
"\n"
"QPushButton:hover{background-color:#16191d;}\n"
"QPushButton:checked{background-color:#16191d;}\n"
"QPushButton:pressed{background-color:#16191d;}\n"
"\n"
"QPushButton:released{background-color:#16191d;}\n"
"QPushButton:focus:pressed{background-color:#16191d;}")
        icon14 = QIcon()
        icon14.addFile(u":/icons/icons/book.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pdfBtn.setIcon(icon14)
        self.pdfBtn.setIconSize(QSize(50, 50))

        self.verticalLayout_62.addWidget(self.pdfBtn, 0, Qt.AlignHCenter)

        self.pushButton = QPushButton(self.widget_64)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(350, 70))
        self.pushButton.setMaximumSize(QSize(350, 70))
        self.pushButton.setFont(font10)
        self.pushButton.clicked.connect(self.go)
        self.pushButton.setStyleSheet(u"QPushButton{background-color:#21252d;}\n"
"\n"
"QPushButton:hover{background-color:#16191d;}\n"
"QPushButton:checked{background-color:#16191d;}\n"
"QPushButton:pressed{background-color:#16191d;}\n"
"\n"
"QPushButton:released{background-color:#16191d;}\n"
"QPushButton:focus:pressed{background-color:#16191d;}")
        self.pushButton.setIcon(icon14)
        self.pushButton.setIconSize(QSize(50, 50))

        self.verticalLayout_62.addWidget(self.pushButton, 0, Qt.AlignHCenter)


        self.verticalLayout_12.addWidget(self.widget_64)

        self.mainPages.addWidget(self.Rapport)
        self.Performence = QWidget()
        self.Performence.setObjectName(u"Performence")
        self.verticalLayout_13 = QVBoxLayout(self.Performence)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_7 = QLabel(self.Performence)
        self.label_7.setObjectName(u"label_7")
        font22 = QFont()
        font22.setPointSize(60)
        self.label_7.setFont(font22)
        self.label_7.setAlignment(Qt.AlignCenter)

        self.verticalLayout_13.addWidget(self.label_7)

        self.mainPages.addWidget(self.Performence)
        self.Machines = QWidget()
        self.Machines.setObjectName(u"Machines")
        self.verticalLayout_14 = QVBoxLayout(self.Machines)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_8 = QLabel(self.Machines)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font22)
        self.label_8.setAlignment(Qt.AlignCenter)

        self.verticalLayout_14.addWidget(self.label_8)

        self.mainPages.addWidget(self.Machines)

        self.verticalLayout_7.addWidget(self.mainPages)


        self.verticalLayout_6.addWidget(self.mainBodyContent)


        self.horizontalLayout.addWidget(self.main)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.pushButton_8.clicked.connect(self.lineEdit.clear)
        self.pushButton_8.pressed.connect(self.lineEdit_2.clear)

        self.mainPages.setCurrentIndex(0)
        self.pushButton_52.setDefault(False)
        self.pushButton_76.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)



    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#if QT_CONFIG(tooltip)
        self.menuButton.setToolTip(QCoreApplication.translate("MainWindow", u"Menu", None))
#endif // QT_CONFIG(tooltip)
        self.menuButton.setText("")
#if QT_CONFIG(tooltip)
        self.devicesBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Devices", None))
#endif // QT_CONFIG(tooltip)
        self.devicesBtn.setText(QCoreApplication.translate("MainWindow", u"Devices", None))
#if QT_CONFIG(tooltip)
        self.switchBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Switch", None))
#endif // QT_CONFIG(tooltip)
        self.switchBtn.setText(QCoreApplication.translate("MainWindow", u"Switch    ", None))
#if QT_CONFIG(tooltip)
        self.routerBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Router", None))
#endif // QT_CONFIG(tooltip)
        self.routerBtn.setText(QCoreApplication.translate("MainWindow", u"Router    ", None))
#if QT_CONFIG(tooltip)
        self.machinesBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Machines", None))
#endif // QT_CONFIG(tooltip)
        self.machinesBtn.setText(QCoreApplication.translate("MainWindow", u"Machines", None))
#if QT_CONFIG(tooltip)
        self.rapportBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Rapport", None))
#endif // QT_CONFIG(tooltip)
        self.rapportBtn.setText(QCoreApplication.translate("MainWindow", u"Rapport              ", None))
#if QT_CONFIG(tooltip)
        self.performenceBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Performance", None))
#endif // QT_CONFIG(tooltip)
        self.performenceBtn.setText(QCoreApplication.translate("MainWindow", u"Performance       ", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"NetCon", None))
        self.homeBtn.setText("")
#if QT_CONFIG(tooltip)
        self.minimizeBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize Window", None))
#endif // QT_CONFIG(tooltip)
        self.minimizeBtn.setText("")
#if QT_CONFIG(tooltip)
        self.restoreBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Restore Window", None))
#endif // QT_CONFIG(tooltip)
        self.restoreBtn.setText("")
#if QT_CONFIG(tooltip)
        self.closeBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close Window", None))
#endif // QT_CONFIG(tooltip)
        self.closeBtn.setText("")
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Bienvenue sur NetCon", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Application Desktop pour l\u2019administration et la supervision des \u00e9quipements r\u00e9seaux", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Choix du Switch", None))
        self.switch1Btn.setText(QCoreApplication.translate("MainWindow", u" Switch 1", None))
        self.switch2Btn.setText(QCoreApplication.translate("MainWindow", u" Switch 2", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Etat des ports", None))
        self.pushButton_49.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.pushButton_50.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.pushButton_51.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.pushButton_52.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.pushButton_53.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.pushButton_54.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.pushButton_55.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.pushButton_56.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.pushButton_57.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.pushButton_58.setText(QCoreApplication.translate("MainWindow", u"10", None))
        self.pushButton_59.setText(QCoreApplication.translate("MainWindow", u"11", None))
        self.pushButton_60.setText(QCoreApplication.translate("MainWindow", u"12", None))
        self.pushButton_61.setText(QCoreApplication.translate("MainWindow", u"13", None))
        self.pushButton_62.setText(QCoreApplication.translate("MainWindow", u"14", None))
        self.pushButton_63.setText(QCoreApplication.translate("MainWindow", u"15", None))
        self.pushButton_64.setText(QCoreApplication.translate("MainWindow", u"16", None))
        self.pushButton_65.setText(QCoreApplication.translate("MainWindow", u"17", None))
        self.pushButton_66.setText(QCoreApplication.translate("MainWindow", u"18", None))
        self.pushButton_67.setText(QCoreApplication.translate("MainWindow", u"19", None))
        self.pushButton_68.setText(QCoreApplication.translate("MainWindow", u"20", None))
        self.pushButton_69.setText(QCoreApplication.translate("MainWindow", u"21", None))
        self.pushButton_70.setText(QCoreApplication.translate("MainWindow", u"22", None))
        self.pushButton_71.setText(QCoreApplication.translate("MainWindow", u"23", None))
        self.pushButton_72.setText(QCoreApplication.translate("MainWindow", u"24", None))
        self.vlan1confBtn.setText(QCoreApplication.translate("MainWindow", u"Configuration Vlan", None))
        self.infoSwt1Btn.setText(QCoreApplication.translate("MainWindow", u"Informations sur le switch", None))
        self.return1.setText("")
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Configuration Vlan", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Nom", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Adreesse IP", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Masque", None))
        self.spinBox.setSuffix("")
        self.spinBox.setPrefix(QCoreApplication.translate("MainWindow", u"VLAN ", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Ajouter", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Supprimer", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Configuration des ports", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Numero De Port", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Vlan", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Type", None))
        self.comboBox_1.setItemText(0, QCoreApplication.translate("MainWindow", u"1", None))
        self.comboBox_1.setItemText(1, QCoreApplication.translate("MainWindow", u"2", None))
        self.comboBox_1.setItemText(2, QCoreApplication.translate("MainWindow", u"3", None))
        self.comboBox_1.setItemText(3, QCoreApplication.translate("MainWindow", u"4", None))
        self.comboBox_1.setItemText(4, QCoreApplication.translate("MainWindow", u"5", None))
        self.comboBox_1.setItemText(5, QCoreApplication.translate("MainWindow", u"6", None))
        self.comboBox_1.setItemText(6, QCoreApplication.translate("MainWindow", u"7", None))
        self.comboBox_1.setItemText(7, QCoreApplication.translate("MainWindow", u"8", None))
        self.comboBox_1.setItemText(8, QCoreApplication.translate("MainWindow", u"9", None))
        self.comboBox_1.setItemText(9, QCoreApplication.translate("MainWindow", u"10", None))
        self.comboBox_1.setItemText(10, QCoreApplication.translate("MainWindow", u"11", None))
        self.comboBox_1.setItemText(11, QCoreApplication.translate("MainWindow", u"12", None))
        self.comboBox_1.setItemText(12, QCoreApplication.translate("MainWindow", u"13", None))
        self.comboBox_1.setItemText(13, QCoreApplication.translate("MainWindow", u"14", None))
        self.comboBox_1.setItemText(14, QCoreApplication.translate("MainWindow", u"15", None))
        self.comboBox_1.setItemText(15, QCoreApplication.translate("MainWindow", u"16", None))
        self.comboBox_1.setItemText(16, QCoreApplication.translate("MainWindow", u"17", None))
        self.comboBox_1.setItemText(17, QCoreApplication.translate("MainWindow", u"18", None))
        self.comboBox_1.setItemText(18, QCoreApplication.translate("MainWindow", u"19", None))
        self.comboBox_1.setItemText(19, QCoreApplication.translate("MainWindow", u"20", None))
        self.comboBox_1.setItemText(20, QCoreApplication.translate("MainWindow", u"21", None))
        self.comboBox_1.setItemText(21, QCoreApplication.translate("MainWindow", u"22", None))
        self.comboBox_1.setItemText(22, QCoreApplication.translate("MainWindow", u"23", None))
        self.comboBox_1.setItemText(23, QCoreApplication.translate("MainWindow", u"24", None))

        self.comboBox_2.setItemText(0, QCoreApplication.translate("MainWindow", u"10", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("MainWindow", u"20", None))
        self.comboBox_2.setItemText(2, QCoreApplication.translate("MainWindow", u"50", None))

        self.comboBox_4.setItemText(0, QCoreApplication.translate("MainWindow", u"untagged ethernet", None))
        self.comboBox_4.setItemText(1, QCoreApplication.translate("MainWindow", u"tagged ethernet", None))

        self.selectBtn.setText(QCoreApplication.translate("MainWindow", u"Ajouter", None))
        self.delport1.setText(QCoreApplication.translate("MainWindow", u"Supprimer", None))
        self.return2.setText("")
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Table des adresses MAC", None))
        self.getmactable1Btn.setText(QCoreApplication.translate("MainWindow", u"Get", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Configuration", None))
        self.getconf1Btn.setText(QCoreApplication.translate("MainWindow", u"Get", None))
        self.pushButton_6.setText("")
        self.pushButton_5.setText("")
        self.return3.setText("")
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"Table des adresses MAC", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Terminal'; font-size:18pt; font-weight:600; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.return4.setText("")
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"Configuration", None))
        self.textEdit_4.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Terminal'; font-size:15pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'MS Shell Dlg 2';\"><br /></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Etat des ports", None))
        self.pushButton_73.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.pushButton_74.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.pushButton_75.setText(QCoreApplication.translate("MainWindow", u"13", None))
        self.pushButton_76.setText(QCoreApplication.translate("MainWindow", u"14", None))
        self.pushButton_77.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.pushButton_78.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.pushButton_79.setText(QCoreApplication.translate("MainWindow", u"15", None))
        self.pushButton_80.setText(QCoreApplication.translate("MainWindow", u"16", None))
        self.pushButton_81.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.pushButton_82.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.pushButton_83.setText(QCoreApplication.translate("MainWindow", u"17", None))
        self.pushButton_84.setText(QCoreApplication.translate("MainWindow", u"18", None))
        self.pushButton_85.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.pushButton_86.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.pushButton_87.setText(QCoreApplication.translate("MainWindow", u"19", None))
        self.pushButton_88.setText(QCoreApplication.translate("MainWindow", u"20", None))
        self.pushButton_89.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.pushButton_90.setText(QCoreApplication.translate("MainWindow", u"10", None))
        self.pushButton_91.setText(QCoreApplication.translate("MainWindow", u"21", None))
        self.pushButton_92.setText(QCoreApplication.translate("MainWindow", u"22", None))
        self.pushButton_93.setText(QCoreApplication.translate("MainWindow", u"11", None))
        self.pushButton_94.setText(QCoreApplication.translate("MainWindow", u"12", None))
        self.pushButton_95.setText(QCoreApplication.translate("MainWindow", u"23", None))
        self.pushButton_96.setText(QCoreApplication.translate("MainWindow", u"24", None))
        self.vlan2confBtn.setText(QCoreApplication.translate("MainWindow", u"Configuration Vlan", None))
        self.infoSwt2Btn.setText(QCoreApplication.translate("MainWindow", u"Informations sur le switch", None))
        self.return5.setText("")
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"Configuration Vlan", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"Nom", None))
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"Adreesse IP", None))
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"Masque", None))
        self.spinBox_4.setSuffix("")
        self.spinBox_4.setPrefix(QCoreApplication.translate("MainWindow", u"VLAN ", None))
        self.pushButton_15.setText(QCoreApplication.translate("MainWindow", u"Ajouter", None))
        self.pushButton_16.setText(QCoreApplication.translate("MainWindow", u"Supprimer", None))
        self.pushButton_17.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"Configuration des ports", None))
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"Numero De Port", None))
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"Vlan", None))
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"Type", None))
        self.comboBox_3.setItemText(0, QCoreApplication.translate("MainWindow", u"1", None))
        self.comboBox_3.setItemText(1, QCoreApplication.translate("MainWindow", u"2", None))
        self.comboBox_3.setItemText(2, QCoreApplication.translate("MainWindow", u"3", None))
        self.comboBox_3.setItemText(3, QCoreApplication.translate("MainWindow", u"4", None))
        self.comboBox_3.setItemText(4, QCoreApplication.translate("MainWindow", u"5", None))
        self.comboBox_3.setItemText(5, QCoreApplication.translate("MainWindow", u"6", None))
        self.comboBox_3.setItemText(6, QCoreApplication.translate("MainWindow", u"7", None))
        self.comboBox_3.setItemText(7, QCoreApplication.translate("MainWindow", u"8", None))
        self.comboBox_3.setItemText(8, QCoreApplication.translate("MainWindow", u"9", None))
        self.comboBox_3.setItemText(9, QCoreApplication.translate("MainWindow", u"10", None))
        self.comboBox_3.setItemText(10, QCoreApplication.translate("MainWindow", u"11", None))
        self.comboBox_3.setItemText(11, QCoreApplication.translate("MainWindow", u"12", None))
        self.comboBox_3.setItemText(12, QCoreApplication.translate("MainWindow", u"13", None))
        self.comboBox_3.setItemText(13, QCoreApplication.translate("MainWindow", u"14", None))
        self.comboBox_3.setItemText(14, QCoreApplication.translate("MainWindow", u"15", None))
        self.comboBox_3.setItemText(15, QCoreApplication.translate("MainWindow", u"16", None))
        self.comboBox_3.setItemText(16, QCoreApplication.translate("MainWindow", u"17", None))
        self.comboBox_3.setItemText(17, QCoreApplication.translate("MainWindow", u"18", None))
        self.comboBox_3.setItemText(18, QCoreApplication.translate("MainWindow", u"19", None))
        self.comboBox_3.setItemText(19, QCoreApplication.translate("MainWindow", u"20", None))
        self.comboBox_3.setItemText(20, QCoreApplication.translate("MainWindow", u"21", None))
        self.comboBox_3.setItemText(21, QCoreApplication.translate("MainWindow", u"22", None))
        self.comboBox_3.setItemText(22, QCoreApplication.translate("MainWindow", u"23", None))
        self.comboBox_3.setItemText(23, QCoreApplication.translate("MainWindow", u"24", None))

        self.comboBox_9.setItemText(0, QCoreApplication.translate("MainWindow", u"10", None))
        self.comboBox_9.setItemText(1, QCoreApplication.translate("MainWindow", u"20", None))
        self.comboBox_9.setItemText(2, QCoreApplication.translate("MainWindow", u"50", None))

        self.comboBox_10.setItemText(0, QCoreApplication.translate("MainWindow", u"untagged ethernet", None))
        self.comboBox_10.setItemText(1, QCoreApplication.translate("MainWindow", u"tagged ethernet", None))

        self.selectBtn_3.setText(QCoreApplication.translate("MainWindow", u"Ajouter", None))
        self.delport1_2.setText(QCoreApplication.translate("MainWindow", u"Supprimer", None))
        self.return6.setText("")
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"Table des adresses MAC", None))
        self.getmactable2Btn.setText(QCoreApplication.translate("MainWindow", u"Get", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"Configuration", None))
        self.getconf2Btn.setText(QCoreApplication.translate("MainWindow", u"Get", None))
        self.pushButton_7.setText("")
        self.pushButton_9.setText("")
        self.return7.setText("")
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"Table des adresses MAC", None))
        self.return8.setText("")
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"Configuration", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Choix du routeur", None))
        self.routerciscoBtn.setText(QCoreApplication.translate("MainWindow", u" Routeur CISCO", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u" Routeur CISCO", None))
        self.tableroutageBtn.setText(QCoreApplication.translate("MainWindow", u"Table de routage", None))
        self.gestionBtn.setText(QCoreApplication.translate("MainWindow", u"Gestion des interfaces", None))
        self.etatinfBtn.setText(QCoreApplication.translate("MainWindow", u"Etat d'interfaces", None))
        self.return9.setText("")
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"Table de routage", None))
        self.textEdit_5.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Terminal'; font-size:15pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.return10.setText("")
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"Gestion des interfaces", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"Numero", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"Adresse IP", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"Masque", None))
        self.spinBox_3.setPrefix(QCoreApplication.translate("MainWindow", u"Interface ", None))
        self.activerintBtn.setText(QCoreApplication.translate("MainWindow", u"Activer", None))
        self.desactiverintBtn.setText(QCoreApplication.translate("MainWindow", u"D\u00e9sactiver", None))
        self.IpBtn.setText(QCoreApplication.translate("MainWindow", u"Affecter une adresse IP", None))
        self.return11.setText("")
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"Etat d'interfaces", None))
        self.textEdit_7.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Terminal'; font-size:15pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"G\u00e9n\u00e9rer un rapport sous forme fichier PDF", None))
        self.pdfBtn.setText(QCoreApplication.translate("MainWindow", u"Rapport Switch", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Rapport Routeur", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Performance", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Machines", None))

    
    
    #sw1
    def table1(self):
                self.textEdit.setText(testsw1.tablemac())
    def conf1(self):
                self.textEdit_4.setText(testsw1.configinfo())
    def getvlan(self):
                testsw1.affectationdesport(self.comboBox_1.currentText(),self.comboBox_2.currentText(),self.comboBox_4.currentText())
    def addvlan(self):
                testsw1.creerVlan(self.spinBox.value(),self.lineEdit.text(),self.lineEdit_2.text())
    def delvlan(self):
                testsw1.supprimerVlan(self.spinBox.value())
    def delport(self):
                testsw1.removePortFromVlan(self.comboBox_1.currentText(),self.comboBox_2.currentText(),self.comboBox_4.currentText())
    def addtobox(self):
                self.comboBox_2.addItem(f'{self.spinBox.value()}')
    def removefrombox(self):
                self.comboBox_2.removeItem(self.spinBox.value())



                #ports 

    def stat1(self):
                if self.pushButton_49.isCheckable() :
                        testsw1.disablePort(1)
                        self.pushButton_49.setCheckable(False)
                else :
                        testsw1.enablePort(1)
    def stat2(self):
                if self.pushButton_50.isCheckable() :
                        testsw1.disablePort(2)
                        self.pushButton_50.setCheckable(False)
                else :
                        testsw1.enablePort(2)
    def stat3(self):
                if self.pushButton_51.isCheckable() :
                        testsw1.disablePort(3)
                        self.pushButton_51.setCheckable(False)
                else :
                        testsw1.enablePort(3)
    def stat4(self):
                if self.pushButton_52.isCheckable() :
                        testsw1.disablePort(4)
                        self.pushButton_52.setCheckable(False)
                else :
                        testsw1.enablePort(4)
    def stat5(self):
                if self.pushButton_53.isCheckable() :
                        testsw1.disablePort(5)
                        self.pushButton_53.setCheckable(False)
                else :
                        testsw1.enablePort(5)
    def stat6(self):
                if self.pushButton_54.isCheckable() :
                        testsw1.disablePort(6)
                        self.pushButton_54.setCheckable(False)
                else :
                        testsw1.enablePort(6)
    def stat7(self):
                if self.pushButton_55.isCheckable() :
                        testsw1.disablePort(7)
                        self.pushButton_55.setCheckable(False)
                else :
                        testsw1.enablePort(7)
    def stat8(self):
                if self.pushButton_56.isCheckable() :
                        testsw1.disablePort(8)
                        self.pushButton_56.setCheckable(False)
                else :
                        testsw1.enablePort(8)
    def stat9(self):
                if self.pushButton_57.isCheckable() :
                        testsw1.disablePort(9)
                        self.pushButton_57.setCheckable(False)
                else :
                        testsw1.enablePort(9)
    def stat10(self):
                if self.pushButton_58.isCheckable() :
                        testsw1.disablePort(10)
                        self.pushButton_58.setCheckable(False)
                else :
                        testsw1.enablePort(10)
    def stat11(self):
                if self.pushButton_59.isCheckable() :
                        testsw1.disablePort(11)
                        self.pushButton_59.setCheckable(False)
                else :
                        testsw1.enablePort(11)
    def stat12(self):
                if self.pushButton_60.isCheckable() :
                        testsw1.disablePort(12)
                        self.pushButton_60.setCheckable(False)
                else :
                        testsw1.enablePort(12)
    def stat13(self):
                if self.pushButton_61.isCheckable() :
                        testsw1.disablePort(13)
                        self.pushButton_61.setCheckable(False)
                else :
                        testsw1.enablePort(13)
    def stat14(self):
                if self.pushButton_62.isCheckable() :
                        testsw1.disablePort(14)
                        self.pushButton_62.setCheckable(False)
                else :
                        testsw1.enablePort(14)
    def stat15(self):
                if self.pushButton_63.isCheckable() :
                        testsw1.disablePort(15)
                        self.pushButton_63.setCheckable(False)
                else :
                        testsw1.enablePort(15)
    def stat16(self):
                if self.pushButton_64.isCheckable() :
                        testsw1.disablePort(16)
                        self.pushButton_64.setCheckable(False)
                else :
                        testsw1.enablePort(16)
    def stat17(self):
                if self.pushButton_65.isCheckable() :
                        testsw1.disablePort(17)
                        self.pushButton_65.setCheckable(False)
                else :
                        testsw1.enablePort(17)
    def stat18(self):
                if self.pushButton_66.isCheckable() :
                        testsw1.disablePort(18)
                        self.pushButton_66.setCheckable(False)
                else :
                        testsw1.enablePort(18)
    def stat19(self):
                if self.pushButton_67.isCheckable() :
                        testsw1.disablePort(19)
                        self.pushButton_67.setCheckable(False)
                else :
                        testsw1.enablePort(19)
    def stat20(self):
                if self.pushButton_68.isCheckable() :
                        testsw1.disablePort(20)
                        self.pushButton_68.setCheckable(False)
                else :
                        testsw1.enablePort(20)
    def stat21(self):
                if self.pushButton_69.isCheckable() :
                        testsw1.disablePort(21)
                        self.pushButton_69.setCheckable(False)
                else :
                        testsw1.enablePort(21)
    def stat22(self):
                if self.pushButton_70.isCheckable() :
                        testsw1.disablePort(22)
                        self.pushButton_70.setCheckable(False)
                else :
                        testsw1.enablePort(22)
    def stat23(self):
                if self.pushButton_71.isCheckable() :
                        testsw1.disablePort(23)
                        self.pushButton_71.setCheckable(False)
                else :
                        testsw1.enablePort(23)
    def stat24(self):
                if self.pushButton_72.isCheckable() :
                        testsw1.disablePort(24)
                        self.pushButton_72.setCheckable(False)
                else :
                        testsw1.enablePort(24)
    def stat25(self):
                if self.pushButton_73.isCheckable() :
                        testsw2.disablePort(1)
                        self.pushButton_73.setCheckable(False)
                else :
                        testsw2.enablePort(1)
    def stat26(self):
                if self.pushButton_74.isCheckable() :
                        testsw2.disablePort(2)
                        self.pushButton_74.setCheckable(False)
                else :
                        testsw2.enablePort(2)
    def stat27(self):
                if self.pushButton_75.isCheckable() :
                        testsw2.disablePort(3)
                        self.pushButton_75.setCheckable(False)
                else :
                        testsw2.enablePort(3)
    def stat28(self):
                if self.pushButton_76.isCheckable() :
                        testsw2.disablePort(4)
                        self.pushButton_76.setCheckable(False)
                else :
                        testsw2.enablePort(4)
    def stat29(self):
                if self.pushButton_77.isCheckable() :
                        testsw2.disablePort(5)
                        self.pushButton_77.setCheckable(False)
                else :
                        testsw2.enablePort(5)
    def stat30(self):
                if self.pushButton_78.isCheckable() :
                        testsw2.disablePort(6)
                        self.pushButton_78.setCheckable(False)
                else :
                        testsw2.enablePort(6)
    def stat31(self):
                if self.pushButton_79.isCheckable() :
                        testsw2.disablePort(7)
                        self.pushButton_79.setCheckable(False)
                else :
                        testsw2.enablePort(7)
    def stat32(self):
                if self.pushButton_80.isCheckable() :
                        testsw2.disablePort(8)
                        self.pushButton_80.setCheckable(False)
                else :
                        testsw2.enablePort(8)
    def stat33(self):
                if self.pushButton_81.isCheckable() :
                        testsw2.disablePort(9)
                        self.pushButton_81.setCheckable(False)
                else :
                        testsw2.enablePort(9)
    def stat34(self):
                if self.pushButton_82.isCheckable() :
                        testsw2.disablePort(10)
                        self.pushButton_82.setCheckable(False)
                else :
                        testsw2.enablePort(10)
    def stat35(self):
                if self.pushButton_83.isCheckable() :
                        testsw2.disablePort(11)
                        self.pushButton_83.setCheckable(False)
                else :
                        testsw2.enablePort(11)
    def stat36(self):
                if self.pushButton_84.isCheckable() :
                        testsw2.disablePort(12)
                        self.pushButton_84.setCheckable(False)
                else :
                        testsw2.enablePort(12)
    def stat37(self):
                if self.pushButton_85.isCheckable() :
                        testsw2.disablePort(13)
                        self.pushButton_85.setCheckable(False)
                else :
                        testsw2.enablePort(13)
    def stat38(self):
                if self.pushButton_86.isCheckable() :
                        testsw2.disablePort(14)
                        self.pushButton_86.setCheckable(False)
                else :
                        testsw2.enablePort(14)
    def stat39(self):
                if self.pushButton_87.isCheckable() :
                        testsw2.disablePort(15)
                        self.pushButton_87.setCheckable(False)
                else :
                        testsw2.enablePort(15)
    def stat40(self):
                if self.pushButton_88.isCheckable() :
                        testsw2.disablePort(16)
                        self.pushButton_88.setCheckable(False)
                else :
                        testsw2.enablePort(16)
    def stat41(self):
                if self.pushButton_89.isCheckable() :
                        testsw2.disablePort(17)
                        self.pushButton_89.setCheckable(False)
                else :
                        testsw2.enablePort(17)
    def stat42(self):
                if self.pushButton_90.isCheckable() :
                        testsw2.disablePort(18)
                        self.pushButton_90.setCheckable(False)
                else :
                        testsw2.enablePort(18)
    def stat43(self):
                if self.pushButton_91.isCheckable() :
                        testsw2.disablePort(19)
                        self.pushButton_91.setCheckable(False)
                else :
                        testsw2.enablePort(19)
    def stat44(self):
                if self.pushButton_92.isCheckable() :
                        testsw2.disablePort(20)
                        self.pushButton_92.setCheckable(False)
                else :
                        testsw2.enablePort(20)
    def stat45(self):
                if self.pushButton_93.isCheckable() :
                        testsw2.disablePort(21)
                        self.pushButton_93.setCheckable(False)
                else :
                        testsw2.enablePort(21)
    def stat46(self):
                if self.pushButton_94.isCheckable() :
                        testsw2.disablePort(22)
                        self.pushButton_94.setCheckable(False)
                else :
                        testsw2.enablePort(22)
    def stat47(self):
                if self.pushButton_95.isCheckable() :
                        testsw2.disablePort(23)
                        self.pushButton_95.setCheckable(False)
                else :
                        testsw2.enablePort(23)
    def stat48(self):
                if self.pushButton_96.isCheckable() :
                        testsw2.disablePort(24)
                        self.pushButton_96.setCheckable(False)
                else :
                        testsw2.enablePort(24)




    #sw2
    def table2(self):
        self.textEdit_2.setText(testsw2.tablemac())
    def conf2(self):
        self.textEdit_3.setText(testsw2.configinfo())
    def getvlan2(self):
        testsw2.affectationdesport(self.comboBox_9.currentText(),self.comboBox_10.currentText(),self.comboBox_3.currentText())
    def addvlan2(self):
        testsw2.creerVlan(self.spinBox_4.value(),self.lineEdit_7.text(),self.lineEdit_8.text())
    def delvlan2(self):
        testsw2.supprimerVlan(self.spinBox_4.value())
    def delport2(self):
        testsw2.removePortFromVlan(self.comboBox_9.currentText(),self.comboBox_10.currentText(),self.comboBox_3.currentText())
    def addtobox2(self):
        self.comboBox_9.addItem(f'{self.spinBox_4.value()}')
    def removefrombox2(self):
        self.comboBox_9.removeItem(self.spinBox_4.value())

    
    #router
    def tableRt(self):
                self.textEdit_5.setText(testRt.routeTable())
    def activerint(self):
                testRt.enableInterface(self.spinBox_3.value())
    def desactiverint(self):
                testRt.disableInterface(self.spinBox_3.value())
    def afectip(self):
                testRt.affecteripint(self.spinBox_3.value(),self.lineEdit_6.text(),self.lineEdit_5.text())
    def intinfo(self):
                self.textEdit_7.setText(testRt.interfaceInfo())