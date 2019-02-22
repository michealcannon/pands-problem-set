# Micheál Cannon - question 3
# program that prints all numbers between 1000 and 10,000 that are divisible by 6 but not 12

# check numbers between 1000 and 10,000
for i in range(1000, 10001):
    # print each number that is zero (modulo 6) but not zero (modulo 12)
    if i % 6 == 0 and i % 12 != 0:
        print(i)
