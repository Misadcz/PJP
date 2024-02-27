def checking(var):
    char = False
    for i in range(0, len(var)):
        if var[i] in identifiers:
            print('ID:' + var)
            char = True
            break
    if char == False:
        print('NUM:' + var)


lines = []

with open('testuj.txt') as f:
    line = f.readline()
    while line:
        lines.append(line)
        line = f.readline()




operators = ['+', '-', '*','/']
keywords = ['div','mod']
var = ''
identifiers = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
for line in lines:
    for i in range(0, len(line)):
        
        if line[i] in identifiers or line[i] in numbers:
            var += line[i]
            if i == len(line) - 1 and var != '':
                checking(var)    
            continue
        
        if var != '':
            if var not in keywords:
                checking(var)
            else:
                print(var.upper())
        var = ''
        if line[i] == '/' and line[i+1] == '/':
            break
        if line[i] in operators:
            print('OP:' + line[i])
        temp = line[i:i+3]
        if line[i] == ';':
            print('SEMICOLON')
        if line[i] == '(':
            print('LPAR')
        if line[i] == ')':
            print('RPAR')