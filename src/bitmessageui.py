# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bitmessageui.ui'
#
# Created: Thu Jun 13 01:02:50 2013
#      by: PyQt4 UI code generator 4.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(795, 561)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/images/can-icon-24px.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setTabShape(QtGui.QTabWidget.Rounded)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.tabWidget.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.tabWidget.setFont(font)
        self.tabWidget.setTabPosition(QtGui.QTabWidget.North)
        self.tabWidget.setTabShape(QtGui.QTabWidget.Rounded)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.inbox = QtGui.QWidget()
        self.inbox.setObjectName(_fromUtf8("inbox"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.inbox)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.tableWidgetInbox = QtGui.QTableWidget(self.inbox)
        self.tableWidgetInbox.setAlternatingRowColors(True)
        self.tableWidgetInbox.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.tableWidgetInbox.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tableWidgetInbox.setWordWrap(False)
        self.tableWidgetInbox.setObjectName(_fromUtf8("tableWidgetInbox"))
        self.tableWidgetInbox.setColumnCount(4)
        self.tableWidgetInbox.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetInbox.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetInbox.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetInbox.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetInbox.setHorizontalHeaderItem(3, item)
        self.tableWidgetInbox.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidgetInbox.horizontalHeader().setDefaultSectionSize(200)
        self.tableWidgetInbox.horizontalHeader().setHighlightSections(False)
        self.tableWidgetInbox.horizontalHeader().setMinimumSectionSize(27)
        self.tableWidgetInbox.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidgetInbox.horizontalHeader().setStretchLastSection(True)
        self.tableWidgetInbox.verticalHeader().setVisible(False)
        self.tableWidgetInbox.verticalHeader().setDefaultSectionSize(26)
        self.verticalLayout_2.addWidget(self.tableWidgetInbox)
        self.textEditInboxMessage = QtGui.QTextEdit(self.inbox)
        self.textEditInboxMessage.setBaseSize(QtCore.QSize(0, 500))
        self.textEditInboxMessage.setObjectName(_fromUtf8("textEditInboxMessage"))
        self.verticalLayout_2.addWidget(self.textEditInboxMessage)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/images/inbox.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.inbox, icon1, _fromUtf8(""))
        self.send = QtGui.QWidget()
        self.send.setObjectName(_fromUtf8("send"))
        self.gridLayout_2 = QtGui.QGridLayout(self.send)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.pushButtonLoadFromAddressBook = QtGui.QPushButton(self.send)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.pushButtonLoadFromAddressBook.setFont(font)
        self.pushButtonLoadFromAddressBook.setObjectName(_fromUtf8("pushButtonLoadFromAddressBook"))
        self.gridLayout_2.addWidget(self.pushButtonLoadFromAddressBook, 3, 2, 1, 2)
        self.label_4 = QtGui.QLabel(self.send)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_2.addWidget(self.label_4, 5, 0, 1, 1)
        self.comboBoxSendFrom = QtGui.QComboBox(self.send)
        self.comboBoxSendFrom.setMinimumSize(QtCore.QSize(300, 0))
        self.comboBoxSendFrom.setObjectName(_fromUtf8("comboBoxSendFrom"))
        self.gridLayout_2.addWidget(self.comboBoxSendFrom, 2, 1, 1, 1)
        self.label_3 = QtGui.QLabel(self.send)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_2.addWidget(self.label_3, 4, 0, 1, 1)
        self.labelFrom = QtGui.QLabel(self.send)
        self.labelFrom.setText(_fromUtf8(""))
        self.labelFrom.setObjectName(_fromUtf8("labelFrom"))
        self.gridLayout_2.addWidget(self.labelFrom, 2, 2, 1, 3)
        self.radioButtonSpecific = QtGui.QRadioButton(self.send)
        self.radioButtonSpecific.setChecked(True)
        self.radioButtonSpecific.setObjectName(_fromUtf8("radioButtonSpecific"))
        self.gridLayout_2.addWidget(self.radioButtonSpecific, 0, 1, 1, 1)
        self.lineEditTo = QtGui.QLineEdit(self.send)
        self.lineEditTo.setObjectName(_fromUtf8("lineEditTo"))
        self.gridLayout_2.addWidget(self.lineEditTo, 3, 1, 1, 1)
        self.textEditMessage = QtGui.QTextEdit(self.send)
        self.textEditMessage.setObjectName(_fromUtf8("textEditMessage"))
        self.gridLayout_2.addWidget(self.textEditMessage, 5, 1, 2, 5)
        self.label = QtGui.QLabel(self.send)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_2.addWidget(self.label, 3, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.send)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_2.addWidget(self.label_2, 2, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 297, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 6, 0, 1, 1)
        self.radioButtonBroadcast = QtGui.QRadioButton(self.send)
        self.radioButtonBroadcast.setObjectName(_fromUtf8("radioButtonBroadcast"))
        self.gridLayout_2.addWidget(self.radioButtonBroadcast, 1, 1, 1, 3)
        self.lineEditSubject = QtGui.QLineEdit(self.send)
        self.lineEditSubject.setText(_fromUtf8(""))
        self.lineEditSubject.setObjectName(_fromUtf8("lineEditSubject"))
        self.gridLayout_2.addWidget(self.lineEditSubject, 4, 1, 1, 5)
        spacerItem1 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 3, 4, 1, 1)
        self.pushButtonSend = QtGui.QPushButton(self.send)
        self.pushButtonSend.setObjectName(_fromUtf8("pushButtonSend"))
        self.gridLayout_2.addWidget(self.pushButtonSend, 7, 5, 1, 1)
        self.labelSendBroadcastWarning = QtGui.QLabel(self.send)
        self.labelSendBroadcastWarning.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelSendBroadcastWarning.sizePolicy().hasHeightForWidth())
        self.labelSendBroadcastWarning.setSizePolicy(sizePolicy)
        self.labelSendBroadcastWarning.setIndent(-1)
        self.labelSendBroadcastWarning.setObjectName(_fromUtf8("labelSendBroadcastWarning"))
        self.gridLayout_2.addWidget(self.labelSendBroadcastWarning, 7, 1, 1, 4)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/images/send.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.send, icon2, _fromUtf8(""))
        self.sent = QtGui.QWidget()
        self.sent.setObjectName(_fromUtf8("sent"))
        self.verticalLayout = QtGui.QVBoxLayout(self.sent)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.tableWidgetSent = QtGui.QTableWidget(self.sent)
        self.tableWidgetSent.setDragDropMode(QtGui.QAbstractItemView.DragDrop)
        self.tableWidgetSent.setAlternatingRowColors(True)
        self.tableWidgetSent.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.tableWidgetSent.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tableWidgetSent.setWordWrap(False)
        self.tableWidgetSent.setObjectName(_fromUtf8("tableWidgetSent"))
        self.tableWidgetSent.setColumnCount(4)
        self.tableWidgetSent.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetSent.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetSent.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetSent.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetSent.setHorizontalHeaderItem(3, item)
        self.tableWidgetSent.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidgetSent.horizontalHeader().setDefaultSectionSize(130)
        self.tableWidgetSent.horizontalHeader().setHighlightSections(False)
        self.tableWidgetSent.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidgetSent.horizontalHeader().setStretchLastSection(True)
        self.tableWidgetSent.verticalHeader().setVisible(False)
        self.tableWidgetSent.verticalHeader().setStretchLastSection(False)
        self.verticalLayout.addWidget(self.tableWidgetSent)
        self.textEditSentMessage = QtGui.QTextEdit(self.sent)
        self.textEditSentMessage.setObjectName(_fromUtf8("textEditSentMessage"))
        self.verticalLayout.addWidget(self.textEditSentMessage)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/images/sent.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.sent, icon3, _fromUtf8(""))
        self.youridentities = QtGui.QWidget()
        self.youridentities.setObjectName(_fromUtf8("youridentities"))
        self.gridLayout_3 = QtGui.QGridLayout(self.youridentities)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.pushButtonNewAddress = QtGui.QPushButton(self.youridentities)
        self.pushButtonNewAddress.setObjectName(_fromUtf8("pushButtonNewAddress"))
        self.gridLayout_3.addWidget(self.pushButtonNewAddress, 0, 0, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(689, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem2, 0, 1, 1, 1)
        self.tableWidgetYourIdentities = QtGui.QTableWidget(self.youridentities)
        self.tableWidgetYourIdentities.setFrameShadow(QtGui.QFrame.Sunken)
        self.tableWidgetYourIdentities.setLineWidth(1)
        self.tableWidgetYourIdentities.setAlternatingRowColors(True)
        self.tableWidgetYourIdentities.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.tableWidgetYourIdentities.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tableWidgetYourIdentities.setObjectName(_fromUtf8("tableWidgetYourIdentities"))
        self.tableWidgetYourIdentities.setColumnCount(3)
        self.tableWidgetYourIdentities.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        font = QtGui.QFont()
        font.setKerning(True)
        item.setFont(font)
        self.tableWidgetYourIdentities.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetYourIdentities.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetYourIdentities.setHorizontalHeaderItem(2, item)
        self.tableWidgetYourIdentities.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidgetYourIdentities.horizontalHeader().setDefaultSectionSize(346)
        self.tableWidgetYourIdentities.horizontalHeader().setMinimumSectionSize(52)
        self.tableWidgetYourIdentities.horizontalHeader().setSortIndicatorShown(True)
        self.tableWidgetYourIdentities.horizontalHeader().setStretchLastSection(True)
        self.tableWidgetYourIdentities.verticalHeader().setVisible(False)
        self.tableWidgetYourIdentities.verticalHeader().setDefaultSectionSize(26)
        self.tableWidgetYourIdentities.verticalHeader().setSortIndicatorShown(False)
        self.tableWidgetYourIdentities.verticalHeader().setStretchLastSection(False)
        self.gridLayout_3.addWidget(self.tableWidgetYourIdentities, 1, 0, 1, 2)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/images/identities.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.youridentities, icon4, _fromUtf8(""))
        self.subscriptions = QtGui.QWidget()
        self.subscriptions.setObjectName(_fromUtf8("subscriptions"))
        self.gridLayout_4 = QtGui.QGridLayout(self.subscriptions)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.label_5 = QtGui.QLabel(self.subscriptions)
        self.label_5.setWordWrap(True)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout_4.addWidget(self.label_5, 0, 0, 1, 2)
        self.pushButtonAddSubscription = QtGui.QPushButton(self.subscriptions)
        self.pushButtonAddSubscription.setObjectName(_fromUtf8("pushButtonAddSubscription"))
        self.gridLayout_4.addWidget(self.pushButtonAddSubscription, 1, 0, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(689, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem3, 1, 1, 1, 1)
        self.tableWidgetSubscriptions = QtGui.QTableWidget(self.subscriptions)
        self.tableWidgetSubscriptions.setAlternatingRowColors(True)
        self.tableWidgetSubscriptions.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.tableWidgetSubscriptions.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tableWidgetSubscriptions.setObjectName(_fromUtf8("tableWidgetSubscriptions"))
        self.tableWidgetSubscriptions.setColumnCount(2)
        self.tableWidgetSubscriptions.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetSubscriptions.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetSubscriptions.setHorizontalHeaderItem(1, item)
        self.tableWidgetSubscriptions.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidgetSubscriptions.horizontalHeader().setDefaultSectionSize(400)
        self.tableWidgetSubscriptions.horizontalHeader().setHighlightSections(False)
        self.tableWidgetSubscriptions.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidgetSubscriptions.horizontalHeader().setStretchLastSection(True)
        self.tableWidgetSubscriptions.verticalHeader().setVisible(False)
        self.gridLayout_4.addWidget(self.tableWidgetSubscriptions, 2, 0, 1, 2)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/images/subscriptions.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.subscriptions, icon5, _fromUtf8(""))
        self.addressbook = QtGui.QWidget()
        self.addressbook.setObjectName(_fromUtf8("addressbook"))
        self.gridLayout_5 = QtGui.QGridLayout(self.addressbook)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.label_6 = QtGui.QLabel(self.addressbook)
        self.label_6.setWordWrap(True)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout_5.addWidget(self.label_6, 0, 0, 1, 2)
        self.pushButtonAddAddressBook = QtGui.QPushButton(self.addressbook)
        self.pushButtonAddAddressBook.setObjectName(_fromUtf8("pushButtonAddAddressBook"))
        self.gridLayout_5.addWidget(self.pushButtonAddAddressBook, 1, 0, 1, 1)
        spacerItem4 = QtGui.QSpacerItem(689, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem4, 1, 1, 1, 1)
        self.tableWidgetAddressBook = QtGui.QTableWidget(self.addressbook)
        self.tableWidgetAddressBook.setAlternatingRowColors(True)
        self.tableWidgetAddressBook.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.tableWidgetAddressBook.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tableWidgetAddressBook.setObjectName(_fromUtf8("tableWidgetAddressBook"))
        self.tableWidgetAddressBook.setColumnCount(2)
        self.tableWidgetAddressBook.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetAddressBook.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetAddressBook.setHorizontalHeaderItem(1, item)
        self.tableWidgetAddressBook.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidgetAddressBook.horizontalHeader().setDefaultSectionSize(400)
        self.tableWidgetAddressBook.horizontalHeader().setHighlightSections(False)
        self.tableWidgetAddressBook.horizontalHeader().setStretchLastSection(True)
        self.tableWidgetAddressBook.verticalHeader().setVisible(False)
        self.gridLayout_5.addWidget(self.tableWidgetAddressBook, 2, 0, 1, 2)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/images/addressbook.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.addressbook, icon6, _fromUtf8(""))
        self.blackwhitelist = QtGui.QWidget()
        self.blackwhitelist.setObjectName(_fromUtf8("blackwhitelist"))
        self.gridLayout_6 = QtGui.QGridLayout(self.blackwhitelist)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.radioButtonBlacklist = QtGui.QRadioButton(self.blackwhitelist)
        self.radioButtonBlacklist.setChecked(True)
        self.radioButtonBlacklist.setObjectName(_fromUtf8("radioButtonBlacklist"))
        self.gridLayout_6.addWidget(self.radioButtonBlacklist, 0, 0, 1, 2)
        self.radioButtonWhitelist = QtGui.QRadioButton(self.blackwhitelist)
        self.radioButtonWhitelist.setObjectName(_fromUtf8("radioButtonWhitelist"))
        self.gridLayout_6.addWidget(self.radioButtonWhitelist, 1, 0, 1, 2)
        self.pushButtonAddBlacklist = QtGui.QPushButton(self.blackwhitelist)
        self.pushButtonAddBlacklist.setObjectName(_fromUtf8("pushButtonAddBlacklist"))
        self.gridLayout_6.addWidget(self.pushButtonAddBlacklist, 2, 0, 1, 1)
        spacerItem5 = QtGui.QSpacerItem(689, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem5, 2, 1, 1, 1)
        self.tableWidgetBlacklist = QtGui.QTableWidget(self.blackwhitelist)
        self.tableWidgetBlacklist.setAlternatingRowColors(True)
        self.tableWidgetBlacklist.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.tableWidgetBlacklist.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tableWidgetBlacklist.setObjectName(_fromUtf8("tableWidgetBlacklist"))
        self.tableWidgetBlacklist.setColumnCount(2)
        self.tableWidgetBlacklist.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetBlacklist.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetBlacklist.setHorizontalHeaderItem(1, item)
        self.tableWidgetBlacklist.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidgetBlacklist.horizontalHeader().setDefaultSectionSize(400)
        self.tableWidgetBlacklist.horizontalHeader().setHighlightSections(False)
        self.tableWidgetBlacklist.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidgetBlacklist.horizontalHeader().setStretchLastSection(True)
        self.tableWidgetBlacklist.verticalHeader().setVisible(False)
        self.gridLayout_6.addWidget(self.tableWidgetBlacklist, 3, 0, 1, 2)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/images/blacklist.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.blackwhitelist, icon7, _fromUtf8(""))
        self.networkstatus = QtGui.QWidget()
        self.networkstatus.setObjectName(_fromUtf8("networkstatus"))
        self.pushButtonStatusIcon = QtGui.QPushButton(self.networkstatus)
        self.pushButtonStatusIcon.setGeometry(QtCore.QRect(680, 440, 21, 23))
        self.pushButtonStatusIcon.setText(_fromUtf8(""))
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/images/redicon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonStatusIcon.setIcon(icon8)
        self.pushButtonStatusIcon.setFlat(True)
        self.pushButtonStatusIcon.setObjectName(_fromUtf8("pushButtonStatusIcon"))
        self.tableWidgetConnectionCount = QtGui.QTableWidget(self.networkstatus)
        self.tableWidgetConnectionCount.setGeometry(QtCore.QRect(20, 70, 241, 241))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(212, 208, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 208, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 208, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.tableWidgetConnectionCount.setPalette(palette)
        self.tableWidgetConnectionCount.setFrameShape(QtGui.QFrame.Box)
        self.tableWidgetConnectionCount.setFrameShadow(QtGui.QFrame.Plain)
        self.tableWidgetConnectionCount.setProperty("showDropIndicator", False)
        self.tableWidgetConnectionCount.setAlternatingRowColors(True)
        self.tableWidgetConnectionCount.setSelectionMode(QtGui.QAbstractItemView.NoSelection)
        self.tableWidgetConnectionCount.setObjectName(_fromUtf8("tableWidgetConnectionCount"))
        self.tableWidgetConnectionCount.setColumnCount(2)
        self.tableWidgetConnectionCount.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetConnectionCount.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetConnectionCount.setHorizontalHeaderItem(1, item)
        self.tableWidgetConnectionCount.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidgetConnectionCount.horizontalHeader().setHighlightSections(False)
        self.tableWidgetConnectionCount.horizontalHeader().setStretchLastSection(True)
        self.tableWidgetConnectionCount.verticalHeader().setVisible(False)
        self.labelTotalConnections = QtGui.QLabel(self.networkstatus)
        self.labelTotalConnections.setGeometry(QtCore.QRect(20, 30, 401, 16))
        self.labelTotalConnections.setObjectName(_fromUtf8("labelTotalConnections"))
        self.labelStartupTime = QtGui.QLabel(self.networkstatus)
        self.labelStartupTime.setGeometry(QtCore.QRect(320, 110, 331, 20))
        self.labelStartupTime.setObjectName(_fromUtf8("labelStartupTime"))
        self.labelMessageCount = QtGui.QLabel(self.networkstatus)
        self.labelMessageCount.setGeometry(QtCore.QRect(350, 130, 361, 16))
        self.labelMessageCount.setObjectName(_fromUtf8("labelMessageCount"))
        self.labelPubkeyCount = QtGui.QLabel(self.networkstatus)
        self.labelPubkeyCount.setGeometry(QtCore.QRect(350, 170, 331, 16))
        self.labelPubkeyCount.setObjectName(_fromUtf8("labelPubkeyCount"))
        self.labelBroadcastCount = QtGui.QLabel(self.networkstatus)
        self.labelBroadcastCount.setGeometry(QtCore.QRect(350, 150, 351, 16))
        self.labelBroadcastCount.setObjectName(_fromUtf8("labelBroadcastCount"))
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/images/networkstatus.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.networkstatus, icon9, _fromUtf8(""))
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 795, 18))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuSettings = QtGui.QMenu(self.menubar)
        self.menuSettings.setObjectName(_fromUtf8("menuSettings"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setMaximumSize(QtCore.QSize(16777215, 22))
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionImport_keys = QtGui.QAction(MainWindow)
        self.actionImport_keys.setObjectName(_fromUtf8("actionImport_keys"))
        self.actionManageKeys = QtGui.QAction(MainWindow)
        self.actionManageKeys.setCheckable(False)
        self.actionManageKeys.setEnabled(True)
        self.actionManageKeys.setObjectName(_fromUtf8("actionManageKeys"))
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionHelp = QtGui.QAction(MainWindow)
        self.actionHelp.setObjectName(_fromUtf8("actionHelp"))
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.actionSettings = QtGui.QAction(MainWindow)
        self.actionSettings.setObjectName(_fromUtf8("actionSettings"))
        self.actionRegenerateDeterministicAddresses = QtGui.QAction(MainWindow)
        self.actionRegenerateDeterministicAddresses.setObjectName(_fromUtf8("actionRegenerateDeterministicAddresses"))
        self.actionDeleteAllTrashedMessages = QtGui.QAction(MainWindow)
        self.actionDeleteAllTrashedMessages.setObjectName(_fromUtf8("actionDeleteAllTrashedMessages"))
        self.menuFile.addAction(self.actionManageKeys)
        self.menuFile.addAction(self.actionDeleteAllTrashedMessages)
        self.menuFile.addAction(self.actionRegenerateDeterministicAddresses)
        self.menuFile.addAction(self.actionExit)
        self.menuSettings.addAction(self.actionSettings)
        self.menuHelp.addAction(self.actionHelp)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.radioButtonSpecific, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.lineEditTo.setEnabled)
        QtCore.QObject.connect(self.radioButtonSpecific, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.labelSendBroadcastWarning.hide)
        QtCore.QObject.connect(self.radioButtonBroadcast, QtCore.SIGNAL(_fromUtf8("clicked()")), self.labelSendBroadcastWarning.show)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.tabWidget, self.tableWidgetInbox)
        MainWindow.setTabOrder(self.tableWidgetInbox, self.textEditInboxMessage)
        MainWindow.setTabOrder(self.textEditInboxMessage, self.radioButtonSpecific)
        MainWindow.setTabOrder(self.radioButtonSpecific, self.radioButtonBroadcast)
        MainWindow.setTabOrder(self.radioButtonBroadcast, self.comboBoxSendFrom)
        MainWindow.setTabOrder(self.comboBoxSendFrom, self.lineEditTo)
        MainWindow.setTabOrder(self.lineEditTo, self.pushButtonLoadFromAddressBook)
        MainWindow.setTabOrder(self.pushButtonLoadFromAddressBook, self.lineEditSubject)
        MainWindow.setTabOrder(self.lineEditSubject, self.textEditMessage)
        MainWindow.setTabOrder(self.textEditMessage, self.pushButtonSend)
        MainWindow.setTabOrder(self.pushButtonSend, self.tableWidgetSent)
        MainWindow.setTabOrder(self.tableWidgetSent, self.textEditSentMessage)
        MainWindow.setTabOrder(self.textEditSentMessage, self.pushButtonNewAddress)
        MainWindow.setTabOrder(self.pushButtonNewAddress, self.tableWidgetYourIdentities)
        MainWindow.setTabOrder(self.tableWidgetYourIdentities, self.pushButtonAddSubscription)
        MainWindow.setTabOrder(self.pushButtonAddSubscription, self.tableWidgetSubscriptions)
        MainWindow.setTabOrder(self.tableWidgetSubscriptions, self.pushButtonAddAddressBook)
        MainWindow.setTabOrder(self.pushButtonAddAddressBook, self.tableWidgetAddressBook)
        MainWindow.setTabOrder(self.tableWidgetAddressBook, self.radioButtonBlacklist)
        MainWindow.setTabOrder(self.radioButtonBlacklist, self.radioButtonWhitelist)
        MainWindow.setTabOrder(self.radioButtonWhitelist, self.pushButtonAddBlacklist)
        MainWindow.setTabOrder(self.pushButtonAddBlacklist, self.tableWidgetBlacklist)
        MainWindow.setTabOrder(self.tableWidgetBlacklist, self.tableWidgetConnectionCount)
        MainWindow.setTabOrder(self.tableWidgetConnectionCount, self.pushButtonStatusIcon)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Bitmessage", None))
        self.tableWidgetInbox.setSortingEnabled(True)
        item = self.tableWidgetInbox.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "To", None))
        item = self.tableWidgetInbox.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "From", None))
        item = self.tableWidgetInbox.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Subject", None))
        item = self.tableWidgetInbox.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Received", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.inbox), _translate("MainWindow", "Inbox", None))
        self.pushButtonLoadFromAddressBook.setText(_translate("MainWindow", "Load from Address book", None))
        self.label_4.setText(_translate("MainWindow", "Message:", None))
        self.label_3.setText(_translate("MainWindow", "Subject:", None))
        self.radioButtonSpecific.setText(_translate("MainWindow", "Send to one or more specific people", None))
        self.textEditMessage.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.label.setText(_translate("MainWindow", "To:", None))
        self.label_2.setText(_translate("MainWindow", "From:", None))
        self.radioButtonBroadcast.setText(_translate("MainWindow", "Broadcast to everyone who is subscribed to your address", None))
        self.pushButtonSend.setText(_translate("MainWindow", "Send", None))
        self.labelSendBroadcastWarning.setText(_translate("MainWindow", "Be aware that broadcasts are only encrypted with your address. Anyone who knows your address can read them.", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.send), _translate("MainWindow", "Send", None))
        self.tableWidgetSent.setSortingEnabled(True)
        item = self.tableWidgetSent.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "To", None))
        item = self.tableWidgetSent.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "From", None))
        item = self.tableWidgetSent.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Subject", None))
        item = self.tableWidgetSent.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Status", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.sent), _translate("MainWindow", "Sent", None))
        self.pushButtonNewAddress.setText(_translate("MainWindow", "New", None))
        self.tableWidgetYourIdentities.setSortingEnabled(True)
        item = self.tableWidgetYourIdentities.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Label (not shown to anyone)", None))
        item = self.tableWidgetYourIdentities.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Address", None))
        item = self.tableWidgetYourIdentities.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Stream", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.youridentities), _translate("MainWindow", "Your Identities", None))
        self.label_5.setText(_translate("MainWindow", "Here you can subscribe to \'broadcast messages\' that are sent by other users. Messages will appear in your Inbox. Addresses here override those on the Blacklist tab.", None))
        self.pushButtonAddSubscription.setText(_translate("MainWindow", "Add new Subscription", None))
        self.tableWidgetSubscriptions.setSortingEnabled(True)
        item = self.tableWidgetSubscriptions.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Label", None))
        item = self.tableWidgetSubscriptions.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Address", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.subscriptions), _translate("MainWindow", "Subscriptions", None))
        self.label_6.setText(_translate("MainWindow", "The Address book is useful for adding names or labels to other people\'s Bitmessage addresses so that you can recognize them more easily in your inbox. You can add entries here using the \'Add\' button, or from your inbox by right-clicking on a message.", None))
        self.pushButtonAddAddressBook.setText(_translate("MainWindow", "Add new entry", None))
        self.tableWidgetAddressBook.setSortingEnabled(True)
        item = self.tableWidgetAddressBook.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Name or Label", None))
        item = self.tableWidgetAddressBook.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Address", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.addressbook), _translate("MainWindow", "Address Book", None))
        self.radioButtonBlacklist.setText(_translate("MainWindow", "Use a Blacklist (Allow all incoming messages except those on the Blacklist)", None))
        self.radioButtonWhitelist.setText(_translate("MainWindow", "Use a Whitelist (Block all incoming messages except those on the Whitelist)", None))
        self.pushButtonAddBlacklist.setText(_translate("MainWindow", "Add new entry", None))
        self.tableWidgetBlacklist.setSortingEnabled(True)
        item = self.tableWidgetBlacklist.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Name or Label", None))
        item = self.tableWidgetBlacklist.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Address", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.blackwhitelist), _translate("MainWindow", "Blacklist", None))
        item = self.tableWidgetConnectionCount.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Stream Number", None))
        item = self.tableWidgetConnectionCount.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Number of Connections", None))
        self.labelTotalConnections.setText(_translate("MainWindow", "Total connections: 0", None))
        self.labelStartupTime.setText(_translate("MainWindow", "Since startup at asdf:", None))
        self.labelMessageCount.setText(_translate("MainWindow", "Processed 0 person-to-person message.", None))
        self.labelPubkeyCount.setText(_translate("MainWindow", "Processed 0 public key.", None))
        self.labelBroadcastCount.setText(_translate("MainWindow", "Processed 0 broadcast.", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.networkstatus), _translate("MainWindow", "Network Status", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuSettings.setTitle(_translate("MainWindow", "Settings", None))
        self.menuHelp.setTitle(_translate("MainWindow", "Help", None))
        self.actionImport_keys.setText(_translate("MainWindow", "Import keys", None))
        self.actionManageKeys.setText(_translate("MainWindow", "Manage keys", None))
        self.actionExit.setText(_translate("MainWindow", "Quit", None))
        self.actionHelp.setText(_translate("MainWindow", "Help", None))
        self.actionAbout.setText(_translate("MainWindow", "About", None))
        self.actionSettings.setText(_translate("MainWindow", "Settings", None))
        self.actionRegenerateDeterministicAddresses.setText(_translate("MainWindow", "Regenerate deterministic addresses", None))
        self.actionDeleteAllTrashedMessages.setText(_translate("MainWindow", "Delete all trashed messages", None))

import bitmessage_icons_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

