import os
import re
import time
import sys
import platform
from colorama import init, Fore, Style

init(autoreset=True)

LOG_PATHS = [
    os.path.expanduser("~\\Documents\\My Games\\Rocket League\\TAGame\\Logs\\Launch.log"),
    os.path.expanduser("~\\AppData\\Local\\Rocket League\\Saved\\Logs\\Launch.log")
]

def get_latest_log_path():
    for path in LOG_PATHS:
        if os.path.exists(path):
            return path
    return None

def follow_log(file_path):
    """Continuously monitor the Rocket League log file for new IPs and update in place."""
    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
        f.seek(0, os.SEEK_END)
        latest_ip = None
        while True:
            line = f.readline()
            if not line:
                time.sleep(0.1)
                continue
            match = re.search(r'GameURL="([\d\.]+:\d+)"', line)
            if match:
                ip = match.group(1)
                if ip != latest_ip:
                    latest_ip = ip
                    sys.stdout.write(
                        f"\r{Fore.LIGHTGREEN_EX} \nServer: {ip}        {Style.RESET_ALL}"
                    )
                    sys.stdout.flush()

def main():
    log_path = get_latest_log_path()
    if not log_path:
        print(Fore.RED + "Rocket League process not found.")
        return
    print(Fore.LIGHTBLUE_EX + f"██████╗ ██╗         ██╗██████╗ ")
    print(Fore.LIGHTBLUE_EX + f"██╔══██╗██║         ██║██╔══██╗")
    print(Fore.LIGHTBLUE_EX + f"██████╔╝██║         ██║██████╔╝")
    print(Fore.LIGHTBLUE_EX + f"██╔══██╗██║         ██║██╔═══╝ ")
    print(Fore.LIGHTBLUE_EX + f"██║  ██║███████╗    ██║██║     ")
    print(Fore.LIGHTBLUE_EX + f"╚═╝  ╚═╝╚══════╝    ╚═╝╚═╝     ")
    follow_log(log_path)

if __name__ == "__main__":
    os.system("cls" if os.name == "nt" else "clear")
    os.system("title IP Parser" if os.name == "nt" else 'echo -ne "\033]0;IP Parser\007"')
    main()
