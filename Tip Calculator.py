## Tip Calculator

meal = 44.34
tax = .0675

badService = .10
averageService = .15
goodService = .20

meal = meal + meal*tax

bad = meal * (1 + badService)
average = meal * (1 + averageService)
good = meal * (1 + goodService)

print(good)
