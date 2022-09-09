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

    def edit_name(self, name):
        self.name = name

    def edit_species(self, species):
        self.species = species

    def edit_class(self, c_class):
        self.c_class = c_class

    def edit_alignment(self, alignment):
        self.alignment = alignment

    def edit_profession(self, profession):
        self.profession = profession

    def add_ability(self, ability):
        self.abilities.append(ability)

    def remove_ability(self, ability):
        self.abilities.remove(ability)

    def add_possession(self, possession):
        self.possessions.append(possession)

    def remove_possession(self, possession):
        self.possessions.remove(possession)

    def set_is_playable(self, is_playable):
        self.is_playable = is_playable

    def set_is_alive(self, is_alive):
        self.is_alive = is_alive


class Creature:
    def __init__(self, species='', agressiveness='', attacks=[], resistances=[], immunities=[]):
        self.species = species
        self.agressiveness = agressiveness
        self.attacks = attacks
        self.resistances = resistances
        self.immunities = immunities
        self.tag = {'type': type(self), 'name': self.name}

    def edit_species(self, species):
        self.species = species

    def edit_agressiveness(self, agressiveness):
        self.agressiveness = agressiveness

    def add_attack(self, attack):
        self.attacks.append(attack)

    def remove_attack(self, attack):
        self.attacks.remove(attack)

    def add_resistance(self, resistance):
        self.resistances.append(resistance)

    def remove_resistance(self, resistance):
        self.resistances.remove(resistance)

    def add_immunity(self, immunity):
        self.immunities.append(immunity)

    def remove_immunity(self, immunity):
        self.immunities.remove(immunity)


class Item:
    def __init__(self, name='', type='', stats=[], is_magical=False, is_cursed=False):
        self.name = name
        self.type = type
        self.stats = stats
        self.is_magical = is_magical
        self.is_cursed = is_cursed
        self.tag = {'type': type(self), 'name': self.name}

    def edit_name(self, name):
        self.name = name

    def edit_type(self, type):
        self.type = type

    def add_stat(self, stat):
        self.stats.append(stat)

    def remove_stat(self, stat):
        self.stats.remove(stat)

    def set_is_magical(self, is_magical):
        self.is_magical = is_magical

    def set_is_cursed(self, is_cursed):
        self.is_cursed = is_cursed


class Location:
    def __init__(self, name='', type=''):
        self.name = name
        self.type = type
        self.tag = {'type': type(self), 'name': self.name}

    def edit_name(self, name):
        self.name = name

    def edit_type(self, type):
        self.type = type


class Quest:
    def __init__(self, giver='', previous_quest=None, objective='',
                 target_location='', reward='', is_completed=False):
        self.giver = giver
        self.previous_quest = previous_quest
        self.objective = objective
        self.target_location = target_location
        self.reward = reward
        self.is_completed = is_completed
        self.tag = {'type': type(self), 'name': self.giver}

    def edit_giver(self, giver):
        self.giver = giver

    def edit_previous_quest(self, previous_quest):
        self.previous_quest = previous_quest

    def edit_objective(self, objective):
        self.objective = objective

    def edit_target_location(self, target_location):
        self.target_location = target_location

    def edit_reward(self, reward):
        self.reward = reward

    def set_is_completed(self, is_completed):
        self.is_completed = is_completed
