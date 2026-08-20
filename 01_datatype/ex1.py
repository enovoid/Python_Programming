# a = 2, b = 3
a = 2, b
print(a)
print(type(a))

x = y = z = 0

a, b = 2, 3
print(a, b)

# 값 swap
temp = a
a = b
b = temp
print(a, b)

a, b = b, a
print(a, b)

# 변수명 규칙 (C와 동일)
# 문자, 숫자, 언더바만 가능
# 숫자로 시작 불가
name2 = "pororo"
_name = "pororo"
