import os
from datetime import datetime


def main():
    now = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    print(f"[{now}] Cronjob erfolgreich ausgeführt!!")

    with open("log.txt", "a", encoding="utf-8") as f:
        f.write(f"Durchlauf am: {now}\n")
    print(f"[{now}] log.txt wurde erfolgreich aktualisiert!")


if __name__ == "__main__":
    main()