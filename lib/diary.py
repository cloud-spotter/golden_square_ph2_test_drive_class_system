from typing import List # for type annotation below (List[str])
from lib.diary_entry import *

class Diary:
    def __init__(self) -> None:
        self.entries = []

    def add(self, entry: DiaryEntry) -> None:
        '''Adds an instance of DiaryEntry to the list of entries'''
        self.entries.append(entry)

    def all(self) -> List[str]:
        '''Returns a list of instances of DiaryEntry'''
        return self.entries

    def count_words(self) -> int:
        '''Returns an integer representing the number of words in all diary entries'''
        entries_words = 0
        for entry in self.entries:
            entries_words += entry.count_words()
        return entries_words

    def reading_time(self, wpm) -> int:
        '''Returns an integer representing an estimate of the reading time in minutes
        #   for the all the entries at the given wpm'''
        return self.count_words() / wpm
