import os
import datetime
import json
from types import SimpleNamespace
import backend.models as m


class Notebook:
    def __init__(self):
        self.campaigns = []
        self.current_campaign = None

    def add_campaign(self, name):
        self.campaigns.append(m.Campaign(name))

    def open_campaign(self, campaign):
        self.current_campaign = campaign


def save_campaign_data(campaign):
    if not os.path.exists('saves'):
        os.makedirs('saves')
    file_path = 'saves/' + str(campaign.name) + '.json'
    with open(file_path, 'w') as write_file:
        json.dump(campaign.data(), write_file, cls=ComplexEncoder, indent=4)


def load_campaign_data(file_path):
    with open(file_path, 'r') as file:
        j = json.load(file)
        characters = [m.Character(**character) for character in j['characters']]
        locations = [m.Location(**location) for location in j['locations']]
        creatures = [m.Creature(**creature) for creature in j['creatures']]
        quests = [m.Quest(**quest) for quest in j['quests']]
        items = [m.Item(**item) for item in j['items']]
        notes = load_notes_data(j['notes'])
        return m.Campaign(j['name'], characters, locations, creatures, quests, items, notes)


def load_notes_data(notes_dict):
    notes = []
    for note in notes_dict:
        timestamp = datetime.datetime.strptime(note['timestamp'], '%Y-%m-%dT%H:%M:%S')
        notes.append(m.Note(note['text'], timestamp, note['tags']))
    return notes


class ComplexEncoder(json.JSONEncoder):
    def default(self, obj):
        if hasattr(obj, 'data'):
            return obj.data()
        elif isinstance(obj, (datetime.date, datetime.datetime)):
            return obj.isoformat()
        else:
            return json.JSONEncoder.default(self, obj)


if __name__ == "__main__":
    campaign = m.Campaign('campaign_1', notes=[
        m.Note(text='new note 1', tags=['Tag1', 'Tag2', 'Tag_ALL']),
        m.Note(text='note 2', tags=['Tag2', 'Tag_ALL'])])
    save_campaign_data(campaign)
    print('Hello World')
