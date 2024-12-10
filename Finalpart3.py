#Theo Gonong, Kevin Henderson, Anthony Le
#Final Project part 3

table = {"p" : {"program" : ["program", "I", ";", "var", "dl", "begin", "sl", "end"]},
         "I" : {"a" : ["L" ,"X"], "b" : ["L" ,"X"], "c" : ["L" ,"X"], "d" : ["L" ,"X"], "l" : ["L" ,"X"], "f" : ["L" ,"X"]},
         "X": {";" : ["λ"], "," : ["λ"], ":" : ["λ"] , "=": ["λ"], "+" : ["λ"], "-" : ["λ"], "*" : ["λ"], "/" : ["λ"], ")": ["λ"], "$" : ["λ"], "a" : ["L" ,"X"], "b" : ["L" ,"X"], "c" : ["L" ,"X"], "d" : ["L" ,"X"], "l" : ["L" ,"X"], "f" : ["L" ,"X"], "0" : ["digit" ,"X"], "1" : ["digit" ,"X"], "2" : ["digit" ,"X"], "3" : ["digit" ,"X"], "4" : ["digit" ,"X"], "5" : ["digit" ,"X"], "6" : ["digit" ,"X"], "7" : ["digit" ,"X"], "8" : ["digit" ,"X"], "9" : ["digit" ,"X"]},
         "dl" : {"a" : ["dec", ":", "type", ";"], "b" : ["dec", ":", "type", ";"], "c" : ["dec", ":", "type", ";"], "d" : ["dec", ":", "type", ";"], "l" : ["dec", ":", "type", ";"], "f" : ["dec", ":", "type", ";"]},
         "dec" : {"a" : ["I", ",", "dec"], "b" : ["I", ",", "dec"], "c" : ["I", ",", "dec"], "d" : ["I", ",", "dec"], "l" : ["I", ",", "dec"], "f" : ["I", ",", "dec"]},
         "type" : {"integer" : ["integer"]},
         "sl" : {"print" : ["stat", "sl"], "a" : ["stat", "sl"], "b" : ["stat", "sl"], "c" : ["stat", "sl"], "d" : ["stat", "sl"], "l" : ["stat", "sl"], "f" : ["stat", "sl"]},
         "stat" : {"print" : ["wr"], "a" : ["as"], "b" : ["as"], "c" : ["as"], "d" : ["as"], "l" : ["as"], "f" : ["as"]},
         "wr" : {"print" : ["print","(", "str", "I",")",";"]},
         "str" : {'"value=",' : ['"value=",'], "a" : ["λ"], "b" : ["λ"], "c" : ["λ"], "d" : ["λ"], "l" : ["λ"], "f" : ["λ"]},
         "as" : {"a" : ["id", "=", "E", ";"], "b" : ["id", "=", "E", ";"], "c" : ["id", "=", "E", ";"], "d" : ["id", "=", "E", ";"], "l" : ["id", "=", "E", ";"], "f" : ["id", "=", "E", ";"]},
         "E" : {"a" : ["T" ,"Q"], "b" : ["T" ,"Q"], "c" : ["T" ,"Q"], "d" : ["T" ,"Q"], "l" : ["T" ,"Q"], "f" : ["T" ,"Q"], "0" : ["T" ,"Q"], "1" : ["T" ,"Q"], "2" : ["T" ,"Q"], "3" : ["T" ,"Q"], "4" : ["T" ,"Q"], "5" : ["T" ,"Q"], "6" : ["T" ,"Q"], "7" : ["T" ,"Q"], "8" : ["T" ,"Q"], "9" : ["T" ,"Q"], "+" : ["T" ,"Q"], "-" : ["T" ,"Q"], "(" : ["T" ,"Q"]},
         "Q" : {";" : ["λ"], ")" : ["λ"],"+" : ["+", "T" ,"Q"], "-" : ["-", "T" ,"Q"]},
         "T" : {"a" : ["F" ,"R"], "b" : ["F" ,"R"], "c" : ["F" ,"R"], "d" : ["F" ,"R"], "l" : ["F" ,"R"], "f" : ["F" ,"R"], "0" : ["F" ,"R"], "1" : ["F" ,"R"], "2" : ["F" ,"R"], "3" : ["F" ,"R"], "4" : ["F" ,"R"], "5" : ["F" ,"R"], "6" : ["F" ,"R"], "7" : ["F" ,"R"], "8" : ["F" ,"R"], "9" : ["F" ,"R"], "+" : ["F" ,"R"], "-" : ["F" ,"R"], "(" : ["F" ,"R"]},
         "R" : {";" : ["λ"], "+" : ["λ"], "-" : ["λ"], ")" : ["λ"], "*" : ["*","F", "R"], "/" : ["/","F", "R"]},
         "F" : {"a" : ["I"], "b" : ["I"], "c" : ["I"], "d" : ["I"], "l" : ["I"], "f" : ["I"], "0" : ["num"], "1" : ["num"], "2" : ["num"], "3" : ["num"], "4" : ["num"], "5" : ["num"], "6" : ["num"], "7" : ["num"], "8" : ["num"], "9" : ["num"], "+" : ["num"], "-" : ["num"], "(" : ["(", "E", ")"]},
         "num" : {"0" : ["sign", "digit", "D"], "1" : ["sign", "digit", "D"], "2" : ["sign", "digit", "D"], "3" : ["sign", "digit", "D"], "4" : ["sign", "digit", "D"], "5" : ["sign", "digit", "D"], "6" : ["sign", "digit", "D"], "7" : ["sign", "digit", "D"], "8" : ["sign", "digit", "D"], "9" : ["sign", "digit", "D"], "+" : ["sign", "digit", "D"], "-" : ["sign", "digit", "D"]},
         "D" : {";" : ["λ"], "+" : ["λ"], "-" : ["λ"], "*" : ["λ"], "/" : ["λ"], ")": ["λ"], "0" : ["digit", "D"], "1" : ["digit", "D"], "2" : ["digit", "D"], "3" : ["digit", "D"], "4" : ["digit", "D"], "5" : ["digit", "D"], "6" : ["digit", "D"], "7" : ["digit", "D"], "8" : ["digit", "D"], "9" : ["digit", "D"]},
         "sign" : {"0" : ["λ"], "1" : ["λ"], "2" : ["λ"], "3" : ["λ"], "4" : ["λ"], "5" : ["λ"], "6" : ["λ"], "7" : ["λ"], "8" : ["λ"], "9" : ["λ"], "+" : ["+"], "-" : ["-"]},
         "digit" : {"0" : ["0"], "1" : ["1"], "2" : ["2"], "3" : ["3"], "4" : ["4"], "5" : ["5"], "6" : ["6"], "7" : ["7"], "8" : ["8"], "9" : ["9"]},
         "L" : {"a" : ["a"], "b" : ["b"], "c" : ["c"], "d" : ["d"], "l" : ["l"], "f" : ["f"]}}

