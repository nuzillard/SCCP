# SCCP
 Short Chain Chlorinated Paraffins, structures produced by pyLSD

## Context
This code was written is order to answer a question by Gyro Funch
on the rdkit-discuss@lists.sourceforge.net mailing list.

The question was about the generation of SMILES chains for 
short chain chlorinated paraffins (SCCP).

These compounds of molecular formula C_{x} H_{2x-y+2} Cl_{y},
x = 10-13, y = 3-12, have a straight carbon backbone
and their average chlorine content ranges from 40% to 70% by mass.

Gyro's question was answered rather expeditiously by means of character string manipulation.
However, the use of the computer-assisted structure elucidation software pyLSD
was attempted, with some success.

The goal of this project is to create a text file with the SMILES chains of all the SCCP,
one per line.

See also a recent review about 
[chemical structure generators](https://journals.plos.org/ploscompbiol/article/authors?id=10.1371/journal.pcbi.1008504).

## Software requirement
First ensure that [pyLSD](http://eos.univ-reims.fr/LSD/JmnSoft/PyLSD) is installed
and that the demo example input file is correctly processed.

Working under a Unix-like system makes it possible to speed up the structure
generation process using [GNU parallel](https://www.gnu.org/software/parallel/).

Copy the `lsdsmi.py` file in the `Variant` directory of pyLSD.
This version of `lsd.py` redirects the SMILES chains of the found structures
to a file named `chlorinated.smi` without generating 2D depictions.

Running `python gen_formula.py > formula.txt` fills the file `formula.txt` with the 28 
molecular formula that correspond to the definition of SCCPs.

Then, running `python gen_Cl_pylsd.py < formula.txt` creates 28 input files for pyLSD (with `.lsd` extension)
and a file named `filelist.txt` that contains 28 lines, one per pyLSD input file name.
The `filelist.txt` file is only used by `parallel`.
Running structure generation without `parallel` is achieved by the `driver.py` script.
Ensure that the `chlorinated.smi` does not exist when starting to generate SMILES.

### Unix-like system, with `parallel`

Copy the pyLSD input files, `filelist.txt`, and `runit` to the `Variant` folder of pyLSD.

Run `cat filelist.txt | parallel runit {}` from `Variant`

The running time was 66 minutes on my laptop with 8 processors.

### Windows 10, or Unix-like system without `parallel`

Copy the pyLSD input files and `driver.py` to the `Variant` folder of pyLSD.

Run `python driver.py` from `Variant`

The running time was about 4 hours on my laptop.

## Result

This procedure resulted in 442,705 structures, stored in file `chlorinated.smi` in directory `Variant`.

Other resolution procedures resulted in 440,334 solutions.

## PyLSD input file

A typical pyLSD input file, `sccp_c10h19Cl3.lsd`, contains:

	FORM "C 10 H 19 Cl 3"
	PIEC 1
	CNTD 1
	BRUL 0
	CCLA 1
	COUF "counter1"
	MULT 1 C 3 (0 1 2 3)
	MULT 2 C 3 (0 1 2 3)
	MULT 3 C 3 (0 1 2 3)
	MULT 4 C 3 (0 1 2 3)
	MULT 5 C 3 (0 1 2 3)
	MULT 6 C 3 (0 1 2 3)
	MULT 7 C 3 (0 1 2 3)
	MULT 8 C 3 (0 1 2 3)
	MULT 9 C 3 (0 1 2 3)
	MULT 10 C 3 (0 1 2 3)
	MULT 11 Cl 3 0
	MULT 12 Cl 3 0
	MULT 13 Cl 3 0
	CARB L1
	PROP L1 2 L1 -

Explanations:

`FORM "C 10 H 19 Cl 3"`: molecular formula.

`PIEC 1`: connected solution, for PyLSD.

`CNTD 1`: connected solution, for LSD.

`BRUL 0`: LSD does not look for a violation of Bredt's rule (no ring and no double bond here).

`CCLA 1`: LSD makes carbon classes with carbon atoms with identical status.

`COUF "counter1"`: name of the file that receives the number of solutions of individual LSD problems. Is different for the different pyLSD input files, so that parallelization of pyLSD runs does not fail.

`MULT 1 C 3 (0 1 2 3)`: atom 1 si a carbon, with sp3 hybridization, of unknown number of attached H atoms.

`MULT 11 Cl 3 0`: atom 11 is a chlorine, with sp3 hybridization, no attached H atom.

`CARB L1`: L1 is the list of all carbon atoms

`PROP L1 2 L1 -`: each carbon atom has two carbon neighbors, or less. This constraint ensures the solutions have a straight carbon backone.

## Checking the result
The problem to be solved was to ensure that all the produced SMILES chains were valid and unique.

The validation is carried out by the `check.py` python script.
Unicity checking resorts on InChIKeys genrated by [rdkit](https://www.rdkit.org/).

Run `python check.py < chlorinated.smi` to see the number of SMILES, of valid SMILES, and of unique SMILES.
