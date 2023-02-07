#Name: Sophia Philips
#GitHub Username: sophiacphilips
#Date: 02/06/2023
#This code is designed to take a list of number from a .txt file and sum them. Once they are summed the
#program writes to a new file the final sum value.




def file_sum():
    """
    defines function named file_sum that will take as a parameter, a text file that contains
    a list of numbers. it will then take that list and sum the numbers in it. the sum will be written to a file
   called sum.txt
    """
    sum = 0 #initializes sum to zero before list has been given
    with open('num_list', 'r') as infile: #opens the text file
        for line in infile: #iterates through lines of the text file
            sum += str(line) #sums list

    with open('sum.txt', 'w') as outfile: #opens file sum.txt to write
        outfile.write(str(sum)) #wrties sum into sum.txt
        infile.close() #closes infile
        outfile.close() #closes outfile







