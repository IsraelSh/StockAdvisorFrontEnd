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

from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from PySide6.QtCore import QDate, Qt
from PySide6.QtGui import QBrush, QCursor, QPalette, QPixmap
from PySide6.QtWidgets import (
    QDateEdit,
    QFileDialog,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QTableWidget,
    QTableWidgetItem,
    QVBoxLayout,
    QWidget,
)


# ======================================== ORDER HISTORY WINDOW ======================================== #
class OrderHistoryWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("📄 Order History – Investment Recap")
        self.resize(1000, 700)

        # ===== Set Background Image ===== #
        base_path = os.path.dirname(__file__)
        image_path = os.path.join(
            base_path, "..", "assets", "images", "background_pic.jpeg"
        )

        palette = QPalette()
        background = QPixmap(image_path)
        palette.setBrush(QPalette.Window, QBrush(background))
        self.setPalette(palette)

        # ===== Global StyleSheet ===== #
        self.setStyleSheet(
            """
            QWidget {
                font-family: 'Segoe UI';
                background-repeat: no-repeat;
                background-position: center;
                color: white;
                font-size: 14px;
            }

            QLabel {
                font-size: 18px;  /* קצת קטן יותר */
                font-weight: bold;
                padding: 4px 0;
            }

            QPushButton {
                background-color: rgba(255, 255, 255, 0.9);
                color: #1a237e;
                font-weight: bold;
                padding: 6px 16px;  /* הצרה קלה */
                font-size: 13px;    /* טקסט קטן יותר */
                border-radius: 12px;
            }

            QPushButton:hover {
                background-color: #c5e1f9;
                color: #0d47a1;
            }

            QTableWidget {
                background-color: rgba(255, 255, 255, 0.95);
                color: black;
                border-radius: 10px;
            }

            QHeaderView::section {
                background-color: #e3f2fd;
                color: #0d47a1;
                font-weight: bold;
                padding: 6px;
            }

            QLineEdit, QDateEdit {
                background-color: rgba(255, 255, 255, 0.9);
                color: black;
                padding: 4px 10px;   /* קומפקטי יותר */
                font-size: 13px;
                border-radius: 8px;
                min-width: 100px;
            }
        """
        )

        # ===== Title ===== #
        self.title = QLabel("📄 Order History")
        self.title.setAlignment(Qt.AlignCenter)

        # ===== Filters ===== #
        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Search stock...")

        self.date_from = QDateEdit()
        self.date_from.setCalendarPopup(True)
        self.date_from.setDate(QDate(2025, 4, 1))

        self.date_to = QDateEdit()
        self.date_to.setCalendarPopup(True)
        self.date_to.setDate(QDate(2025, 4, 30))

        self.filter_button = QPushButton("🔎 Filter")
        self.filter_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.filter_button.clicked.connect(self.apply_filters)

        self.export_button = QPushButton("📁 Export CSV")
        self.export_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.export_button.clicked.connect(self.export_to_csv)

        self.graph_button = QPushButton("📊 Show Graph")
        self.graph_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.graph_button.clicked.connect(self.toggle_graph)

        # ===== Filter Layout ===== #
        filter_layout = QHBoxLayout()
        filter_layout.addWidget(QLabel("From:"))
        filter_layout.addWidget(self.date_from)
        filter_layout.addWidget(QLabel("To:"))
        filter_layout.addWidget(self.date_to)
        filter_layout.addWidget(self.search_input)
        filter_layout.addWidget(self.filter_button)
        filter_layout.addWidget(self.export_button)
        filter_layout.addWidget(self.graph_button)

        # ===== Order Table ===== #
        self.table = QTableWidget()
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(
            ["Date", "Type", "Stock", "Amount", "Total ($)"]
        )
        self.table.setSortingEnabled(True)

        # ===== Chart Setup (hidden) ===== #
        self.graph_canvas = FigureCanvas(Figure(figsize=(6, 3)))
        self.graph_canvas.hide()

        # ===== Full Data ===== #
        self.full_data = [
            ("2025-04-01", "Buy", "AAPL", 10, 1800),
            ("2025-04-02", "Sell", "TSLA", 5, 1200),
            ("2025-04-03", "Buy", "MSFT", 8, 1600),
            ("2025-04-04", "Sell", "GOOGL", 6, 2000),
            ("2025-04-05", "Buy", "AMZN", 4, 950),
        ]

        self.load_data(self.full_data)

        # ===== Layout ===== #
        layout = QVBoxLayout()
        layout.addWidget(self.title)
        layout.addLayout(filter_layout)
        layout.addWidget(self.table)
        layout.addWidget(self.graph_canvas)
        self.setLayout(layout)

    # ===== Load data into the table ===== #
    def load_data(self, data):
        self.table.setRowCount(len(data))
        for row, row_data in enumerate(data):
            for col, val in enumerate(row_data):
                self.table.setItem(row, col, QTableWidgetItem(str(val)))

    # ===== Apply filters by date and stock name ===== #
    def apply_filters(self):
        text = self.search_input.text().lower()
        from_date = self.date_from.date().toString("yyyy-MM-dd")
        to_date = self.date_to.date().toString("yyyy-MM-dd")

        filtered = []
        for row in self.full_data:
            date, action, stock, amount, total = row
            if from_date <= date <= to_date:
                if text == "" or text in stock.lower():
                    filtered.append(row)

        self.load_data(filtered)
        self.filtered_data = filtered

    # ===== Export current table to CSV ===== #
    def export_to_csv(self):
        path, _ = QFileDialog.getSaveFileName(
            self, "Save Orders", "", "CSV Files (*.csv)"
        )
        if path:
            with open(path, "w") as f:
                f.write("Date,Type,Stock,Amount,Total($)\n")
                for row in getattr(self, "filtered_data", self.full_data):
                    f.write(",".join(map(str, row)) + "\n")

    # ===== Toggle the graph visibility ===== #
    def toggle_graph(self):
        if self.graph_canvas.isVisible():
            self.graph_canvas.hide()
            self.graph_button.setText("Show Graph 📊 ")
        else:
            self.update_graph()
            self.graph_canvas.show()
            self.graph_button.setText("Hide Graph 🙈📈")

    # ===== Update matplotlib chart ===== #
    def update_graph(self):
        self.graph_canvas.figure.clf()
        ax = self.graph_canvas.figure.add_subplot(111)

        data = getattr(self, "filtered_data", self.full_data)
        dates = [row[0] for row in data]
        buys = [row[3] if row[1] == "Buy" else 0 for row in data]
        sells = [row[3] if row[1] == "Sell" else 0 for row in data]

        ax.bar(dates, buys, label="Buy Qty", color="#81c784")
        ax.bar(dates, sells, label="Sell Qty", color="#ef5350", bottom=buys)

        ax.set_title("Orders Summary 📊 ")
        ax.set_xlabel("Date")
        ax.set_ylabel("Amount")
        ax.legend()
        ax.grid(True, linestyle="--", alpha=0.6)

        self.graph_canvas.draw()

        ax.set_title("Orders Summary 📊 ")
        ax.set_xlabel("Date")
        ax.set_ylabel("Amount")
        ax.legend()
        ax.grid(True, linestyle="--", alpha=0.6)

        self.graph_canvas.draw()
