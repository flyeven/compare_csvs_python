compare_csvs_python
===================

Python - Compare/Diff csv files using python, numpy

This single script is used to compare a set of similar csv files and report the differences between each set of file,
row and column wise. Many times, your programs could generate a set of csv files as reports or output. You might
have to run the programs multiple times for various options. Or sometimes, you generate various set of reports for
debugging. 
In all these scenarios, instead of manually checking each and every column, this automated script will become very
very handy inorder to spot the differences.

This tool uses the python package named numpy. Numpy is very popular in the data analysis world.
Just a single np.recfromtxt() function call converts/reads an entire csv file into a numpy array. This really 
simplifies processing csv files.

Note:
This works for similar csv files (they should have similar number of columns and similar set of data columns)
