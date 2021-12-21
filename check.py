# python check.py < chlorinated.smi

import sys
from rdkit import Chem

d = dict()
nok = 0
for ismi, s in enumerate(sys.stdin, 1):
	smi = s.strip()
	mol = Chem.MolFromSmiles(smi)
	if mol:
		ikk = Chem.MolToInchiKey(mol)
		d[ikk] = None
		nok += 1
	else:
		sys.stdout.write("Bad: %d: %s\n" % (ismi, smi))
sys.stdout.write("%d SMILES\n" % (ismi,))
sys.stdout.write("%d good SMILES\n" % (nok,))
sys.stdout.write("%d unique good SMILES\n" % (len(d),))
