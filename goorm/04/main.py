# 조건문 1

age = int(input())
if age >= 65 or age < 6:
    cost = 0
elif age >= 19:
    cost = 1550
elif age >= 13:
    cost = 900
elif age >= 6:
    cost = 550

print(f"나이: {age}세\n지하철 요금: {cost}원")

# 조건문 2
# 연도 (year)를 입력 받아 윤년 여부를 판별하여 출력해보세요.

year = int(input())
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print("윤년입니다.")
else:
    print("평년입니다.")

# 조건문 3
one_to_three = 3000 * 120 // 100
four_to_six = 4000 * 110 // 100

grade = int(input())
if grade >= 1 and grade <= 3:
    print(f"{grade}학년 급식비: {one_to_three}원")
elif grade >= 4 and grade <= 6:
    print(f"{grade}학년 급식비: {four_to_six}원")
else:
    print("없는 학년입니다.")


# 조건문 4
grade = input()
if grade == "A":
    print("Excellent!")
elif grade == "B":
    print("Great!")
elif grade == "C":
    print("Good!")
elif grade == "D" or grade == "E":
    print("Don't give up!")
else:
    print("없는 등급입니다.")

# 조건문 5
id = input()
pwd = input()
if "@" not in id:
    print("이메일 형식이 아닙니다.")
elif not id.endswith("@dimigo.hs.kr"):
    print("학교 이메일이 아닙니다.")
elif pwd != id[: id.index("@")]:
    print("초기 비밀번호가 아닙니다.")
else:
    print("로그인 성공, 비밀번호를 초기화하세요.")

# 조건문 6
# 정수 두 개를 입력받아 각 입력 값의 홀수 또는 짝수를 출력하고 두 수를 더한 결과 역시 홀수 짝수를 판별하여 출력해 보세요.
# 예를 들어, 2 3을 입력받으면 짝수 + 홀수 = 홀수를 출력하고, 3 5를 입력받으면 홀수 + 홀수 = 짝수를 출력합니다.
num_01, num_02 = map(int, input().split())
sum = num_01 + num_02

a = "짝수" if num_01 % 2 == 0 else "홀수"
b = "짝수" if num_02 % 2 == 0 else "홀수"
c = "짝수" if sum % 2 == 0 else "홀수"
print(f"{a} + {b} = {c}")

# 조건문 7
year, month, day = map(int, input().split())
if (year - month + day) % 10 == 0:
    print("대박")
else:
    print("그럭저럭")

# 조건문 8
id = int(input())
class_number = (id // 100) % 10
if class_number == 1:
    print("이비")
elif class_number == 2:
    print("디콘")
elif class_number == 3 or class_number == 4:
    print("웹플")
elif class_number == 5 or class_number == 6:
    print("해방")
else:
    print("잘못된 학번입니다.")

# 조건문 9
a, b, c = map(int, input().split())
height = int(input())
if height > a and height > b and height > c:
    print("통과")
else:
    print("줄에 걸림")

# 조건문 10
height, weight = map(float, input().split())
height = height / 100
bmi = weight / (height * height)
print(f"BMI: {bmi:.2f}")
if bmi < 18.5:
    print("저체중")
elif bmi < 23:
    print("정상")
elif bmi < 25:
    print("과체중")
elif bmi < 35:
    print("비만")
else:
    print("고도비만")

# 조건문 11
a, b, c, d = map(int, input().split())
count = a + b + c + d
if count == 1:
    print("도")
elif count == 2:
    print("개")
elif count == 3:
    print("걸")
elif count == 4:
    print("윷")
else:
    print("모")

# 조건문 12
a, b, c = map(int, input().split())
if a < b + c and b < a + c and c < a + b:
    print("yes")
else:
    print("no")
