def saving(save_item1, save_item2):
    file=open("CodeFest_data.txt","w")
    line=str(save_item1)+"*"+str(save_item2)
    file.write(line)
    file.close()

def retrieve():
    import datetime
    Deadline=[]
    file=open("CodeFest_data.txt","r")
    line=file.readline()
    line=line.split("*")
    task=line[0]
    retrieved_deadline=line[1]
    task=task[2:-2]
    task=task.split("\', \'")
    retrieved_deadline=retrieved_deadline[2:-2]
    retrieved_deadline=retrieved_deadline.split("\', \'")
    
    return task,retrieved_deadline

def conversion_to_datetime(retrieved_deadline):
    Deadline=[]
    for i in range(len(retrieved_deadline)):
        Date=datetime.date(int(retrieved_deadline[i][0:4]),int(retrieved_deadline[i][5:7]),int(retrieved_deadline[i][8:10]))
        Deadline.append(Date)
    return Deadline

def conversion_to_string(Deadline):
    for i in range(len(Deadline)):
        Deadline[i]=str(Deadline[i])
    return Deadline
def Planner_Inputs(Task, Deadline, repeat):
    import datetime
    from datetime import date

    while repeat==True:
        Task_temp=input("Enter task that needs to be completed:")
        repeat_input_flag=True
        while repeat_input_flag==True:

            System_date=date.today()
            try:
                Deadline_day=int(input("Day to be submitted (Eg.5, means: 5th):"))
                Deadline_month=int(input("Month to be submitted (Eg.4 , means April):"))
                Deadline_year=int(input("Year to be submitted(Format:yyyy)Eg. 2021):"))
                Input_date=datetime.date(Deadline_year,Deadline_month,Deadline_day)
                repeat_input_flag=False
            except ValueError:
                print("Input DAY or MONTH might not exist. Please try again.")
            else:
                while Input_date<System_date:
                    print("invalid date")
                    Deadline_day=int(input("Day to be submitted (Eg.5, means: 5th):"))
                    Deadline_month=int(input("Month to be submitted (Eg.4 , means April):"))
                    Deadline_year=int(input("Year to be submitted(Format:yyyy)Eg. 2021):"))
                    Input_date=datetime.date(Deadline_year,Deadline_month,Deadline_day)
                    repeat_input_flag=False
        Task.append(Task_temp)
        Deadline.append(str(Input_date))
        
        option_flag=False
        while option_flag==False:
            option=input("If you want to add more tasks to planner? (options:'y' or 'n'):")
            if option=="n":
                repeat=False
                option_flag=True
            elif option=="y":
                option_flag=True
    return Task, Deadline

import datetime
def schedule(array, deadline):
    spaces="                              "
    n=len(deadline)-1
    swaps=True
    while swaps==True:
          swaps=False
          for i in range(n):
              if deadline[i]>deadline[i+1]:
                  deadline[i],deadline[i+1]=deadline[i+1],deadline[i]
                  array[i],array[i+1]=array[i+1],array[i]
                  swaps=True
          n=n-1
    print("Tasks                              Due\n")
    today= datetime.date.today()
    for i in range(len(deadline)):
        daysleft=deadline[i]-today
        if daysleft.days>=0:
            spacelen=30-(len(array[i])-5)
            print(array[i],spaces[0:spacelen],deadline[i],"\n")
def reminder(array, deadline):
    today=datetime.date.today()
    for i in range(len(array)):
        daysleft=deadline[i]-today
        if daysleft.days<0:
            None
        elif daysleft.days==0:
            print(array[i]," is due today.")
        elif daysleft.days==1:
           print(array[i],"is due tomorrow. Please finish it now.")
        elif daysleft.days>7:
            if daysleft.days%4==0:
                print(array[i],"is due",str(daysleft.days),"days from now. Please plan for it.")
        elif daysleft.days%2==0:
            print(array[i],"is due",str(daysleft.days),"days from now. Please plan for it.")
        
    
def waiting(no_of_times, symbol, time_gap):     #prints text letter after letter
    global time
    for i in range (no_of_times):
        time.sleep(time_gap)
        print(symbol,end="")

