#12.	Напишите функцию Python, которая проверяет, является ли переданная строка палиндромом или нет.  
a = input()

def reverse(a): 
    return a[::-1] 
  
def palindrome(a): 
    rev = reverse(a) 
    if (a == rev): 
        print("Да")
    else: print('Нет')

palindrome(a)