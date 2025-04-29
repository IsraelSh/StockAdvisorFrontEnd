📁 StockAdvisor Frontend - README

👋 Welcome!

This project is a Python GUI application built with PySide6 that connects to a Stock Advisor Backend (ASP.NET Core Web API).

---

🛠 Requirements:
- Python 3.10 or higher
- Internet access to install required libraries
- Backend server running at http://localhost:5025 (or update BASE_URL if needed)

---

⚙️ How to set up:

1. Make sure Python is installed.
2. Open a terminal (Command Prompt or VSCode Terminal).
3. Navigate to the project folder (where main.py is located).
4. Install all required libraries by running:
   
   pip install -r requirements.txt

---

🚀 How to run the project:

Option 1 (Manually):
- Open the terminal in the project folder
- Run:

   python main.py

Option 2 (Recommended):
- Just double-click `run_frontend.bat`
- It will install everything and run the app automatically!

---

❗ Notes:
- Ensure that your Backend is running before starting the Frontend.
- If the Backend address changes, update it inside `api_service.py` (in the BASE_URL variable).
- All background images must be located under `assets/images/`.

---

👨‍💻 Built with ❤️ by Israel S., Elyasaf C., and Eldad C.
