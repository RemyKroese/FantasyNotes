from datetime import datetime


class Campaign:
    def __init__(self, name, characters=[], locations=[], creatures=[], quests=[], notes=[]):
        self.name = name
        self.characters = characters
        self.locations = locations
        self.creatures = creatures
        self.quests = quests
        self.notes = notes

    def edit_name(self, new_name):
        self.name = new_name

    def add_character(self, character):
        self.characters.append(character)

    def remove_character(self, character):
        self.characters.remove(character)

    def add_location(self, location):
        self.locations.append(location)

    def remove_location(self, location):
        self.locations.remove(location)

    def add_creaturer(self, creature):
        self.creatures.append(creature)

    def remove_creature(self, creature):
        self.creatures.remove(creature)

    def add_quest(self, quest):
        self.quests.append(quest)

    def remove_quest(self, quest):
        self.quests.remove(quest)

    def add_note(self, note):
        self.notes.append(note)

    def remove_note(self, note):
        self.notes.remove(note)


class Note:
    def __init__(self, text, timestamp=datetime.now(), tags=[]):
        self.text = text
        self.timestamp = timestamp
        self.tags = tags

    def has_tag(self, tag):
        return tag in self.tags

    def edit(self, new_text, added_tags, removed_tags):
        self.text = new_text
        for tag in added_tags:
            self.tags.append(tag)
        for tag in removed_tags:
            self.tags.remove(tag)


class Character:
    def __init__(self, name='', species='', c_class='', alignment='', profession='',
                 abilities=[], possessions=[], is_playable=False, is_alive=True):
        self.name = name
        self.species = species
        self.c_class = c_class
        self.alignment = alignment
        self.profession = profession
        self.abilities = abilities
        self.possessions = possessions
        self.is_playable = is_playable
        self.is_alive = is_alive
        self.tag = {'type': type(self), 'name': self.name}


class Creature:
    def __init__(self, species='', agressiveness='', attacks=[], resistances=[], immunities=[]):
        self.species = species
        self.agressiveness = agressiveness
        self.attacks = attacks
        self.resistances = resistances
        self.immunities = immunities
        self.tag = {'type': type(self), 'name': self.name}


class Item:
    def __init__(self, name='', type='', stats='', is_magical=False, is_cursed=False):
        self.name = None
        self.type = None
        self.stats = None
        self.is_magical = None
        self.is_cursed = None
        self.tag = {'type': type(self), 'name': self.name}


class Location:
    def __init__(self, name='', location='', type=''):
        self.name = name
        self.location = location
        self.type = type
        self.tag = {'type': type(self), 'name': self.name}


class Quest:
    def __init__(self, giver='', previous_quest=None, goal='',
                 target_location='', reward='', is_completed=False):
        self.giver = giver
        self.previous_quest = previous_quest
        self.goal = goal
        self.target_location = target_location
        self.reward = None
        self.is_completed = None
        self.tag = {'type': type(self), 'name': self.giver}
