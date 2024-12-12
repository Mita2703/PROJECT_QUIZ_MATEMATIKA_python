# project game
# from youtube   : Vishes Programming https://youtu.be/QDCsjxzqIFY?si=knAivfQzmYiZ-hkf
# dibuat oleh    : Mita Octavia

from tkinter import*
from random import randint , choice

root = Tk()
root.geometry("540x500")
root.title("Matematika Kelas 1 dan Kelas 2 SD")

number1 = randint (1, 10)
number2 = randint (1,10)

operator = choice(['+', '-', '*','/'])

question = StringVar ()
answer = StringVar ()
givenAnswer = StringVar()
Score = IntVar()
QuestionNumber = IntVar()

def generateQuestion () :

    global questionLabel

    QuestionNumber.set(QuestionNumber.get() + 1 )

    number1 = randint (1, 10)
    number2 = randint (1,10)

    operator = choice(['+', '-', '*','/'])

    question.set(str(number1) + operator + str(number2))
    answer.set(eval(question.get()))

    if questionLabel :
        questionLabel.destroy()

    questionLabel = Label (root, text=f"SOAL : {question.get()}" , font=('arial', 15))
    questionLabel.grid (row=2 , column=0)

def checkAnswer() :

    global scoreLabel

    if QuestionNumber.get() > 10 :
        return 


    global resultLabel

    if resultLabel :
        resultLabel.destroy()

    if str(answer.get()) == givenAnswer.get() :
        Score.set(Score.get() + 1)
        resultLabel= Label (root, text="BENAR" , font= ('arial bold', 15), fg="green")
        resultLabel.grid(row=4 , column=0)
        scoreLabel= Label (root, text=f"Score : {Score.get()} ", font= ('arial bold', 15), fg="black")
        scoreLabel.grid(row=5 , column=0)

    else:  
        resultLabel= Label (root, text="SALAH" , font= ('arial bold', 15), fg="red")
        resultLabel.grid(row=4 , column=0)


    if QuestionNumber.get() == 10 :
        scoreLabel.destroy()
        scoreLabel= Label (root, text=f"Score : {Score.get()} ", font= ('arial bold', 15), fg="black")
        scoreLabel.grid(row=5 , column=0)

    else :
        generateQuestion()

def restart():

    global scoreLabel
    scoreLabel.destroy()
    Score.set(0)
    QuestionNumber.set(0)
    generateQuestion()

    scoreLabel= Label (root, text=f"Score : {Score.get()} ", font= ('arial bold', 15), fg="black")
    scoreLabel.grid(row=5 , column=0)

headingLabel1 = Label (root, text= "Quiz Maths" , font=('arial bold', 20))
headingLabel1.grid(row=0, column = 0)

questionScale = Scale(root, from_=0, to=10, orient=HORIZONTAL, length=400, variable=QuestionNumber) 
questionScale.grid(row=1 , column=0)

complateQuestionLebel = Label (root, text="10th question")
complateQuestionLebel.grid(row=1 , column=1)

questionLabel = Label (root, text= question.get(), font=('arial', 15))
questionLabel.grid (row=2 , column=0)

answerEntry = Entry(root, textvariable= givenAnswer, font=('arial', 15), width=25)
answerEntry.grid (row=3 , column=0)

submitButton = Button(root, text= 'KIRIM', fg="pink", bg="black", font= ('arial bold', 10), command= checkAnswer)
submitButton.grid (row=3 , column=1)

resultLabel= Label (root, text="MULAI" , font= ('arial bold', 15), fg="blue")
resultLabel.grid(row=4 , column=0)

scoreLabel= Label (root, text=f" Score : {Score.get()} " , font= ('arial bold', 15), fg="grey")
scoreLabel.grid(row=5 , column=0)

submitButton = Button(root, text= "ULANG" , fg="black",  bg="pink", font= ('arial bold', 10),width=25, command= restart)
submitButton.grid (row=6 , column=0)

generateQuestion()

root.mainloop()