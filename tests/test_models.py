import backend.models as m
from datetime import datetime
import pytest


####################################################################################################
#                                                                                                  #
#                                      Campaign unit tests                                         #
#                                                                                                  #
####################################################################################################

TEST_CAMPAIGN_NAME = 'my campaign'


def test_can_edit_campaign_name():
    TEST_NAME = 'new_name'
    campaign = m.Campaign(name=TEST_CAMPAIGN_NAME)
    campaign.edit_name(TEST_NAME)
    assert campaign.name == TEST_NAME


TEST_CHAR_1 = m.Character(name='char 1')
TEST_CHAR_2 = m.Character(name='char 2')
TEST_CHAR_3 = m.Character(name='new char 1')
TEST_CHAR_4 = m.Character(name='existing char 1')


@pytest.mark.parametrize('new_chars, existing_chars, expected_chars_list', [
    ([TEST_CHAR_1], [], [TEST_CHAR_1]),
    ([TEST_CHAR_1, TEST_CHAR_2], [], [TEST_CHAR_1, TEST_CHAR_2]),
    ([TEST_CHAR_3], [TEST_CHAR_4], [TEST_CHAR_4, TEST_CHAR_3])])
def test_can_add_characters_to_campaign(new_chars, existing_chars, expected_chars_list):
    campaign = m.Campaign(TEST_CAMPAIGN_NAME, characters=existing_chars)
    for char in new_chars:
        campaign.add_character(char)
    for i in range(len(campaign.characters)):
        assert campaign.characters[i] == expected_chars_list[i]


@pytest.mark.parametrize('removed_chars, existing_chars, expected_chars_list', [
    ([TEST_CHAR_1], [TEST_CHAR_1], []),
    ([TEST_CHAR_1], [TEST_CHAR_1, TEST_CHAR_2], [TEST_CHAR_2]),
    ([TEST_CHAR_3, TEST_CHAR_1],  [TEST_CHAR_1, TEST_CHAR_2, TEST_CHAR_3, TEST_CHAR_4],
     [TEST_CHAR_2, TEST_CHAR_4])])
def test_can_remove_characters_from_campaign(removed_chars, existing_chars, expected_chars_list):
    campaign = m.Campaign(TEST_CAMPAIGN_NAME, characters=existing_chars)
    for char in removed_chars:
        campaign.remove_character(char)
    for i in range(len(campaign.characters)):
        assert campaign.characters[i] == expected_chars_list[i]


TEST_LOC_1 = m.Location(name='loc 1')
TEST_LOC_2 = m.Location(name='loc 2')
TEST_LOC_3 = m.Location(name='new loc 1')
TEST_LOC_4 = m.Location(name='existing loc 1')


@pytest.mark.parametrize('new_locs, existing_locs, expected_locs_list', [
    ([TEST_LOC_1], [], [TEST_LOC_1]),
    ([TEST_LOC_1, TEST_LOC_2], [], [TEST_LOC_1, TEST_LOC_2]),
    ([TEST_LOC_3], [TEST_LOC_4], [TEST_LOC_4, TEST_LOC_3])])
def test_can_add_locations_to_campaign(new_locs, existing_locs, expected_locs_list):
    campaign = m.Campaign(TEST_CAMPAIGN_NAME, locations=existing_locs)
    for loc in new_locs:
        campaign.add_location(loc)
    for i in range(len(campaign.locations)):
        assert campaign.locations[i] == expected_locs_list[i]


@pytest.mark.parametrize('removed_locs, existing_locs, expected_locs_list', [
    ([TEST_LOC_1], [TEST_LOC_1], []),
    ([TEST_LOC_1], [TEST_LOC_1, TEST_LOC_2], [TEST_LOC_2]),
    ([TEST_LOC_3, TEST_LOC_1],  [TEST_LOC_1, TEST_LOC_2, TEST_LOC_3, TEST_LOC_4],
     [TEST_LOC_2, TEST_LOC_4])])
def test_can_remove_locations_from_campaign(removed_locs, existing_locs, expected_locs_list):
    campaign = m.Campaign(TEST_CAMPAIGN_NAME, locations=existing_locs)
    for loc in removed_locs:
        campaign.remove_location(loc)
    for i in range(len(campaign.locations)):
        assert campaign.locations[i] == expected_locs_list[i]


