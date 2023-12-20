import time, playsound
print('\n\n-----In this game, I will ask you to rewrite 10 different trinomials in factored form.-----\n-----For example, if I gave you "X**2 + x - 6", the answer would be "(x + 3)(x - 2)". -----\n\n')
time.sleep(6)
print('\n\n-----if you answer correctly, you will move on to the next questions. If your answer is   -----\n-----wrong or not written in proper form, you will get to try again until you get it right-----\n\n')
time.sleep(6)
print('Get ready...')
time.sleep(2)
x=1
q1=('rewrite "x**2-9x+20" --->: ')
while x==1:
    if input(q1) == ("(x-4)(x-5)"):
        print('Correct')
        playsound
        x=x+1
        pass
    else:
        print('tryagain')
time.sleep(2)
q2=('wdasdawdasd')