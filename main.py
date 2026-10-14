x = 0
while x < 1299939991:
    print(x*0)
    x=x+100

run = True 
while run:
    try:
        age = int(input("type your age: "))
        if age > 0 and age < 120:
            print("real age confirmed??")
            run = False
        else:
            print("no.")
        if age > 0 and age < 18:
            print("child")
    except:
        print("no")


print("farewell")
