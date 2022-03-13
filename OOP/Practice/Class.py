class Unit: 
    # python에서 쓰는 생성자
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성 되었습니다".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

# marine1, marine2, tank is the Instance of the Unit Class
# marine1 = Unit("마린", 40, 5)
# marine2 = Unit("마린", 40, 5)
# tank = Unit("Tank", 150, 35)

# 레이스: 공중 유닛, 비행기, 클로킹(상대방에게 보이지 않음)
wraith1 = Unit("Wraith", 80, 5)
print("유닛 이름: {0}, 공격력: {1}".format(wraith1.name, wraith1.damage))

# Mind Control: 상대방 유닛을 내 것으로 만드는 것(빼앗음)
wraith2 = Unit("빼앗은 Wraith", 80, 5)
wraith2.clocking = True

if wraith2.clocking == True:
    print("{0} 는 현재 클로킹 상태입니다.".format(wraith2.name))

