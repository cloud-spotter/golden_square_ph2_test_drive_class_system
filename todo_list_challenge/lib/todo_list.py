from typing import List
from lib.todo import Todo

class TodoList:
    def __init__(self) -> None:
        self.todos = []

    def add(self, todo: Todo) -> None:
        '''Adds an instance of Todo to the list of todos'''
        if todo.task != "":
            self.todos.append(todo)
        else:
            raise Exception("Empty todo. Please enter a task.")
    
    def incomplete(self) -> List[Todo]:
        '''Returns a list of Todo instances representing the todos that are not complete'''
        incomplete = []
        for todo in self.todos:
            if todo.complete == False:
                incomplete.append(todo)
        return incomplete

    def complete(self) -> List[Todo]:
        '''Returns a list of Todo instances representing the todos that are complete'''
        return [todo for todo in self.todos if todo.complete]

    def give_up(self) -> None:
        '''Marks all todos as complete'''
        for todo in self.todos:
            todo.complete = True