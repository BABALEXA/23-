#15.Напишите программу на языке Python, которая принимает в качестве входных данных последовательность слов 
a = input()

def alphavet(a):
    c = ''
    a = a.split('-')
    b = sorted(a)
    for i in range(len(b)):
        if i == len(b)-1:
            c = c + b[i]
        else: c = c + b[i] + '-'
    print(c)
alphavet(a)