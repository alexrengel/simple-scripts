#!/usr/bin/env python3

import sys, getopt, os

def main(argv):
        good_name_count = 0
        bad_name_count = 0
        inputfile = ''
        outputfile = ''
        try:
                opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
        except getopt.GetoptError:
                print ('usergen.py -i <inputfile> -o <outputfile>')
                sys.exit(2)
        for opt, arg in opts:
                if opt == '-h':
                        print ('usergen.py -i <inputfile> -o <outputfile>')
                        sys.exit()
                elif opt in ("-i", "--ifile"):
                        inputfile = arg
                elif opt in ("-o", "--ofile"):
                        outputfile = arg
        i_file = open(inputfile, 'r')
        o_file = open(outputfile, 'w')
        lines = i_file.read()
        aux = lines.splitlines()
        for foo, bar in enumerate(aux):
                names = bar.split()
                #check to see if it contains first and last name
                if len(names) == 2:
                        good_name_count += 1
                        o_file.write((names[0]).lower()+'\n')
                        o_file.write((names[1]).lower()+'\n')
                        o_file.write((names[0]+names[1]).lower()+'\n')
                        o_file.write((names[0]+'.'+names[1]).lower()+'\n')
                        o_file.write((names[1]+names[0]).lower()+'\n')
                        o_file.write((names[1]+'.'+names[0]).lower()+'\n')
                        o_file.write((names[0][0]+names[1]).lower()+'\n')
                        o_file.write((names[0][0]+'.'+names[1]).lower()+'\n')
                else:
                        bad_name_count += 1
        o_file.close()
        i_file.close()
        #summary
        print ("%d names where read (%d good, %d bad): %d variations created at %s!"%(good_name_count+bad_name_count,good_name_count,bad_name_count,good_name_count*8,outputfile))

if __name__ == "__main__":
        main(sys.argv[1:])
