# Enable logging for debugging

import logging

logging.basicConfig(level=logging.INFO)

def read_input_file(filename):
    with open(filename, 'r') as file:
        return file.read()
def tokenize(input_string):
    return input_string.replace("(", " ( ").replace(")", " ) ").split()

def predictive_parse(tokens, parsing_table, start_symbol):
    reserved_words = ["program", "var", "begin", "end", "integer", "print"] # ADDED BY ME
    stack = ["$", start_symbol]
    errors = []
    readtok = False
    print("tokens are: ",tokens)#FOR TESTING
    for token in tokens:
        
        print("TOKEN LOOP!!!")
        while stack[-1] != '$':
            if readtok == True:
                readtok = False
                break
            print(stack) #FOR TESTING
            print("token is:", token)#FOR TESTING
            top = stack.pop()
            print("top of stack:", top)
            if token == 'end':
                top = stack.pop()
                logging.info(f"Matched token: {token}")
                print(stack) #for testing
                continue

            if top == token:
                print("test") #FOR TESTING
                logging.info(f"Matched token: {token}")
                break  # Match terminal
            elif top in parsing_table:  # Non-terminal
                if top in reserved_words and token != top: #flags if any reserved words besides integer and print are missing
                    errors.append(f"{top} is expected")
                if token in parsing_table[top] and token in reserved_words:
                    print("!")
                    #token[0] added by me
                    stack.extend(reversed(parsing_table[top][token]))
                    logging.info(f"Expanded {top} -> {parsing_table[top][token]}")
                else:
                    for x in token:
                        if x == 'e':
                                errors.append(f"Unexpected token: {token} after {top}")
                                logging.error(f"Unexpected token: {token} after {top}")
                                return "Error detected in parsing"
                        if token == '“value=”,':
                            break
                        readword = False
                        # if top == "as": #test line
                        #     break
                        while readword == False:
                            print("character:", x)
                            print("top of stack:", top)
                            # if top == "R" and x == 'c': #test line due to Q grammar issue
                            # #     stack.pop()
                            # #     stack.pop()
                            #     #MAYBE UNCOMMENT
                            #     errors.append(f"Unexpected token: {token} after {top}")
                            #     logging.error(f"Unexpected token: {token} after {top}")
                            #     return "Error detected in parsing"

                            if top == "blank": #THIS LINE IS WHERE THE ISSUES START I THINK
                                #POTENTIALLY, FALSE READING 3 OR R HERE BECAUSE OF SIGN GRAMMAR(READS 3 ON BLANK INSTEAD OF MOVING TO DIGIT TO READ 3)
                                print("blankpop")#FOR TESTING
                                print(stack) #FOR TESTING
                                top = stack.pop()
                                if top == 'Q':
                                    if x in parsing_table[top]:
                                        stack.extend(reversed(parsing_table[top][x]))
                                        logging.info(f"Expanded {top} ->{x} {parsing_table[top][x]}")
                                        top = stack.pop()
                                    

                                else:
                                    readword = True #CAUSING SOME FALSE READINGS LATER ON IN SL!!!
                                # readword = True #CAUSING SOME FALSE READINGS LATER ON IN SL!!!
                                if top == "R": #test line due to Q grammar issue
                                    if x == "*":
                                        stack.extend(reversed(parsing_table[top][x]))
                                        logging.info(f"Expanded {top} ->{x} {parsing_table[top][x]}")
                                        top = stack.pop()
                                    else:
                                        top = stack.pop()
                                        top = stack.pop()
                                        print("R test")

                                # print(x)
                                # print(top) #FOR TESTING
                            elif x in parsing_table[top]:
                                index = tokens.index(token)
                                if tokens[index+1] == ":" and top == "dec":
                                    stack.extend(reversed(parsing_table[top][":"]))
                                    logging.info(f"Expanded {top} ->{x} {parsing_table[top][":"]}")
                                    print(stack) #FOR TESTING
                                    top = stack.pop()
                                if top == "L" or top == "digit":
                                    logging.info(f"Expanded {top} ->{x} {parsing_table[top][x]}")
                                    print("INFO:root:Matched token:", x)
                                    print(stack) #FOR TESTING
                                    
                                    top = stack.pop()
                                    readword = True
                                else:
                                    stack.extend(reversed(parsing_table[top][x]))
                                    logging.info(f"Expanded {top} ->{x} {parsing_table[top][x]}")
                                    print(stack) #FOR TESTING
                                    print("elsepop")
                                    top = stack.pop()

                            if top == token:
                                
                                logging.info(f"Matched token: {token}")
                                readword = True
                    readtok = True

            else: #FOR TESTING
                print("!!!")
                errors.append(f"Unexpected stack top: {top}")
                logging.error(f"Unexpected stack top: {top}")
                return "Error detected in parsing"

    if len(errors) == 0:
        stack.pop()
        return "Ready to compile"
    else:
        for x in range(len(errors)):
            print(errors[x])