TEST_CRE_1 = m.Creature(species='cre 1')
TEST_CRE_2 = m.Creature(species='cre 2')
TEST_CRE_3 = m.Creature(species='new cre 1')
TEST_CRE_4 = m.Creature(species='existing cre 1')


@pytest.mark.parametrize('new_cres, existing_cres, expected_cres_list', [
    ([TEST_CRE_1], [], [TEST_CRE_1]),
    ([TEST_CRE_1, TEST_CRE_2], [], [TEST_CRE_1, TEST_CRE_2]),
    ([TEST_CRE_3], [TEST_CRE_4], [TEST_CRE_4, TEST_CRE_3])])
def test_can_add_creatures_to_campaign(new_cres, existing_cres, expected_cres_list):
    campaign = m.Campaign(TEST_CAMPAIGN_NAME, creatures=existing_cres)
    for cre in new_cres:
        campaign.add_creature(cre)
    for i in range(len(campaign.creatures)):
        assert campaign.creatures[i] == expected_cres_list[i]


@pytest.mark.parametrize('removed_cres, existing_cres, expected_cres_list', [
    ([TEST_CRE_1], [TEST_CRE_1], []),
    ([TEST_CRE_1], [TEST_CRE_1, TEST_CRE_2], [TEST_CRE_2]),
    ([TEST_CRE_3, TEST_CRE_1],  [TEST_CRE_1, TEST_CRE_2, TEST_CRE_3, TEST_CRE_4],
     [TEST_CRE_2, TEST_CRE_4])])
def test_can_remove_remove_creatures_from_campaign(removed_cres, existing_cres, expected_cres_list):
    campaign = m.Campaign(TEST_CAMPAIGN_NAME, creatures=existing_cres)
    for cre in removed_cres:
        campaign.remove_creature(cre)
    for i in range(len(campaign.creatures)):
        assert campaign.creatures[i] == expected_cres_list[i]


TEST_QUEST_1 = m.Quest(giver='quest 1')
TEST_QUEST_2 = m.Quest(giver='quest 2')
TEST_QUEST_3 = m.Quest(giver='new quest 1')
TEST_QUEST_4 = m.Quest(giver='existing quest 1')


@pytest.mark.parametrize('new_quests, existing_quests, expected_quests_list', [
    ([TEST_QUEST_1], [], [TEST_QUEST_1]),
    ([TEST_QUEST_1, TEST_QUEST_2], [], [TEST_QUEST_1, TEST_QUEST_2]),
    ([TEST_QUEST_3], [TEST_QUEST_4], [TEST_QUEST_4, TEST_QUEST_3])])
def test_can_add_quests_to_campaign(new_quests, existing_quests, expected_quests_list):
    campaign = m.Campaign(TEST_CAMPAIGN_NAME, quests=existing_quests)
    for quest in new_quests:
        campaign.add_quest(quest)
    for i in range(len(campaign.quests)):
        assert campaign.quests[i] == expected_quests_list[i]


@pytest.mark.parametrize('removed_quests, existing_quests, expected_quests_list', [
    ([TEST_QUEST_1], [TEST_QUEST_1], []),
    ([TEST_QUEST_1], [TEST_QUEST_1, TEST_QUEST_2], [TEST_QUEST_2]),
    ([TEST_QUEST_3, TEST_QUEST_1],  [TEST_QUEST_1, TEST_QUEST_2, TEST_QUEST_3, TEST_QUEST_4],
     [TEST_QUEST_2, TEST_QUEST_4])])
def test_can_remove_remove_quests_from_campaign(removed_quests, existing_quests,
                                                expected_quests_list):
    campaign = m.Campaign(TEST_CAMPAIGN_NAME, quests=existing_quests)
    for quest in removed_quests:
        campaign.remove_quest(quest)
    for i in range(len(campaign.quests)):
        assert campaign.quests[i] == expected_quests_list[i]


TEST_ITEM_1 = m.Item(name='item 1')
TEST_ITEM_2 = m.Item(name='item 2')
TEST_ITEM_3 = m.Item(name='new item 1')
TEST_ITEM_4 = m.Item(name='existing item 1')


@pytest.mark.parametrize('new_items, existing_items, expected_items_list', [
    ([TEST_ITEM_1], [], [TEST_ITEM_1]),
    ([TEST_ITEM_1, TEST_ITEM_2], [], [TEST_ITEM_1, TEST_ITEM_2]),
    ([TEST_ITEM_3], [TEST_ITEM_4], [TEST_ITEM_4, TEST_ITEM_3])])
