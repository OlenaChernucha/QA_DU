import json

def read_tasks_from_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

def calculation_tasks_user(tasks, user_id):
    tasks_completed = 0
    tasks_uncompleted = 0

    for task in tasks:
        if task["userId"] == user_id:
            if task["completed"]:
                tasks_completed += 1
            else:
                tasks_uncompleted += 1

    return tasks_completed, tasks_uncompleted

if __name__ == '__main__':
    json_file_path = 'todos.json'
    tasks = read_tasks_from_json(json_file_path)

    user_id = 1  
    completed, uncompleted = calculation_tasks_user(tasks, user_id)
    print(f"User number ID {user_id} has {completed} and {uncompleted} tasks.")
