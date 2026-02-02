capital = 100
rate = 0.1

for month in range(1, 13):
    capital += capital * rate
    print("Bulan", month, ":", round(capital, 2))
