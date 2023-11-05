import pytest
from lib.diary import *
from lib.diary_entry import *

"""
Test Diary instantiates 
"""
def test_diary_instantiates():
    diary = Diary()

"""
Test Diary initialises with a title and contents
"""
def test_diary_initialises_with_title_and_contents():
    diary = Diary()
    diary_entry_1 = DiaryEntry("First Entry", "Dear Diary, it's Monday again.")
    diary.add(diary_entry_1)
    assert diary.all() == [diary_entry_1]

"""
Test word count calculation for multiple DiaryEntries in a Diary
"""
def test_count_words():
    diary = Diary()
    diary.add(DiaryEntry("First Entry", "Two words."))
    diary.add(DiaryEntry("Second Entry", "Three words here."))
    assert diary.count_words() == 5

"""
Test reading time estimation for multiple DiaryEntries in a Diary
"""
# See integration test 3

"""
Test Diary returns most appropriate entry to read,
given the user's wpm reading rate and minutes available
"""
# See integration test 4