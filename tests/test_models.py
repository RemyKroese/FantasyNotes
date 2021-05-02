import src.models as m
import datetime
import pytest

TEST_CURRENT_TIME = datetime.datetime.now()
TEST_NOTE_TEXT = 'my note'


@pytest.mark.parametrize('note_tags, requested_tag', [
    (['tag1'], 'tag1'),
    (['tag1', 'tag2'], 'tag1'),
    (['tag1', 'tag2'], 'tag2')])
def test_note_has_tag(note_tags, requested_tag):
    new_note = m.Note(TEST_NOTE_TEXT, TEST_CURRENT_TIME, note_tags)
    assert new_note.has_tag(requested_tag)


@pytest.mark.parametrize('note_tags, requested_tag', [
    (['tag1'], 'tag2'),
    (['tag1', 'tag2'], 'tag3')])
def test_note_does_not_have_tag(note_tags, requested_tag):
    new_note = m.Note(TEST_NOTE_TEXT, TEST_CURRENT_TIME, note_tags)
    assert not new_note.has_tag(requested_tag)
