# Test-drive a Multi-Class Program

## Exercise Introduction
_Abridged from the Makers material_

The principle here is similar to jumping from methods to classes. We still need
to generate examples and encode these as tests, followed up by implementing
behaviour to match those examples.

Tests for multiple classes acting together are called **integration tests** or
sometimes **feature tests**. Tests for a single class or method are called
**unit tests**.

We create integration tests like this:

```python
# File: tests/test_music_library_integration.py
from lib.music_library import MusicLibrary
from lib.track import Track


def test_music_library_integration():
    library = MusicLibrary()
    track_1 = Track("Always The Hard Way", "Terror")
    track_2 = Track("Higher Place", "Malevolence")
    library.add(track_1)
    library.add(track_2)
    assert library.search_by_title("Always") == [track_1]

# ...

```

However, this is quite a bit to test-drive in one go, so we comment out all but
one line:

```python
# File: tests/test_music_library_integration.py
def test_music_library_integration():
  library = MusicLibrary()
  # track_1 = Track("Always The Hard Way", "Terror")
  # track_2 = Track("Higher Place", "Malevolence")
  # library.add(track_1)
  # library.add(track_2)
  # assert library.search_by_title("Always") == [track_1]
  
  
  # ...

```

And then focus on our `MusicLibrary` class. We create a unit test for that
class:

```python
# File: tests/test_unit_music_library.py

def test_music_library():
    library = MusicLibrary()
  
  # ...

```

Implement it:

```python
# File: lib/music_library.py

class MusicLibrary:
  pass

```

And then back to the integration test to uncomment the next line:

```python
# File: tests/test_music_library_integration_spec.py

def test_music_library_integration():
  library = MusicLibrary()
  track_1 = Track("Always The Hard Way", "Terror")
  # track_2 = Track("Higher Place", "Malevolence")
  # library.add(track_1)
  # library.add(track_2)
  # assert library.search_by_title("Always") == [track_1]
  
  # ...

```

And so on.

At some point you will come across another problem. How do you unit test
`MusicLibrary` without relying on `Track` and inadvertently making it an
integration test?

We are going to leave that subject alone for now and come back to it later. For
now, if you feel yourself about to write a unit test that should exist in the
integration tests — put it in the integration tests and leave it out of the unit
tests. This may make some of your unit tests quite small, which is OK.

## Exercise

Test-drive a class system based on this design.

This is quite a bit to think about — so I suggest making a list of examples for
your integration tests first in a text file, before you start on test-driving,
to make sure you've thought through the full system.

```python
# File: lib/diary.py

class Diary:
    def __init__(self):
        pass

    def add(self, entry):
        # Parameters:
        #   entry: an instance of DiaryEntry
        # Returns:
        #   Nothing
        # Side-effects:
        #   Adds the entry to the entries list
        pass

    def all(self):
        # Returns:
        #   A list of instances of DiaryEntry
        pass

    def count_words(self):
        # Returns:
        #   An integer representing the number of words in all diary entries
        # HINT:
        #   This method should make use of the `count_words` method on DiaryEntry.
        pass

    def reading_time(self, wpm):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        # Returns:
        #   An integer representing an estimate of the reading time in minutes
        #   if the user were to read all entries in the diary.
        pass

    def find_best_entry_for_reading_time(self, wpm, minutes):
        # Parameters:
        #   wpm:     an integer representing the number of words the user can
        #            read per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   An instance of DiaryEntry representing the entry that is closest to,
        #   but not over, the length that the user could read in the minutes
        #   they have available given their reading speed.
        pass


# File: lib/diary_entry.py

class DiaryEntry:
    # Public Properties:
    #   title: a string
    #   contents: a string

    def __init__(self, title, contents): # title, contents are strings
        # Side-effects:
        #   Sets the title and contents properties
        pass

    def count_words(self):
        # Returns:
        #   An integer representing the number of words in the contents
        pass

    def reading_time(self, wpm):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        # Returns:
        #   An integer representing an estimate of the reading time in minutes
        #   for the contents at the given wpm.
        pass

    def reading_chunk(self, wpm, minutes):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   A string representing a chunk of the contents that the user could
        #   read in the given number of minutes.
        # If called again, `reading_chunk` should return the next chunk,
        # skipping what has already been read, until the contents is fully read.
        # The next call after that it should restart from the beginning.
        pass
```


## Challenge

Test-drive a class system based on this design:

```python
# File: lib/todo_list.py
class TodoList:
    def __init__(self):
        pass

    def add(self, todo):
        # Parameters:
        #   todo: an instance of Todo
        # Returns:
        #   Nothing
        # Side-effects:
        #   Adds the todo to the list of todos
        pass
      
    def incomplete(self):
        # Returns:
        #   A list of Todo instances representing the todos that are not complete
        pass

    def complete(self):
        # Returns:
        #   A list of Todo instances representing the todos that are complete
        pass

    def give_up(self):
        # Returns:
        #   Nothing
        # Side-effects:
        #   Marks all todos as complete
        pass


# File: lib/todo.py
class Todo:
    # Public Properties:
    #   task: a string representing the task to be done
    #   complete: a boolean representing whether the task is complete

    def __init__(self, task):
        # Parameters:
        #   task: a string representing the task to be done
        # Side-effects:
        #   Sets the task property
        #   Sets the complete property to False
        pass

    def mark_complete(self):
        # Returns:
        #   Nothing
        # Side-effects:
        #   Sets the complete property to True
        pass
```