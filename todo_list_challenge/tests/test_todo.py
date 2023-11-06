from lib.todo import Todo

"""
Test that an instance of ToDo intializes with the task given to it
"""
def test_class_initalizes_correctly():
    todo = Todo("Go for a jog")
    assert todo.task == "Go for a jog"

"""
Test that an instance of ToDo intializes with the 'complete' attribute set to False
"""
def test_complete_attribute_initializes_to_false():
    todo = Todo("Go for a jog")
    assert todo.complete == False