def test_can_add_items_to_campaign(new_items, existing_items, expected_items_list):
    campaign = m.Campaign(TEST_CAMPAIGN_NAME, items=existing_items)
    for item in new_items:
        campaign.add_item(item)
    for i in range(len(campaign.items)):
        assert campaign.items[i] == expected_items_list[i]


@pytest.mark.parametrize('removed_items, existing_items, expected_items_list', [
    ([TEST_ITEM_1], [TEST_ITEM_1], []),
    ([TEST_ITEM_1], [TEST_ITEM_1, TEST_ITEM_2], [TEST_ITEM_2]),
    ([TEST_ITEM_3, TEST_ITEM_1],  [TEST_ITEM_1, TEST_ITEM_2, TEST_ITEM_3, TEST_ITEM_4],
     [TEST_ITEM_2, TEST_ITEM_4])])
def test_can_remove_remove_items_from_campaign(removed_items, existing_items, expected_items_list):
    campaign = m.Campaign(TEST_CAMPAIGN_NAME, items=existing_items)
    for item in removed_items:
        campaign.remove_item(item)
    for i in range(len(campaign.items)):
        assert campaign.items[i] == expected_items_list[i]


TEST_NOTE_1 = m.Note(text='note 1', tags=['Tag1', 'Tag_ALL'])
TEST_NOTE_2 = m.Note(text='note 2', tags=['Tag2', 'Tag_ALL'])
TEST_NOTE_3 = m.Note(text='new note 1', tags=['Tag1', 'Tag2', 'Tag_ALL'])
TEST_NOTE_4 = m.Note(text='existing note 1')


@pytest.mark.parametrize('new_notes, existing_notes, expected_notes_list', [
    ([TEST_NOTE_1], [], [TEST_NOTE_1]),
    ([TEST_NOTE_1, TEST_NOTE_2], [], [TEST_NOTE_1, TEST_NOTE_2]),
    ([TEST_NOTE_3], [TEST_NOTE_4], [TEST_NOTE_4, TEST_NOTE_3])])
def test_can_add_notes_to_campaign(new_notes, existing_notes, expected_notes_list):
    campaign = m.Campaign(TEST_CAMPAIGN_NAME, notes=existing_notes)
    for note in new_notes:
        campaign.add_note(note)
    for i in range(len(campaign.notes)):
        assert campaign.notes[i] == expected_notes_list[i]


@pytest.mark.parametrize('removed_notes, existing_notes, expected_notes_list', [
    ([TEST_NOTE_1], [TEST_NOTE_1], []),
    ([TEST_NOTE_1], [TEST_NOTE_1, TEST_NOTE_2], [TEST_NOTE_2]),
    ([TEST_NOTE_3, TEST_NOTE_1],  [TEST_NOTE_1, TEST_NOTE_2, TEST_NOTE_3, TEST_NOTE_4],
     [TEST_NOTE_2, TEST_NOTE_4])])
def test_can_remove_notes_from_campaign(removed_notes, existing_notes, expected_notes_list):
    campaign = m.Campaign(TEST_CAMPAIGN_NAME, notes=existing_notes)
    for note in removed_notes:
        campaign.remove_note(note)
    for i in range(len(campaign.notes)):
        assert campaign.notes[i] == expected_notes_list[i]


@pytest.mark.parametrize('tag, existing_notes, expected_notes_list', [
    ('Tag1', [TEST_NOTE_1], [TEST_NOTE_1]),
    ('Tag1', [TEST_NOTE_2], []),
    ('Tag2', [TEST_NOTE_1, TEST_NOTE_2], [TEST_NOTE_2]),
    ('Tag1', [TEST_NOTE_1, TEST_NOTE_2, TEST_NOTE_3], [TEST_NOTE_1, TEST_NOTE_3]),
    ('Tag2', [TEST_NOTE_1, TEST_NOTE_2, TEST_NOTE_3], [TEST_NOTE_2, TEST_NOTE_3]),
    ('Tag4', [TEST_NOTE_1, TEST_NOTE_2, TEST_NOTE_3], []),
    ('Tag_ALL', [TEST_NOTE_1, TEST_NOTE_2, TEST_NOTE_3], [TEST_NOTE_1, TEST_NOTE_2, TEST_NOTE_3])])
