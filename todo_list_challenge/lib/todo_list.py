from typing import List
from lib.todo import Todo

class TodoList:
    def __init__(self) -> None:
        self.todos = []

    def add(self, todo: Todo) -> None:
        '''Adds an instance of Todo to the list of todos'''
        self.todos.append(todo)
    
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