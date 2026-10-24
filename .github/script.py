import os
from datetime import datetime


def main():
    now = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    print(f"[{now}] Cronjob erfolgreich ausgeführt!!")


if __name__ == "__main__":
    main()