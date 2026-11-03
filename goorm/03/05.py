n = int(input())

thousand = n // 1000
hundred = (n % 1000) // 100
ten = (n % 100) // 10
one = n % 10

reverse = one * 1000 + ten * 100 + hundred * 10 + thousand

print(f"{reverse:04d}")
