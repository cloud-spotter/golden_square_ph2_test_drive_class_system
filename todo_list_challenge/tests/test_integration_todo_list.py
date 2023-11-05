from lib.todo_list import *
from lib.todo import *

"""
1. When two new Todo instances are added to a TodoList instance,
TodoList retrieves and returns these
"""
def test_todo_list_integration_returns_all_incomplete_todos():
    todo_list = TodoList()
    todo_1 = Todo("Codewars practice", False)
    todo_2 = Todo("Recap Golden Square material", False)
    todo_list.add(todo_1)
    todo_list.add(todo_2)
    assert todo_list.incomplete() == [todo_1, todo_2]




