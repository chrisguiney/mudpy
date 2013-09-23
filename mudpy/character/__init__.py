from functools import partial

from .. import races
from .. import classes
from ..magic import SpellBook


class Character(object):

    def __init__(self, name, description, equipment, inventory, attributes, level=1, race="Human", base_class="Fighter",
                 spellbook=None):
        """

        @param name: Name of Character
        @type name: str

        @param description: Description of Character
        @type description: str
        
        @param equipment: Dictionary of item slot to equipped item
        @type equipment: dict
        
        @param inventory: List of items
        @type inventory: list of item

        @param attributes: Dictionary of attributes to values
        @type attributes: dict

        @param level: Integer level number
        @type level: int

        @param race: Name of race as string
        @type race: str

        @param base_class: Name of base character class as string
        @type base_class: str

        @param spellbook: Spellbook object of memorized spells
        @type spellbook: SpellBook
        @return: None
        """
        self.name = name
        self.level = level
        self.description = description
        self.attributes = attributes

        self.equipment = equipment
        self.inventory = inventory

        self.race = getattr(races, race, partial(races.raise_invalid_race, race))()
        self.base_class = getattr(classes, base_class)()

        self.spellbook = spellbook

        if self.base_class.is_caster and spellbook is None:
            self.spellbook = SpellBook()

    def cast(self, spell, on_target):
        return (spell.base_damage.roll() + spell.level_modifier(self.level)) - on_target.resistance(spell.damage_type)

    def resistance(self, damage_type):
        pass

    def equip(self, item):
        assert(item in self.inventory)
        self.equipment[item.slot] = item