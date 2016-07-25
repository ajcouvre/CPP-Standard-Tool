#This Function creates a dictionary of dictionaries that contains
#Each Example lines in a list, given a name "Ex.#", counts the number of error in each example
#LineDictionary["Ex.#"] = {"Lines":[], "Error":0}
def read_file(filename):
	LineDictionary = {}
	ExampleReader = 0
	DictCreation = 0
	counter = 0
	inFile = open(filename)
	
	for line in inFile:
		if "end example ]" in line:
			ExampleReader = 0
			DictCreation = 0
		if "[ Example:" in line:
			ExampleReader = 1
			continue
		if ExampleReader == 1 and DictCreation == 0:
			counter += 1
			LineDictionary['Ex.'+str(counter)] = {"Lines":[], "Error":0}
			DictCreation = 1
		if ExampleReader == 1 and DictCreation == 1:
			LineDictionary["Ex."=str(counter)]["Lines"].append(line)
			if "error" in line:
				LineDictionary['Ex."+str(counter)]["Error"] += 1
	filename.close()
	return LineDictionary

#This Function Prints the dictionary name, each line, and the number of errors
def print_norm_dict(LineDictionary):
	for key, value in LineDictionary.iteritems():
		print key
		print
		for line in value["Lines"]:
			print line
		print "Error:", value["Error"]

def print_mutant_dict(MutantDictionary):
	for key, value in MutantDictionary.iteritems():
		print key
		for name, lines in value:
			print name
				for line in lines:
					print line
		
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
		for i in range(0, OriginalDict["Error"]+1):
			if i == 0:
				MutantDict[key]["Original"] = []
				for line in value["Lines"]:
					MutantDict[key]["Original"].append(line)
			else:
				MutantDict[key]["Error " + str(i)] = []
				for line in value["Lines"]:
					MutantDict[key]["Error " + str(i)].append(line)
				for x in range(0, len(ErrorIndex)):
					if x == i-1:
						continue
					else:
						MutantDict[key]["Error " + str(i)].pop(ErrorIndex[x])
				if i == OriginalDict["Error"]:
					MutantDict[key]["No Errors"] = []
					for line in value["Lines"]:
						MutantDict[key]["No Errors"].append(line)
					for index in ErrorIndex:
						MutantDict[key]["No Errors"].pop(index)
					