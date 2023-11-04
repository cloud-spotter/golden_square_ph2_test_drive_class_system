from lib.diary_entry import *

"""
Test #count_words returns total word count for a diary entry
"""
def test_count_words():
    entry = DiaryEntry("Monday", "Hello World!")
    assert entry.count_words() == 2 

"""
Test reading time estimation for a DiaryEntry
"""
def test_reading_time():
    entry = DiaryEntry("Tuesday Motivation", "'Quality is not an act. It is a habit.' Aristotle")
    wpm = 10
    assert entry.reading_time(wpm) == 1 #10 words at reading speed 10wpm: 1 minute

"""
Test chunk reading for a DiaryEntry and given time available to read
"""
def test_reading_chunk_two_chunks():
    entry = DiaryEntry("Monday Motivation", "'It does not matter how slowly you go as long as you do not stop.' Confucius")
    wpm = 4  # Read at a slow rate
    minutes = 2  
    chunk1 = entry.reading_chunk(wpm, minutes)
    chunk2 = entry.reading_chunk(wpm, minutes)
    
    assert chunk1 == "'It does not matter how slowly you go"
    assert chunk2 == "as long as you do not stop.' Confucius" 