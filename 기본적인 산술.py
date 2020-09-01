import math

# 더하기
print(1 + 2)  # 3

# 뺴기
print(50 - 4)  # 46

# 곱하기
print(12 * 3)  # 36

# 나누기
print(5000 / 3)  # 1666.6666666667

# 몫
print(50 // 8)  # 6

# 나머지
print(50 % 8)  # 2

# 제곱
print(2 ** 3)  # 8

# 올림
print(math.ceil(3.14))  # 4

# 내림
print(math.floor(3.14))  # 3
print(math.trunc(-3.14))  # -3 (0을 향한다)
print(math.trunc(3.14))  # 3 (0을 향한다)

# 반올림
print(round(3.1415))  # 3
print(round(3.1415, 2))  # 3.14 (몇번째 자리에서 반올림할것인지 두번째 인자로 전달)
print(round(31.415, -1))  # 30.0 (음수도 가능)

print(round(4.5))  # 4 (반올림할 자리의 숫자가 5일 때 앞자리 숫자가 짝수면 내림)
print(round(3.5))  # 4 (반올림할 자리의 숫자가 5일 때 앞자리 숫자가 홀수면 올림)
