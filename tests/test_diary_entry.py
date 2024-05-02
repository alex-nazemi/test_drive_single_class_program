from lib.DiaryEntry import DiaryEntry
import pytest

def test_diary_entry_format():
    diary_entry = DiaryEntry("My title", "Some contents")
    result = diary_entry.format()
    assert result == "My title: Some contents"

def test_count_words():
    diary_entry = DiaryEntry("My title", "Some contents")
    result = diary_entry.count_words()
    assert result == 4

def test_reading_time():
    diary_entry = DiaryEntry("My title", "Some contents")
    result = diary_entry.reading_time(1)
    assert result == 4

def test_reading_chunks():
    diary_entry = DiaryEntry("My title", "one two three four five six")
    result = diary_entry.reading_chunk(2, 1)
    assert result == "one two"

def test_raise_error_if_no_title_content_given():
    with pytest.raises(Exception) as err:
        diary_entry = DiaryEntry("", "")
    
    assert str(err.value) == "Empty title and content!" 






