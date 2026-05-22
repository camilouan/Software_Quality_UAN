import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.storage import TaskStorage


def test_storage_save_and_load():
    storage = TaskStorage("test_driver.json")

    storage.save([{"title": "Test", "done": False}])

    data = storage.load()

    assert len(data) == 1