import random
def english():
    grade = int(input("would you like 1. IGCSE questions or 2. AS level questions: "))
    if grade==1:
        
        unique=[]
        prefix = ['write a letter', 'write a story','write a blog','write a diary entry', 'write a report']
        letter = [' to your parents describing your new school and hostel', ' to the hotel manager about the issues you have faced since staying at his hotel', ' to the editor of a newspaper, to persuade them to write an article making a plea to the people to switch over to solar energy to conserve electricity']
        story = [' on a time when you got lost somewhere', ' about a time you experienced a new emotion/feeling', ' about a time when you rebelled against your parents or teacher']
        blog = [' on  how to use GitHub and explain its benefits and downsides', ' on your take on the recent events happening about the US elections',' on a new product you recently stumbled upon']
        diary = [' on your first day on your school trip to Manali', ' about your feeling after a very important exam', ' after a whole day of community service']
        report = [' on a recently held Seminar on Conservation of Water as a part of World Water Day celebrations', ' on an accident that took place at school', ' on a recent wold record']
        flag = False

        number = int(input("enter the number of questions you want(less than 5): "))

        for count in range (0, number+1):
            if count ==0:
                writing = random.randint (0,4)
                question = random.randint(0,2)
                unique.append(question)
                
            else:
                flag = False
                while (flag!= True):
                    writing = random.randint(0,4)
                    question = random.randint(0,2)
                    for i in range (0,len(unique)):
                        if (unique[i]==question):
                            flag = True
                            break
                    if (flag == False):
                        break
                if (flag == False):
                    unique.append(question)
            if (flag == False):
                if writing == 0:
                    print(prefix[writing], letter[question])
                if writing == 1:
                    print(prefix[writing], story[question])
                if writing == 2:
                    print(prefix[writing], blog[question])
                if writing == 3:
                    print(prefix[writing], diary[question])
                if writing == 4:
                    print(prefix[writing], report[question])
    if grade == 2:
        unique=[]
        prefix = ['write a letter', 'write a story','write a blog']
        letter = [' Imagining that you are the manager of a large office where a company"s desks have been in use for the past year. Write an letter to the company to express your dissatisfaction with the product and to persuade them to give you a refund', ' to your local MP, giving your views on whether or not GCSEs should be replaced with a new system', ' to the Head Teacher, giving your views on whether or not the school should keep the uniform, or if it should be abolished to allow students to wear what they want']
        story = [' which begins with the following sentence: "David woke up and realised he had forgotten to set his alarm." In your writing, create a sense of urgency and anticipation', ' from the perspective of a shop assistant selling a valuable item', ' called The Circus. In your writing, focus on sound, movement and colour to help the reader imagine the scene']
        blog = [' called In Good Shape. In your writing, suggest the best ways for young people in your area to keep fit and healthy without having to spend much money',' on your take on the recent events happening about the US elections',' on what your most epic failure were (and how did you overcome it)?']
        flag = False

        number = int(input("enter the number of questions you want(less than 4): "))

        for count in range (0, number+1):
            writing = random.randint (0,2)
            question = random.randint(0,2)
            if count ==0:
                writing = random.randint (0,2)
                question = random.randint(0,2)
                unique.append(question)
            else:
                flag = False
                while (flag!= True):
                    question = random.randint(0,2)
                    for i in range (0,len(unique)):
                        if (unique[i]==question):
                            flag = True
                            break
                    if (flag == False):
                        break
                if (flag == False):
                    unique.append(question)
            if (flag == False):
                if writing == 0:
                    print(prefix[writing], letter[question])
                if writing == 1:
                    print(prefix[writing], story[question])
                if writing == 2:
                    print(prefix[writing], blog[question])
            count +=1

