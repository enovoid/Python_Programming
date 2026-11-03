price, paid = map(int, input().split())

change = paid - price

coin500 = change // 500
remain = change % 500

coin100 = remain // 100
remain = remain % 100

coin50 = remain // 50
remain = remain % 50

coin10 = remain // 10

print(f"거스름돈: {change:,}원")
print(f"500원: {coin500}개, 100원: {coin100}개,  50원: {coin50}개, 10원: {coin10}개")
