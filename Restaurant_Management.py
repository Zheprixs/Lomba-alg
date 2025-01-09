from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QMessageBox, QLineEdit, QComboBox, QStackedWidget
import datetime

# Get the current date and format it
now = datetime.datetime.now()
formatted_date = now.strftime("%A, %B %d, %Y")

# Initialize the application and main window
app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('restaurant')
main_win.resize(200, 100)

# Create a stacked widget to switch between layouts
stacked_widget = QStackedWidget()
layout1_widget = QWidget()
layout2_widget = QWidget()

# Variables to store user login details and command
stored_user = ''
stored_pass = ''
input_user = ''
input_password = ''
command_save = ''

# Create widgets for the login page
login_admin = QLabel('Login to your account')
input_login_admin = QLineEdit()
password_admin = QLabel('Password:')
password = QLineEdit()
command_title = QLabel('Choose what you want to do!!!')
command = QComboBox()
welcome = QLabel('Welcome Admin!')
button1 = QPushButton('login')
button2 = QPushButton('go')

# Create layouts for the login page
layoutv = QVBoxLayout()
layoutv.addWidget(login_admin, alignment=Qt.AlignCenter)
layoutv.addWidget(input_login_admin, alignment=Qt.AlignCenter)
layoutv.addWidget(password_admin, alignment=Qt.AlignCenter)
layoutv.addWidget(password, alignment=Qt.AlignCenter)
layoutv.addWidget(button1, alignment=Qt.AlignCenter)
layout1_widget.setLayout(layoutv)

# Create layouts for the main page
layoutv2 = QVBoxLayout()
layoutv2.addWidget(welcome, alignment=Qt.AlignCenter)
layoutv2.addWidget(command_title, alignment=Qt.AlignCenter)
layoutv2.addWidget(command, alignment=Qt.AlignCenter)
layoutv2.addWidget(button2, alignment=Qt.AlignCenter)
layout2_widget.setLayout(layoutv2)

# Add command options to the combo box
command_list = ['History', 'Total Earnings', 'Start']
command.addItems(command_list)

# Add layouts to the stacked widget
stacked_widget.addWidget(layout1_widget)
stacked_widget.addWidget(layout2_widget)

# Set the main layout of the main window
main_layout = QVBoxLayout()
main_layout.addWidget(stacked_widget)
main_win.setLayout(main_layout)

# Function to handle login
def login():
    global stored_user, stored_pass, input_user, input_password, command_save
    # Set stored login details
    stored_user = 'Admin'
    stored_pass = 'admin1235'
    # Get input login details
    input_user = input_login_admin.text()
    input_password = password.text()

    # Check if input login details match stored login details
    if input_user == stored_user and input_password == stored_pass:
        # If they match, switch to the main page
        stacked_widget.setCurrentIndex(1)
    else:
        # If they don't match, show an error message
        QMessageBox.critical(main_win, 'error', 'Your input does not match!')

# Function to handle main page commands
def main_page():
    global stored_user, stored_pass, input_user, input_password, command_save
    # Get the selected command
    command_save = command.currentText()

    # Read history and profit files
    with open('history.txt', 'r') as file:
        history_save = file.read()
    with open('profit.txt', 'r') as file:
        profit_save = file.read()

    # Perform actions based on the selected command
    if command_save == 'History':
        QMessageBox.information(main_win, 'Successful', 'Export success!!! \nPlease check history.txt')
    elif command_save == 'Total Earnings':
        QMessageBox.information(main_win, 'Profit', 'Your Total Earnings Today: ' + profit_save)
    elif command_save == 'Start':
        # Write the current date to the history file and clear the profit file
        with open('history.txt', 'a') as file:
            file.write('\n' + '\n' + formatted_date + '\n')
        QMessageBox.information(main_win, 'success', 'Starting the program!!!')
        with open('profit.txt', 'w') as file:
            file.write('0')
        QMessageBox.information(main_win, 'success', 'Success')

# Connect buttons to functions
button1.clicked.connect(login)
button2.clicked.connect(main_page)

# Show the main window and run the application
main_win.show()
app.exec_()
