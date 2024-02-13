import sqlite3 as sq
import logging

Format = "%(asctime)s %(levelname)s %(message)s"
logging.basicConfig(
    filename="./log/DatabaseLog.log", level=logging.DEBUG, format=Format
)


class Database:
    def __init__(self):
        """Initialize a new instance of the Database class.

        This method creates a new instance of the Database class and automatically calls the createDb method
        to set up the necessary database for the ToDo list application.
        """
        self.createDb()

    def createDb(self):
        """Create the database and necessary table for the ToDo list application.

        This method establishes a connection to the SQLite database located at "./database/TodoData.db" and creates
        a 'tasks' table with columns for 'todo' (task description), 'deadline' (task deadline), 'priority'
        (task priority), and 'status' (task completion status).

        If the table already exists, it logs a warning but does not raise an error.
        """

        self.connection = sq.connect("./database/TodoData.db")
        try:
            with self.connection:
                self.cursor = self.connection.cursor()
                self.cursor.execute(
                    """
                        CREATE TABLE tasks (
                            todo text,
                            deadline text,
                            priority text,
                            status int
                            )
                        """
                )
        except sq.Error as e:
            logging.warning(f"Cant Create Table:: {e}")

    def loadData(self) -> list:
        """Fetch the user's tasks and associated details from the database.

        Returns:
            list: A list containing tuples, where each tuple represents a task with its unique rowid,
            description, deadline, priority, and status.
        """
        try:
            self.cursor.execute("SELECT rowid, * FROM tasks")
            return self.cursor.fetchall()
        except sq.Error as e:
            logging.error(f"Unable to fetch data from DataBase:\t{e}")
            return []

    def taskDetail_name(self, task) -> tuple:
        """Look up a task in the database and retrieve its details.

        Args:
            task (str): The task to look up.

        Returns:
            tuple: A tuple containing the details of the specified task (description, deadline, priority, and status).
                   If the task is not found, returns None.
        """

        try:
            self.cursor.execute("SELECT * FROM tasks WHERE todo = ?", (str(task),))
            return self.cursor.fetchone()
        except sq.Error as e:
            logging.error(f"Unable to load the details for: {task} \t\t{e}")
            return None

    def createTask(self, newtodo, newdeadline, newpriority, newstatus) -> None:
        """Create a new task and save it in the database with the provided details.

        Args:
            newtodo (str): The description of the new task.
            newdeadline (str): The deadline for the new task.
            newpriority (str): The priority level of the new task.
            newstatus (int): The completion status of the new task (0 for incomplete, 1 for complete).

        Note:
            - The newtodo, newdeadline, and newpriority parameters should not be empty for a task to be created.
            - If the task creation is successful, the changes are committed to the database.

        If incomplete data is provided, a warning is logged, and no task is created.
        """

        if newtodo and newdeadline and newpriority:
            try:
                self.cursor.execute(
                    """INSERT INTO tasks VALUES (?,?,?,?)""",
                    (newtodo.title(), newdeadline, newpriority, newstatus),
                )
                self.connection.commit()
            except sq.Error as e:
                logging.error(f"Unable to create task: {e}")
        else:
            logging.warning("Incomplete data was provided")

    def updateTask(self, previous_name, newtodo, deadline, priority, status) -> None:
        """Update the details of a task in the database.

        Args:
            previous_name (str): The name of the task to be updated.
            newtodo (str): The new description for the task.
            deadline (str): The new deadline for the task.
            priority (str): The new priority level for the task.
            status (int): The new completion status for the task (0 for incomplete, 1 for complete).

        Note:
            - If a task with the provided 'previous_name' is found, its details are updated with the new values.
            - The 'newtodo', 'deadline', and 'priority' parameters should not be empty for an update to occur.
            - If the update is successful, the changes are committed to the database.

        If no task is found with the specified name, an error is logged.
        """

        if self.taskDetail_name(previous_name):
            try:
                self.cursor.execute(
                    "UPDATE tasks SET todo = ?, deadline = ?, priority = ?, status = ? WHERE todo = ?",
                    (newtodo.title(), deadline, priority, status, previous_name),
                )
                self.connection.commit()
            except sq.Error as e:
                logging.error(f"Unable to update task \t\t{e}")
        else:
            logging.error(f"No task with the name {previous_name}")

    def deleteTask(self, task) -> None:
        """Delete an entry of a task from the database.

        Args:
            task (str): The title of the task to delete.

        Note:
            - If a task with the provided title is found, it is deleted from the database.
            - If the deletion is successful, the changes are committed to the database.

        If an error occurs during deletion, an error is logged.
        """
        try:
            self.cursor.execute("DELETE from tasks WHERE todo = ?", (task,))
            self.connection.commit()
        except sq.Error as e:
            logging.error(f"Unable to delete task:\t\t{e}")

    def del_completed(self) -> None:
        """Delete all completed tasks from the database.

        Note:
            - Deletes tasks with a status of 1 (completed) from the database.
            - If the deletion is successful, the changes are committed to the database.

        If an error occurs during deletion, an error is logged.
        """

        try:
            self.cursor.execute("DELETE FROM tasks WHERE status = 1")
            self.connection.commit()
        except sq.Error as e:
            logging.error(f"Unable to delete all completed tasks {e}")
