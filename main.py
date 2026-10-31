import json
import os


FILENAME = "dictionary.json"


def load_data():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r", encoding="utf-8") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return {}
    return {}


def save_data(data):
    with open(FILENAME, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def show_menu():
    print("\n--- АНГЛО-ФРАНЦУЗСКИЙ СЛОВАРЬ ---")
    print("1. посмотреть все слова")
    print("2. найти слово (перевод)")
    print("3. добавить новое слово")
    print("4. изменить существующее слово")
    print("5. удалить слово")
    print("0. выйти")


def main():
    dictionary = load_data()

    while True:
        show_menu()
        choice = input("\nвыбери пункт в меню: ").strip()

        if choice == "1":
            if not dictionary:
                print("Словарь пока пустой.")
            else:
                print("\nсписок слов (Английский - Французский):")
                for eng, fr in dictionary.items():
                    print(f"- {eng} : {fr}")

        elif choice == "2":
            word = input("введи англ слово для поиска: ").strip().lower()
            if word in dictionary:
                print(f"перевод: {dictionary[word]}")
            else:
                print("шо ты написал, такого слвоа нету")

        elif choice == "3":
            eng = input("введи англ слово: ").strip().lower()
            if eng in dictionary:
                print("такое слово уже есть, используй лучше ")
            else:
                fr = input("введи перевод на французский: ").strip().lower()
                dictionary[eng] = fr
                save_data(dictionary)
                print("слово добавлено")

        elif choice == "4":
            eng = (
                input(
                    "введи англ слово, которое хочешь изменить: "
                )
                .strip()
                .lower()
            )
            if eng in dictionary:
                print(f"текущий перевод: {dictionary[eng]}")
                new_fr = (
                    input("введи новый перевод на французский ").strip().lower()
                )
                dictionary[eng] = new_fr
                save_data(dictionary)
                print("перевод изменен")
            else:
                print("шо ты написал, такого слвоа нету")

        elif choice == "5":
            eng = (
                input("введи англ слово для удаления ").strip().lower()
            )
            if eng in dictionary:
                del dictionary[eng]
                save_data(dictionary)
                print("Слово удалено!")
            else:
                print("шо ты написал, такого слвоа нету")

        elif choice == "0":
            print("чао")
            break
        else:
            print("Error! нужно другое значеие(0-5)")


if __name__ == "__main__":
    main()
