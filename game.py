from datetime import datetime

dt = datetime.now()
ts = datetime.timestamp(dt)

def ask_question(questions):
    score = 0
    for i in questions:
        print(i["Question"])
        print(i["Option"])

        a = input("Enter answer:")
        if (a == i["Answer"]): 
            score += 10
            print("Right")
        
        elif (a == "pass"):
            print("You passed the question")
        else:
            score -=5
            print("Wrong")

    print(score)
    with open('output.txt','a') as file:
        print("The score is: ", score, file=file)
        print('\nThe timestamp is:',ts, file=file)
        print('\nThe date & time is:',dt, file=file)


question1 ={
    "Question" :"What is the smallest country in the world?",
    "Option" :["A. Nepal", "B. Vatican City", "C. Canada", "D. France"],
    "Answer" : "B"
}
question2 ={
    "Question" :"What is the largest country in the world?",
    "Option" :["A. Russia", "B. USA", "C. Germany", "D. England"],
    "Answer" : "A"
}
question3 ={
    "Question" :"What is the hottest continent on Earth?",
    "Option" :["A. Europe", "B. Asia", "C. North America", "D. Africa"],
    "Answer" : "D"
}
question4 ={
    "Question" :"What is the longest river in the world?",
    "Option" :["A. Mississippi River", "B. Amazon River", "C. Nile", "D. Rhine River"],
    "Answer" : "C"
}
question5 ={
    "Question" :"Who was the first female Prime Minister of Australia?",
    "Option" :["A. Julia Gillard", "B. Lara Giddings", "C. KatyGallagher", "D. Anna Bligh"],
    "Answer" : "A"
}
question6 ={
    "Question" :"WWhich Beatles song was banned from the BBC for its lyrics?",
    "Option" :["A. Yesterday", "B. I am the Walrus", "C. Here comes the sun", "D. Norwegian Wood"],
    "Answer" : "B"
}
question7 ={
    "Question" :"Which year was the Premier League founded?",
    "Option" :["A. 1996", "B. 1997", "C. 1994", "D. 1992"],
    "Answer" : "D"
}
question8 ={
    "Question" :"Which singer was known amongst the other things as 'The king of pop'?",
    "Option" :["A. Bruno Mars", "B. Lady Gaga", "C. Michael Jackson", "D. Dan Reynolds"],
    "Answer" : "C"
}
question9 ={
    "Question" :"Taylor Swift grew up on what type of farm?",
    "Option" :["A. Home Farm", "B. Cattle Farm", "C. Christmas Tree Farm", "D. Fish Farm"],
    "Answer" : "C"
}
question10 ={
    "Question" :"What is the name of Kim Kardashian's eldest child?",
    "Option" :["A. North West", "B. Saint West", "C. Psalm West", "D. Chicago West"],
    "Answer" : "A"
}
existing_questions = [question1, question2, question3, question4, question5, question6, question7, question8, question9, question10]
other = input("Do you want to enter question?")
new_question =[]
if other == "y":
    a = int(input("How many number of new questions do you want to enter?"))
    for i in range (a):
        question = input("Enter the Question:")
        options = []

        for i in range(4):
            option = input("Enter option")
            options.append(option)
        answer = int(input("Enter the answer"))
        existing_questions.append({
            "Question" :question,
            "Option" : options,
            "Answer" : answer
        })

    cont = input("Do you want to continue?")

    if cont == "y":
        ask_question(existing_questions)

else:
    ask_question(existing_questions)