def test_can_filter_notes_from_campaign(tag, existing_notes, expected_notes_list):
    campaign = m.Campaign(TEST_CAMPAIGN_NAME, notes=existing_notes)
    filtered_notes = campaign.filter_notes(tag)
    assert filtered_notes == expected_notes_list


####################################################################################################
#                                                                                                  #
#                                      Notes unit tests                                            #
#                                                                                                  #
####################################################################################################

TEST_CURRENT_TIME = datetime.now()
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


####################################################################################################
#                                                                                                  #
#                                      Character unit tests                                        #
#                                                                                                  #
####################################################################################################

def test_can_edit_character_name():
    TEST_NAME = 'new_name'
    character = m.Character(name='my character')
    character.edit_name(TEST_NAME)
    assert character.name == TEST_NAME


def test_can_edit_character_species():
    TEST_SPECIES = 'Dwarf'
    character = m.Character(species='Human')
    character.edit_species(TEST_SPECIES)
    assert character.species == TEST_SPECIES


def test_can_edit_character_class():
    TEST_CLASS = 'Rogue'
    character = m.Character(c_class='Fighter')
    character.edit_class(TEST_CLASS)
    assert character.c_class == TEST_CLASS


def test_can_edit_character_alignment():
    TEST_ALIGNMENT = 'Evil'
    character = m.Character(alignment='Good')
    character.edit_alignment(TEST_ALIGNMENT)
    assert character.alignment == TEST_ALIGNMENT


def test_can_edit_character_profession():
    TEST_PROFESSION = 'Smith'
    character = m.Character(profession='Adventurer')
    character.edit_profession(TEST_PROFESSION)
    assert character.profession == TEST_PROFESSION


@pytest.mark.parametrize('new_abilities, existing_abilities, expected_abilities_list', [
    (['a1'], [], ['a1']),
    (['a1', 'a2'], [], ['a1', 'a2']),
    (['a3'], ['a4'], ['a4', 'a3'])])
def test_can_add_abilities_to_character(new_abilities, existing_abilities,
                                        expected_abilities_list):
    character = m.Character(abilities=existing_abilities)
    for ability in new_abilities:
        character.add_ability(ability)
    for i in range(len(character.abilities)):
        assert character.abilities[i] == expected_abilities_list[i]


@pytest.mark.parametrize('removed_abilities, existing_abilities, expected_abilities_list', [
    (['a1'], ['a1'], []),
    (['a1'], ['a1', 'a2'], ['a2']),
    (['a3', 'a1'],  ['a1', 'a2', 'a3', 'a4'], ['a2', 'a4'])])
def test_can_remove_abilities_from_character(removed_abilities, existing_abilities,
                                             expected_abilities_list):
    character = m.Character(abilities=existing_abilities)
    for ability in removed_abilities:
        character.remove_ability(ability)
    for i in range(len(character.abilities)):
        assert character.abilities[i] == expected_abilities_list[i]


@pytest.mark.parametrize('new_possessions, existing_possessions, expected_possessions_list', [
    (['i1'], [], ['i1']),
    (['i1', 'i2'], [], ['i1', 'i2']),
    (['i3'], ['i4'], ['i4', 'i3'])])
def test_can_add_possessions_to_character(new_possessions, existing_possessions,
                                          expected_possessions_list):
    character = m.Character(possessions=existing_possessions)
    for possession in new_possessions:
        character.add_possession(possession)
    for i in range(len(character.possessions)):
        assert character.possessions[i] == expected_possessions_list[i]


@pytest.mark.parametrize('removed_possessions, existing_possessions, expected_possessions_list', [
    (['i1'], ['i1'], []),
    (['i1'], ['i1', 'i2'], ['i2']),
    (['i3', 'i1'],  ['i1', 'i2', 'i3', 'i4'], ['i2', 'i4'])])
def test_can_remove_possessions_from_character(removed_possessions, existing_possessions,
                                               expected_possessions_list):
    character = m.Character(possessions=existing_possessions)
    for possession in removed_possessions:
        character.remove_possession(possession)
    for i in range(len(character.possessions)):
        assert character.possessions[i] == expected_possessions_list[i]


def test_can_edit_character_is_playable_status():
    character = m.Character(is_playable=False)
    character.set_is_playable(True)
    assert character.is_playable is True
    character.set_is_playable(False)
    assert character.is_playable is False


def test_can_edit_character_is_alive_status():
    character = m.Character(is_alive=False)
    character.set_is_alive(True)
    assert character.is_alive is True
    character.set_is_alive(False)
    assert character.is_alive is False


