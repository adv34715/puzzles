'''
Author: Yimeng Zhao
Date: Apr 11, 2017

This .py file is for vAuto Programming Test.

The program first will ask user how to input the words. There are 2 
apprach, from file or from keyboard. The program will take input based on 
user selection. Then sorts the words alphabetically into four columns, 
vertically, then horizontally. The last row would contain empty cells 
if the number of words are not evenly divisible by 4. Besides, users
can remove the word in the column.

Input: a valid file path if user select input from path (option 1)
	   input from keyboard if user select type the words (option 2)
	   input a word or a word list to remove, after input words is done

Output: alphabetically sorted words in four columns, both vertically and horizontally.

'''

# read file, the filePath is given by user
def readFile():
	filePath = input("please input a valid file path:")
	with open(filePath,"r+") as f:
		inputList = f.read().split(',')
		return (inputList)
# take user input as input source.
def inputSelection():
	inputSelect = 0
	while((inputSelect != "1") and (inputSelect != "2")):
		inputSelect = input("How do you want to input all the words? \n1.From a file 2. Type words one by one \n")
	if(inputSelect == "1"): 
		inputList=readFile()
		#return inputList
	elif(inputSelect == "2"):
		inputWord = input("input your words here, separate words with a comma. \nWhen you finish, press enter. \n")
		inputList = inputWord.split(",")
	inputList = [x.strip(" ") for x in inputList] 	
	return inputList

# prepare for vertical show
def vertical(inputList,l):
	last = []          # the last row of output
	outList = []       # the output list in the order of horizontal
	rNum = int(l/4)    # how many rows with 4 words
	cNum = l%4         # how many words in the last row
	shift = [rNum]*3   # when change to another column
	if cNum > 0:
		for i in range(cNum):
			shift[i] += 1
			last.append(inputList[(rNum+1)*i+rNum])

	# put output into a list in the order of horizontal
	for i in range(rNum):
		row = i
		outList.append(inputList[row])
		for j in range(3):
			row += shift[j]
			outList.append(inputList[row])
	outList += last
	return (outList)

# a function to show output
def showOutput(inputList,l):
	n = l%4
	outputList = inputList[:]
	if(n>0):
		outputList += [" "]*(4-n)
	for a,b,c,d in zip(outputList[::4],outputList[1::4],outputList[2::4],outputList[3::4]):
		print('{:<15}{:<1}{:<15}{:<1}{:<15}{:<1}{:<}'.format('-'*15,"+",'-'*15,"+",'-'*15,"+",'-'*15))
		print ('{:<15}{:<1}{:<15}{:<1}{:<15}{:<1}{:<}'.format(a,"|",b,"|",c,"|",d))

# display all the output nicely
def displayOutput(inputList):   
	inputList.sort()
	l = len(inputList) # how many words in inputList
	print(l," words in total.")
	outList=vertical(inputList,l)
	print("\nvertical: \n")
	showOutput(outList,l)
	print("\nhorizontal: \n")
	showOutput(inputList,l)
	print("\n")

def main():
	inputList = inputSelection()
	displayOutput(inputList)
	removeList = input("Do you want to remove any words? \nIf so, input the word or a word list. \nIf not, please press enter.\n")
	
	if len(removeList) > 0:
		removeList = removeList.split(",")
		removeList = [x.strip(" ") for x in removeList] 
		removeLength =  len(removeList)
		failRemove = []
		for rl in removeList:
			if rl in inputList:
				inputList.remove(rl)
			else:
				failRemove.append(rl)
		failLength = len(failRemove)
		if(failLength == 0):
			print("Successfully remove %s word(s)." %removeLength)
			displayOutput(inputList)
		else:
			print("Successfully remove %s word(s)." %(removeLength-failLength))
			print("%s word(s) failed." %failLength)
			print("The failed words are: %s" %", ".join(failRemove))
			displayOutput(inputList)

# begins here
main()