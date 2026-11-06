'''
Лабораторна робота: 5
Варіант: 11
Студент: Возний Микита
Група: 2
'''
import math
def f(x):
    return(math.atan(x)-1/x)
eps = 3*10**(-4)
'''
На графіку бачимо, що корінь лежить десь між 1 і 2
Щоб похідна phi(x) по модулю була менше 1 на цьому відрізку, виберемо phi(x) = 1/arctan(x)
'''
x0 = 1.5
a = 1
b = 2

def phi(x):
    return(1/math.atan(x))
'''
Похідна phi(x) = (1/atan(x))' = -atan(x)' * (atan(x))^(-2) = 1/((arctan(x))^2*(x^2+1)) вона монотонно зростає на відрізку (a,b)
отже максимум по модулю похідної на відрізку (x_n,x_n-1) буде при min(...)
'''
def dphi(x):
    return( 1 / ( (x**2+1) * (math.atan(x)**2) ) )

def solve_iteration():
    i = 0
    x1 = x0
    x2 = phi(x0)
    q = 1
    solved = False
    while solved == False:
        q = dphi(min(x1,x2))
        if dphi(max(x1,x2)) < 0:
            if x2-x1 < eps:
                solved = True
                continue
        else:
            if dphi(max(x1,x2)) <= (1-q)/q*eps:
                solved = True
                continue
        # After checking if solved solve
        i = i+1
        x1 = x2
        x2 = phi(x1)
        print(f'Кількість ітерацій {i} X_n {x1} X_n+1 {x2}')
    print(f"Розв'язано, x = {x2}, кількість ітерацій {i}")

solve_iteration()
