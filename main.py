import sys

from PySide6.QtWidgets import QApplication

from views.loginWindow import LoginWindow


def main():
    app = QApplication(sys.argv)

    # פותחים את חלון ההתחברות
    login_window = LoginWindow()
    login_window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()

if __name__ == "__main__":
    main()