####################################################################################################
#                                                                                                  #
#                                      Creature unit tests                                         #
#                                                                                                  #
####################################################################################################

def test_can_edit_creature_species():
    TEST_SPECIES = 'Rat'
    creature = m.Creature(species='Skeleton')
    creature.edit_species(TEST_SPECIES)
    assert creature.species == TEST_SPECIES


def test_can_edit_creature_agressiveness():
    TEST_AGRESSIVENESS = 'Agressive'
    creature = m.Creature(agressiveness='Neutral')
    creature.edit_agressiveness(TEST_AGRESSIVENESS)
    assert creature.agressiveness == TEST_AGRESSIVENESS


@pytest.mark.parametrize('new_attacks, existing_attacks, expected_attacks_list', [
    (['a1'], [], ['a1']),
    (['a1', 'a2'], [], ['a1', 'a2']),
    (['a3'], ['a4'], ['a4', 'a3'])])
def test_can_add_attacks_to_creature(new_attacks, existing_attacks, expected_attacks_list):
    creature = m.Creature(attacks=existing_attacks)
    for attack in new_attacks:
        creature.add_attack(attack)
    for i in range(len(creature.attacks)):
        assert creature.attacks[i] == expected_attacks_list[i]


@pytest.mark.parametrize('removed_attacks, existing_attacks, expected_attacks_list', [
    (['a1'], ['a1'], []),
    (['a1'], ['a1', 'a2'], ['a2']),
    (['a3', 'a1'],  ['a1', 'a2', 'a3', 'a4'], ['a2', 'a4'])])
def test_can_remove_attacks_from_creature(removed_attacks, existing_attacks, expected_attacks_list):
    creature = m.Creature(attacks=existing_attacks)
    for attack in removed_attacks:
        creature.remove_attack(attack)
    for i in range(len(creature.attacks)):
        assert creature.attacks[i] == expected_attacks_list[i]


@pytest.mark.parametrize('new_resistances, existing_resistances, expected_resistances_list', [
    (['r1'], [], ['r1']),
    (['r1', 'r2'], [], ['r1', 'r2']),
    (['r3'], ['r4'], ['r4', 'r3'])])
def test_can_add_resistances_to_creature(new_resistances, existing_resistances,
                                         expected_resistances_list):
    creature = m.Creature(resistances=existing_resistances)
    for resistance in new_resistances:
        creature.add_resistance(resistance)
    for i in range(len(creature.resistances)):
        assert creature.resistances[i] == expected_resistances_list[i]


@pytest.mark.parametrize('removed_resistances, existing_resistances, expected_resistances_list', [
    (['r1'], ['r1'], []),
    (['r1'], ['r1', 'r2'], ['r2']),
    (['r3', 'r1'],  ['r1', 'r2', 'r3', 'r4'], ['r2', 'r4'])])
def test_can_remove_resistances_from_creature(removed_resistances, existing_resistances,
                                              expected_resistances_list):
    creature = m.Creature(resistances=existing_resistances)
    for resistance in removed_resistances:
        creature.remove_resistance(resistance)
    for i in range(len(creature.resistances)):
        assert creature.resistances[i] == expected_resistances_list[i]


@pytest.mark.parametrize('new_immunities, existing_immunities, expected_immunities_list', [
    (['i1'], [], ['i1']),
    (['i1', 'i2'], [], ['i1', 'i2']),
    (['i3'], ['i4'], ['i4', 'i3'])])
def test_can_add_immunities_to_character(new_immunities, existing_immunities,
                                         expected_immunities_list):
    creature = m.Creature(immunities=existing_immunities)
    for immunity in new_immunities:
        creature.add_immunity(immunity)
    for i in range(len(creature.immunities)):
        assert creature.immunities[i] == expected_immunities_list[i]


@pytest.mark.parametrize('removed_immunities, existing_immunities, expected_immunities_list', [
    (['i1'], ['i1'], []),
    (['i1'], ['i1', 'i2'], ['i2']),
    (['i3', 'i1'],  ['i1', 'i2', 'i3', 'i4'], ['i2', 'i4'])])
def test_can_remove_immunities_from_character(removed_immunities, existing_immunities,
                                              expected_immunities_list):
    creature = m.Creature(immunities=existing_immunities)
    for immunity in removed_immunities:
        creature.remove_immunity(immunity)
    for i in range(len(creature.immunities)):
        assert creature.immunities[i] == expected_immunities_list[i]


