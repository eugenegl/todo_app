# main.py

def display_menu():
    print("\n--- Список дел ---")
    print("1. Показать задачи")
    print("2. Добавить задачу")
    print("3. Удалить задачу")
    print("4. Редактировать задачу")  # Новая опция
    print("5. Выход")

def show_tasks(tasks):
    if not tasks:
        print("Список задач пуст.")
    else:
        print("\nВаши задачи:")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")

def add_task(tasks):
    task = input("Введите новую задачу: ")
    tasks.append(task)
    print(f"Задача '{task}' добавлена.")

def delete_task(tasks):
    show_tasks(tasks)
    if tasks:
        try:
            idx = int(input("Введите номер задачи для удаления: "))
            if 1 <= idx <= len(tasks):
                removed_task = tasks.pop(idx - 1)
                print(f"Задача '{removed_task}' удалена.")
            else:
                print("Неверный номер задачи.")
        except ValueError:
            print("Пожалуйста, введите корректный номер.")

def edit_task(tasks):
    show_tasks(tasks)
    if tasks:
        try:
            idx = int(input("Введите номер задачи для редактирования: "))
            if 1 <= idx <= len(tasks):
                new_task = input("Введите новое описание задачи: ")
                old_task = tasks[idx - 1]
                tasks[idx - 1] = new_task
                print(f"Задача '{old_task}' изменена на '{new_task}'.")
            else:
                print("Неверный номер задачи.")
        except ValueError:
            print("Пожалуйста, введите корректный номер.")

def main():
    tasks = []
    while True:
        display_menu()
        choice = input("Выберите опцию: ")
        if choice == '1':
            show_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            delete_task(tasks)
        elif choice == '4':
            edit_task(tasks)  # Обработка новой опции
        elif choice == '5':
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()