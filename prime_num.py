min_num = 1
max_num = 50

for num in range (min_num, max_num ):
    if num > 1:
        for a in range (2, num):
            if (num % a) == 0:
                break
            else:
                print(num)