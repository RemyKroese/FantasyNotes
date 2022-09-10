from json import load
import os
import filecmp
from datetime import datetime
import backend.models as m
import backend.notebook as notebook

ASSETS = os.path.join(os.path.dirname(__file__), 'assets/')

####################################################################################################
#                                                                                                  #
#                                      Data persistence unit tests                                 #
#                                                                                                  #
####################################################################################################


character1 = m.Character(name='Jeremiah', species='Half-Elf', c_class='Rogue',
                         alignment='Chaotic Neutral', profession='Criminal',
                         abilities=['Uncanny Dodge', 'Fast Hands', 'Sneak Attack'],
                         possessions=['100 Gold', '3 Potion of Healing'],
                         is_playable=True, is_alive=True)
character2 = m.Character(name='Knurble Wobblebob', species='Gnome', c_class='Wizard',
                         alignment='Chaotic Good', profession='Sage',
                         abilities=['Arcane Recovery', 'Gnome Cunning'],
                         possessions=['10 Gold'],
                         is_playable=True, is_alive=True)

location1 = m.Location(name='Waterdeep', l_type='City')
location2 = m.Location(name='Phandalin', l_type='Town')

creature1 = m.Creature(species='Rat', agressiveness='Hostile',
                       attacks=['Bite', 'Scratch'],
                       resistances=['Piercing', 'Blunt'],
                       immunities=['Fire'])
creature2 = m.Creature(species='Demon', agressiveness='Hostile',
                       attacks=['Claw', 'Second Attack'],
                       resistances=['Slashing'],
                       immunities=['Fire', 'Thunder', 'Lightning'])

quest1 = m.Quest(giver='Arthur', previous_quest='Find the dragon\'s lair',
                 objective='Kill the dragon.',
                 target_location='Dragon\'s lair in the lost cave',
                 reward='100 Gold', is_completed=False)
quest2 = m.Quest(giver='Waterdeep\'s mayor', previous_quest=None,
                 objective='Provide security during the festival',
                 target_location='Waterdeep\'s city centre',
                 reward='100 Gold', is_completed=False)

item1 = m.Item(name='Lightbringer', i_type='magic weapon',
               stats=['+1 to attack rolls', '+1d6 bonus damage to undead'],
               is_magical=True, is_cursed=False)

item2 = m.Item(name='Dagger+1', i_type='Melee weapon',
               stats=['+1 to attack rolls', ],
               is_magical=False, is_cursed=False)

note1 = m.Note(text='Jeremiah comes from Waterdeep',
               timestamp=datetime.strptime('2022-09-10 00:00:00', '%Y-%m-%d %H:%M:%S'),
               tags=['Jeremiah', 'Waterdeep'])
note2 = m.Note(text='The dragon is near Neverwinter',
               timestamp=datetime.strptime('2022-09-10 00:00:00', '%Y-%m-%d %H:%M:%S'),
               tags=['Dragon', 'Neverwinter'])

campaign = m.Campaign(name='campaign_1', characters=[character1, character2],
                      locations=[location1, location2], creatures=[creature1, creature2],
                      quests=[quest1, quest2], items=[item1, item2], notes=[note1, note2])


def test_can_save_campaign_to_file():
    expected_result = ASSETS + 'expected_campaign_data.json'
    result_file_path = 'saves/campaign_1.json'
    if os.path.exists(result_file_path):
        os.remove(result_file_path)
    notebook.save_campaign_data(campaign)
    assert os.path.exists(result_file_path)
    assert filecmp.cmp(result_file_path, expected_result) is True


def test_can_load_campaign_from_file():
    result_file_path = ASSETS + 'expected_campaign_data.json'
    loaded_campaign = notebook.load_campaign_data(result_file_path)
    assert loaded_campaign.notes == campaign.notes
