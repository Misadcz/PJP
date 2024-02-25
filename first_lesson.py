
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
        for i in range(1,len(lst)-1):
            if lst[i-1] == '(' and lst[i+1] == ')':
                lst[i-1] = 'x'
                lst[i+1] = 'x'
                lst = deleter(lst)
                repeat = True
    return lst

n = int(input())

all = []

for i in range(n):
    inp  = input()
    all.append(inp)

for i in range(len(all)):
    inp = ""
    inp = all[i]

    inp = inp.replace(" ","")
    inp = list(inp.strip())
    reset = False
    
    for i in range(len(inp)):
        if inp[i] =='+' or inp[i] == '-' or inp[i] == "*" or inp[i] == "/":
            if inp[i+1] == '+' or inp[i+1] == '-' or inp[i+1] == '*' or inp[i+1] == '/':
                print('ERROR')
                reset = True
    if reset == True:
        continue
            
    check_lst = ['0','1','2','3','4','5','6','7','8','9','(',')','+','-','*','/']
    reset = False
    for i in inp:
        if i not in check_lst:
            print('ERROR')
            reset = True
            break
    if reset == True:
        continue
    
    lst = []

    num = ''
    for i in inp:
        if i.isdigit():
            num += i
        else:
            if num != '':
                lst.append(num)
                num = ''
            lst.append(i)
    if num != '':
        lst.append(num)

    if len(lst) < 3:
        if lst[0] =='-':
            print("ERROR")
            continue
    if(len(lst)) < 2:
        print(lst[0])
        continue
    
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
           # print(lst)
            lst = deleter(lst)
        lst = bracket_checker(lst)    
    print(lst[0])
