# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dave.ui'
#
# Created: Thu Dec 31 10:53:23 2015
#      by: PyQt4 UI code generator 4.10.3
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
        MainWindow.resize(590, 723)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(590, 500))
        MainWindow.setAcceptDrops(True)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.mainGridLayout = QtGui.QGridLayout(self.centralwidget)
        self.mainGridLayout.setMargin(2)
        self.mainGridLayout.setSpacing(2)
        self.mainGridLayout.setObjectName(_fromUtf8("mainGridLayout"))
        self.sequenceGroupBox = QtGui.QGroupBox(self.centralwidget)
        self.sequenceGroupBox.setObjectName(_fromUtf8("sequenceGroupBox"))
        self.verticalLayout = QtGui.QVBoxLayout(self.sequenceGroupBox)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.sequenceLabel = QtGui.QLabel(self.sequenceGroupBox)
        self.sequenceLabel.setObjectName(_fromUtf8("sequenceLabel"))
        self.verticalLayout.addWidget(self.sequenceLabel)
        self.mainGridLayout.addWidget(self.sequenceGroupBox, 0, 1, 1, 4)
        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setMargin(0)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.notificationGroupBox = QtGui.QGroupBox(self.widget)
        self.notificationGroupBox.setMinimumSize(QtCore.QSize(260, 0))
        self.notificationGroupBox.setObjectName(_fromUtf8("notificationGroupBox"))
        self.gridLayout = QtGui.QGridLayout(self.notificationGroupBox)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.estimatesGroupBox = QtGui.QGroupBox(self.notificationGroupBox)
        self.estimatesGroupBox.setMinimumSize(QtCore.QSize(84, 0))
        self.estimatesGroupBox.setObjectName(_fromUtf8("estimatesGroupBox"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.estimatesGroupBox)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.spaceLabel = QtGui.QLabel(self.estimatesGroupBox)
        self.spaceLabel.setObjectName(_fromUtf8("spaceLabel"))
        self.verticalLayout_2.addWidget(self.spaceLabel)
        self.timeLabel = QtGui.QLabel(self.estimatesGroupBox)
        self.timeLabel.setObjectName(_fromUtf8("timeLabel"))
        self.verticalLayout_2.addWidget(self.timeLabel)
        self.remainingLabel = QtGui.QLabel(self.estimatesGroupBox)
        self.remainingLabel.setObjectName(_fromUtf8("remainingLabel"))
        self.verticalLayout_2.addWidget(self.remainingLabel)
        self.completionLabel = QtGui.QLabel(self.estimatesGroupBox)
        self.completionLabel.setObjectName(_fromUtf8("completionLabel"))
        self.verticalLayout_2.addWidget(self.completionLabel)
        self.gridLayout.addWidget(self.estimatesGroupBox, 11, 0, 1, 3)
        self.fromAddressLineEdit = QtGui.QLineEdit(self.notificationGroupBox)
        self.fromAddressLineEdit.setObjectName(_fromUtf8("fromAddressLineEdit"))
        self.gridLayout.addWidget(self.fromAddressLineEdit, 4, 0, 1, 3)
        self.statusMsgCheckBox = QtGui.QCheckBox(self.notificationGroupBox)
        self.statusMsgCheckBox.setObjectName(_fromUtf8("statusMsgCheckBox"))
        self.gridLayout.addWidget(self.statusMsgCheckBox, 10, 0, 1, 1)
        self.fromPasswordLabel = QtGui.QLabel(self.notificationGroupBox)
        self.fromPasswordLabel.setObjectName(_fromUtf8("fromPasswordLabel"))
        self.gridLayout.addWidget(self.fromPasswordLabel, 5, 0, 1, 3)
        self.errorMsgCheckBox = QtGui.QCheckBox(self.notificationGroupBox)
        self.errorMsgCheckBox.setObjectName(_fromUtf8("errorMsgCheckBox"))
        self.gridLayout.addWidget(self.errorMsgCheckBox, 9, 0, 1, 1)
        self.frequencyLabel = QtGui.QLabel(self.notificationGroupBox)
        self.frequencyLabel.setObjectName(_fromUtf8("frequencyLabel"))
        self.gridLayout.addWidget(self.frequencyLabel, 10, 1, 1, 1)
        self.frequencySpinBox = QtGui.QSpinBox(self.notificationGroupBox)
        self.frequencySpinBox.setObjectName(_fromUtf8("frequencySpinBox"))
        self.gridLayout.addWidget(self.frequencySpinBox, 10, 2, 1, 1)
        self.toAddressLabel = QtGui.QLabel(self.notificationGroupBox)
        self.toAddressLabel.setObjectName(_fromUtf8("toAddressLabel"))
        self.gridLayout.addWidget(self.toAddressLabel, 7, 0, 1, 3)
        self.smtpServerLabel = QtGui.QLabel(self.notificationGroupBox)
        self.smtpServerLabel.setObjectName(_fromUtf8("smtpServerLabel"))
        self.gridLayout.addWidget(self.smtpServerLabel, 1, 0, 1, 3)
        self.fromAddressLabel = QtGui.QLabel(self.notificationGroupBox)
        self.fromAddressLabel.setObjectName(_fromUtf8("fromAddressLabel"))
        self.gridLayout.addWidget(self.fromAddressLabel, 3, 0, 1, 3)
        self.toAddressLineEdit = QtGui.QLineEdit(self.notificationGroupBox)
        self.toAddressLineEdit.setObjectName(_fromUtf8("toAddressLineEdit"))
        self.gridLayout.addWidget(self.toAddressLineEdit, 8, 0, 1, 3)
        self.smtpServerLineEdit = QtGui.QLineEdit(self.notificationGroupBox)
        self.smtpServerLineEdit.setText(_fromUtf8(""))
        self.smtpServerLineEdit.setObjectName(_fromUtf8("smtpServerLineEdit"))
        self.gridLayout.addWidget(self.smtpServerLineEdit, 2, 0, 1, 3)
        self.fromPasswordLineEdit = QtGui.QLineEdit(self.notificationGroupBox)
        self.fromPasswordLineEdit.setEchoMode(QtGui.QLineEdit.PasswordEchoOnEdit)
        self.fromPasswordLineEdit.setObjectName(_fromUtf8("fromPasswordLineEdit"))
        self.gridLayout.addWidget(self.fromPasswordLineEdit, 6, 0, 1, 3)
        self.GroupBox = QtGui.QGroupBox(self.notificationGroupBox)
        self.GroupBox.setMinimumSize(QtCore.QSize(0, 50))
        self.GroupBox.setObjectName(_fromUtf8("GroupBox"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.GroupBox)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.progressBar = QtGui.QProgressBar(self.GroupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.verticalLayout_4.addWidget(self.progressBar)
        self.gridLayout.addWidget(self.GroupBox, 12, 0, 1, 3)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 14, 0, 1, 1)
        self.warningsGroupBox = QtGui.QGroupBox(self.notificationGroupBox)
        self.warningsGroupBox.setObjectName(_fromUtf8("warningsGroupBox"))
        self.gridLayout_2 = QtGui.QGridLayout(self.warningsGroupBox)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.numWarningsToPause = QtGui.QSpinBox(self.warningsGroupBox)
        self.numWarningsToPause.setMinimum(1)
        self.numWarningsToPause.setObjectName(_fromUtf8("numWarningsToPause"))
        self.gridLayout_2.addWidget(self.numWarningsToPause, 1, 0, 1, 1)
        self.numWarningsToPauseLabel = QtGui.QLabel(self.warningsGroupBox)
        self.numWarningsToPauseLabel.setObjectName(_fromUtf8("numWarningsToPauseLabel"))
        self.gridLayout_2.addWidget(self.numWarningsToPauseLabel, 1, 1, 1, 1)
        self.clearWarningsPushButton = QtGui.QPushButton(self.warningsGroupBox)
        self.clearWarningsPushButton.setObjectName(_fromUtf8("clearWarningsPushButton"))
        self.gridLayout_2.addWidget(self.clearWarningsPushButton, 2, 0, 1, 1)
        self.currentWarnings = DaveWarningsViewer(self.warningsGroupBox)
        self.currentWarnings.setObjectName(_fromUtf8("currentWarnings"))
        self.gridLayout_2.addWidget(self.currentWarnings, 0, 0, 1, 2)
        self.gridLayout.addWidget(self.warningsGroupBox, 13, 0, 1, 2)
        self.verticalLayout_5.addWidget(self.notificationGroupBox)
        self.mainGridLayout.addWidget(self.widget, 1, 4, 1, 1)
        self.widget_2 = QtGui.QWidget(self.centralwidget)
        self.widget_2.setObjectName(_fromUtf8("widget_2"))
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.widget_2)
        self.verticalLayout_7.setSpacing(2)
        self.verticalLayout_7.setMargin(2)
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.commandGroupBox = QtGui.QGroupBox(self.widget_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.commandGroupBox.sizePolicy().hasHeightForWidth())
        self.commandGroupBox.setSizePolicy(sizePolicy)
        self.commandGroupBox.setObjectName(_fromUtf8("commandGroupBox"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.commandGroupBox)
        self.verticalLayout_3.setMargin(4)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.commandSequenceTreeView = DaveCommandTreeViewer(self.commandGroupBox)
        self.commandSequenceTreeView.setObjectName(_fromUtf8("commandSequenceTreeView"))
        self.verticalLayout_3.addWidget(self.commandSequenceTreeView)
        self.verticalLayout_7.addWidget(self.commandGroupBox)
        self.groupBox = QtGui.QGroupBox(self.widget_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMaximumSize(QtCore.QSize(16777215, 185))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_6.setMargin(4)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.commandTableView = QtGui.QTableView(self.groupBox)
        self.commandTableView.setMaximumSize(QtCore.QSize(16777215, 150))
        self.commandTableView.setShowGrid(False)
        self.commandTableView.setObjectName(_fromUtf8("commandTableView"))
        self.commandTableView.horizontalHeader().setVisible(False)
        self.commandTableView.horizontalHeader().setDefaultSectionSize(100)
        self.commandTableView.verticalHeader().setVisible(False)
        self.commandTableView.verticalHeader().setDefaultSectionSize(17)
        self.verticalLayout_6.addWidget(self.commandTableView)
        self.verticalLayout_7.addWidget(self.groupBox)
        self.widget_3 = QtGui.QWidget(self.widget_2)
        self.widget_3.setObjectName(_fromUtf8("widget_3"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget_3)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.runButton = QtGui.QPushButton(self.widget_3)
        self.runButton.setObjectName(_fromUtf8("runButton"))
        self.horizontalLayout.addWidget(self.runButton)
        self.abortButton = QtGui.QPushButton(self.widget_3)
        self.abortButton.setObjectName(_fromUtf8("abortButton"))
        self.horizontalLayout.addWidget(self.abortButton)
        self.validateSequenceButton = QtGui.QPushButton(self.widget_3)
        self.validateSequenceButton.setObjectName(_fromUtf8("validateSequenceButton"))
        self.horizontalLayout.addWidget(self.validateSequenceButton)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout_7.addWidget(self.widget_3)
        self.mainGridLayout.addWidget(self.widget_2, 1, 1, 1, 3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 590, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuXML = QtGui.QMenu(self.menubar)
        self.menuXML.setObjectName(_fromUtf8("menuXML"))
        self.menuNotifications = QtGui.QMenu(self.menubar)
        self.menuNotifications.setObjectName(_fromUtf8("menuNotifications"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew_Sequence = QtGui.QAction(MainWindow)
        self.actionNew_Sequence.setObjectName(_fromUtf8("actionNew_Sequence"))
        self.actionQuit = QtGui.QAction(MainWindow)
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.actionGenerate = QtGui.QAction(MainWindow)
        self.actionGenerate.setObjectName(_fromUtf8("actionGenerate"))
        self.actionGenerateXML = QtGui.QAction(MainWindow)
        self.actionGenerateXML.setObjectName(_fromUtf8("actionGenerateXML"))
        self.actionSendTestEmail = QtGui.QAction(MainWindow)
        self.actionSendTestEmail.setObjectName(_fromUtf8("actionSendTestEmail"))
        self.menuFile.addAction(self.actionNew_Sequence)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menuXML.addAction(self.actionGenerateXML)
        self.menuNotifications.addAction(self.actionSendTestEmail)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuXML.menuAction())
        self.menubar.addAction(self.menuNotifications.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Dave", None))
        self.sequenceGroupBox.setTitle(_translate("MainWindow", "Sequence File", None))
        self.sequenceLabel.setText(_translate("MainWindow", "NA", None))
        self.notificationGroupBox.setTitle(_translate("MainWindow", "Notifications", None))
        self.estimatesGroupBox.setTitle(_translate("MainWindow", "Estimates", None))
        self.spaceLabel.setText(_translate("MainWindow", "TextLabel", None))
        self.timeLabel.setText(_translate("MainWindow", "TextLabel", None))
        self.remainingLabel.setText(_translate("MainWindow", "TextLabel", None))
        self.completionLabel.setText(_translate("MainWindow", "TextLabel", None))
        self.statusMsgCheckBox.setText(_translate("MainWindow", "e-mail status messages", None))
        self.fromPasswordLabel.setText(_translate("MainWindow", "From password:", None))
        self.errorMsgCheckBox.setText(_translate("MainWindow", "e-mail error messages", None))
        self.frequencyLabel.setText(_translate("MainWindow", "Frequency:", None))
        self.toAddressLabel.setText(_translate("MainWindow", "To address:", None))
        self.smtpServerLabel.setText(_translate("MainWindow", "SMTP server:", None))
        self.fromAddressLabel.setText(_translate("MainWindow", "From address:", None))
        self.GroupBox.setTitle(_translate("MainWindow", "Sequence Progress", None))
        self.warningsGroupBox.setTitle(_translate("MainWindow", "Warnings", None))
        self.numWarningsToPauseLabel.setText(_translate("MainWindow", "Number of Warnings  to Pause", None))
        self.clearWarningsPushButton.setText(_translate("MainWindow", "Clear Warnings", None))
        self.commandGroupBox.setTitle(_translate("MainWindow", "Command Sequence", None))
        self.groupBox.setTitle(_translate("MainWindow", "Command Details", None))
        self.runButton.setText(_translate("MainWindow", "Run", None))
        self.abortButton.setText(_translate("MainWindow", "Abort", None))
        self.validateSequenceButton.setText(_translate("MainWindow", "Validate", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuXML.setTitle(_translate("MainWindow", "XML", None))
        self.menuNotifications.setTitle(_translate("MainWindow", "Notifications", None))
        self.actionNew_Sequence.setText(_translate("MainWindow", "Load Sequence", None))
        self.actionQuit.setText(_translate("MainWindow", "Quit", None))
        self.actionGenerate.setText(_translate("MainWindow", "Generate (Version 1.0)", None))
        self.actionGenerateXML.setText(_translate("MainWindow", "Generate XML", None))
        self.actionSendTestEmail.setText(_translate("MainWindow", "Send Test Email", None))

from daveWarnings import DaveWarningsViewer
from sequenceViewer import DaveCommandTreeViewer
