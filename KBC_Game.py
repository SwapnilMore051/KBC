#Getting ready with data
questions=[
    'Who is developer of Python language?',
    'When did India get independence?',
    'What is the currency in India?',
    'Which state does Pune belong to?',
    'Which is latest iPhone?',
    'In the game of ludo the discs or tokens are of how many colours?',
    'Which of these are names of national parks located in Madhya Pradesh?',
    'What will be the output of the following code snippet? print(2**3 + (5 + 6)**(1 + 1))',
    'What is the maximum length of a Python identifier?',
    'How is a code block indicated in Python?',
    'Which of the following concepts is not a part of Python?',
    'Which of the following statements are used in Exception Handling in Python?',
    'Which of the following types of loops are not supported in Python?'
]

answers=[
    'Guido Van',
    '1947',
    'INR',
    'Maharashtra',
    'iPhone 13',
    'Four',
    'Kanha and Madhav',
    '129',
    'No fixed length is specified',
    'Indentation',
    'Pointers',
    'All of the above',
    'do-while'
]

options=[
    ['Dennis RRitchi','Alan Frank','Guido Van','Albert'],
    ['1947','1995','2000','1950'],
    ['Pounds','Dollars','Euros','INR'],
    ['Maharashtra','Rajasthan','Goa','Assam'],
    ['iPhone SE2','iPhone 14','iPhone 12','iPhone 13'],
    ['One','Two','Three','Four'],
    ['Krishna and Kanhaiya','Kanha and Madhav','Ghanshyam and Murari','Girdhar and Gopal'],
    ['129','8','121','28'],
    ['32','16','128','No fixed length is specified'],
    ['Brackets','Indentation','Key','None of the above'],
    ['Pointers','Loops','Dynamic typing','All of the above'],
    ['try','except','finally','All of the above'],
    ['for','while','do-while','None of the above']
]

#KBC Logic 1

def play_game(username, questions, answers, options):
    print("Hello",username,"Welcome to the KBC Game")
    score=0
    for i in range(len(questions)):
        current_question=questions[i]
        correct_answer=answers[i]
        current_question_options=options[i]
        print("Questions:",current_question)
        for index,each_option in enumerate(current_question_options):     #enumerate is used for indexing the elements
            print(index+1,") ",each_option,sep='')                        #Here we take 'index+1' for starting indexing from 1    

        user_answer_index=int(input("Enter your choice(1,2,3 or 4): "))
        user_answer=current_question_options[user_answer_index-1]         #we take 'index-1' because in above line we take 'index+1' it is for balancing
        if user_answer==correct_answer:
            print("Correct answer")
            score=score+100
        else:
            print("Wrong answer")
            break
    print("Your final score is",score)
    return username, score


def view_scores(names_and_scores):
    for name,score in names_and_scores.items():
        print(name,"has scored",score)
    


def KBC(questions,answers,options):
    names_and_scores={}
    while True:
        print("Welcome to the Game")
        print("1)Play Game\n2)View Scores\n3)Exit")
        choice=int(input("Please enter your choice: "))

        if choice==1:
            username=input("Please enter your Name: ")
            username,score=play_game (username,questions,answers,options)
            names_and_scores[username]=score
    
        elif choice==2:
            view_scores(names_and_scores)

        elif choice==3:
            break

        else:
            print("Your choice is NOT VALID")

KBC (questions,answers,options)