from PySide6.QtWidgets import QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget

from services.api_service import APIService


class LoginView(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window

        layout = QVBoxLayout()

        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("שם משתמש")

        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("סיסמה")
        self.password_input.setEchoMode(QLineEdit.Password)

        self.login_button = QPushButton("התחבר")
        self.login_button.clicked.connect(self.handle_login)

        layout.addWidget(QLabel("התחברות למערכת"))
        layout.addWidget(self.username_input)
        layout.addWidget(self.password_input)
        layout.addWidget(self.login_button)

        self.setLayout(layout)

    def handle_login(self):
        username = self.username_input.text()
        password = self.password_input.text()
        response = APIService.login(username, password)
        if response.get("success"):
            self.main_window.navigate_to_dashboard()
        else:
            from PySide6.QtWidgets import QMessageBox

            QMessageBox.warning(self, "שגיאה", "שם משתמש או סיסמה שגויים")
