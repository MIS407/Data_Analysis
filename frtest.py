__author__ = 'sree'
import csv
with open ('banklist.csv') as f:
  f_csv = csv.reader(f)
  for line in f_csv:
    print (line)
    
with open ('newfile.txt', 'wt') as f:
  print ('Hello World\n', file=f)
  
with open ('newfile.txt', 'rt') as f:
  for line in f:
    print (f)
    
myfile = open ('newfile.txt', 'r')
myfile.readline()
 open('newfile.txt').read()
 
 print (open('newfile.txt').read())
 
 for line in open('newfile.txt'):
  print (line, end='')
close('newfile.txt')
