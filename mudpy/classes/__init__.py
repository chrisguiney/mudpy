from ..magic import spells

__author__ = 'chris'

class BaseClass(object):
    is_caster = False

class Caster(BaseClass):
    is_caster = True

class Fighter(BaseClass):
    pass

class Monk(BaseClass):
    pass

class Ranger(Caster):
    pass

class Druid(Caster):
    pass

class Cleric(BaseClass):
    pass

class Wizard(Caster):
    spell_schedule = {}

class Sorceror(Caster):
    spell_schedule = {
        1: [spells.MagicMissle, spells.Grease]
    }

class Bard(Caster):
    pass

class Rogue(BaseClass):
    pass