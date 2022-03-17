# Quiz) 당신의 학교에서는 파이썬 코딩 대회를 주최합니다.
# 참석률을 높이기 위해 댓글 이벤트를 진행하기로 하였습니다.
# 댓글 작성자들 중에 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰을 받게 됩니다.
# 추첨 프로그램을 작성하시오.

# 조건1 : 편의상 댓글은 20명이 작성하였고 아이디는 1~20이라고 가정
# 조건2 : 댓글 내용과 상관 없이 무작위로 추첨하되 중복 불가
# 조건3 : random 모듈의 shuffle과 sample을 활용

# (출력 예제)
# -- 당첨자 발표 --
# 치킨 당첨자 : 1
# 커피 당첨자 : [2, 3, 4]
# -- 축하합니다 --

# (활용 예제)
from random import *
# comment = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
comment = list(range(1,21))
shuffle(comment)
winners = sample(comment, 4)

# chicken = sample(comment, 1)
# coffee = sample(comment, 3)

print("--당첨자 발표--\n치킨 당첨자: {0}\n커피 당첨자 : {1}\n--축하합니다--"\
    .format(winners[0], winners[1:]))

##????? why 4, [2,3,4]
