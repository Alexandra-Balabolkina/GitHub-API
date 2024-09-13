import os
import requests
from dotenv import load_dotenv

load_dotenv()

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
GITHUB_USERNAME = os.getenv("GITHUB_USERNAME")
REPO_NAME = os.getenv("REPO_NAME")

headers = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json",
}

BASE_URL = "https://api.github.com"


def create_repository():
    """Создание нового репозитория."""
    url = f"{BASE_URL}/user/repos"
    data = {
        "name": REPO_NAME,
        "private": False,
    }

    response = requests.post(url, json=data, headers=headers)

    if response.status_code == 201:
        print(f"Repository '{REPO_NAME}' created successfully.")
    else:
        print(f"Failed to create repository. Status code: {response.status_code}")
        print(response.json())


def check_repository():
    """Проверка наличия репозитория в списке пользователя."""
    url = f"{BASE_URL}/user/repos"

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        repos = [repo['name'] for repo in response.json()]
        if REPO_NAME in repos:
            print(f"Repository '{REPO_NAME}' exists.")
        else:
            print(f"Repository '{REPO_NAME}' not found.")
    else:
        print(f"Failed to fetch repositories. Status code: {response.status_code}")
        print(response.json())


def delete_repository():
    """Удаление созданного репозитория."""
    url = f"{BASE_URL}/repos/{GITHUB_USERNAME}/{REPO_NAME}"

    response = requests.delete(url, headers=headers)

    if response.status_code == 204:
        print(f"Repository '{REPO_NAME}' deleted successfully.")
    else:
        print(f"Failed to delete repository. Status code: {response.status_code}")
        print(response.json())


if __name__ == "__main__":
    create_repository()
    check_repository()
    delete_repository()
