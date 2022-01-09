from method_overriding import *

vulture = AttackUnit("벌쳐", 80, 10, 20)
dropship = FlyableUnit("드랍쉽", 200, 3)
battlecruiser = FlyableAttackUnit("배틀크루저", 500, 25, 3)

dropship.move("11시")
vulture.move("9시")
battlecruiser.move("3시")

# 배틀크루저 - 벌쳐 공격, 벌쳐 파괴
battlecruiser.attack("11시", vulture.name)
while vulture.hp >= 0:
    vulture.damaged(battlecruiser.damage)