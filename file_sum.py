




def file_sum(a_file):
    """
    defines function named file_sum that will take as a parameter, the name of a text file (a_file) that contains
    a list of numbers. it will then take that list and sum the numbers in it. the sum will be written to a file
   called sum.txt
    """
    sum = 0 #initializes sum to zero before list has been given
    with open(a_file, 'r') as infile: #opens the text file
        for line in infile: #iterates through lines of the text file
            sum += str(line) #sums list

    with open('sum.txt', 'w') as outfile: #opens file sum.txt to write
        outfile.write(str(sum)) #wrties sum into sum.txt
        infile.close() #closes infile
        outfile.close() #closes outfile
       





