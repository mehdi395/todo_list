def todo_list():
    tasks = []

    while True:
        print("\n--- مدیریت لیست کارها ---")
        print("1. افزودن وظیفه")
        print("2. حذف وظیفه")
        print("3. نمایش وظایف")
        print("4. خروج")

        choice = input("انتخاب کنید (1-4): ")

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
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")
        elif choice == "4":
            print("خروج از برنامه. موفق باشید!")
            break
        else:
            print("انتخاب نامعتبر!")

todo_list()