####################################################################################################
#                                                                                                  #
#                                      Item unit tests                                             #
#                                                                                                  #
####################################################################################################

def test_can_edit_item_name():
    TEST_NAME = 'Neverwinter'
    item = m.Item(name='Waterdeep')
    item.edit_name(TEST_NAME)
    assert item.name == TEST_NAME


def test_can_edit_item_type():
    TEST_TYPE = 'Bow'
    item = m.Item(i_type='Sword')
    item.edit_type(TEST_TYPE)
    assert item.type == TEST_TYPE


@pytest.mark.parametrize('new_stats, existing_stats, expected_stats_list', [
    (['s1'], [], ['s1']),
    (['s1', 's2'], [], ['s1', 's2']),
    (['s3'], ['s4'], ['s4', 's3'])])
def test_can_add_stats_to_item(new_stats, existing_stats, expected_stats_list):
    item = m.Item(stats=existing_stats)
    for stat in new_stats:
        item.add_stat(stat)
    for i in range(len(item.stats)):
        assert item.stats[i] == expected_stats_list[i]


@pytest.mark.parametrize('removed_stats, existing_stats, expected_stats_list', [
    (['s1'], ['s1'], []),
    (['s1'], ['s1', 's2'], ['s2']),
    (['s3', 's1'],  ['s1', 's2', 's3', 's4'], ['s2', 's4'])])
def test_can_remove_stats_from_item(removed_stats, existing_stats, expected_stats_list):
    item = m.Item(stats=existing_stats)
    for stat in removed_stats:
        item.remove_stat(stat)
    for i in range(len(item.stats)):
        assert item.stats[i] == expected_stats_list[i]


def test_can_edit_item_is_magical_status():
    item = m.Item(is_magical=False)
    item.set_is_magical(True)
    assert item.is_magical is True
    item.set_is_magical(False)
    assert item.is_magical is False


def test_can_edit_item_is_cursed_status():
    item = m.Item(is_cursed=False)
    item.set_is_cursed(True)
    assert item.is_cursed is True
    item.set_is_cursed(False)
    assert item.is_cursed is False


####################################################################################################
#                                                                                                  #
#                                      Location unit tests                                         #
#                                                                                                  #
####################################################################################################

def test_can_edit_location_name():
    TEST_NAME = 'Neverwinter'
    location = m.Location(name='Waterdeep')
    location.edit_name(TEST_NAME)
    assert location.name == TEST_NAME


def test_can_edit_location_type():
    TEST_TYPE = 'Town'
    location = m.Location(l_type='City')
    location.edit_type(TEST_TYPE)
    assert location.type == TEST_TYPE


####################################################################################################
#                                                                                                  #
#                                      Quest unit tests                                            #
#                                                                                                  #
####################################################################################################

def test_can_edit_quest_giver():
    TEST_GIVER = 'Jon Snow'
    quest = m.Quest(giver='Legolas')
    quest.edit_giver(TEST_GIVER)
    assert quest.giver == TEST_GIVER


def test_can_edit_quest_objective():
    TEST_OBJECTIVE = 'Kill a dragon'
    quest = m.Quest(objective='Kill a witch')
    quest.edit_objective(TEST_OBJECTIVE)
    assert quest.objective == TEST_OBJECTIVE


def test_can_edit_quest_previous_quest():
    TEST_QUEST_1 = m.Quest(objective='Kill a witch')
    TEST_QUEST_2 = m.Quest(objective='Find the red dragon')
    quest = m.Quest(previous_quest=TEST_QUEST_1)
    quest.edit_previous_quest(TEST_QUEST_2)
    assert quest.previous_quest == TEST_QUEST_2


def test_can_edit_quest_target_location():
    TEST_TARGET_LOCATION = 'Mountains'
    quest = m.Quest(target_location='Forest')
    quest.edit_target_location(TEST_TARGET_LOCATION)
    assert quest.target_location == TEST_TARGET_LOCATION


def test_can_edit_quest_reward():
    TEST_REWARD = '100 gold'
    quest = m.Quest(reward='50 gold')
    quest.edit_reward(TEST_REWARD)
    assert quest.reward == TEST_REWARD


def test_can_edit_quest_is_completed_status():
    quest = m.Quest(is_completed=False)
    quest.set_is_completed(True)
    assert quest.is_completed is True
    quest.set_is_completed(False)
    assert quest.is_completed is False
