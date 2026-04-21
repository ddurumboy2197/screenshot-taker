import heapq

class Task:
    def __init__(self, name, priority, deadline):
        self.name = name
        self.priority = priority
        self.deadline = deadline

class PriorityQueueTaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        heapq.heappush(self.tasks, (task.priority, task.deadline, task.name))

    def remove_task(self, task_name):
        self.tasks = [(priority, deadline, name) for priority, deadline, name in self.tasks if name != task_name]

    def get_next_task(self):
        if not self.tasks:
            return None
        return heapq.heappop(self.tasks)

    def update_task_priority(self, task_name, new_priority):
        for i, (priority, deadline, name) in enumerate(self.tasks):
            if name == task_name:
                self.tasks[i] = (new_priority, deadline, name)
                heapq.heapify(self.tasks)
                break

    def update_task_deadline(self, task_name, new_deadline):
        for i, (priority, deadline, name) in enumerate(self.tasks):
            if name == task_name:
                self.tasks[i] = (priority, new_deadline, name)
                heapq.heapify(self.tasks)
                break

    def print_tasks(self):
        for priority, deadline, name in self.tasks:
            print(f"Task: {name}, Priority: {priority}, Deadline: {deadline}")

# Test
task_manager = PriorityQueueTaskManager()

task1 = Task("Task 1", 1, 10)
task2 = Task("Task 2", 2, 5)
task3 = Task("Task 3", 3, 15)

task_manager.add_task(task1)
task_manager.add_task(task2)
task_manager.add_task(task3)

task_manager.print_tasks()

next_task = task_manager.get_next_task()
print(f"Next task: {next_task[2]}")

task_manager.update_task_priority("Task 2", 1)
task_manager.print_tasks()

task_manager.update_task_deadline("Task 3", 10)
task_manager.print_tasks()

task_manager.remove_task("Task 2")
task_manager.print_tasks()
```

Bu kodda biz quyidagilar qilamiz:

1. `Task` classi yaratamiz, unda taskning nomi, priority va deadline mavjud.
2. `PriorityQueueTaskManager` classi yaratamiz, unda biz quyidagilar qilamiz:
 * `add_task` methodi: taskni priority queuega qo'shadi.
 * `remove_task` methodi: taskni priority queue dan olib tashlaydi.
 * `get_next_task` methodi: priority queue dan eng past priorityga ega taskni olib qaytaradi.
 * `update_task_priority` methodi: taskning priorityini yangilaydi.
 * `update_task_deadline` methodi: taskning deadlineini yangilaydi.
 * `print_tasks` methodi: priority queuedagi barcha tasklarni chiqaradi.
3. Test uchun biz quyidagilar qilamiz:
 * `Task` classining uchta obyekti yaratamiz: `task1`, `task2` va `task3`.
 * `PriorityQueueTaskManager` obyekti yaratamiz va unga uchta task qo'shamiz.
 * `print_tasks` methodini chaqiramiz.
 * `get_next_task` methodini chaqiramiz.
 * `update_task_priority` methodini chaqiramiz.
 * `update_task_deadline` methodini chaqiramiz.
 * `print_tasks` methodini chaqiramiz.
 * `remove_task` methodini chaqiramiz.
 * `print_tasks` methodini chaqiramiz.
