#This Function creates a dictionary of dictionaries that contains
#Each Example lines in a list, given a name "Ex.#", counts the number of error in each example
#LineDictionary["Ex.#"] = {"Lines":[], "Error":0}
import os


def read_file(filename):
	LineDictionary = {}
	ExampleReader = 0
	DictCreation = 0
	counter = 0
	inFile = open(filename, 'r')
	
	for line in inFile:
		last_char = ' '
		for character in line:
			if ord(character) > 126 and last_char == '/':
				line = line.replace(character, '*')
				last_char = '*'
			elif ord(character) > 126 and last_char == '*':
				line = line.replace(character, '')
				last_char = '*'
			else:	
				last_char = character
		if "end example ]" in line:
			ExampleReader = 0
			DictCreation = 0
		if "[ Example:" in line:
			ExampleReader = 1
			continue
		if ExampleReader == 1 and DictCreation == 0:
			counter += 1
			LineDictionary['t'+str(counter)] = {"Lines":[], "Error":0}
			DictCreation = 1
		if ExampleReader == 1 and DictCreation == 1:
			LineDictionary["t"+str(counter)]["Lines"].append(line)
			if "error" in line:
				LineDictionary["t"+str(counter)]["Error"] += 1
	inFile.close()
	return LineDictionary

#This Function Prints the dictionary name, each line, and the number of errors
def print_norm_dict(LineDictionary):
	for key, value in LineDictionary.iteritems():
		print key
		print
		for index, line in enumerate(value["Lines"]):
			print index, line
		print "Error:", value["Error"]

def print_mutant_dict(MutantDictionary):
	for key, value in MutantDictionary.iteritems():
		print key
		for name, lines in value.iteritems():
			print name
			for x, line in enumerate( lines):
				print x,line
		
#This function will create a Dictionary of Mutants for each example to include the original
#and one copy with only a single error. 
def create_mutants(OriginalDict):
	MutantDict = {}
	for key, value in OriginalDict.iteritems():
		MutantDict[key] = {}
		ErrorIndex = []
		for i,line in enumerate(value["Lines"]):
			if "error" in line:
				ErrorIndex.append(i)
#		print key, ErrorIndex
		for i in range(0, value["Error"]+2):
			
		
			if i == 0:
				MutantDict[key]["orig"] = []
				for line in value["Lines"]:
					MutantDict[key]["orig"].append(line)
			else:
			        if i == value["Error"]+1:
					MutantDict[key]["noerr"] = []
					for line in value["Lines"]:
						MutantDict[key]["noerr"].append(line)
					for x in range(len(ErrorIndex)-1, -1, -1):
						MutantDict[key]["noerr"].pop(ErrorIndex[x])
				else:
					MutantDict[key]["err-" + str(i)] = []
					for line in value["Lines"]:
						MutantDict[key]["err-" + str(i)].append(line)
					for x in range(len(ErrorIndex)-1,-1, -1):
						if x == i-1:
							continue
						else:
							MutantDict[key]["err-" + str(i)].pop(ErrorIndex[x])

	

	for key, value in MutantDict.iteritems():
		for name, lines in value.iteritems():
			for i, line in enumerate(lines):
				if line == "N4296":
					if i < 5:
						for j in range(0, i+1):
							lines.pop(i-j)
					else:
						for j in range(0,6):
							lines.pop(i-j)


	return MutantDict


def write_files(MutantDict):
	os.makedirs("Examples")

	for name, example in MutantDict.iteritems():
		for mutant, lines in example.iteritems():
			newFile = open('Examples/'+name + '-' +  mutant + ".cpp", 'w')
#			headers = open('CPP_Headers.h', 'r')
#			for line in headers:
#				newFile.write(line)
#			newFile.write('\n')	
			for line in lines:
				newFile.write(line)
				#newFile.write("\n")

			
