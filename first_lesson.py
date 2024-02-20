
def deleter(lst):
    found = 0
    for i in range(len(lst)):
        if lst[i] == 'x':
            found += 1
    for i in range(found):
        lst.remove('x')
    return lst

def bracket_checker(lst):
    repeat = True
    while repeat==True :
        repeat = False
        for i in range(len(lst)-1):
            if lst[i-1] == '(' and lst[i+1] == ')':
                lst[i-1] = 'x'
                lst[i+1] = 'x'
                lst = deleter(lst)
                repeat = True
    return lst

n = int(input())

all = []

for i in range(2):
    input  = str(input())
    all.append(input)
#TADY JE PROBLEM


for i in range(len(all)):
    input = all[i]

    input = input.replace(" ","")
    input = list(input.strip())

    lst = []

    num = ''
    for i in input:
        if i.isdigit():
            num += i
        else:
            if num != '':
                lst.append(num)
                num = ''
            lst.append(i)
    if num != '':
        lst.append(num)

    # print(lst)

    if len(lst) < 3:
        if lst[0] =='-':
            print("ERROR")
            exit()
    if(len(lst)) < 2:
        print(lst[0])
        exit()


    while len(lst) > 1:        
            
        l = len(lst)-1
        i = 0
        while i < l:
            if lst[i+1].isdigit() and lst[i-1].isdigit():
                if lst[i] == '*':
                    temp = int(lst[i-1]) * int(lst[i+1])
                    lst[i] = str(temp)
                    lst[i+1]='x'
                    lst[i-1]='x'
                    l -= 2
                    i = 0
                elif lst[i] == '/':
                    temp = int(int(lst[i-1]) / int(lst[i+1]))
                    lst[i] = str(temp)
                    lst[i+1]='x'
                    lst[i-1]='x'
                    l -= 2
                    i = 0
            i+=1    
            # print(lst)
            lst = deleter(lst)
            
        lst = bracket_checker(lst)
        # print(lst)

        l = len(lst)-1

        i = 0
        while i < l:
            if lst[i+1].isdigit() and lst[i-1].isdigit():
                if lst[i] == '+':
                    if len(lst)> 3:
                            if lst[i+2] != '*' and lst[i+2] != '/':
                                if lst[i-2] != '*' and lst[i-2] != '/':
                                    temp = int(lst[i-1]) + int(lst[i+1])
                                    lst[i] = str(temp)
                                    lst[i+1]='x'
                                    lst[i-1]='x'
                                    l -= 2
                                    i = 0
                    else:
                        temp = int(lst[i-1]) + int(lst[i+1])
                        lst[i] = str(temp)
                        lst[i+1]='x'
                        lst[i-1]='x'
                        l -= 2
                        i = 0
                elif lst[i] == '-':
                    if len(lst)> 3:
                            if lst[i+2] != '*' and lst[i+2] != '/':
                                if lst[i-2] != '*' and lst[i-2] != '/':
                                    temp = int(lst[i-1]) - int(lst[i+1])
                                    lst[i] = str(temp)
                                    lst[i+1]='x'
                                    lst[i-1]='x'
                                    l -= 2
                                    i = 0  
                    else:
                        temp = int(lst[i-1]) - int(lst[i+1])
                        lst[i] = str(temp)
                        lst[i+1]='x'
                        lst[i-1]='x'
                        l -= 2
                        i = 0
            i+=1    
            print(lst)
            lst = deleter(lst)
        lst = bracket_checker(lst)    
    print(lst)