progerr = False
varerr = False
begerr = False
enderr = False
interr = False
printerr = False
semierr = False #;
comerr = False
perierr = False
openparerr = False
closeparerr = False
hassemi = False
readdollar = False
hascomma = False
with open("final24.txt", 'r') as f:
    stack = []
    stack.append("$")
    stack.append("p")
    for line in f:

        for word in line.split():
            read = False
            while read == False:
                match stack[-1]:
                    case 'p':
                        stack.pop()
                        match word:
                            case "program":
                                for x in reversed(table['p']['program']):
                                    stack.append(x)
                            case _:
                                for x in reversed(table['p']['program']):
                                    if x != "program":
                                        stack.append(x)
                                    else:
                                        break
                                progerr = True

                    case 'I':
                        stack.pop()
                        match word[0]:
                            case 'a':
                                for x in reversed(table['I']['a']):
                                    stack.append(x)
                            case 'b':
                                for x in reversed(table['I']['b']):
                                    stack.append(x)
                            case 'c':
                                for x in reversed(table['I']['c']):
                                    stack.append(x)
                            case 'd':
                                for x in reversed(table['I']['d']):
                                    stack.append(x)
                            case 'l':
                                for x in reversed(table['I']['l']):
                                    stack.append(x)
                            case 'f':
                                for x in reversed(table['I']['f']):
                                    stack.append(x)
                            case _:
                                pass #for now
                        for char in range(len(word)):
                            readchar = False
                            while readchar == False:
                                match stack[-1]:
                                    case 'L':
                                        stack.pop()
                                        match word[char]:
                                            case 'a':
                                                for x in reversed(table['L']['a']):
                                                    stack.append(x)
                                            case 'b':
                                                for x in reversed(table['L']['b']):
                                                    stack.append(x)
                                            case 'c':
                                                for x in reversed(table['L']['c']):
                                                    stack.append(x)
                                            case 'd':
                                                for x in reversed(table['L']['d']):
                                                    stack.append(x)
                                            case 'l':
                                                for x in reversed(table['L']['l']):
                                                    stack.append(x)
                                            case 'f':
                                                for x in reversed(table['L']['f']):
                                                    stack.append(x)
                                            case _:
                                                pass #for now
                                    case "X":
                                        stack.pop()
                                        match word[char]:
                                            case '1':
                                                for x in reversed(table['X']['1']):
                                                    stack.append(x)
                                            case '2':
                                                for x in reversed(table['X']['2']):
                                                    stack.append(x)
                                            case '3':
                                                for x in reversed(table['X']['3']):
                                                    stack.append(x)
                                            case '4':
                                                for x in reversed(table['X']['4']):
                                                    stack.append(x)
                                            case '5':
                                                for x in reversed(table['X']['5']):
                                                    stack.append(x)
                                            case '6':
                                                for x in reversed(table['X']['6']):
                                                    stack.append(x)
                                            case '7':
                                                for x in reversed(table['X']['7']):
                                                    stack.append(x)
                                            case '8':
                                                for x in reversed(table['X']['8']):
                                                    stack.append(x)
                                            case '9':
                                                for x in reversed(table['X']['9']):
                                                    stack.append(x)
                                            case '0':
                                                for x in reversed(table['X']['0']):
                                                    stack.append(x)
                                            case 'a':
                                                for x in reversed(table['X']['a']):
                                                    stack.append(x)
                                            case 'b':
                                                for x in reversed(table['X']['b']):
                                                    stack.append(x)
                                            case 'c':
                                                for x in reversed(table['X']['c']):
                                                    stack.append(x)
                                            case 'd':
                                                for x in reversed(table['X']['d']):
                                                    stack.append(x)
                                            case 'l':
                                                for x in reversed(table['X']['l']):
                                                    stack.append(x)
                                            case 'f':
                                                for x in reversed(table['X']['f']):
                                                    stack.append(x)
                                            case ';':
                                                stack.append(table['X'][';'][0])
                                                # read = True
                                                hassemi = True
                                            case ',':
                                                stack.append(table['X'][','][0])
                                            case ':':
                                                stack.append(table['X'][':'][0])
                                            case '=':
                                                stack.append(table['X']['='][0])
                                            case '+':
                                                stack.append(table['X']['+'][0])
                                            case '-':
                                                stack.append(table['X']['-'][0])
                                            case '*':
                                                stack.append(table['X']['*'][0])
                                            case '/':
                                                stack.append(table['X']['/'][0])
                                            case ')':
                                                stack.append(table['X'][')'][0])
                                            case '$':
                                                stack.append(table['X']['$'][0])
                                            case _:
                                                pass
                                    case "digit":
                                        stack.pop()
                                        match word[char]:
                                            case '1':
                                                for x in reversed(table['digit']['1']):
                                                    stack.append(x)
                                            case '2':
                                                for x in reversed(table['digit']['2']):
                                                    stack.append(x)
                                            case '3':
                                                for x in reversed(table['digit']['3']):
                                                    stack.append(x)
                                            case '4':
                                                for x in reversed(table['digit']['4']):
                                                    stack.append(x)
                                            case '5':
                                                for x in reversed(table['digit']['5']):
                                                    stack.append(x)
                                            case '6':
                                                for x in reversed(table['digit']['6']):
                                                    stack.append(x)
                                            case '7':
                                                for x in reversed(table['digit']['7']):
                                                    stack.append(x)
                                            case '8':
                                                for x in reversed(table['digit']['8']):
                                                    stack.append(x)
                                            case '9':
                                                for x in reversed(table['digit']['9']):
                                                    stack.append(x)
                                            case '0':
                                                for x in reversed(table['digit']['0']):
                                                    stack.append(x)
                                    case 'λ':
                                        #might cause problems - MAYBE NOT?
                                        readchar = True
                                        stack.pop()
                                        
                                    case _:
                                        readchar = True
                                        stack.pop()
                                        

                    case ";":
                        stack.pop()
                        if hassemi == False:
                            semierr = True
                        read = True
                    case "var":
                        if line != "var":
                            varerr = True
                        stack.pop()
                        read = True
                    case "dl":
                        stack.pop()
                        match word[0]:
                            case 'a':
                                for x in reversed(table['dl']['a']):
                                    stack.append(x)
                            case 'b':
                                for x in reversed(table['dl']['b']):
                                    stack.append(x)
                            case 'c':
                                for x in reversed(table['dl']['c']):
                                    stack.append(x)
                            case 'd':
                                for x in reversed(table['dl']['d']):
                                    stack.append(x)
                            case 'l':
                                for x in reversed(table['dl']['l']):
                                    stack.append(x)
                            case 'f':
                                for x in reversed(table['dl']['f']):
                                    stack.append(x)
                            case _:
                                pass #for now
                        for w in line.split(): #NEED TO ITERATE THROUGH EVERY LETTER, NOT WORD
                            readword = False
                            print(w)
                            while readword == False:
                                print(stack)
                                print("looping!")
                                match stack[-1]:
                                    case "dec":                   
                                        stack.pop()
                                        match w:
                                            case 'a':
                                                for x in reversed(table["dec"]['a']):
                                                    stack.append(x)
                                            case 'b':
                                                for x in reversed(table["dec"]['b']):
                                                    stack.append(x)
                                            case 'c':
                                                for x in reversed(table["dec"]['c']):
                                                    stack.append(x)
                                            case 'd':
                                                for x in reversed(table["dec"]['d']):
                                                    stack.append(x)
                                            case 'l':
                                                for x in reversed(table["dec"]['l']):
                                                    stack.append(x)
                                            case 'f':
                                                for x in reversed(table["dec"]['f']):
                                                    stack.append(x)
                                            case _:
                                                pass #for now
                                    case 'I':
                                        stack.pop()
                                        match w:
                                            case 'a':
                                                for x in reversed(table['I']['a']):
                                                    stack.append(x)
                                            case 'b':
                                                for x in reversed(table['I']['b']):
                                                    stack.append(x)
                                            case 'c':
                                                for x in reversed(table['I']['c']):
                                                    stack.append(x)
                                            case 'd':
                                                for x in reversed(table['I']['d']):
                                                    stack.append(x)
                                            case 'l':
                                                for x in reversed(table['I']['l']):
                                                    stack.append(x)
                                            case 'f':
                                                for x in reversed(table['I']['f']):
                                                    stack.append(x)
                                            case _:
                                                pass #for now
                                    case 'L':
                                        stack.pop()
                                        print(w)
                                        match w:
                                            case 'a':
                                                for x in reversed(table['L']['a']):
                                                    stack.append(x)
                                            case 'b':
                                                for x in reversed(table['L']['b']):
                                                    stack.append(x)
                                            case 'c':
                                                for x in reversed(table['L']['c']):
                                                    stack.append(x)
                                            case 'd':
                                                for x in reversed(table['L']['d']):
                                                    stack.append(x)
                                            case 'l':
                                                for x in reversed(table['L']['l']):
                                                    stack.append(x)
                                            case 'f':
                                                for x in reversed(table['L']['f']):
                                                    stack.append(x)
                                            case _:
                                                pass #for now
                                    case "X":
                                        print("x!")
                                        stack.pop()
                                        match w:
                                            case '1':
                                                for x in reversed(table['X']['1']):
                                                    stack.append(x)
                                            case '2':
                                                for x in reversed(table['X']['2']):
                                                    stack.append(x)
                                            case '3':
                                                for x in reversed(table['X']['3']):
                                                    stack.append(x)
                                            case '4':
                                                for x in reversed(table['X']['4']):
                                                    stack.append(x)
                                            case '5':
                                                for x in reversed(table['X']['5']):
                                                    stack.append(x)
                                            case '6':
                                                for x in reversed(table['X']['6']):
                                                    stack.append(x)
                                            case '7':
                                                for x in reversed(table['X']['7']):
                                                    stack.append(x)
                                            case '8':
                                                for x in reversed(table['X']['8']):
                                                    stack.append(x)
                                            case '9':
                                                for x in reversed(table['X']['9']):
                                                    stack.append(x)
                                            case '0':
                                                for x in reversed(table['X']['0']):
                                                    stack.append(x)
                                            case 'a':
                                                for x in reversed(table['X']['a']):
                                                    stack.append(x)
                                            case 'b':
                                                for x in reversed(table['X']['b']):
                                                    stack.append(x)
                                            case 'c':
                                                for x in reversed(table['X']['c']):
                                                    stack.append(x)
                                            case 'd':
                                                for x in reversed(table['X']['d']):
                                                    stack.append(x)
                                            case 'l':
                                                for x in reversed(table['X']['l']):
                                                    stack.append(x)
                                            case 'f':
                                                for x in reversed(table['X']['f']):
                                                    stack.append(x)
                                            case ';':
                                                stack.append(table['X'][';'][0])
                                            case ',':
                                                stack.append(table['X'][','][0])
                                                hascomma = True
                                            case ':':
                                                stack.append(table['X'][':'][0])
                                            case '=':
                                                stack.append(table['X']['='][0])
                                            case '+':
                                                stack.append(table['X']['+'][0])
                                            case '-':
                                                stack.append(table['X']['-'][0])
                                            case '*':
                                                stack.append(table['X']['*'][0])
                                            case '/':
                                                stack.append(table['X']['/'][0])
                                            case ')':
                                                stack.append(table['X'][')'][0])
                                            case '$':
                                                stack.append(table['X']['$'][0])
                                            case _:
                                                pass
                                    case "digit":
                                        stack.pop()
                                        match word[char]:
                                            case '1':
                                                for x in reversed(table['digit']['1']):
                                                    stack.append(x)
                                            case '2':
                                                for x in reversed(table['digit']['2']):
                                                    stack.append(x)
                                            case '3':
                                                for x in reversed(table['digit']['3']):
                                                    stack.append(x)
                                            case '4':
                                                for x in reversed(table['digit']['4']):
                                                    stack.append(x)
                                            case '5':
                                                for x in reversed(table['digit']['5']):
                                                    stack.append(x)
                                            case '6':
                                                for x in reversed(table['digit']['6']):
                                                    stack.append(x)
                                            case '7':
                                                for x in reversed(table['digit']['7']):
                                                    stack.append(x)
                                            case '8':
                                                for x in reversed(table['digit']['8']):
                                                    stack.append(x)
                                            case '9':
                                                for x in reversed(table['digit']['9']):
                                                    stack.append(x)
                                            case '0':
                                                for x in reversed(table['digit']['0']):
                                                    stack.append(x)
                                    case 'λ':
                                        #might cause problems - MAYBE NOT?
                                        stack.pop()
                                    case ',':
                                        stack.pop()
                                        readword = True
                                        comerr = True
                                        
                                    case _:
                                        readword = True
                                        stack.pop()
                                        print(stack)
                        
                    case "begin":
                        print("here next")
                        stack.pop()
                        read = True
                    case "sl":
                        # print(stack)
                        break
                        
                    case "end":
                        pass #end loop somehow
                    case _:
                        readdollar = True
                        stack.pop()
                        read = True
        if hassemi == True or semierr == True and read == True:
            pass
        
        
         
        # if readdollar == True:
        #     break
    #if (make error messages)