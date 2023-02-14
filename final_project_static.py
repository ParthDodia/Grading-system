grades = {
"english":[90,95,81],
"math" : [100,95,92,98],
"history" : [76,98]
}

def main():
    print('your grade manager contains grade for: \n')
    for i in grades:
        print(f"> {i}")
    step1()

def step1():
    print(f"\nwhich class would you like to work with or 'end' to finish (",end='')
    for i in grades:
        print(f"{i} ",end=' ')
    print("):",end=' ')
    while True:    
        a = input()
        try:    
            if a.lower()=='end':
                terminate()
            elif a.lower() in grades:
                step2(a)
            else:
                raise ValueError('Invalid Input')
        except ValueError as excpt:
            print(excpt)
            print('Enter a valid input to continue. ',end='')

def step2(a):
    print('*'*35)
    print('reporting or maintenance')
    print("\n1 = reporting")
    print("2 = maintenance")
    print("0 = exit")
    while True:
        b = input("which function : ")
        #print(a)
        try:
            if b=='1':
                reporting(a)
            elif b=='2':
                maintenance(a)
            elif b=='0':
                step1()
            else:
                raise ValueError('Invalid Input')
        except ValueError as excpt:
            print(excpt)
            print('Enter a valid input to continue.\n')

def terminate():
    print("finished processing grades")
    for i in grades:
        print(f"{i}")
    #print(grades)
    exit()

def reporting(a):
    print("*"*30)
    print("*"+"grade reporting".center(28)+"*")
    print("*"*30+'\n')
    for i in grades:
        if a==i:
            z=grades[i]
    #print(z)
    while True:
        c = input("Command (best worst average end summary): ")
        try:
            if c.lower()=='best':
                print(f"\nyour best score in {a} was: {max(z)}")
            elif c.lower()=='worst':
                print(f"\nyour worst score in {a} was: {min(z)}")
            elif c.lower()=='average':
                print(f"\nyour average score in {a} was: {round((sum(z)/len(z)),2)}")
            elif c.lower()=='summary':
                print('grades in class: ',end='')
                for x in z:
                    print(x,end=' ')
                print('\n')
            elif c.lower()=='end':
                step2(a)
            else:
                raise ValueError("Invalid Input")
        except ValueError as excpt:
            print(excpt)
            print('Enter a valid input to continue.\n') 

def maintenance(a):
    print("*"*30)
    print(f"Maintaining grades for {a}\n")
    for i in grades:
        if a==i:
            z=grades[i]
    print('currently the grades are: ',end='')
    for i in z:
        print(i,end=' ')
    print('\n')
    while True:
        print("1) change a grade")
        print("2) add a grade")
        print("3) delete a grade")
        print("4) end")
        c = input("what would you like to do: ")
        if c=='4':
            step2(a)
        try:
            if c=='1':
                b=int(input('which grade should be changed: '))
                if b not in z:
                    raise ValueError('Grade not found')
                else:
                    d = z.index(b)
                    f=int(input('what is the new grade :'))
                    z[d] = f
                print('updated grades are: ',end='')
                for i in z:
                    print(i,end=' ')
                print('\n')
            elif c=='2':
                x = input('what is the new grade: ')
                if x.isdigit():
                    x=int(x)
                    if x>0 and x<=100:
                        z.append(x)
                        print(f"ok, {a} now has the following grades:")
                        for i in z:
                            print(i,end=' ')
                        print('\n')
                    else:
                        raise ValueError("Grade cannot exceed 100") 
                        #print(grades)
                else:
                    raise TypeError('Invalid input')
                print('updated grades are: ',end='')
                for i in z:
                    print(i,end=' ')
                print('\n')
            elif c=='3':
                x = int(input('which grade should be deleted: '))
                if x not in z:
                    raise ValueError('Grade not found')
                else:
                    for i in z:
                        if x==i:
                            z.remove(i)
                print('updated grades are: ',end='')
                for i in z:
                    print(i,end=' ')
                print('\n')
            else:
                raise ValueError('Invalid input')                   
        except ValueError as excpt:
            print(excpt)
            print('Enter a valid input to continue.\n')
            print('current grades are: ',end='')
            for i in z:
                print(i,end=' ')
            print('\n')
   
if __name__=="__main__":
    main()
