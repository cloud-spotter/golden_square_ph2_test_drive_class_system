from lib.todo_list import *

"""
Test #complete returns all complete todos 
"""
def test_todo_list_returns_all_complete_todos():
    todo_list = TodoList()
    todo_list1 = Todo("Recap Python TDD")
    todo_list2 = Todo("Codewars practice")
    todo_list1.mark_complete()
    todo_list2.mark_complete()

    todo_list.add(todo_list1)
    todo_list.add(todo_list2)
    
    assert todo_list.complete() == [todo_list1, todo_list2]

