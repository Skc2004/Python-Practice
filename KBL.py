def KBL():
    questions=["What is the Capital of India\n","Who is the Prime Minister of India\n","Who is the President of India\n","What is the name of brother of Thor in MCU\n"]
    options=["a.Kolkata \nb.Delhi \nc.New Delhi \nd.Chennai\n","a.Narendra Damodardas Modi \nb.Manmohan Singh \nc.Pappu Gandhi \nd.Lalu Yadav\n","a.Pranab Mukherjee \nb.APJ Abdul Kalam \nc.Draupadi Murmu \nd.Satyam Kumar Choudhary\n","a.Ben Strokes \nb.Zeus \nc.Odin \nd.Loki\n"]
    answers=['c','a','c','d']
    amount=[10000,20000,40000,80000,100000]
    winnings=0
    def c1():
        print("-: Choose from the following Modes :-\n")
        print("1. Editor Mode\n2. Player Mode\n")
        a=int(input("Enter your Choice :"))
        if(a==1):
            print("All Question along with with answers and options are :-\n")
            print("-----------------------------------------------------------------\n")
            for i in range(len(questions)):
                print(i," ",questions[i])
                print(options[i])
                print("Answer : ",answers[i])
            print("\n \n")
            def c2():
                print("1. Add a question\n","2. Remove a question\n")
                n=int(input("Enter your Choice :"))
                if(a==1):
                    questions.append(str(input("Enter your question : ")))
                    options.append(str(input("Enter the options (a to d) : ")))
                    answers.append(str(input("Enter the answer : ")))
                    print("\n")
                    def c4():
                        print("Choose from the following :- \n")
                        print("1.Continue in Editor Mode\n","2.Main Menu\n")
                        t=int(input("Enter your choice :"))
                        if(t==1):
                            c2()
                        elif(t==2):
                            c1()
                        else:
                            print("Invalid Input!!!")
                            c4()
                    c4()
                elif(a==2):
                    x=int(input("Enter index of the question to be removed :"))
                    questions.pop(x)
                    options.pop(x)
                    answers.pop(x)
                    print("\n")
                    def c5():
                        print("Choose from the following :- \n")
                        print("1.Continue in Editor Mode\n","2.Main Menu\n")
                        t=int(input("Enter your choice :"))
                        if(t==1):
                            c2()
                        elif(t==2):
                            c1()
                        else:
                            print("Invalid Input!!!")
                            c5()
                    c5()
                else:
                    print("Invalid Choice")
                    c2()
            c2()
        elif(a==2):
            print("-: LETS BEGIN THE GAME :-")
            winnings=0
            for i in range(len(questions)):
                print(i+1," ",questions[i],options[i])
                y=str(input("Enter your option :"))
                print("\n")
                if(y==answers[i]):
                    print("CORRECT ANSWER!!!!!!!\n")
                    winnings=winnings+amount[i]
                    print("\n")
                    def c3():
                        print("-: Choose from the following :- ")
                        print("1. Replay KBL\n","2. Exit KBL\n")
                        q=int(input("Enter your choice :"))
                        if(q==1):
                            KBL()
                        elif(q==2):
                            print("THANK YOU FOR PLAYING KBL !!!")
                            exit()
                        else:
                            print("Invalid Choice")
                            c3()
                else:
                    print("WRONG ANSWER!!!!!!!\n")
                    print("\n")
                    print("Total Winnings : ",winnings,"\n","\n")
                    c3()
            print("Total Winnings : ",winnings,"\n","\n")
            c3()
        else:
            print("Invalid Choice")
            c1()
    c1()
print("Welcome to KBL")
print("----------------------")
KBL()
