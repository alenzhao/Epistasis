#!/usr/bin/env python

import sys

# Split an MSA id
def msaIdParse(id):
	id = id.replace(":","\t").replace("-","\t").replace("[","\t").replace("]","\t")
	(trid, start, end, aaidx, t) = id.split("\t")
	return (trid, start, end, aaidx)

#-------------------------------------------------------------------------------
# Main
#-------------------------------------------------------------------------------

linesByvcfId = dict()

# Read stdin
print "Reading stdin:"
count = 1
for l in sys.stdin:
	# Parse input
	(vcfId, msa1, msa2, llr, llnull, llalt) = l.rstrip().split('\t')
	(trid1, start1, end1, aaidx1) = msaIdParse(msa1)
	(trid2, start2, end2, aaidx2) = msaIdParse(msa2)

	ll = float(llr)
	if ll < 0: llr = "0"

	# Add to map
	if( msa1 == msa2 ): out = "\t".join( (trid1, start1, end1, aaidx1, trid2, start2, end2, aaidx2, llr, llnull, llalt) ) + "\n"
	else: out = "\t".join( (trid1, start1, end1, aaidx1, trid2, start2, end2, aaidx2, "-1", llnull, llalt) ) + "\n"

	count += 1
