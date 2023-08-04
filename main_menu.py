
def addition_сложение(a,b):
    return a + b   
       
def subtraction_вычитание(a,b):
    return a - b

def division_деление(a,b):
    if b == 0:
         print ('деление на ноль - ошибка!-division by zero - errorr! ')
         return ''
    return a / b  
 
def multiplication_умножение(a,b):
    return a * b

def разделитель_separator(example):
    for i in  example:
        if i in '+-/*':
            index = example.index(i)
            a=int(example[:index])
            b=int(example[index+1:])
            s=example[index]
            return a , s , b
знаки= {
    '+':addition_сложение,
    '-':subtraction_вычитание,
    '*':multiplication_умножение,
    '/':division_деление
    
}


def main():
    example=input('write an example-напишите пример:')
    a , s , b = разделитель_separator(example)
    матФ= знаки.get(s)
    ответ_answer =матФ(a,b)
    print('ответ = ', ответ_answer)



main()



