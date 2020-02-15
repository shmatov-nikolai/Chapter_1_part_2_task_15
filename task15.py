'''
Write the code, which will print numbers from 0 till your age. And if your age
is odd, will be printed all odd numbers till your age, if even all even numbers.
'''


def vozrast_perebor(age):
    number = []
    if age % 2 == 0:
        for i in range(1, age+1):
            if i % 2 == 0:
                number.append(i)
    else:
        for i in range(1, age+1):
            if i % 2 != 0:
                number.append(i)
    print(number)

vozrast_perebor(30)