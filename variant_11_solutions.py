'''
Лабораторна робота: 5
Варіант: 11
Студент: Возний Микита
Група: 2
'''

import math
def f(x):
    return(math.atan(x)-1/x)
#eps = 0.0004
'''
На графіку бачимо, що корінь лежить десь між 1 і 2
Щоб похідна phi(x) по модулю була менше 1 на цьому відрізку, виберемо phi(x) = 1/arctan(x)
'''
#x0 = 1.5
a = 1
b = 2

def phi(x):
    return(1/math.atan(x))
'''
Похідна phi(x) = (1/atan(x))' = -atan(x)' * (atan(x))^(-2) = 1/((arctan(x))^2*(x^2+1)) вона монотонно зростає на відрізку (a,b)
отже максимум по модулю похідної на відрізку (x_n,x_n-1) буде при min(...)
'''
def dphi(x):
    return( -1 / ( (x**2+1) * (math.atan(x)**2) ) )

def solve_iteration(phi,dphi,eps):
    i = 0
    x1 = x0
    x2 = phi(x0)
    q = 1
    solved = False
    returnlist = []
    while solved == False:
        q = dphi(min(x1,x2))
        if dphi(max(x1,x2)) < 0:
            if abs(x2-x1) < eps:
                solved = True
                continue
        ''' для нашої функції dphi<0 на всьому відрізку, тому інший варіант не потребує імплементації
        else:
            if dphi(max(x1,x2)) <= (1-q)/q*eps:
                solved = True
                continue
        '''
        # After checking if solved solve
        i = i+1
        x1 = x2
        x2 = phi(x1)
        #print(f'Кількість ітерацій {i} X_n {x1} X_n+1 {x2}')
        returnlist.append(f'Кількість ітерацій {i} X_n {x1} X_n+1 {x2}')
    #print(f"Розв'язано, x = {x2}, кількість ітерацій {i}")
    returnlist.append(x2)
    returnlist.append(i)
    return(returnlist)

def save_to_file(biglist):
    #спочатку можифікуємо функцію ітерації щоб замість друкування вона повертала лог-список
    with open("results_variant_11.txt", "w", encoding="utf-8") as file:
        iterations = biglist[-1]
        x = biglist[-2]
        file.write(f'Корінь = {x}\n')
        file.write(f'Кількість ітерацій = {iterations}\n')
        for k in range(len(biglist)-2):
            file.write(f'{biglist[k]}\n')

if __name__ == "__main__":
    x0 = 1.5
    eps = 0.0004
    biglist = solve_iteration(phi,dphi,eps)
    save_to_file(biglist)

    #save_to_file(solve_iteration,phi,dphi,eps)
    print('кількість ітерацій -',biglist[-1],'корінь -',biglist[-2])




