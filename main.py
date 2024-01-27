import os
from datetime import datetime

class TaskForge:
    def __init__(self, file_path):
        self.file_path = file_path
        self.initialize_files()

    def initialize_files(self):
        if not os.path.exists(self.file_path):
            with open(self.file_path, 'w') as file:
                file.write("# TaskForge Priorities\n\n"
                           "## Books\n- Priority: 7\n- File: books_tasks.md\n- History: books_history.md\n\n"
                           "## Movies\n- Priority: 5\n- File: movies_tasks.md\n- History: movies_history.md\n\n"
                           "## Music\n- Priority: 8\n- File: music_tasks.md\n- History: music_history.md\n\n"
                           "## Meditation\n- Priority: 9\n- File: meditation_tasks.md\n- History: meditation_history.md")

    def update_tasks(self, task, tasks_list, priority):
        tasks_file = f"{task.lower()}_tasks.md"
        with open(tasks_file, 'w') as file:
            file.write(f"# {task} Tasks\n\nPriority: {priority}\n\n")
            for item in tasks_list:
                file.write(f"- {item}\n")

    def update_history(self, task, history_list):
        history_file = f"{task.lower()}_history.md"
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(history_file, 'a') as file:
            for item in history_list:
                file.write(f"- {item} --on-time-- {timestamp}\n")

    def check_meditation(self):
        history_file = 'meditation_history.md'
        try:
            with open(history_file, 'r') as file:
                lines = file.readlines()

            if lines:
                last_meditation_line = lines[-1]
                last_meditation_timestamp = last_meditation_line.split('--on-time--')[-1].strip()
                last_meditation_time = datetime.strptime(last_meditation_timestamp, "%Y-%m-%d %H:%M:%S")
                # time_since_last_meditation = datetime.now() - last_meditation_time
                # print(f"It's been {time_since_last_meditation.days} days, {time_since_last_meditation.seconds // 3600} hours, and "
                #       f"{(time_since_last_meditation.seconds // 60) % 60} minutes since your last meditation.")
                return last_meditation_time
            else:
                return False
                print("No meditation history found.")
        except FileNotFoundError:
            print("Meditation history file not found.")

# Example Usage
task_forge = TaskForge('TaskForge.md')

# Check how long it's been since the last meditation
task_forge.update_history("Meditation", ["Completed: 30 minutes meditation"])

print(task_forge.check_meditation())