from PyQt6 import QtCore, QtWidgets, QtGui


class Edit_Task_Ui(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(524, 186)
        Form.setMinimumSize(QtCore.QSize(524, 186))
        Form.setMaximumSize(QtCore.QSize(524, 186))

        Form.setStyleSheet("background-color: rgb(255, 255, 255);")
        Form.setWindowIcon(QtGui.QIcon("./mainIcon.png"))
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox = QtWidgets.QGroupBox(parent=Form)
        self.groupBox.setStyleSheet('font: 75 10pt "Arial";')
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_3.setStyleSheet('font: 75 12pt "Arial";')
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.task_name = QtWidgets.QLineEdit(parent=self.groupBox)
        self.task_name.setStyleSheet('font: 75 12pt "Georgia";')
        self.task_name.setText("")
        self.task_name.setObjectName("task_name")
        self.horizontalLayout.addWidget(self.task_name)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem = QtWidgets.QSpacerItem(
            1,
            20,
            QtWidgets.QSizePolicy.Policy.Minimum,
            QtWidgets.QSizePolicy.Policy.Preferred,
        )
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_2.setStyleSheet('font: 75 12pt "Arial";')
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        spacerItem1 = QtWidgets.QSpacerItem(
            20,
            20,
            QtWidgets.QSizePolicy.Policy.Preferred,
            QtWidgets.QSizePolicy.Policy.Minimum,
        )
        self.horizontalLayout_2.addItem(spacerItem1)
        self.deadline = QtWidgets.QDateEdit(parent=self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.deadline.sizePolicy().hasHeightForWidth())
        self.deadline.setSizePolicy(sizePolicy)
        self.deadline.setStyleSheet('font: 70 10pt "Arial";')
        self.deadline.setDateTime(
            QtCore.QDateTime(QtCore.QDate(2024, 1, 1), QtCore.QTime(1, 0, 0))
        )
        self.deadline.setObjectName("deadline")
        self.horizontalLayout_2.addWidget(self.deadline)
        spacerItem2 = QtWidgets.QSpacerItem(
            30,
            20,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum,
        )
        self.horizontalLayout_2.addItem(spacerItem2)
        self.label_4 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_4.setStyleSheet('font: 75 12pt "Arial";')
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        spacerItem3 = QtWidgets.QSpacerItem(
            20,
            20,
            QtWidgets.QSizePolicy.Policy.Preferred,
            QtWidgets.QSizePolicy.Policy.Maximum,
        )
        self.horizontalLayout_2.addItem(spacerItem3)
        self.priority = QtWidgets.QComboBox(parent=self.groupBox)
        self.priority.setFrame(False)
        self.priority.setObjectName("priority")
        self.priority.addItem("")
        self.priority.addItem("")
        self.priority.addItem("")
        self.horizontalLayout_2.addWidget(self.priority)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem4 = QtWidgets.QSpacerItem(
            1,
            20,
            QtWidgets.QSizePolicy.Policy.Minimum,
            QtWidgets.QSizePolicy.Policy.Preferred,
        )
        self.verticalLayout.addItem(spacerItem4)
        self.createTask = QtWidgets.QPushButton(parent=self.groupBox)
        self.createTask.setStyleSheet(
            "color: rgb(255, 255, 255);\n"
            'font: 75 12pt "Georgia";\n'
            "background-color: rgb(65, 205, 82);"
        )
        self.createTask.setObjectName("createTask")
        self.verticalLayout.addWidget(self.createTask)

        self.verticalLayout_2.addWidget(self.groupBox)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Edit Task"))
        self.groupBox.setTitle(_translate("Form", "Edit Task"))
        self.label_3.setText(_translate("Form", "Task Name:"))
        self.task_name.setPlaceholderText(_translate("Form", "New Todo"))
        self.label_2.setText(_translate("Form", "Deadline:"))
        self.label_4.setText(_translate("Form", "Priority:"))
        self.priority.setItemText(0, _translate("Form", "High Priority"))
        self.priority.setItemText(1, _translate("Form", "Medium Priority"))
        self.priority.setItemText(2, _translate("Form", "Low Priority"))
        self.createTask.setText(_translate("Form", "Update Task"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Edit_Task_Ui()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
