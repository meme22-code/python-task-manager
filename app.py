from tasks import add_task, show_tasks, complete_task
def main():
    while True:
        print("\n=== مدير المهام ===")
        print("1) اضافة مهمة")
        print("2) عرض المهام")
        print("3) انهاء مهمة")
        print("4) خروج")

        choice = input("اختر: ")

        if choice == "1":
            title = input("عنوان المهمة: ")
            add_task(title)

        elif choice == "2":
            show_tasks()

        elif choice == "3":
            show_tasks()
            num = int(input("رقم المهمة: "))
            complete_task(num)

        elif choice == "4":
            print("الى اللفاء")
            break

        else:
            print("اختيار غير صحيح")

if __name__ == "__main__":
    main()