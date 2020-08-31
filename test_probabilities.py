from probabilities import p_hit, p_wound, p_not_saved, calc_distribution, Reroll
from fractions import Fraction

### p_hit
assert p_hit(5) == Fraction(1, 3), "WS 5+ should hit 1/3rd of the time"
assert p_hit(4) == Fraction(1, 2), "WS 4+ should hit half of the time"
assert p_hit(3) == Fraction(2, 3), "WS 3+ should hit 2/3rds of the time"
assert p_hit(2) == Fraction(5, 6), "WS 2+ should hit 5/6tsh of the time"

assert p_hit(3, -1) == Fraction(1, 2), "WS 3+ with -1 to hit should hit half of the time"
assert p_hit(3, -2) == Fraction(1, 2), "WS 3+ with -2 to hit should hit half of the time"
assert p_hit(3, 1) == Fraction(5, 6), "WS 3+ with +1 to hit should hit 5/6ths of the time"
assert p_hit(3, 2) == Fraction(5, 6), "WS 3+ with +1 to hit should hit 5/6ths of the time"
assert p_hit(2, 1) == Fraction(5, 6), "WS 2+ with +1 to hit should hit 5/6ths of the time (ones always miss)"


assert p_hit(3, rerolls=Reroll.ones) == Fraction(28, 36), "WS 3+, re-roll ones should hit 28/36th of the time"
assert p_hit(3, rerolls=Reroll.every) == Fraction(32, 36), "WS 3+, re roll all should hit 32/36th of the time"

assert p_hit(3, modifier=-1, rerolls=Reroll.every) == Fraction(27, 36), "WS 3+, -1 to hit, re-roll all should hit 28/36th of the time"
assert p_hit(3, modifier=-2, rerolls=Reroll.every) == Fraction(27, 36), "WS 3+, -2 to hit, re roll all should hit 32/36th of the time"
assert p_hit(3, modifier=1, rerolls=Reroll.every) == Fraction(35, 36), "WS 3+, +1 to hit, re-roll all should hit 28/36th of the time"
assert p_hit(3, modifier=2, rerolls=Reroll.every) == Fraction(35, 36), "WS 3+, +2 to hit, re roll all should hit 32/36th of the time"

assert p_hit(3, modifier=-1, always_hit_on=3) == Fraction(2, 3)

# p_wound
assert p_wound(2, 4) == Fraction(1, 6)
assert p_wound(3, 4) == Fraction(1, 3)
assert p_wound(4, 4) == Fraction(1, 2)
assert p_wound(5, 4) == Fraction(2, 3)
assert p_wound(8, 4) == Fraction(5, 6)

assert p_wound(2, 4, modifier=-1) == Fraction(1, 6)
assert p_wound(2, 4, modifier=1) == Fraction(1, 3)
assert p_wound(3, 4, modifier=-1) == Fraction(1, 6)
assert p_wound(3, 4, modifier=2) == Fraction(1, 2)

assert p_wound(5, 4, rerolls=Reroll.ones) == Fraction(28, 36)
assert p_wound(5, 4, rerolls=Reroll.every) == Fraction(32, 36)

assert p_wound(5, 4, modifier=-1, rerolls=Reroll.every) == Fraction(27, 36)
assert p_wound(5, 4, modifier=-2, rerolls=Reroll.every) == Fraction(27, 36)
assert p_wound(5, 4, modifier=1, rerolls=Reroll.every) == Fraction(35, 36)
assert p_wound(5, 4, modifier=2, rerolls=Reroll.every) == Fraction(35, 36)

assert p_wound(5, 4, modifier=-1, always_wound_on=3) == Fraction(2, 3)

# p_not_saved
assert p_not_saved(4, 0) == Fraction(3, 6)
assert p_not_saved(4, 1) == Fraction(2, 3)
assert p_not_saved(2, 4) == Fraction(5, 6)
assert p_not_saved(3, 4) == 1

assert p_not_saved(2, 4, 4) == Fraction(1, 2)
assert p_not_saved(2, 1, 4) == Fraction(1, 3)

assert p_not_saved(2, 4, modifier=-1) == 1
assert p_not_saved(2, 3, modifier=-1) == Fraction(5, 6)
assert p_not_saved(3, 1, modifier=1) == Fraction(1, 3)

assert p_not_saved(3, 0, rerolls=Reroll.ones) == Fraction(8, 36)
assert p_not_saved(3, 0, rerolls=Reroll.every) == Fraction(4, 36)


# calc_distribution
assert calc_distribution(3, 4, 3) == Fraction(4, 9)
assert calc_distribution(3, 4, 3, 4) == Fraction(2, 9)
assert calc_distribution(3, 4, 3, armor_save=4, ap=1) == Fraction(8, 27)

print("All test passed.")