def biologyworksheet(): #variables: n=random question number; b=flag to exit loop and module mathworksheet;file=variable opening file,Q1 = question extracted
    print("INSTRUCTIONS: \n *Do not leave spaces. \n *All answers must be in upper case, unless otherwise mentioned.") 
    global b
    b=False
    import random
    upper=10 #Number of questions from data.txt
    
    while b==False:
        
        def newreset(): #To reset setting
            obj=biology()
            obj.start()
        
        class biology():   #To store current data when module is called
            def __init__(self,g=int(input("Enter grade: \n Press 1: for IGCSE \n Press 2: for As and A level \n: "))):

                if g==1:
                    self.grade='IGCSEbio.txt'
                else:
                    self.grade='A level.txt'
                
                self.markedasdone=[]
                 
                self.file=open( self.grade ,'r')

                self.correct=0

            def markasdone(self,n):  #to mark the completed questions
                self.markedasdone.append(n)
                if len(self.markedasdone)==upper:
                    print("Number of correct answers: ",self.correct) 
                    print("All question sets solved! RESET...")
                    newreset()

            def checkifdone(self,n):   #To check if question extracted is solved
                done=False
                for i in range(0,len(self.markedasdone)):
                    if self.markedasdone[i]==n:
                        done=True
                return done
            
            def extract(self,n):     #extracting from .txt file
                string=''
                for i in range(0,n):
                    string=self.file.readline()
                self.file.close()
                self.file=open(self.grade,'r')
                return string

            def formquestion(self,string):    #to form question and the answer
                Q1=''
                ans=''
                
                while True:
                    for i in range(0,len(string)):
                        if string[i]==string[i+1] and string[i+1]==string[i+2] and string[i]=='*':
                            y=i+4
                            break
                        Q1=Q1+string[i]
                    break
                
                while True:
                    for i in range(y, len(string)-5):
                        ans=ans+string[i]
                    break
                return Q1,ans
                
            def start(self):   #start function
              while True:  
                ch=int(input("Press 1 to exit OR 2 to continue: "))
                if ch==1:
                    print("Number of correct answers: ",self.correct)
                    print("EXITING....")
                    b=True
                    break
                if ch==2:
                    while True:
                        n=random.randint(1,upper)
                        if self.checkifdone(n)==False:
                             
                            break
                     
                    string=self.extract(n)
                    Q1,ans=self.formquestion(string)
                     
                    print(Q1)
                    answer=input("Answer:")
                    if answer==ans:
                        print("Good Job")
                        self.correct=self.correct+1
                    else:
                        print("Wrong answer! Answer =",ans)
                    self.markasdone(n) 

        if b==False:
            newreset()
        
        break

def chemworksheet(): #variables: n=random question number; b=flag to exit loop and module mathworksheet;file=variable opening file,Q1 = question extracted
    print("INSTRUCTIONS: \n *Do not leave spaces. \n *All answers must be in upper case, unless otherwise mentioned.") 
    global b
    b=False
    import random
    
    upper=10 #Number of questions from .txt
    
    while b==False:
        
        def newreset(): #To reset setting
            obj=chem()
            obj.start()
            
        class chem():   #To store current data when module is called
            def __init__(self):
                g=int(input("CHOOSE GRADE LEVEL: \n1 for IGCSE \n2 for As and A level: \n \nENTER: "))

                if g==1:
                     
                    self.grade='IGCSEchem.txt'
                else:
                     
                    self.grade='Alevelchem.txt'
                
                self.markedasdone=[]
                 
                self.file=open( self.grade ,'r')

                self.correct=0


            def markasdone(self,n):  #to mark the completed questions
                self.markedasdone.append(n)
                if len(self.markedasdone)==upper:
                    print("Number of correct answers: ",self.correct) 
                    print("All question sets solved! RESET...")
                    newreset()

            def checkifdone(self,n):   #To check if question extracted is solved
                done=False
                for i in range(0,len(self.markedasdone)):
                    if self.markedasdone[i]==n:
                        done=True
                return done
            
            def extract(self,n):     #extracting from .txt file
                string=''
                for i in range(0,n):
                    string=self.file.readline()
                self.file.close()
                self.file=open(self.grade,'r')
                return string

            def formquestion(self,string):    #to form question and the answer
                Q1=''
                ans=''
                
                while True:
                    for i in range(0,len(string)):
                        if string[i]==string[i+1] and string[i+1]==string[i+2] and string[i]=='*':
                            y=i+4
                            break
                        Q1=Q1+string[i]
                    break
                
                while True:
                    for i in range(y, len(string)-5):
                        ans=ans+string[i]
                    break
                return Q1,ans

            def start(self):   #start function
              while True:  
                ch=int(input("Press 1 to exit OR 2 to continue: "))
                if ch==1:
                    print("Number of correct answers: ",self.correct)
                    print("EXITING....")
                    b=True
                    break
                if ch==2:
                    while True:
                        n=random.randint(1,upper)
                        if self.checkifdone(n)==False:
                             
                            break
                     
                    string=self.extract(n)
                    Q1,ans=self.formquestion(string)
                     
                    print(Q1)
                    answer=input("Answer:")
                    if answer==ans:
                        print("Good Job")
                        self.correct=self.correct+1
                    else:
                        print("Wrong answer! Answer =",ans)
                    self.markasdone(n) 

        if b==False:
            newreset()
        
        break

