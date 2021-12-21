# python gen_Cl_pylsd.py < formula.txt

import sys

def make_file(formula, indx):
	pieces = formula.split()
	nc = pieces[1]
	nh = pieces[3]
	nf = pieces[5]
	filename = 'sccp_c' + nc + 'h' + nh + 'cl' + nf + '.lsd'
	with open(filename, 'w') as fh:
		fh.write("FORM \"C" + ' ' + nc + " H " + nh + " Cl " + nf + '\"\n')
		fh.write("PIEC 1\n")
		fh.write("CNTD 1\n")
		fh.write("BRUL 0\n")
		fh.write("CCLA 1\n")
                fh.write("COUF \"counter" + str(indx) + "\"\n")
		nnc = int(nc)
		nnf = int(nf)
		for iat in range(1, nnc+1):
			fh.write("MULT %d C 3 (0 1 2 3)\n" % (iat,))
		for iat in range(nnc+1, nnc+nnf+1):
			fh.write("MULT %d Cl 3 0\n" % (iat,))
		fh.write("CARB L1\n")
		fh.write("PROP L1 2 L1 -\n")
	return filename

def run():
	filenames = []
        indx = 1
	for f in sys.stdin:
		formula = f.strip()
		filename = make_file(formula, indx)
                indx += 1
		filenames.append(filename)
	fns = '\n'.join(filenames)
	with open('filelist.txt', 'w') as fout:
		fout.write(fns)

if __name__ == "__main__":
#	make_file ("C 10 H 19 Cl 3", 1)
	run()
