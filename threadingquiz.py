from time import *
import threading
score = 0
def countdown():
    global mytimer
    mytimer = 60
    for x in range(60):
        mytimer = mytimer - 1
        sleep(1)
    print("Out of Time")
    print(f'you scored {score}/100')
countdown_thread = threading.Thread(target = countdown)
countdown_thread.start()


try:
    while mytimer > 0:
        name = input("Enter the Name::::")
        print("Are you ready for the quiz",name)
        confirm = input("<<<<<Yes or NO >>>>>")
        print("You have 5 minutes to complete the quiz... ")
        if confirm == "Yes":
            print("*****************************************")
            print("|-------|COMPUTER BASED QUESTIONS|------|")
            print("*****************************************")
            print("Question :: 1")
            print("-----------------------------------------")
            print("Who is the Father of Computer?")
            print("a ::Einsten")
            print("b ::Jeraald")
            print("c ::Charles Babbage")
            print("d ::Michael Faraday")
            ans = input("Enter the answer(a,b,c,d):::")
            print("-----------------------------------------")
            if ans == "c":
                print(f'{ans} is the Correct Answer')
                score = score +20
                print("Score for First Question::::",score)
                print(mytimer,"seconds remains!!!!")
               
            else:
                print("Incorrect answer::::C is the correct Answer")
                print("Score for First Question::::",score)
                print(mytimer,"seconds remains!!!!")
               
            print()
            sleep(1.0)
            if mytimer==0:
                break
            print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")   
            
            print("Question :: 2")
            print("-----------------------------------------")
            print("Full Form of ::CPU?")
            print("a ::Control Processing Unit")
            print("b ::Central Processing Unit")
            print("c ::Control Processed Unit")
            print("d ::Centrak Process Unit")
            ans = input("Enter the answer(a,b,c,d):::")
            print("-----------------------------------------")
            if ans == "a":
                print(f'{ans} is the Correct Answer')
                score = score +20
                print("Score for Second Question::::",score)
                print(mytimer,"seconds remains!!!")
            else:
                print("Incorrect answer::::A is the correct Answer")
                print("Score for Second Question::::",score)
                print(mytimer,"seconds remains!!!")
            print()
            if mytimer==0:
                break
            print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
               

            print("Question :: 2")
            print("-----------------------------------------")
            print("which command is used to select the whole document?")
            print("a ::Ctrl+B")
            print("b ::Ctrl+V")
            print("c ::Ctrl+C")
            print("d ::Ctrl+A")
            ans = input("Enter the answer(a,b,c,d):::")
            print("-----------------------------------------")
            if ans == "d":
                print(f'{ans} is the Correct Answer')
                score = score +20
                print("Score for Third Question::::",score)
                print(mytimer,"seconds remains!!!")
            else:
                print("Incorrect answer::::D is the correct Answer")
                print("Score for Third Question::::",score)
                print(mytimer,"seconds remains!!!")

            if mytimer==0:
                break
            print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")   
    
            print("Question :: 4")
            print("-----------------------------------------")
            print("Full Form of ::NOS in Computer?")
            print("a ::New Old Stock")
            print("b ::Network Operating System")
            print("c ::Not Otherwise Specified")
            print("d ::National  Occean Service")
            ans = input("Enter the answer(a,b,c,d):::")
            print("-----------------------------------------")
            if ans == "b":
                print(f'{ans} is the Correct Answer')
                score = score +20
                print("Score for Fourth Question::::",score)
                print(mytimer,"seconds remains!!!")
            else:
                print("Incorrect answer::::B is the correct Answer")
                print("Score for Fourth Question::::",score)
                print(mytimer,"seconds remains!!!")
            print()
            if mytimer==0:
                break
            print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")      

            print("Question :: 5")
            print("-----------------------------------------")
            print("What does RAM stand for?")
            print("a ::Non of Below")
            print("b ::Remote Access Memory")
            print("c ::Reallocate Automatic Memory")
            print("d ::Random Access Memory")
            ans = input("Enter the answer(a,b,c,d):::")
            print("-----------------------------------------")
            if ans == "d":
                print(f'{ans} is the Correct Answer')
                score = score +20
                print("Score for Fifth Question::::",score)
                print(mytimer,"seconds remains!!!")
            else:
                print("Incorrect answer::::D is the correct Answer")
                print("Score for Fifth Question::::",score)
                print(mytimer,"seconds remains!!!")
            print()
            if mytimer==0:
                break
            print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")      

            print(f'Total Score of {name} is {score}/100 in {mytimer} seconds!!')
            print("*****************************************")
            print("---------------THANK YOU-----------------")
            print("*****************************************")

            exit()  
        else:
            print("Thanks for the response!!!!")

        exit()
except TypeError:
    print("invalid choice!!!")

except IndexError:
    print("Something Wrong!!!")
finally:
    print("Nothing Went Wrong!!!!")
    


