# python driver.py

import glob
import os

lsdglob = "sccp*.lsd"
lsdfilenames = glob.glob(lsdglob)
for fn in lsdfilenames:
	command = "python lsdsmi.py " + fn
	code = os.system(command)
