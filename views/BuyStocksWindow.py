# ╔═════════════════════════════════╗
# ║         📁 Python Project 📁
# ║
# ║  ✨ Team Members ✨
# ║
# ║  🧑‍💻 Elyasaf Cohen 311557227 🧑‍💻
# ║  🧑‍💻 Eldad Cohen   207920711 🧑‍💻
# ║  🧑‍💻 Israel Shlomo 315130344 🧑‍💻
# ║
# ╚══════════════════════════════════╝
import os

from PySide6.QtCore import Qt
from PySide6.QtGui import QBrush, QPalette, QPixmap
from PySide6.QtWidgets import (
    QFormLayout,
    QLineEdit,
    QMessageBox,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


# ======================================== BUY STOCKS WINDOW ======================================== #
class BuyStocksWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("🌊 Buy Stocks – Responsive Design 🌊")
        self.resize(800, 500)

        # ===== Set Background Image ===== #
        base_path = os.path.dirname(__file__)
        image_path = os.path.join(
            base_path, "..", "assets", "images", "background_pic.jpeg"
        )

        palette = QPalette()
        background = QPixmap(image_path)
        palette.setBrush(QPalette.Window, QBrush(background))
        self.setPalette(palette)

        # ========== CSS Styling for Modern Blue Look ========== #
        self.setStyleSheet(
            """
            QLabel {
                color: white;
                font-size: 16px;
                font-weight: bold;
            }
            QLineEdit {
                background-color: #e3f2fd;
                color: #0d47a1;
                border: 1px solid #90caf9;
                border-radius: 6px;
                padding: 6px;
            }
            QPushButton {
                background-color: rgba(255, 255, 255, 0.8);
                color: #0d47a1;
                font-weight: bold;
                border-radius: 16px;
                padding: 10px 24px;
            }
            QPushButton:hover {
                background-color: rgba(255, 255, 255, 1.0);
            }
        """
        )

        # ========== Inputs and Labels ========== #
        self.stock_input = QLineEdit()
        self.stock_input.setPlaceholderText("e.g., AAPL")
        self.amount_input = QLineEdit()
        self.amount_input.setPlaceholderText("e.g., 10")

        # ========== Submit Button ========== #
        self.execute_purchase_button = QPushButton("✅ Execute Purchase")
        self.execute_purchase_button.clicked.connect(self.on_click_execute_purchase)

        # ========== Form Layout ========== #
        form_layout = QFormLayout()
        form_layout.addRow("Stock name:", self.stock_input)
        form_layout.addRow("Amount:", self.amount_input)

        # ========== Container Layout ========== #
        form_container = QWidget()
        form_container.setLayout(form_layout)
        form_container.setMaximumWidth(400)

        main_layout = QVBoxLayout()
        main_layout.setAlignment(Qt.AlignCenter)
        main_layout.setSpacing(25)
        main_layout.addWidget(form_container)
        main_layout.addWidget(self.execute_purchase_button, alignment=Qt.AlignCenter)

        self.setLayout(main_layout)

    # ========== Confirmation Logic ========== #
    def on_click_execute_purchase(self):
        stock = self.stock_input.text()
        amount = self.amount_input.text()

        if not stock or not amount:
            QMessageBox.warning(self, "Missing Fields ⚠️", "Please fill all the fields")
            return

        QMessageBox.information(
            self, "Done ✅", f"{amount} shares of {stock} were successfully ordered! 🚀"
        )
        QMessageBox.information(
            self, "Done ✅", f"{amount} shares of {stock} were successfully ordered! 🚀"
        )
