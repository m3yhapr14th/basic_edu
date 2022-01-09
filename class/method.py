class Unit:
    def __init__(self, name, hp ,damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성 되었습니다.".format(self.name))
        print("체력: {0}, 공격력: {1}".format(self.hp, self.damage))

# 공격 유닛
class AttackUnit:
    def __init__(self, name, hp ,damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    def attack(self, location, enemy): # 메소드
        print("{0}: {1} 방향으로 {2}을 공격 합니다. [공격력 {3}]" \
            .format(self.name, location, enemy, self.damage))

    def damaged(self, damage): # 메소드
        print("{0}: {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0}: 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} 유닛이 파괴되었습니다.".format(self.name))

# 히드라: 공격 유닛, 침.
hydra1 = AttackUnit("히드라", 40, 10)
marine1 = AttackUnit("마린", 50, 15)
hydra1.attack("5시", marine1.name)

while hydra1.hp >= 1:
    hydra1.damaged(marine1.damage)

