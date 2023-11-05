
class DiaryEntry:
    def __init__(self, title: str, contents: str):
        self.title = title
        self.contents = contents
        self._current_index = 0
    
    def __str__(self):
    '''Returns a human-readable string representation of the DiaryEntry'''
    return f"Title: {self.title}\nContents: {self.contents}"
    
    def count_words(self) -> int:
        '''Returns an integer representing the number of words in the contents''' 
        words = self.contents.split()
        return len(words)
    
    def reading_time(self, wpm: int) -> int:
        '''Returns an integer representing an estimate of the reading time in minutes
        for the contents at the given wpm'''
        words_to_read = self.count_words()
        return words_to_read / wpm

    def reading_chunk(self, wpm: int, minutes: int) -> str:
        '''Returns a string representing a chunk of the contents that the user could
        read in the given number of minutes'''
        words = self.contents.split()
        word_limit = wpm * minutes
        words_to_read = min(len(words), word_limit)  # Calculate max no. of words to read without going over contents total or word limit
        text_chunk = " ".join(words[self._current_index:self._current_index + words_to_read])
        self._current_index += words_to_read

        if self._current_index >= len(words):
            self._current_index = 0

        return text_chunk 