import json
import random
import os

DATA_FILE = "places.json"

# -----------------------
# Load / Save
# -----------------------
def load_places():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as file:
        return json.load(file)

def save_places(places):
    with open(DATA_FILE, "w") as file:
        json.dump(places, file, indent=2)

# -----------------------
# Features
# -----------------------
def get_categories(places):
    categories = set()
    for place in places:
        for cat in place["category"]:
            categories.add(cat)
    return sorted(categories)

def suggest_place(places):
    if not places:
        print("No places yet!")
        return

    categories = get_categories(places)

    print("\nAvailable categories:", ", ".join(categories))
    choice = input("Choose category (or press Enter for random): ").lower()

    if choice:
        filtered = [p for p in places if choice in p["category"]]
    else:
        filtered = places

    if not filtered:
        print("No places found.")
        return

    place = random.choice(filtered)

    print(f"\n📍 {place['name']}")
    print(f"📖 {place['fact']}")
    print(f"🎯 {place['mission']}")

def add_place(places):
    name = input("Place name: ")
    fact = input("Fact: ")
    mission = input("Mission: ")
    categories = input("Categories (comma separated): ").lower().split(",")

    place = {
        "name": name,
        "fact": fact,
        "mission": mission,
        "category": [c.strip() for c in categories],
        "photos": []
    }

    places.append(place)
    save_places(places)
    print("Place added! ✅")

def add_photo(places):
    name = input("Which place did you visit? ").lower()

    for place in places:
        if place["name"].lower() == name:
            photo = {
                "file": input("Photo file path: "),
                "note": input("Note: "),
                "rating": int(input("Rating (1-5): "))
            }
            place["photos"].append(photo)
            save_places(places)
            print("Photo added! 📸")
            return

    print("Place not found.")

def view_photos(places):
    for place in places:
        if place["photos"]:
            print(f"\n📍 {place['name']}")
            for photo in place["photos"]:
                print(f" - {photo['file']} | {photo['note']} | ⭐ {photo['rating']}")

# -----------------------
# Main Menu
# -----------------------
def main():
    places = load_places()

    while True:
        print("\n=== Budapest Explorer ===")
        print("1. Get a place suggestion")
        print("2. Add a new place")
        print("3. Add a photo to a place")
        print("4. View my photo catalogue")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            suggest_place(places)
        elif choice == "2":
            add_place(places)
        elif choice == "3":
            add_photo(places)
        elif choice == "4":
            view_photos(places)
        elif choice == "5":
            print("Goodbye 👋")
            break
        else:
            print("Invalid choice.")

# Run the app
main()