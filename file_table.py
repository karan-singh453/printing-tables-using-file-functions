# first loop to create unique file for each table
for i in range(2,21):
    #creating file by the name "mul(the tables name).txt" in append mode
    with open(f'mul{i}.txt','a') as f:
        #second loop to print tables in the text files
        for j in range(1,11):
            f.write(f"{i}*{j}={i*j}\n")
