class Todo:
    def __init__(self, task: str) -> None:
        self.task = task
        self.complete = False

    def mark_complete(self) -> None:
        '''Sets the complete property to True'''
        self.complete = True