#!/usr/bin/python
# -*- coding: utf-8 -*-

# Solver script to call external C# code, for the course Optimization-002: Discrete Optimization
# Modified from the original Java example given in the course materials

import os
from subprocess import Popen, PIPE

def solve_it(input_data):

    # Writes the inputData to a temporary file

    tmp_file_name = 'tmp.data'
    tmp_file = open(tmp_file_name, 'w')
    tmp_file.write(input_data)
    tmp_file.close()
    
    projectName = 'TravelingSalesman'

    # replace this with your compiled executable (from csc or mono)
    exe = '/' + projectName +'/bin/Debug/' + projectName + '.exe'

    # the windows case. 
    if os.name == 'nt':    
        workingDirectory = os.getcwd().replace('\\','/')
        exe = workingDirectory + exe
        process = Popen([exe, '-file=' + tmp_file_name], stdout=PIPE)
    # the regular case (posix systems). Run mono.
    else:
        process = Popen(['mono','.' + exe, '-file=' + tmp_file_name], stdout=PIPE)
    (stdout, stderr) = process.communicate()

    # removes the temporay file
    # os.remove(tmp_file_name)

    return stdout.strip()

import sys

if __name__ == '__main__':
    sys.argv.append("data\\tsp_200_2");
    if len(sys.argv) > 1:
        file_location = sys.argv[1].strip()
        input_data_file = open(file_location, 'r')
        input_data = ''.join(input_data_file.readlines())
        input_data_file.close()
        print solve_it(input_data)
    else:
        print 'This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/ks_5_1)'

