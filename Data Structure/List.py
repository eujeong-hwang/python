# List []

# 지하철 칸 별로 10명, 20명, 30명
subway = []
subway1 = 10
subway2 = 20
subway3 = 30

subway.append(subway1)
subway.append(subway2)
subway.append(subway3)
print(subway)

subway =["유재석", "조세호", "박명수"]

# 조세호씨가 몇 번째 칸에 탔나요?
print(subway.index("조세호"))

# 하하씨가 다음 정류장에서 다음 칸에 탐.
subway.append("하하")
print(subway)

# 정형돈을 유재석/ 조세호 사이에 태워봄
subway.insert(1, "정형돈")
print(subway)

subway.insert(3, "황유정")
print(subway)

# 지하철에 있는 사람을 한 명씩 뒤에서 꺼냄
print(subway.pop())
print(subway)