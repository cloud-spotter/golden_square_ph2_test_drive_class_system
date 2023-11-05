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

    def reading_time(self, wpm: int) -> int:
        '''Returns an integer representing an estimate of the reading time in minutes
        for the all the entries at the given wpm'''
        return self.count_words() / wpm
    
    def find_best_entry_for_reading_time(self, wpm: int, minutes: int) -> int:
        '''Returns a string representing the content best suited to the time available in minutes,
        and given reading speed (wpm)'''
        word_limit = wpm * minutes
        sorted_entries = sorted(self.entries, key=lambda entry: entry.count_words(), reverse=True)
        
        for entry in sorted_entries:
            entry_length = entry.count_words()
            if entry_length <= word_limit:
                if entry_length == word_limit:
                    return entry  # Perfect fit scenario
                else:
                    return entry  # Next best, if no perfect fit