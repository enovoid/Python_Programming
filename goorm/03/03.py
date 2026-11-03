price, n = map(int, input().split())

total = price * n
discount = total * 0.9

print(f"총 금액: {total:,}원")
print(f"할인된 금액: {discount:,.1f}원")
