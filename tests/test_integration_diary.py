from lib.diary import *
from lib.diary_entry import *

"""
1. When two new DiaryEntry objects are created
The Diary instance retrieves and returns these in the same order 
"""
def test_diary_integration_return_all_entries():
    diary = Diary()
    diary_entry_1 = DiaryEntry("First Entry", "Dear Diary, it's Monday again.")
    diary_entry_2 = DiaryEntry("Monday Motivation", "'It does not matter how slowly you go as long as you do not stop.' Confucius")
    diary.add(diary_entry_1)
    diary.add(diary_entry_2)
    assert diary.all() == [diary_entry_1, diary_entry_2]

"""
2. Given a Diary instance (diary) with multiple DiaryEntry instances, 
diary calculates and returns the word count across all entries
"""
def test_diary_integration_entries_word_count():
    diary = Diary()
    diary_entry_1 = DiaryEntry("First Entry", "Dear Diary, it's Monday.")
    diary_entry_2 = DiaryEntry("Monday Motivation", "'It does not matter how slowly you go as long as you do not stop.' Confucius")
    diary.add(diary_entry_1)
    diary.add(diary_entry_2)
    assert diary.count_words() == 20

"""
3. Given a reading time,
a Diary instance calculates and returns the estimated reading time across all entries (in wpm)
"""
def test_diary_integration_estimate_entries_reading_time():
    diary = Diary()
    diary.add(DiaryEntry("First Entry", "Dear Diary, it's Monday."))
    diary.add(DiaryEntry("Monday Motivation", "'It does not matter how slowly you go as long as you do not stop.' Confucius"))
    diary.add(DiaryEntry("Tuesday Motivation", "'Quality is not an act. It is a habit.' Aristotle"))
    
    wpm = 10
    expected_reading_time = 3
    assert diary.reading_time(wpm) == expected_reading_time

"""
4. Given a Diary instance with multiple diary entries
Diary finds the best entry to read for a given time frame
"""
def test_diary_integration_find_best_entry_for_time():
    diary = Diary()
    diary_entry_1 = DiaryEntry("First Entry", "Dear Diary, it's Monday.")
    diary_entry_2 = DiaryEntry("Monday Motivation", "'It does not matter how slowly you go as long as you do not stop.' Confucius")
    diary.add(diary_entry_1) 
    diary.add(diary_entry_2)

    minutes = 1
    wpm = 10
    best_entry = diary.find_best_entry_for_reading_time(wpm, minutes)
    assert best_entry == diary_entry_1