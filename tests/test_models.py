import backend.models as m
from datetime import datetime
import pytest

TEST_CAMPAIGN_NAME = 'my campaign'
TEST_CURRENT_TIME = datetime.now()
TEST_NOTE_TEXT = 'my note'
TEST_NOTE_1 = m.Note('note 1')
TEST_NOTE_2 = m.Note('note 2')
TEST_NOTE_3 = m.Note('new note 1')
TEST_NOTE_4 = m.Note('existing note 1')


@pytest.mark.parametrize('new_notes, existing_notes, expected_notes_list', [
    ([TEST_NOTE_1], [], [TEST_NOTE_1]),
    ([TEST_NOTE_1, TEST_NOTE_2], [], [TEST_NOTE_1, TEST_NOTE_2]),
    ([TEST_NOTE_3], [TEST_NOTE_4], [TEST_NOTE_4, TEST_NOTE_3])])
def test_add_notes_to_campaign(new_notes, existing_notes, expected_notes_list):
    campaign = m.Campaign(TEST_CAMPAIGN_NAME, notes=existing_notes)
    for note in new_notes:
        campaign.add_note(note)
    for i in range(len(campaign.notes)):
        assert campaign.notes[i] == expected_notes_list[i]


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
