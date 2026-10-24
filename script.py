import requests
from datetime import datetime

def fetch_mensa_meals():
    # Mensa-ID 42 = Mensa am Park in Leipzig (OpenMensa ID)
    mensa_id = 42
    today = datetime.now().strftime("%Y-%m-%d")
    url = f"https://openmensa.org/api/v2/canteens/{mensa_id}/days/{today}/meals"

    try:
        response = requests.get(url, timeout=10)
        
        # Status 404 = Mensa hat heute zu (z. B. Wochenende oder Feiertag)
        if response.status_code == 404:
            return "Heute gibt es keinen Speiseplan (Mensa geschlossen oder Wochenende)."
        
        response.raise_for_status()
        meals = response.json()

        if not meals:
            return "Keine Angebote für heute gefunden."

        meal_list = []
        for meal in meals:
            name = meal.get("name")
            category = meal.get("category", "Gericht")
            prices = meal.get("prices", {})
            student_price = prices.get("students")
            
            price_str = f" ({student_price:.2f} €)" if student_price else ""
            meal_list.append(f"  - [{category}] {name}{price_str}")

        return "\n".join(meal_list)

    except Exception as e:
        return f"Fehler beim Abrufen des Speiseplans: {e}"

def main():
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    today_str = datetime.now().strftime("%d.%m.%Y")
    
    print(f"Lade Speiseplan für {today_str}...")
    meals_info = fetch_mensa_meals()

    log_entry = f"=== Mensa-Speiseplan vom {today_str} (Stand: {now}) ===\n{meals_info}\n\n"

    with open("log.txt", "a", encoding="utf-8") as f:
        f.write(log_entry)

    print("Speiseplan erfolgreich in log.txt gespeichert!")

if __name__ == "__main__":
    main()