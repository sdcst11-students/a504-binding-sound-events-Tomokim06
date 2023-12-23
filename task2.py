import time, playsound

def start():
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
    playsound.playsound("Correct.mp3",block=False)
    print('Correct')
    printscore()

def wronganswer():
    playsound.playsound("Wrong.mp3",block=False)
    print('Incorrect')
    printscore()


q1=('rewrite "x**2-9x+20" --->: ')
p = input(q1)
if p == ("(x-4)(x-5)") or p == ("(x-5)(x-4)"):
    score1=score1+1
    score2=score2+1
    rightanswer()
else:
    score2=score2+1
    wronganswer()

q2=('rewrite "x**2+7x+6" --->: ')
p = input(q2)
if p == ("(x+1)(x+6)") or p == ("(x+6)(x+1)"):
    score1=score1+1
    score2=score2+1
    rightanswer()
else:
    score2=score2+1
    wronganswer()


q3=('rewrite "x**2-2x-80" --->: ')
p = input(q3)
if p == ("(x-10)(x+8)") or p == ("(x+8)(x-10)"):
    score1=score1+1
    score2=score2+1
    rightanswer()
else:
    score2=score2+1
    wronganswer()

q4=('rewrite "-4**2-21x-5" --->: ')
p = input(q4)
if p == ("-(x+5)(4x+1") or p == ("-(4x+1)(x+5)"):
    score1=score1+1
    score2=score2+1
    rightanswer()
else:
    score2=score2+1
    wronganswer()

q5=('rewrite "x**2+9x+14" --->: ')
p = input(q5)
if p == ("(x+7)(x+2)") or p == ("(x+2)(x+7)"):
    score1=score1+1
    score2=score2+1
    rightanswer()
else:
    score2=score2+1
    wronganswer()

q6=('rewrite "x**2-18x+80" --->: ')
p = input(q6)
if p == ("(x-10)(x-8)") or p == ("(x-8)(x-10)"):
    score1=score1+1
    score2=score2+1
    rightanswer()
else:
    score2=score2+1
    wronganswer()

q7=('rewrite "x**2-2x-80" --->: ')
p = input(q7)
if p == ("(x+2)(x-5)") or p == ("(x-5)(x+2)"):
    score1=score1+1
    score2=score2+1
    rightanswer()
else:
    score2=score2+1
    wronganswer()

q8=('rewrite "x**2-20x-100" --->: ')
p = input(q8)
if p == ("(x-10)(x-10)") or p == ("(x-10)**2"):
    score1=score1+1
    score2=score2+1
    rightanswer()
else:
    score2=score2+1
    wronganswer()

q9=('rewrite "x**2+5x+4" --->: ')
p = input(q9)
if p == ("(x+1)(x+4)") or p == ("(x+4)(x+1)"):
    score1=score1+1
    score2=score2+1
    rightanswer()
else:
    score2=score2+1
    wronganswer()

q10=('rewrite "x**2+8x+12" --->: ')
p = input(q10)
if p == ("(x+2)(x+6)") or p == ("(x+6)(x+2)"):
    score1=score1+1
    score2=score2+1
    rightanswer()
else:
    score2=score2+1
    playsound.playsound("Wrong.mp3",block=False)
    print('Incorrect')

print("You finished.")
print(f"Your final score was {score1}/{score2}")
time.sleep(2)
