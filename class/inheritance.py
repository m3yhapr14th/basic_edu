# 상속
class Unit: # 부모 클래스
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

# 공격 유닛
class AttackUnit(Unit): # 자식 클래식
    def __init__(self, name, hp ,damage):
#        self.name = name # Unit에 상속되는 변수로 써줄 필요 없음
#        self.hp = hp
        Unit.__init__(self, name, hp)
        self.damage = damage

    def attack(self, location, enemy):
        print("{0}: {1} 방향으로 {2}을 공격 합니다. [공격력 {3}]" \
            .format(self.name, location, enemy, self.damage))

    def damaged(self, damage):
        print("{0}: {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0}: 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} 유닛이 파괴되었습니다.".format(self.name))

# 메딕: 의무병


# 히드라: 공격 유닛, 침.
hydra1 = AttackUnit("히드라", 40, 10)
marine1 = AttackUnit("마린", 50, 15)
hydra1.attack("5시", marine1.name)

while hydra1.hp >= 1:
    hydra1.damaged(marine1.damage)

# 드랍쉽: 공중 유닛, 수송기. 마린/파이어뱃/탱크 등을 수송. 공격 기능 없음
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed
        
    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]". format(name, location, self.flying_speed))

# 다중 상송
# 공중 공격 유닛 클래스
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, damage)
        Flyable.__init__(self, flying_speed)

## 발키리: 공중 공격 유닛, 한번에 14발 미사일 발사
valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)
valkyrie.fly("발키리", "3시")

class FlyableUnit(Unit, Flyable):
    def __init__(self, name, hp, flying_speed):
        Unit.__init__(self, name, hp)
        Flyable.__init__(self, flying_speed)

dropship = FlyableUnit("드랍쉽", 100, 10)
dropship.fly("드랍쉽", "3시")