# The parsing table
parsing_table = {
    "P": {"program": ["program", "I", ";", "var", "dl", "begin", "sl", "end"]},
    "I": {"a": ["L", "X"], "b": ["L", "X"], "c": ["L", "X"], "d": ["L", "X"], "l": ["L", "X"], "f": ["L", "X"]},
    "X": {";": ["blank"], ",": ["blank"], ":": ["blank"], "=": ["blank"], "+": ["blank"], "-": ["blank"], "*": ["blank"], "/": ["blank"], ")": ["blank"], "$": ["blank"], "a": ["L", "X"], "b": ["L", "X"], "c": ["L", "X"], "d": ["L", "X"], "l": ["L", "X"], "f": ["L", "X"], "0": ["digit", "X"], "1": ["digit", "X"], "2": ["digit", "X"], "3": ["digit", "X"], "4": ["digit", "X"], "5": ["digit", "X"], "6": ["digit", "X"], "7": ["digit", "X"], "8": ["digit", "X"], "9": ["digit", "X"]},
    "dl": {"a": ["dec", ":", "type", ";"], "b": ["dec", ":", "type", ";"], "c": ["dec", ":", "type", ";"], "d": ["dec", ":", "type", ";"], "l": ["dec", ":", "type", ";"], "f": ["dec", ":", "type", ";"]},
    "dec" : {":" : ["I"], "a" : ["I", ",", "dec"], "b" : ["I", ",", "dec"], "c" : ["I", ",", "dec"], "d" : ["I", ",", "dec"], "l" : ["I", ",", "dec"], "f" : ["I", ",", "dec"]},
    "type": {"integer": ["integer"]},
    "sl": {"print": ["stat", "sl"], "a": ["stat", "sl"], "b": ["stat", "sl"], "c": ["stat", "sl"], "d": ["stat", "sl"], "l": ["stat", "sl"], "f": ["stat", "sl"]},
    "stat": {"print": ["wr"], "a": ["as"], "b": ["as"], "c": ["as"], "d": ["as"], "l": ["as"], "f": ["as"]},
    "wr": {"print": ["print", "(", "str", "I", ")", ";"]},
    "str": {'"value=",': ['"value=","'], "a": ["blank"], "b": ["blank"], "c": ["blank"], "d": ["blank"], "l": ["blank"], "f": ["blank"]},
    "as": {"a": ["I","=","E",";"], "b": ["I","=", "E",";"], "c": ["I","=", "E",";"], "d": ["I","=", "E",";"], "l": ["I","=", "E",";"], "f": ["I","=", "E",";"]},
    "E" : {"a" : ["T" ,"Q"], "b" : ["T" ,"Q"], "c" : ["T" ,"Q"], "d" : ["T" ,"Q"], "l" : ["T" ,"Q"], "f" : ["T" ,"Q"], "0" : ["T" ,"Q"], "1" : ["T" ,"Q"], "2" : ["T" ,"Q"], "3" : ["T" ,"Q"], "4" : ["T" ,"Q"], "5" : ["T" ,"Q"], "6" : ["T" ,"Q"], "7" : ["T" ,"Q"], "8" : ["T" ,"Q"], "9" : ["T" ,"Q"], "+" : ["T" ,"Q"], "-" : ["T" ,"Q"], "(" : ["T" ,"Q"]},
    "Q" : {";" : ["blank"], ")" : ["blank"],"+" : ["+", "T" ,"Q"], "-" : ["-", "T" ,"Q"]},
    "T" : {"a" : ["F" ,"R"], "b" : ["F" ,"R"], "c" : ["F" ,"R"], "d" : ["F" ,"R"], "l" : ["F" ,"R"], "f" : ["F" ,"R"], "0" : ["F" ,"R"], "1" : ["F" ,"R"], "2" : ["F" ,"R"], "3" : ["F" ,"R"], "4" : ["F" ,"R"], "5" : ["F" ,"R"], "6" : ["F" ,"R"], "7" : ["F" ,"R"], "8" : ["F" ,"R"], "9" : ["F" ,"R"], "+" : ["F" ,"R"], "-" : ["F" ,"R"], "(" : ["F" ,"R"]},
    "R" : {";" : ["blank"], "+" : ["blank"], "-" : ["blank"], ")" : ["blank"], "*" : ["*","F", "R"], "/" : ["/","F", "R"]},
    "F" : {"a" : ["I"], "b" : ["I"], "c" : ["I"], "d" : ["I"], "l" : ["I"], "f" : ["I"], "0" : ["num"], "1" : ["num"], "2" : ["num"], "3" : ["num"], "4" : ["num"], "5" : ["num"], "6" : ["num"], "7" : ["num"], "8" : ["num"], "9" : ["num"], "+" : ["num"], "-" : ["num"], "(" : ["(", "E", ")"]},
    "num" : {"0" : ["sign", "digit", "D"], "1" : ["sign", "digit", "D"], "2" : ["sign", "digit", "D"], "3" : ["sign", "digit", "D"], "4" : ["sign", "digit", "D"], "5" : ["sign", "digit", "D"], "6" : ["sign", "digit", "D"], "7" : ["sign", "digit", "D"], "8" : ["sign", "digit", "D"], "9" : ["sign", "digit", "D"], "+" : ["sign", "digit", "D"], "-" : ["sign", "digit", "D"]},
    "D" : {";" : ["blank"], "+" : ["blank"], "-" : ["blank"], "*" : ["blank"], "/" : ["blank"], ")": ["blank"], "0" : ["digit", "D"], "1" : ["digit", "D"], "2" : ["digit", "D"], "3" : ["digit", "D"], "4" : ["digit", "D"], "5" : ["digit", "D"], "6" : ["digit", "D"], "7" : ["digit", "D"], "8" : ["digit", "D"], "9" : ["digit", "D"]},
    "sign" : {"0" : ["blank"], "1" : ["blank"], "2" : ["blank"], "3" : ["blank"], "4" : ["blank"], "5" : ["blank"], "6" : ["blank"], "7" : ["blank"], "8" : ["blank"], "9" : ["blank"], "+" : ["+"], "-" : ["-"]},
    "digit" : {"0" : ["0"], "1" : ["1"], "2" : ["2"], "3" : ["3"], "4" : ["4"], "5" : ["5"], "6" : ["6"], "7" : ["7"], "8" : ["8"], "9" : ["9"]},
    "L" : {"a" : ["a"], "b" : ["b"], "c" : ["c"], "d" : ["d"], "l" : ["l"], "f" : ["f"]}
}
# parsing_table = {
#     "P": {"program": ["program", "I", ";", "var", "dl", "begin", "sl", "end"]},
#     "I": {"a": ["L", "X"], "b": ["L", "X"], "c": ["L", "X"], "d": ["L", "X"], "l": ["L", "X"], "f": ["L", "X"]},
#     "X": {";": ["blank"], ",": ["blank"], ":": ["blank"], "=": ["blank"], "+": ["blank"], "-": ["blank"], "*": ["blank"], "/": ["blank"], ")": ["blank"], "$": ["blank"], "a": ["L", "X"], "b": ["L", "X"], "c": ["L", "X"], "d": ["L", "X"], "l": ["L", "X"], "f": ["L", "X"], "0": ["digit", "X"], "1": ["digit", "X"], "2": ["digit", "X"], "3": ["digit", "X"], "4": ["digit", "X"], "5": ["digit", "X"], "6": ["digit", "X"], "7": ["digit", "X"], "8": ["digit", "X"], "9": ["digit", "X"]},
#     "dl": {"a": ["dec", ":", "type", ";"], "b": ["dec", ":", "type", ";"], "c": ["dec", ":", "type", ";"], "d": ["dec", ":", "type", ";"], "l": ["dec", ":", "type", ";"], "f": ["dec", ":", "type", ";"]},
#     "dec" : {":" : ["I"], "a" : ["I", ",", "dec"], "b" : ["I", ",", "dec"], "c" : ["I", ",", "dec"], "d" : ["I", ",", "dec"], "l" : ["I", ",", "dec"], "f" : ["I", ",", "dec"]},
#     "type": {"integer": ["integer"]},
#     "sl": {"print": ["stat", "sl"], "a": ["stat", "sl"], "b": ["stat", "sl"], "c": ["stat", "sl"], "d": ["stat", "sl"], "l": ["stat", "sl"], "f": ["stat", "sl"]},
#     "stat": {"print": ["wr"], "a": ["S"], "b": ["S"], "c": ["S"], "d": ["S"], "l": ["S"], "f": ["S"]},
#     "wr": {"print": ["print", "(", "str", "I", ")", ";"]},
#     "str": {'"value=",': ['"value=","'], "a": ["blank"], "b": ["blank"], "c": ["blank"], "d": ["blank"], "l": ["blank"], "f": ["blank"]},
#     "S" : {"a": ["I", "as"], "b": ["I", "as"], "c": ["I", "as"], "d": ["I", "as"], "l": ["I", "as"], "f": ["I", "as"]},
#     "as": {"=": ["=", "E"]},
#     "E" : {"a" : ["T" ,"Q"], "b" : ["T" ,"Q"], "c" : ["T" ,"Q"], "d" : ["T" ,"Q"], "l" : ["T" ,"Q"], "f" : ["T" ,"Q"], "0" : ["T" ,"Q"], "1" : ["T" ,"Q"], "2" : ["T" ,"Q"], "3" : ["T" ,"Q"], "4" : ["T" ,"Q"], "5" : ["T" ,"Q"], "6" : ["T" ,"Q"], "7" : ["T" ,"Q"], "8" : ["T" ,"Q"], "9" : ["T" ,"Q"], "+" : ["T" ,"Q"], "-" : ["T" ,"Q"], "(" : ["T" ,"Q"]},
#     "Q" : {";" : ["blank"], ")" : ["blank"],"+" : ["+", "T" ,"Q"], "-" : ["-", "T" ,"Q"]},
#     "T" : {"a" : ["F" ,"R"], "b" : ["F" ,"R"], "c" : ["F" ,"R"], "d" : ["F" ,"R"], "l" : ["F" ,"R"], "f" : ["F" ,"R"], "0" : ["F" ,"R"], "1" : ["F" ,"R"], "2" : ["F" ,"R"], "3" : ["F" ,"R"], "4" : ["F" ,"R"], "5" : ["F" ,"R"], "6" : ["F" ,"R"], "7" : ["F" ,"R"], "8" : ["F" ,"R"], "9" : ["F" ,"R"], "+" : ["F" ,"R"], "-" : ["F" ,"R"], "(" : ["F" ,"R"]},
#     "R" : {";" : ["blank"], "+" : ["blank"], "-" : ["blank"], ")" : ["blank"], "*" : ["*","F", "R"], "/" : ["/","F", "R"]},
#     "F" : {"a" : ["I"], "b" : ["I"], "c" : ["I"], "d" : ["I"], "l" : ["I"], "f" : ["I"], "0" : ["num"], "1" : ["num"], "2" : ["num"], "3" : ["num"], "4" : ["num"], "5" : ["num"], "6" : ["num"], "7" : ["num"], "8" : ["num"], "9" : ["num"], "+" : ["num"], "-" : ["num"], "(" : ["(", "E", ")"]},
#     "num" : {"0" : ["sign", "digit", "D"], "1" : ["sign", "digit", "D"], "2" : ["sign", "digit", "D"], "3" : ["sign", "digit", "D"], "4" : ["sign", "digit", "D"], "5" : ["sign", "digit", "D"], "6" : ["sign", "digit", "D"], "7" : ["sign", "digit", "D"], "8" : ["sign", "digit", "D"], "9" : ["sign", "digit", "D"], "+" : ["sign", "digit", "D"], "-" : ["sign", "digit", "D"]},
#     "D" : {";" : ["blank"], "+" : ["blank"], "-" : ["blank"], "*" : ["blank"], "/" : ["blank"], ")": ["blank"], "0" : ["digit", "D"], "1" : ["digit", "D"], "2" : ["digit", "D"], "3" : ["digit", "D"], "4" : ["digit", "D"], "5" : ["digit", "D"], "6" : ["digit", "D"], "7" : ["digit", "D"], "8" : ["digit", "D"], "9" : ["digit", "D"]},
#     "sign" : {"0" : ["blank"], "1" : ["blank"], "2" : ["blank"], "3" : ["blank"], "4" : ["blank"], "5" : ["blank"], "6" : ["blank"], "7" : ["blank"], "8" : ["blank"], "9" : ["blank"], "+" : ["+"], "-" : ["-"]},
#     "digit" : {"0" : ["0"], "1" : ["1"], "2" : ["2"], "3" : ["3"], "4" : ["4"], "5" : ["5"], "6" : ["6"], "7" : ["7"], "8" : ["8"], "9" : ["9"]},
#     "L" : {"a" : ["a"], "b" : ["b"], "c" : ["c"], "d" : ["d"], "l" : ["l"], "f" : ["f"]}
# }

input_string = read_input_file("final24.txt")
tokens = tokenize(input_string)
result = predictive_parse(tokens, parsing_table, "P")
print(result)

