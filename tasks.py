from storage import load_tasks, save_tasks

def add_task(title):
    tasks = load_tasks()
    tasks.append({
        "title": title,
        "done": False
    })
    save_tasks(tasks)
    print("تمت اضافة المهمة")

def show_tasks():
    tasks = load_tasks()
    if not tasks:
        print("لا توجد مهام")
        return
    
    for i, task in enumerate(tasks, start=1):
        status = "ok" if task["done"] else "not ok"
        print(f"{i} {task['title']} [{status}]")

def complete_task(index):
    tasks = load_tasks()
    if index < 1 or index > len(tasks):
        print("رقم غير صحيح")
        return
    
    tasks[index - 1]["done"] = True
    save_tasks(tasks)
    print("تم انهاء المهمة")
