<<<<<<< HEAD
=======
def save_tasks_to_file(tasks, filename="tasks.txt"):
    with open(filename, "w") as file:
        for task in tasks:
            file.write(task + "\n")
    print("وظایف ذخیره شدند!")


def load_tasks_from_file(filename="tasks.txt"):
    tasks = []
    try:
        with open(filename, "r") as file:
            tasks = [line.strip() for line in file]
        print("وظایف بارگذاری شدند!")
    except FileNotFoundError:
        print("هیچ فایل ذخیره‌شده‌ای یافت نشد!")
    return tasks


>>>>>>> save_to_file
def todo_list():
    tasks = []

    while True:
        print("\n--- مدیریت لیست کارها ---")
        print("1. افزودن وظیفه")
        print("2. حذف وظیفه")
        print("3. نمایش وظایف")
<<<<<<< HEAD
        print("4. خروج")

        choice = input("انتخاب کنید (1-4): ")
=======
        print("4. ذخیره وظایف")
        print("5. بارگذاری وظایف")
        print("6. خروج")

        choice = input("انتخاب کنید (1-6): ")
>>>>>>> save_to_file

        if choice == "1":
            task = input("وظیفه جدید را وارد کنید: ")
            tasks.append(task)
            print("وظیفه اضافه شد.")
        elif choice == "2":
            task = input("وظیفه‌ای که می‌خواهید حذف کنید را وارد کنید: ")
            if task in tasks:
                tasks.remove(task)
                print("وظیفه حذف شد.")
            else:
                print("وظیفه یافت نشد!")
        elif choice == "3":
            print("\nلیست وظایف:")
<<<<<<< HEAD
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")
        elif choice == "4":
=======
            if tasks:
                for i, task in enumerate(tasks, start=1):
                    print(f"{i}. {task}")
            else:
                print("لیست وظایف خالی است!")
        elif choice == "4":
            save_tasks_to_file(tasks)
        elif choice == "5":
            tasks = load_tasks_from_file()
        elif choice == "6":
>>>>>>> save_to_file
            print("خروج از برنامه. موفق باشید!")
            break
        else:
            print("انتخاب نامعتبر!")

<<<<<<< HEAD
todo_list()

=======

todo_list()
>>>>>>> save_to_file
