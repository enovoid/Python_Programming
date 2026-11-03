# 비교 연산자 1
A, B, C = map(int, input().split())
print("True" if A < B and B < C else "False")

# 비교 연산자 2
A, B = map(int, input().split())
print("True" if A * B < 0 else "False")

# 비교 연산자 3
A, B, C = map(int, input().split())
print("True" if A != B and B != C and C != A else "False")

# 논리 연산자 1
N = int(input())
print("True" if N % 3 == 0 or N % 5 == 0 else "False")

# 논리 연산자 2
A, B, C = map(int, input().split())
print("False" if (A == B == C) or (A != B and B != C and C != A) else "True")

# 논리 연산자 3
A, B, C = map(int, input().split())
print(
    "True" if (A + B + C) / 3 >= 80 and (A >= 60 and B >= 60 and C >= 60) else "False"
)

# 논리 연산자 4
height, age = map(int, input().split())
print("True" if height >= 130 and age >= 8 else "False")

# 논리 연산자 5
member, price, coupon = map(int, input().split())
print(
    "True"
    if member == 1 and (price >= 50000 or (coupon == 1 and price >= 30000))
    else "False"
)

# 멤버십 연산자 1
fruits_list, fruit = input().split(), input()
print(fruit in fruits_list)

# 멤버십 연산자 2
post = input()
print("광고" in post or "도박" in post or "욕설" in post)

# 삼항 연산자
N = int(input())
print("Even" if N % 2 == 0 else "Odd")

# 삼항 연산자 2
N = int(input())
print(N if N >= 0 else -N)

# 삼항 연산자 3
N = input()
print("대문자" if "A" <= N <= "Z" else "소문자" if "a" <= N <= "z" else "알파벳 아님")
