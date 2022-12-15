a, b = int(input()), int(input())
sum_of_deviders = 0
max_devider = 0

for i in range(a, b + 1):
    counter = 0
    for j in range(1, i + 1):
        if i % j == 0:
            counter += j
            if counter >= sum_of_deviders:
                sum_of_deviders = counter
                max_devider = i
print(max_devider, sum_of_deviders)
