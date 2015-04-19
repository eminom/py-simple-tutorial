import os;

def createWriteFile():
	ls = os.linesep
	while True:
		fname = input("Input name:")
		if os.path.exists(fname):
			print("Error:%s already exists" % fname)
		else:
			break
	
	all = []
	print("Input contents in lines>")
	while True:
		entry = input(">")
		if '.' == entry:
			break
		else:
			all.append(entry)
	
	with open(fname, "w") as fout:
		fout.writelines(['%s%s' % (x, ls) for x in all])
	
	print('done')

if '__main__' == __name__:
	createWriteFile()
	
