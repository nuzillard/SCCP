# python gen_formula.py > formula.txt
import sys

for nc in range(10, 14):
	for ncl in range(3, 13):
		nh = 2*nc - ncl + 2
		mcl = 35.5 * ncl
		mw = 12.0*nc + nh + mcl
		pcl = mcl / mw
		if (pcl < 0.4) or (pcl > 0.7):
			continue
		line = "C %d H %d Cl %d\n" % (nc, nh, ncl)
		sys.stdout.write(line)
