from lib.todo_list import *
import pytest

"""
Test #complete returns all complete todos 
"""
def test_todo_list_returns_all_complete_todos():
    todo_list = TodoList()
    todo_1 = Todo("Recap Python TDD")
    todo_2 = Todo("Codewars practice")
    todo_1.mark_complete()
    todo_2.mark_complete()

    todo_list.add(todo_1)
    todo_list.add(todo_2)
    
    assert todo_list.complete() == [todo_1, todo_2]

"""
Test #give_up marks all todos as complete
"""
def test_mark_all_todos_complete():
    todo_list = TodoList()
    todo_1 = Todo("Recap Python TDD")
    todo_2 = Todo("Codewars practice")
    todo_3 = Todo("Add README to this repo")

    todo_list.add(todo_1)
    todo_list.add(todo_2)
    todo_list.add(todo_3)

    todo_list.give_up()
    assert todo_list.complete() == [todo_1, todo_2, todo_3]

"""
When an empty todo is passed to #add, 
an error is raised
"""
def test_add_raises_error_for_empty_todo():
    todo_list = TodoList()
    with pytest.raises(Exception) as e:
        todo_list.add(Todo(""))
    error_message = str(e.value)
    assert error_message == "Empty todo. Please enter a task."
