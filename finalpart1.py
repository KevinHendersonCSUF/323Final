#Theo Gonong, Kevin Henderson, Anthony Le
#Final Project part 1

with open("final.txt", 'r') as fone:
    with open("final24.txt", 'w') as ftwo:
       for line in fone.readlines():
        # if "(*" not in line and "*)" not in line and line.isspace() == False:
        #     line = ' '.join(line.split())
        #     format_line = line.strip()
        #     ftwo.write(format_line + '\n')
        if line.isspace() == False:
            comment = "(*" 
            line = ' '.join(line.split())
            format_line = line.strip()
            ftwo.write(format_line.split(comment)[0] + '\n')