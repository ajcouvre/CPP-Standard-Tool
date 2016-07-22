import MutantTest.py
import subprocess


inFile = input("Input the PDF name to turn to text: ")
pageRangeStart, pageRangeEnd = int(input("Please enter the page range, separated by a space, -1 -1 for all:")
outFile = input("Name of the output file: ")


if pageRangeStart == -1 and pageRangeEnd == -1:
	proc = subprocess.Popen(['python', 'pdf2txt.py', '-o', outFile, inFile])
else:
	page_list = [x for x in range(pageRangeStart, pageRangeEnd+1)]
	proc = subprocess.Popen(['python', 'pdf2txt.py', '-p', ', '.join(page_list), '-o', outFile, inFile])


#Create Normal Dictionary from output file, print to test
LineDictionary = read_file(outFile)
print_norm_dict(LineDictionary)


#Create Mutant Dictionary from normal dictionary, print to test
MutantDictionary = create_mutant(LineDictionary)
print_mutant_dict(MutantDictionary)