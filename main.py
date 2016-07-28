import MutantTest as MT
import subprocess


inFile = raw_input("Input the PDF name to turn to text: ")
pageRangeStart = raw_input("Please enter the page start, -1 for all:")
pageRangeEnd = raw_input("Please enter the page end, -1 for all, same page for single page:")
outFile = raw_input("Name of the output file: ")
pageRangeStart = int(pageRangeStart)
pageRangeEnd = int(pageRangeEnd)

if pageRangeStart == -1 and pageRangeEnd == -1:
	proc = subprocess.Popen(['python', 'pdf2txt.py', '-o', outFile, inFile])
elif pageRangeStart == pageRangeEnd:
	proc = subprocess.Popen(['python', 'pdf2txt.py', '-p', str(pageRangeStart), '-o', outFile, inFile])
else:
	page_list = [str(x) for x in range(pageRangeStart, pageRangeEnd+1)]
	page_string = ', '.join(page_list)
	proc = subprocess.Popen(['python', 'pdf2txt.py', '-p', page_string, '-o', outFile, inFile])


#Create Normal Dictionary from output file, print to test
LineDictionary = MT.read_file(outFile)
MT.print_norm_dict(LineDictionary)


#Create Mutant Dictionary from normal dictionary, print to test
MutantDictionary = MT.create_mutants(LineDictionary)
MT.print_mutant_dict(MutantDictionary)

MT.write_files(MutantDictionary)


