import requests


class APIService:
    BASE_URL = "http://localhost:5025/api"

    @staticmethod
    def login(username, password):
        try:
            response = requests.post(
                f"{APIService.BASE_URL}/User/login",
                json={"username": username, "password": password},
            )
            response.raise_for_status()

            return {
                "success": "welcome back" in response.text.lower(),
                "message": response.text,
            }

        except Exception as e:
            return {"success": False, "message": str(e)}
