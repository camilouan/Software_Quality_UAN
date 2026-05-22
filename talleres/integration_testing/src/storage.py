import json
import os

class TaskStorage:
    def __init__(self, filepath):
        self.filepath = filepath

        if not os.path.exists(filepath):
            with open(filepath, 'w') as f:
                json.dump([], f)

    def load(self):
        with open(self.filepath, 'r') as f:
            return json.load(f)

    def save(self, tasks):
        with open(self.filepath, 'w') as f:
            json.dump(tasks, f, indent=2)
