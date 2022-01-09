class Unit: # 부모 클래스
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed

    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도: {2}]".format(self.name, location, self.speed))

# 공격 유닛
class AttackUnit(Unit): # 자식 클래식
    def __init__(self, name, hp , speed, damage):
        Unit.__init__(self, name, hp, speed)
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


# 공중 유닛
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed
        
    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]". format(name, location, self.flying_speed))

# 다중 상송
# 공중 공격 유닛 클래스
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage)
        Flyable.__init__(self, flying_speed)

    def move(self, location): # move 함수 재 정의(새로운)
        print("[공중 유닛 이동]")
        self.fly(self.name, location)

# 공중 유닛
class FlyableUnit(Unit, Flyable):
    def __init__(self, name, hp, flying_speed):
        Unit.__init__(self, name, hp, 0)
        Flyable.__init__(self, flying_speed)

# 벌쳐 : 지상 유닛, 기동성이 좋음
# vulture = AttackUnit("벌쳐", 80, 10, 20)

# 배틀크루저: 공중 유닛, 체력 높음, 공격력 높음
# battlecruiser = FlyableAttackUnit("배틀크루저", 500, 25, 3)

# 지상유닛, 공중유닛 이동 함수가 달라 귀찮음
# vulture.move("11시")
# battlecruiser.fly(battlecruiser.name, "9시")
# battlecruiser.move("9시")
