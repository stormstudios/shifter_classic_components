import mgear.core.pyqt as gqt
QtGui, QtCore, QtWidgets, wrapInstance = gqt.qt_import()


class Ui_Form(object):

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(294, 354)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox_3 = QtWidgets.QGroupBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.groupBox_3)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.masterLocal_lineEdit = QtWidgets.QLineEdit(self.groupBox_3)
        self.masterLocal_lineEdit.setObjectName("masterLocal_lineEdit")
        self.horizontalLayout_2.addWidget(self.masterLocal_lineEdit)
        self.masterLocal_pushButton = QtWidgets.QPushButton(self.groupBox_3)
        self.masterLocal_pushButton.setObjectName("masterLocal_pushButton")
        self.horizontalLayout_2.addWidget(self.masterLocal_pushButton)
        self.gridLayout_4.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.groupBox_3)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.masterGlobal_lineEdit = QtWidgets.QLineEdit(self.groupBox_3)
        self.masterGlobal_lineEdit.setObjectName("masterGlobal_lineEdit")
        self.horizontalLayout_4.addWidget(self.masterGlobal_lineEdit)
        self.masterGlobal_pushButton = QtWidgets.QPushButton(self.groupBox_3)
        self.masterGlobal_pushButton.setObjectName("masterGlobal_pushButton")
        self.horizontalLayout_4.addWidget(self.masterGlobal_pushButton)
        self.gridLayout_4.addLayout(self.horizontalLayout_4, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox_3, 1, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 2, 0, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.neutralPose_checkBox = QtWidgets.QCheckBox(self.groupBox)
        self.neutralPose_checkBox.setText("Neutral Pose")
        self.neutralPose_checkBox.setObjectName("neutralPose_checkBox")
        self.verticalLayout.addWidget(self.neutralPose_checkBox)
        self.overrideNegate_checkBox = QtWidgets.QCheckBox(self.groupBox)
        self.overrideNegate_checkBox.setText("Override Negate Axis Direction For \"R\" Side")
        self.overrideNegate_checkBox.setObjectName("overrideNegate_checkBox")
        self.verticalLayout.addWidget(self.overrideNegate_checkBox)
        self.addJoints_checkBox = QtWidgets.QCheckBox(self.groupBox)
        self.addJoints_checkBox.setText("Add Joints")
        self.addJoints_checkBox.setChecked(True)
        self.addJoints_checkBox.setObjectName("addJoints_checkBox")
        self.verticalLayout.addWidget(self.addJoints_checkBox)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(gqt.fakeTranslate("Form", "Form", None, -1))
        self.groupBox_3.setTitle(gqt.fakeTranslate("Form", "Chain Master", None, -1))
        self.label.setText(gqt.fakeTranslate("Form", "Local:", None, -1))
        self.masterLocal_pushButton.setText(gqt.fakeTranslate("Form", "<<", None, -1))
        self.label_3.setText(gqt.fakeTranslate("Form", "Global:", None, -1))
        self.masterGlobal_pushButton.setText(gqt.fakeTranslate("Form", "<<", None, -1))
