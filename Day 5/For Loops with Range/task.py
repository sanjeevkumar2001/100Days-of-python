i = []
for score in range(1, 101):
    if score % 5 == 0 and score % 3 != 0:
        i.append('Buzz')
    elif score % 3 == 0 and score % 5 != 0:
        i.append('Fizz')
    elif score % 3 == 0 and score % 5 == 0:
        i.append('FizzBuzz')
    else:
        i.append(score)
print(i)
