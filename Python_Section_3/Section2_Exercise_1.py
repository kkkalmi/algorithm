# TODO: 더블 팩토리얼을 계산하는 재귀 함수 작성
def double_factorial(n):
    a = 1
    if n == 1:
      a = a * 1
      return a
    elif n == 2:
      a = a * 2
      return a
    else:
      a = n * double_factorial(n-2)
      return a

# 예시 출력
print(double_factorial(5))  # 출력: 15
print(double_factorial(10))  # 출력: 48