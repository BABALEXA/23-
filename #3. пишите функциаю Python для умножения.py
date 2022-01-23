#3.	пишите функциаю Python для умножения всех чисел в списке.  
a = list(map(int,input().split(',')))

def umnojenie(a):
    s = 1
    for i in range(len(a)):
        s = s * a[i]
    print(s)
umnojenie(a)