from . import Spell
from ..dice import Dice


class MagicMissle(Spell):
    name = "Magic Missle"
    description = """
    Magic missile shoots arcane missles at the target for 1d4 damage.  For each additional 4 levels of the caster,
    each missle will do an additional 1d4 damage
    """
    base_damage = Dice(1, 4)
    level_modifier = lambda x: [Dice(1, 4).roll() for _ in xrange(0, x / 4)]