def economicsworksheet(): #variables: n=random question number; b=flag to exit loop and module; file=variable opening file,Q1 = question extracted
    print("INSTRUCTIONS: \n *Do not leave spaces. \n *Answer must be written in capital letters, unless otherwise mentioned.") 
    global b
    b=False
    import random
    upper=10 #Number of questions from data.txt
    
    while b==False:
        
        def newreset(): #To reset setting
            obj=economics()
            obj.start()

        class economics():   #To store current data when module is called
            def __init__(self,g=int(input("Enter grade: \n Press 1: for IGCSE \n Press 2: for As and A level \n: "))):

                if g==1:
                    self.grade='EconomicsIGCSE.txt'
                else:
                    self.grade='EconomicsAlevel.txt'
                
                self.markedasdone=[]
                 
                self.file=open( self.grade ,'r')

                self.correct=0

            def markasdone(self,n):  #to mark the completed questions
                self.markedasdone.append(n)
                if len(self.markedasdone)==upper:
                    print("Number of correct answers: ",self.correct) 
                    print("All question sets solved! RESET...")
                    newreset()

            def checkifdone(self,n):   #To check if question extracted is solved
                done=False
                for i in range(0,len(self.markedasdone)):
                    if self.markedasdone[i]==n:
                        done=True
                return done
            
            def extract(self,n):     #extracting from .txt file
                string=''
                for i in range(0,n):
                    string=self.file.readline()
                self.file.close()
                self.file=open(self.grade,'r')
                return string

            def formquestion(self,string):    #to form question and the answer
                Q1=''
                ans=''
                
                while True:
                    for i in range(0,len(string)):
                        if string[i]==string[i+1] and string[i+1]==string[i+2] and string[i]=='*':
                            y=i+4
                            break
                        Q1=Q1+string[i]
                    break
                
                while True:
                    for i in range(y, len(string)-5):
                        ans=ans+string[i]
                    break
                return Q1,ans

            def start(self):   #start function
              while True:  
                ch=int(input("Press 1 to exit OR 2 to continue: "))
                if ch==1:
                    print("Number of correct answers: ",self.correct)
                    print("EXITING....")
                    b=True
                    break
                if ch==2:
                    while True:
                        n=random.randint(1,upper)
                        if self.checkifdone(n)==False:
                             
                            break
                     
                    string=self.extract(n)
                    Q1,ans=self.formquestion(string)
                     
                    print(Q1)
                    answer=input("Answer:")
                    if answer==ans:
                        print("Good Job")
                        self.correct=self.correct+1
                    else:
                        print("Wrong answer! Answer =",ans)
                    self.markasdone(n) 

        if b==False:
            newreset()
        
        break

