__author__ = 'srivenkatesh'

import numpy as np
import sys
import os

def runmain(argv=None):
    if len(sys.argv) != 3:
        print "Error : 2 cmd line args expected : Press any key to close"
        var = raw_input()
        return

    path1 = os.getcwd() + "/" + sys.argv[1]
    path2 = os.getcwd() + "/" + sys.argv[2]

    csv_files = os.listdir(path1)
    for f1 in csv_files:
        file_name_1 = path1 + "/" + f1
        file_name_2 = path2 + "/" + f1

        diff_found = 0
        fnames_title = file_name_1 + " -- " + file_name_2
        print "File : " + fnames_title
        print "=" * len(fnames_title)

        #parsing the csv files into a numpy array
        matrix1 = np.recfromtxt(file_name_1, delimiter=",", names=True)
        names1 = matrix1.dtype.names

        matrix2 = np.recfromtxt(file_name_2, delimiter=",", names=True)
        names2 = matrix2.dtype.names

        if len(names1) != len(names2):
            print "The number of columns are not equal in both csv files"
            return

        num_of_columns = len(names1)
        for i in range(len(matrix1)):
            for j in range(num_of_columns):
                if matrix1[i][j] != matrix2[i][j]:
                    print 'Differs : ', names1[j], i, j
                    diff_found = 1

        if diff_found == 0:
            print "No Diff Found"
        print "\n"


    print "Done: Press any key to close"
    var = raw_input()

if __name__ == "__main__":
    runmain()