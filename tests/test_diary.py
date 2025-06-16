from lib.diary import *
"""
Given a title and contents 
#format returns a string, like: 
"My title: The contents of my diary"
"""

def test_given_title_contents_returns_formated_string():
    diary_entry = DiaryEntry("My title", "Some contents")
    result = diary_entry.format()
    assert result == "My title: Some contents"

"""
Given a diary entry 
#count_words returns the number of words in the title and contents
"""

def test_given_diary_entry_count_words_title_contents():
    diary_entry = DiaryEntry("My title ", "Some contents")
    result = diary_entry.count_words()
    assert result == 4
    
"""
Given a wpm of 2
And a text with two words 
#reading_time returns 1 minute 
"""

def test_reading_time_with_two_wpm_and_two_words():
    diary_entry = DiaryEntry("My title ", "Some contents")
    result = diary_entry.reading_time(2)
    assert result == 1

"""
Given a wpm of 2
And a text with 6 words 
#reading_time returns 3 minutes
"""

def test_reading_time_with_2_wpm_and_six_words():
    diary_entry = DiaryEntry("My title ", "one, two, three, four, five, six")
    result = diary_entry.reading_time(2)
    assert result == 3

"""
Given wpm and minutes, calculate how much a user can read based on those numbers
and return them a snippet of text that equates to that 
"""

def test_take_wpm_and_minutes_and_provide_chunk_text_that_equals_that():
    entry = DiaryEntry("My Title", "one two three four five six")
    result = entry.reading_chunk(2, 1)  # 2 wpm * 1 minute = 2 words
    assert result == "one two"
    
def test_reading_chunk_returns_next_chunk():
    entry = DiaryEntry("My Title", "one two three four five six")
    entry.reading_chunk(2, 1)  # reads "one two"
    result = entry.reading_chunk(2, 1)  # next 2 words
    assert result == "three four"

def test_reading_chunk_wraps_to_start():
    entry = DiaryEntry("My Title", "one two three four")
    entry.reading_chunk(2, 1)  # "one two"
    entry.reading_chunk(2, 1)  # "three four"
    result = entry.reading_chunk(2, 1)  # should wrap: "one two" again
    assert result == "one two"
