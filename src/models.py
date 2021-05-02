class Campaign:
    def __init__(self, name, characters=[], locations=[], creatures=[], quests=[], notes=[]):
        self.name = name
        self.characters = characters
        self.locations = locations
        self.creatures = creatures
        self.quests = quests
        self.notes = notes


class Note:
    def __init__(self, text, timestamp, tags=[]):
        self.text = text
        self.timestamp = timestamp
        self.tags = tags

    def has_tag(self, tag):
        return tag in self.tags


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
