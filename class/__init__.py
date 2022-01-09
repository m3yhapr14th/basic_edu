# 파이썬에서 쓰이는 생성자
# 객체가 만들어질때 자동으로 생성

class Unit:
    def __init__(self, name, hp ,damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성 되었습니다.".format(self.name))
        print("체력: {0}, 공격력: {1}".format(self.hp, self.damage))

# 마린, 탱크는 Unit 클래스의 인스턴스라고 표현
# 만들어질때 자동으로 호출됨
# __init__ 에서 self를 제외하고 나머지
marine1 = Unit("마린", 40, 5)
marine2 = Unit("마린", 40, 5)
tank = Unit("탱크", 150, 35)

# 규칙에 맞지 않으면 사용 불가(name, hp, damage)
# marine3 = Unit("마린", 40)
# marine4 = Unit("마린")

# 멤버 변수
# 레이스 : 공중 유닛, 비행기. 클로킹 (상대방에게 보이지 않음)

wraith1 = Unit("레이스", 80, 5)
print("유닛 이름: {0}, 공격력: {1}".format(wraith1.name, wraith1.damage)) # 멤버 변수를 외부에서 사용

# 마인드 컨트롤: 상대방 유닛을 내 것으로 만드는 것
wraith2 = Unit("빼앗은 레이스", 80, 5)
# 외부에서 clocking이라는 변수를 추가 확장
wraith2.clocking = True

if wraith2.clocking == True:
    print("{0}는 현재 클로킹 상태입니다.".format(wraith2.name))

# 추가되지 않은 객체는 사용할 수 없음
if wraith1.clocking == True:
    print("{0}는 현재 클로킹 상태입니다.".format(wraith1.name))