def mathworksheet(): #variables: n=random question number; b=flag to exit loop and module mathworksheet;file=variable opening file,Q1 = question extracted
    print("INSTRUCTIONS: \n *Do not leave spaces. \n *Answer must be written in the form mentioned in the question. \n *All answers must be in lower case, unless otherwise mentioned.") 
    global b
    b=False
    import random
    upper=7 #Number of questions from .txt
    
    while b==False:
        
        def newreset(): #To reset setting
            obj=math()
            obj.start()

        class math():   #To store current data when module is called
            def __init__(self):
                g=int(input("Enter your grade: \n1 for IGCSE  \n2 for As and A level: "))

                if g==1:
                     
                    self.grade='IGCSE.txt'
                else:
                     
                    self.grade='Alevel.txt'
                
                self.markedasdone=[]
                 
                self.file=open( self.grade ,'r')

                self.correct=0

            def markasdone(self,n):  #to mark the completed questions
                self.markedasdone.append(n)
                if len(self.markedasdone)==upper:
                    print("Number of correct answers: ",self.correct) 
                    print("All question sets solved! RESET...")
                    newreset()

            def checkifdone(self,n):   #To check if question extracted is solved
                done=False
                for i in range(0,len(self.markedasdone)):
                    if self.markedasdone[i]==n:
                        done=True
                return done
            
            def extract(self,n):     #extracting from .txt file
                string=''
                for i in range(0,n):
                    string=self.file.readline()
                self.file.close()
                self.file=open(self.grade,'r')
                return string

            def formquestion(self,string):    #to form question and the answer
                Q1=''
                ans=''
                
                while True:
                    for i in range(0,len(string)):
                        if string[i]==string[i+1] and string[i+1]==string[i+2] and string[i]=='*':
                            y=i+4
                            break
                        Q1=Q1+string[i]
                    break
                
                while True:
                    for i in range(y, len(string)-5):
                        ans=ans+string[i]
                    break
                return Q1,ans

            def start(self):   #start function
              while True:  
                ch=int(input("Press 1 to exit OR 2 to continue: "))
                if ch==1:
                    print("Number of correct answers: ",self.correct)
                    print("EXITING....")
                    b=True
                    break
                if ch==2:
                    while True:
                        n=random.randint(1,upper)
                        if self.checkifdone(n)==False:        
                            break
                     
                    string=self.extract(n)
                    Q1,ans=self.formquestion(string)
                     
                    print(Q1)
                    answer=input("Answer:")
                    if answer==ans:
                        print("Good Job")
                        self.correct=self.correct+1
                    else:
                        print("Wrong answer! Answer =",ans)
                    self.markasdone(n) 

        if b==False:
            newreset()
        break

def physicsworksheet(): #variables: n=random question number; b=flag to exit loop and module mathworksheet;file=variable opening file,Q1 = question extracted
    print("INSTRUCTIONS: \n *Do not leave spaces. \n *All answers must be in Upper case, unless otherwise mentioned.") 
    global b
    b=False
    import random
    upper=10 #Number of questions from .txt
    
    while b==False:
        
        def newreset(): #To reset setting
            obj=physics()
            obj.start()
            
        class physics():   #To store current data when module is called
            def __init__(self):
                g=int(input("Enter your grade: \n1 for IGCSE  \n2 for As and A level: "))

                if g==1:
                     
                    self.grade='physics ig.txt'
                else:
                     
                    self.grade='physics A LEVEL.txt'
                
                self.markedasdone=[]
                 
                self.file=open( self.grade ,'r')

                self.correct=0

            def markasdone(self,n):  #to mark the completed questions
                self.markedasdone.append(n)
                if len(self.markedasdone)==upper:
                    print("Number of correct answers: ",self.correct) 
                    print("All question sets solved! RESET...")
                    newreset()

            def checkifdone(self,n):   #To check if question extracted is solved
                done=False
                for i in range(0,len(self.markedasdone)):
                    if self.markedasdone[i]==n:
                        done=True
                return done
            
            def extract(self,n):     #extracting from .txt file
                string=''
                for i in range(0,n):
                    string=self.file.readline()
                self.file.close()
                self.file=open(self.grade,'r')
                return string

            def formquestion(self,string):    #to form question and the answer
                Q1=''
                ans=''
                
                while True:
                    for i in range(0,len(string)):
                        if string[i]==string[i+1] and string[i+1]==string[i+2] and string[i]=='*':
                            y=i+4
                            break
                        Q1=Q1+string[i]
                    break
                
                while True:
                    for i in range(y, len(string)-5):
                        ans=ans+string[i]
                    break
                return Q1,ans

            def start(self):   #start function
              while True:  
                ch=int(input("Press 1 to exit OR 2 to continue: "))
                if ch==1:
                    print("Number of correct answers: ",self.correct)
                    print("EXITING....")
                    b=True
                    break
                if ch==2:
                    while True:
                        n=random.randint(1,upper)
                        if self.checkifdone(n)==False:
                            break
                    string=self.extract(n)
                    Q1,ans=self.formquestion(string)
                    print(Q1)
                    answer=input("Answer:")
                    if answer==ans:
                        print("Good Job")
                        self.correct=self.correct+1
                    else:
                        print("Wrong answer! Answer =",ans)
                    self.markasdone(n) 
        if b==False:
            newreset()
        break

