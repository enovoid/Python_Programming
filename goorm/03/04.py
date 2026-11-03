price, count, discount = map(int, input().split())

before = price * count
discount = before * discount / 100
after = before - discount

print(f"할인 전 입장료: {before:,}원")
print(f"할인 금액: {int(discount):,}원")
print(f"할인 후 입장료: {int(after):,}원")
