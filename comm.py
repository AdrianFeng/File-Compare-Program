#!/usr/bin/python

#CS 35L Zhen Feng 
import sys, locale
from optparse import OptionParser

locale.setlocale(locale.LC_ALL,'')
class comm: #define a class that used to records the input files' lines
     def __init__(self, file):
        content=open(file,'r')
        self.line=content.readlines()
        content.close()
class std_in: # create a class that records the standard input
     def __init__(self, content):
        self.line=content
#define a function that print the lines differently according to
#the current option and the current files        
def write (string, coln, opt1, opt2,opt3): 
    if coln==1: # printing option for lines in file_1
       if opt1==0:
          sys.stdout.write(string)
    if coln==2:# printing option  for lines in file_2
       if opt1==1 and opt2==0:
          sys.stdout.write(string)
       elif opt1==0 and opt2==0:
         sys.stdout.write("	"+string)
    if coln==3:# printing option for lines in both files
       if opt1==1:
          if opt2==1 and opt3==0:
             sys.stdout.write(string)
          elif opt2==0 and opt3==0:
               sys.stdout.write("	"+string)
       elif opt1==0:
          if opt2==1 and opt3==0:
             sys.stdout.write("	"+string)
          elif opt2==0 and opt3==0:
               sys.stdout.write("		"+string)   
def main ():
    version_msg = "%prog 2.0"
    usage_msg = """%prog [OPTION]... FILE
Output randomly selected lines from FILE."""
    #define parser
    parser = OptionParser(version=version_msg,
                          usage=usage_msg)
    # define each specific option and their default values and their set
    # values when option is choosen default is 0 means write down≈
    parser.add_option("-1",action="store_true", dest="option_1", default=0,
                      help="suppress printing of column1")
    parser.add_option("-2",action="store_true", dest="option_2", default=0,
                      help="suppress printing of column2")
    parser.add_option("-3",action="store_true", dest="option_3", default=0,
                      help="suppress printing of column3")
    parser.add_option("-u",action="store_true", dest="option_u", default=0,
                      help="use this if input is unsorted ")
    # define the option arguments and the input_file arguments order 
    options, args = parser.parse_args(sys.argv[1:])
    input1=args[0]
    input2=args[1]
    # when input file arguments is "-" then read the standard input
    # otherwise read the file
    if input1=="-":
       stdin=sys.stdin.readlines()
       file1=std_in(stdin)
    else:
       file1=comm(input1)
    if input2=="-":
       stdin=sys.stdin.readlines()
       file2=std_in(stdin)
    else:
       file2=comm(input2)
    max1=len(file1.line)
    #print(max1)
    max2=len(file2.line)
    #print(max2)
    index1=0
    index2=0 
    opt_1=options.option_1
    opt_2=options.option_2
    opt_3=options.option_3
    # control loop for non"-u" option
    if options.option_u==0 :
       while index1<max1  and index2<max2 :
           if file1.line[index1]==file2.line[index2]:
              write(file1.line[index1],3,opt_1,opt_2,opt_3 )
              # print(index1)
              index1+=1
              index2+=1
           elif file1.line[index1]<file2.line[index2]:
              write(file1.line[index1],1,opt_1,opt_2,opt_3 )
             ## print(index1) 
              index1+=1
           elif file1.line[index1]>file2.line[index2]:
             ## print (index1+index2)
              write(file2.line[index2],2,opt_1,opt_2,opt_3 )
              ##print(index2)
              index2+=1
   # ouput the rest file
       if ((index1<max1) or (index2<max2)) :
          while (index1<max1) :
               write(file1.line[index1],1,opt_1,opt_2,opt_3 )
               index1+=1
              # print(index1)
          while (index2<max2) :
               write(file2.line[index2],2,opt_1,opt_2,opt_3 )
               index2+=1
              # print(index2)
   # control loop for "-u" option 
    elif (options.option_u==True) : 
        while (index1<max1) :
             nosame=1
             for content in file2.line :
                if file1.line[index1]==content :
                    write(content, 3, opt_1, opt_2,opt_3)
                    file2.line.remove(content)
                    nosame=0
                    break
             if nosame==1:
                write(file1.line[index1],1,opt_1,opt_2,opt_3)
             index1=index1+1
        if (len(file2.line) != 0) :
           for content in file2.line :
               write(content,2,opt_1,opt_2,opt_3)
if __name__ == "__main__":
   main()