import time

subject=["English", "Maths", "Physics", "Chemistry", "Biology", "Economics","RETURN"]
repeat=True
while repeat==True:
    print("===================================================================")
    text="Welcome to your personal study assistant!!\n"
    for index in range(len(text)):
        waiting(1, text[index], 0.01)
    print("===================================================================\n\n")
    waiting(1, "\n", 1)
    
    text="THINGS YOU CAN EXPLORE"
    for index in range(len(text)):
        waiting(1, text[index], 0.01)
    text1="\n1. Get prepared for school deadlines\n"
    text2="2. Get study materials\n"
    text3="3. Close App\n\n"
    for index in range(len(text1)):
        waiting(1, text1[index], 0.01)
    for index in range(len(text2)):
        waiting(1, text2[index], 0.01)
    for index in range(len(text3)):
        waiting(1, text3[index], 0.01)
    choice1=input("Your Choice? :")

    choice1_flag=False
    while choice1_flag==False:
        if choice1=="1" or choice1=="2" or choice1=="3":
            choice1_flag=True
        else:
            choice1=input("Incorrect choice. Please choose again:")

    if choice1=="1":
        file=open("CodeFest_data.txt","r")
        line=file.readline()
        if len(line)==0:
            array_of_tasks=[]
            array_of_deadlines=[]
            continue_flag=True
            array_of_tasks, array_of_deadlines= Planner_Inputs(array_of_tasks, array_of_deadlines, continue_flag)
            array_of_deadlines=conversion_to_datetime(array_of_deadlines)
            schedule(array_of_tasks, array_of_deadlines)
            reminder(array_of_tasks, array_of_deadlines)
        else:
            array_of_tasks, array_of_deadlines=retrieve()
            option_flag=False
            while option_flag==False:
                option=input("If you want to add more tasks to planner? (options:'y' or 'n'):")
                if option=="n":
                    continue_flag=False
                    option_flag=True
                elif option=="y":
                    continue_flag=True
                    option_flag=True
            array_of_tasks, array_of_deadlines= Planner_Inputs(array_of_tasks, array_of_deadlines, continue_flag)
            array_of_deadlines=conversion_to_datetime(array_of_deadlines)
            schedule(array_of_tasks, array_of_deadlines)
            reminder(array_of_tasks, array_of_deadlines)
        array_of_deadlines=conversion_to_string(array_of_deadlines)
        saving(array_of_tasks, array_of_deadlines)
        file.close()

    elif choice1=="2":
        text="Subjects to choose from:\n"
        for index in range(len(text)):
            waiting(1, text[index], 0.01)
            
        for index in range(len(subject)):
            text=str(index+1)+"."+subject[index]+"\n"
            for index in range(len(text)):
                waiting(1, text[index], 0.01)
        choice2=input("Your Choice? :")
        choice2_flag=False
        while choice2_flag==False:
            if choice2=="1" or choice2=="2" or choice2=="3" or choice2=="4" or choice2=="5" or choice2=="6" or choice2=="7":
                choice2_flag=True
            else:
                choice2=input("Incorrect choice. Please choose again:")
        if choice2=="1":
            #------------------------------------------------------------------------------------call ENGLISH function
            english()          #for understanding purpose
        elif choice2=="2":
            #------------------------------------------------------------------------------------call MATHS function
            mathworksheet()           #for understanding purpose
        elif choice2=="3":
            #------------------------------------------------------------------------------------call PHYSICS function
            physicsworksheet()        #for understanding purpose
        elif choice2=="4":
            #------------------------------------------------------------------------------------call CHEMISTRY function
            chemworksheet()       #for understanding purpose
        elif choice2=="5":
            #------------------------------------------------------------------------------------call BIOLOGY function
            biologyworksheet()          #for understanding purpose
        elif choice2=="6":
            #------------------------------------------------------------------------------------call ECONOMICS function
            economicsworksheet()        #for understanding purpose
        elif choice2=="7":
            None
    elif choice1=="3":
        repeat=False
print("Thank you ")                                           

'''800 LINESSSSS'''
