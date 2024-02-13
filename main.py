from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QWidget, QListWidgetItem, QApplication
from PyQt6.QtCore import Qt
import logging
from database_manager import Database

from interface.editTaskUi import Edit_Task_Ui

database = Database()

Format = "%(asctime)s %(levelname)s %(message)s"
logging.basicConfig(filename="log/Ui.log", level=logging.DEBUG, format=Format)


class Main_Ui(object):
    """The main user interface class for the ToDo list application.

    This class is responsible for creating and managing the main graphical user interface
    of the ToDo list application.
    """

    def setupUi(self, Form):
        """Set up the main user interface components and layout.

        Args:
            Form: The main window form provided by QtWidget.
        """

        Form.setObjectName("Form")
        Form.resize(582, 500)
        Form.setMinimumSize(QtCore.QSize(582, 500))
        Form.setMaximumSize(QtCore.QSize(582, 500))
        Form.setStyleSheet(
            "QWidget{\n"
            "    background-color: rgb(255, 255, 255);\n"
            "}\n"
            "QPushButton{\n"
            "color: rgb(255, 255, 255);\n"
            "background-color: rgb(65, 205, 82);\n"
            'font: 75 12pt "Arial";\n'
            "}"
        )
        self.groupBox_2 = QtWidgets.QGroupBox(parent=Form)
        self.groupBox_2.setGeometry(QtCore.QRect(30, 440, 521, 48))
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.line_3 = QtWidgets.QFrame(parent=self.groupBox_2)
        self.line_3.setGeometry(QtCore.QRect(290, 10, 3, 28))
        self.line_3.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.line_3.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_3.setObjectName("line_3")
        Form.setWindowIcon(QtGui.QIcon("mainIcon.png"))

        """ACTION BUTTIONS"""

        # EDIT BTN
        self.edit_task_btn = QtWidgets.QPushButton(parent=self.groupBox_2)
        self.edit_task_btn.setGeometry(QtCore.QRect(310, 10, 90, 26))
        self.edit_task_btn.setObjectName("edit_task_btn")
        self.edit_task_btn.clicked.connect(self.edit_task)

        # DETAIL BTN
        self.detail_btn = QtWidgets.QPushButton(parent=self.groupBox_2)
        self.detail_btn.setGeometry(QtCore.QRect(10, 11, 101, 26))
        self.detail_btn.setObjectName("detail_btn")
        self.detail_btn.clicked.connect(self.display_details)

        # DELETE COMPLETED TASK BTN
        self.del_completed_btn = QtWidgets.QPushButton(parent=self.groupBox_2)
        self.del_completed_btn.setGeometry(QtCore.QRect(130, 11, 141, 26))
        self.del_completed_btn.setObjectName("del_completed_btn")
        self.del_completed_btn.clicked.connect(self.del_completed)

        # DELETE TASK BTN
        self.del_task_btn = QtWidgets.QPushButton(parent=self.groupBox_2)
        self.del_task_btn.setGeometry(QtCore.QRect(420, 10, 90, 26))
        self.del_task_btn.setObjectName("del_task_btn")
        self.del_task_btn.clicked.connect(self.delete_selected)

        self.groupBox = QtWidgets.QGroupBox(parent=Form)
        self.groupBox.setGeometry(QtCore.QRect(30, 10, 521, 122))
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

        # TASK NAME BUTTON
        self.task_name = QtWidgets.QLineEdit(parent=self.groupBox)
        self.task_name.setStyleSheet('font: 75 12pt "Georgia";')
        self.task_name.setObjectName("task_name")

        self.horizontalLayout.addWidget(self.task_name)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem = QtWidgets.QSpacerItem(
            20,
            40,
            QtWidgets.QSizePolicy.Policy.Minimum,
            QtWidgets.QSizePolicy.Policy.Expanding,
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

        # The Task Deadline
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
            QtWidgets.QSizePolicy.Policy.Minimum,
        )
        self.horizontalLayout_2.addItem(spacerItem3)

        # The task priority combobox
        self.priority = QtWidgets.QComboBox(parent=self.groupBox)
        self.priority.setFrame(False)
        self.priority.setObjectName("priority")
        self.priority.addItem("")
        self.priority.addItem("")
        self.priority.addItem("")

        self.horizontalLayout_2.addWidget(self.priority)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem4 = QtWidgets.QSpacerItem(
            20,
            40,
            QtWidgets.QSizePolicy.Policy.Minimum,
            QtWidgets.QSizePolicy.Policy.Expanding,
        )
        self.verticalLayout.addItem(spacerItem4)

        # The button to create task
        self.create_task_btn = QtWidgets.QPushButton(parent=self.groupBox)
        self.create_task_btn.setStyleSheet(
            "color: rgb(255, 255, 255);\n"
            'font: 75 12pt "Georgia";\n'
            "background-color: rgb(65, 205, 82);"
        )
        self.create_task_btn.setObjectName("create_task_btn")
        self.create_task_btn.clicked.connect(self.create_task)

        self.verticalLayout.addWidget(self.create_task_btn)

        # The list widget to display the tasks.
        self.listWidget = QtWidgets.QListWidget(parent=Form)
        self.listWidget.setGeometry(QtCore.QRect(30, 150, 521, 271))
        self.listWidget.setObjectName("listWidget")
        self.listWidget.addItem(QListWidgetItem(""))
        self.listWidget.itemChanged.connect(self.update_item_status)

        self.label = QtWidgets.QLabel(parent=Form)
        self.label.setGeometry(QtCore.QRect(244, 138, 90, 16))
        self.label.setStyleSheet(
            'font: 75 12pt "Arial";\n' "background-color: rgb(255, 255, 255);"
        )
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")

        # Things to do on app startup
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.update_task_display()
        self.edit_task_ui = Edit_Task_Ui()
        self.form = QWidget()
        self.edit_task_ui.setupUi(self.form)

    def create_task(self):
        """Get input from the interface, then create a data entry in the database.

        Retrieves task details from the user interface, including task title, deadline, and priority.
        Checks if the task title is empty and displays an error if it is.
        If the task title is not empty, it checks if the task already exists in the database.
        If the task doesn't exist, a new task is created in the database with the provided details.
        Resets the input fields and updates the task display on the user interface.

        Note:
            - The task title, deadline, and priority are retrieved from the corresponding interface elements.
            - An error is displayed if the task title is empty.
            - If the task already exists in the database, an error is displayed.
            - If the task creation is successful, the input fields are reset, and the task display is updated.
        """

        todo = self.task_name.text().strip()
        todo_deadline = self.deadline.text()
        todo_priority = self.priority.currentText()

        # check if task title is empty
        if todo == "":
            self.create_task_error()
        else:
            try:
                existing_task = database.taskDetail_name(todo)
                # check if the task exist
                if existing_task == None:
                    database.createTask(todo.title(), todo_deadline, todo_priority, 0)
                    self.reset_input()
                    self.update_task_display()
                else:
                    self.task_exist_error()
            except:
                logging.log("Unable to create task")

    def update_task_display(self):
        """Load the data from the database and create a checkbox for each task.

        Retrieves the task data from the database using the 'loadData' method.
        Clears all tasks from the QListWidget to avoid duplicate display.
        Iterates through the retrieved tasks and creates a QListWidgetItem for each task.
        Sets the item's flags to include Qt.ItemFlag.ItemIsUserCheckable, making it checkable.
        Sets the check state of the item based on the completion status of the task.
        """

        tasks = database.loadData()

        # Remove all task from the QListWidget to avoid duplicate display.
        self.listWidget.clear()

        for task in tasks:
            todo = task[1]
            # Create a QListWidgetItem.
            item = QListWidgetItem(todo, self.listWidget)
            # Set its flags to include Qt.ItemFlag.ItemIsUserCheckable. so that it can be checkable.
            item.setFlags(item.flags() | Qt.ItemFlag.ItemIsUserCheckable)
            # Set its checkState to Qt.CheckState.Unchecked
            checkState = [Qt.CheckState.Unchecked, Qt.CheckState.Checked]
            item.setCheckState(checkState[task[-1]])
            # Use item.checkState() and item.setCheckState() to access and modify the check state of items.

    def create_task_error(self):
        """Display an error message for task creation with empty title.

        Shows a QMessageBox with an error message indicating that a task title should be entered
        before clicking on 'Add New Task'.
        """
        task_error_dialog = QtWidgets.QMessageBox()
        task_error_dialog.setText(
            "Please enter a task before clicking on 'Add New Task'"
        )
        task_error_dialog.setFont(QtGui.QFont("Georgia", 12))
        task_error_dialog.setWindowTitle("Create Task Error")
        task_error_dialog.setWindowIcon(QtGui.QIcon("mainIcon.png"))
        task_error_dialog.setIcon(QtWidgets.QMessageBox.Icon.Critical)
        task_error_dialog.exec()

    def task_exist_error(self):
        """Display a warning message for a task that already exists.

        Shows a QMessageBox with a warning message indicating that another task with similar details already exists.
        """
        task_error = QtWidgets.QMessageBox()
        task_error.setText("Another Task with similar detail exist.")
        task_error.setFont(QtGui.QFont("Georgia", 12))
        task_error.setWindowTitle("Duplicate Task Error")
        task_error.setWindowIcon(QtGui.QIcon("mainIcon.png"))
        task_error.setIcon(QtWidgets.QMessageBox.Icon.Warning)
        task_error.exec()

    def update_item_status(self, item):
        """Update the completion status of a task based on its check state.

        Args:
            item: The QListWidgetItem whose check state is being updated.
        """
        if item.checkState() == Qt.CheckState.Checked:
            todo = database.taskDetail_name(item.text())
            database.updateTask(item.text(), todo[0], todo[1], todo[2], 1)
        else:
            todo = database.taskDetail_name(item.text())
            database.updateTask(item.text(), todo[0], todo[1], todo[2], 0)

    def delete_selected(self):
        """Delete the selected task from the ToDo list.

        Retrieves the currently selected item from the QListWidget.
        If no item is selected, displays a simple dialog prompting the user to select a task.
        If an item is selected, displays a confirmation dialog with the task details.
        If the user confirms deletion, deletes the task from the database and updates the task display.
        """
        item = self.listWidget.currentItem()
        if item == None:
            msg = (
                "Which task would you like to delete?\nPlease select it from the list."
            )
            self.simple_dialog(msg, "Delete Task")
        else:
            msg = f"Are you sure you'll like to delete the below task?\nTask Name: {item.text()}"
            response = self.del_task(msg)
            if response:
                database.deleteTask(item.text())
                self.update_task_display()

    def reset_input(self):
        """Reset the input fields in the task creation interface.

        Clears the text in the task name input field.
        Resets the deadline input field to a default date and time.
        Sets the priority dropdown to the default value ('High Priority').
        """
        self.task_name.setText("")
        self.deadline.setDateTime(
            QtCore.QDateTime(QtCore.QDate(2024, 1, 1), QtCore.QTime(1, 0, 0))
        )
        self.priority.setCurrentText("High Priority")

    def del_completed(self):
        """Delete all completed tasks from the ToDo list.

        Displays a confirmation dialog asking if the user wants to clear all completed tasks.
        If the user confirms, deletes all completed tasks from the database and updates the task display.
        """
        response = self.del_task(
            message="Are you sure you want to clear all completed tasks?\nThis action cannot be undone."
        )
        if response == 1:
            database.del_completed()
        self.update_task_display()

    def del_task(self, message):
        """Display a confirmation dialog for task deletion.

        Args:
            message (str): The message to be displayed in the confirmation dialog.

        Returns:
            int: 1 if the user clicks 'Yes', None otherwise.
        """
        del_task = QtWidgets.QMessageBox()
        del_task.setText(message)
        del_task.setFont(QtGui.QFont("Georgia", 12))
        del_task.setWindowTitle("Delete Task Confirmation")
        del_task.setWindowIcon(QtGui.QIcon("mainIcon.png"))
        del_task.setIcon(QtWidgets.QMessageBox.Icon.Warning)
        del_task.setStandardButtons(
            QtWidgets.QMessageBox.StandardButton.Yes
            | QtWidgets.QMessageBox.StandardButton.No
        )
        clicked_btn = del_task.exec()

        if clicked_btn == QtWidgets.QMessageBox.StandardButton.Yes:
            return 1
        else:
            return None

    def edit_task(self):
        """Edit the details of the selected task.

        Retrieves the currently selected item from the QListWidget.
        If no item is selected, displays a simple dialog prompting the user to select a task.
        If an item is selected, retrieves the details of the task from the database.
        Sets the details in the Edit Task window's input fields and displays the window.
        Connects the 'Save Changes' button to the 'save_changes' method.
        """
        item = self.listWidget.currentItem()
        if item == None:
            msg = "Which task would you like to edit?\nPlease select it from the list."
            self.simple_dialog(msg, "Edit Task")
        else:
            todo = database.taskDetail_name(item.text())
            self.previous_text = todo[0]

            self.edit_task_ui.task_name.setText(self.previous_text)
            month, day, year = todo[1].split("/")
            self.edit_task_ui.deadline.setDate(
                QtCore.QDate(int(year), int(month), int(day))
            )
            self.edit_task_ui.priority.setCurrentText(todo[2])
            self.form.show()
            self.edit_task_ui.createTask.clicked.connect(self.save_changes)

    def save_changes(self):
        """Save the changes made to the details of a task.

        Retrieves the original details of the task from the database.
        Gets the new details from the Edit Task window's input fields.
        Checks if the task title is empty and displays an error if it is.
        Displays a confirmation dialog to confirm saving the changes.
        If the user confirms, updates the task in the database, updates the task display,
        and resets the input fields. Hides the Edit Task window.
        """
        todo = database.taskDetail_name(self.previous_text)
        todo_title = self.edit_task_ui.task_name.text().strip()
        todo_deadline = self.edit_task_ui.deadline.text()
        todo_priority = self.edit_task_ui.priority.currentText()

        # check if task title is empty
        if todo_title == "":
            self.create_task_error()
        else:
            msg = f"Are you sure you'll like to save the changes made to this task."
            response = self.del_task(msg)
            if response:
                database.updateTask(
                    self.previous_text,
                    todo_title,
                    todo_deadline,
                    todo_priority,
                    todo[-1],
                )
                self.update_task_display()
                self.edit_task_ui.task_name.setText("")
                self.edit_task_ui.deadline.setDate(QtCore.QDate(2024, 1, 1))
                self.edit_task_ui.priority.setCurrentText("High Priority")
                self.form.hide()

    def simple_dialog(self, message, title):
        """Display a simple information dialog.

        Args:
            message (str): The message to be displayed in the dialog.
            title (str): The title of the dialog.
        """
        task_detail_dialog = QtWidgets.QMessageBox()
        task_detail_dialog.setText(message)
        task_detail_dialog.setFont(QtGui.QFont("Georgia", 12))
        task_detail_dialog.setWindowTitle(title)
        task_detail_dialog.setWindowIcon(QtGui.QIcon("mainIcon.png"))
        task_detail_dialog.setIcon(QtWidgets.QMessageBox.Icon.Information)
        task_detail_dialog.exec()

    def display_details(self):
        """Display details of the selected task.

        Retrieves the currently selected item from the QListWidget.
        If no item is selected, displays a message indicating to select a task for details.
        If an item is selected, retrieves the details of the task from the database.
        Formats the details and displays them in an information dialog.
        """
        item = self.listWidget.currentItem()
        if item == None:
            msg = "Select the task you want to view details for.\nYou'll see informations such as task title, deadline, priority and completion status."
        else:
            task = database.taskDetail_name(item.text())
            status = ["Uncompleted", "Completed"][task[-1]]
            msg = f"Task Name: {task[0]}\nDeadline: {task[1]}\nPriority: {task[2]}\nCompletion Status: {status}"
        self.simple_dialog(msg, "Task detail")

    def retranslateUi(self, Form):
        """Translate and set the text for various UI elements.

        Args:
            Form: The main window form provided by QtWidgets.
        """
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "ToDo-List App"))
        self.edit_task_btn.setText(_translate("Form", "Edit"))
        self.detail_btn.setText(_translate("Form", "Detail"))
        self.del_completed_btn.setText(_translate("Form", "Clear Completed"))
        self.del_task_btn.setText(_translate("Form", "Delete Task"))
        self.groupBox.setTitle(_translate("Form", "To-Do Input"))
        self.label_3.setText(_translate("Form", "Task Name:"))
        self.task_name.setPlaceholderText(_translate("Form", "New Todo"))
        self.label_2.setText(_translate("Form", "Deadline:"))
        self.label_4.setText(_translate("Form", "Priority:"))
        self.priority.setItemText(0, _translate("Form", "High Priority"))
        self.priority.setItemText(1, _translate("Form", "Medium Priority"))
        self.priority.setItemText(2, _translate("Form", "Low Priority"))
        self.create_task_btn.setText(_translate("Form", "Add New Task"))
        self.label.setText(_translate("Form", "ToDo List"))


if __name__ == "__main__":
    """Entry point for the ToDo-List application.

    Initializes the Qt application and the main window.
    Creates an instance of the Main_Ui class and sets up the user interface.
    Displays the main window and starts the application event loop.
    """
    import sys

    app = QApplication(sys.argv)
    Form = QWidget()
    ui = Main_Ui()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
