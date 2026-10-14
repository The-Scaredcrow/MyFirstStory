import random as r

slump= r.randint(1, 111111)

run=True
while (run):
    userinput = int(input("number 1-111111      "))
    try : 

        if (slump > userinput): 
            print("1. (if) variabeln är större")
            
        elif (slump < userinput): 
            print("2. (elif) variabeln är mindre")
            
        else: 
            print("3. (else) variabeln inehåller", slump,)

            run=False
    except:
        print("no")
        break
 
