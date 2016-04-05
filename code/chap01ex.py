"""This file contains code for use with "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

import numpy as np
import sys

import nsfg
import thinkstats2


def ReadFemPreg(dct_file='2002FemPreg.dct',
                dat_file='2002FemPreg.dat.gz'):
    """Reads the NSFG pregnancy data.

    dct_file: string file name
    dat_file: string file name

    returns: DataFrame
    """
    dct = thinkstats2.ReadStataDct(dct_file)
    df = dct.ReadFixedWidth(dat_file, compression='gzip')
    nsfg.CleanFemPreg(df)
    return df

def NumPregs(df):
	mapper = nsfg.MakePregMap(df)
	cs = {}
	for k,v in mapper.iteritems():
		cs[len(mapper[k])] = cs.get(len(mapper[k]),0) +1

	print cs

	return df.pregnum.value_counts()


def main(script):
    """Tests the functions in this module.

    script: string script name
    """
    df = ReadFemPreg()
    print NumPregs(df)
    
    print('%s: All tests passed.' % script)


if __name__ == '__main__':
    main(*sys.argv)
