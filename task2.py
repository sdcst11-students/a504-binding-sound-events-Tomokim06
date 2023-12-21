import time, playsound
print('\n\n-----In this game, I will ask you to rewrite 10 different trinomials in factored form.-----\n-----For example, if I gave you "X**2 + x - 6", the answer would be "(x + 3)(x - 2)". -----\n\n')
time.sleep(6)
print('\n\n-----if you answer correctly, you will move on to the next questions. If your answer is-----\n-----wrong or not written in proper form, you will move on to the next question.       -----\n\n')
time.sleep(6)
print('Get ready...')
time.sleep(2)

score1=0
score2=0


def printscore():
    print(f"Your score is {score1}/{score2}")
    time.sleep(2)


def rightanswer():
    print('Correct')
    playsound.playsound("Correct.mp3",block=False)

def wronganswer():
    playsound.playsound("Wrong.mp3",block=False)
    print('Incorrect') 


q1=('rewrite "x**2-9x+20" --->: ')
if input(q1) == ("(x-4)(x-5)") or input(q1) == ("(x-5)(x-4)"):
    score1=score1+1
    score2=score2+1
    print('Correct')
    playsound.playsound("Correct.mp3",block=False)
else:
    score2=score2+1
    playsound.playsound("Wrong.mp3",block=False)
    print('Incorrect') 
printscore()

q2=('rewrite "x**2+7x+6" --->: ')
if input(q2) == ("(x+1)(x+6)") or input(q2) == ("(x+6)(x+1)"):
    score1=score1+1
    score2=score2+1
    print('Correct')
    playsound.playsound("Correct.mp3",block=False)
else:
    score2=score2+1
    playsound.playsound("Wrong.mp3",block=False)
    print('Incorrect') 
printscore()

q3=('rewrite "x**2-2x-80" --->: ')
if input(q3) == ("(x-10)(x+8)") or input(q3) == ("(x+8)(x-10)"):
    score1=score1+1
    score2=score2+1
    print('Correct')
    playsound.playsound("Correct.mp3",block=False)
else:
    score2=score2+1
    playsound.playsound("Wrong.mp3",block=False)
    print('Incorrect') 
printscore()

q4=('rewrite "-4**2-21x-5" --->: ')
if input(q4) == ("-(x+5)(4x+1") or input(q4) == ("-(4x+1)(x+5)"):
    score1=score1+1
    score2=score2+1
    rightanswer()
else:
    score2=score2+1
    wronganswer()
    pass
printscore()

q5=('rewrite "x**2+9x +14" --->: ')
if input(q5) == ("(x+7)(x+2)") or input(q5) == ("(x+2)(x+7)"):
    score1=score1+1
    score2=score2+1
    rightanswer()
else:
    score2=score2+1
    wronganswer()
printscore()

q6=('rewrite "y2-18y+80" --->: ')
if input(q6) == ("(x-10)(x-8)") or input(q6) == ("(x-8)(x-10)"):
    score1=score1+1
    score2=score2+1
    rightanswer()
else:
    score2=score2+1
    wronganswer()
printscore()

q7=('rewrite "x**2-2x-80" --->: ')
if input(q7) == ("(x+2)(x-5)") or input(q7) == ("(x-5)(x+2)"):
    score1=score1+1
    score2=score2+1
    rightanswer()
else:
    score2=score2+1
    wronganswer()
printscore()

q8=('rewrite "x**2-20x-100" --->: ')
if input(q8) == ("(x-10)(x-10)") or input(q8) == ("(x-10)**2"):
    score1=score1+1
    score2=score2+1
    rightanswer()
else:
    score2=score2+1
    wronganswer()
printscore()

q9=('rewrite "x**2+5x+4" --->: ')
if input(q9) == ("(x+1)(x+4)") or input(q9) == ("(x+4)(x+1)"):
    score1=score1+1
    score2=score2+1
    rightanswer()
else:
    score2=score2+1
    wronganswer()
printscore()

q10=('rewrite "x**2+8x+12" --->: ')
if input(q10) == ("(x+2)(x+6)") or input(q10) == ("(x+6)(x+2)"):
    score1=score1+1
    score2=score2+1
    rightanswer()
else:
    score2=score2+1
    wronganswer()
printscore()

print("You finished.")
time.sleep(2)
