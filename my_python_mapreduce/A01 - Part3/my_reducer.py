#!/usr/bin/python

# --------------------------------------------------------
#           PYTHON PROGRAM
# Here is where we are going to define our set of...
# - Imports
# - Global Variables
# - Functions
# ...to achieve the functionality required.
# When executing > python 'this_file'.py in a terminal,
# the Python interpreter will load our program,
# but it will execute nothing yet.
# --------------------------------------------------------

import sys
import codecs
from datetime import datetime

#---------------------------------------
#  FUNCTION get_key_value
#---------------------------------------
def get_key_value(line):
    # 1. We create the output variable
    res = ()

    # 2. We remove the end of line char
    line = line.replace('\n', '')

    # 3. We get the key and value
    words = line.split('\t')
    day = words[0]
    hour = words[1]

    # 4. We process the value
    hour = hour.rstrip(')')
    hour = hour.strip('(')

    # 4. We assign res
    res = (day, hour)

    # 5. We return res
    return res

# ------------------------------------------
# FUNCTION my_reduce
# ------------------------------------------
def my_reduce(my_input_stream, my_output_stream, my_reducer_input_parameters):
    out = []
    measurement_time = my_reducer_input_parameters[0]

    datetime_format = '%Y-%m-%d\t(%H:%M:%S)\n'

    ran_out_count = 0
    starting_time =""
    current_time = ""

    for input in my_input_stream:
        # res = get_key_value(input)
        # amount = res[1]
        # day_hour = res[0]
        # if day_hour in out:
        #     out[day_hour] = out[day_hour] + amount
        #     total_amount = total_amount + amount
        # else:
        #     out[day_hour] = amount
        if starting_time == "":
            starting_time = datetime.strptime(input, datetime_format)
            current_time = starting_time
            ran_out_count = ran_out_count + 1

        next_time = datetime.strptime(input, datetime_format)

        if next_time == current_time:
            continue

        if (next_time - current_time).total_seconds() == measurement_time * 60:
            # We are 5 minutes apart
            ran_out_count = ran_out_count + 1
            current_time = next_time

        if (next_time - current_time).total_seconds() > 5 * 60:
            # We are more than 5 minute apart
            out.append(str(starting_time.strftime("%Y-%m-%d\t(%H:%M:%S")) + ", " + str(ran_out_count) + ")\n")
            ran_out_count = 0
            starting_time = ""
            current_time = ""




    print("hello")

    for fin in sorted(out):

        my_output_stream.write(fin)

    # for fin in sorted(out.keys(), key=lambda item: out[item], reverse=True):
    #     percent = float(out[fin] / ran_outs) * 100
    #     my_str = fin + "\t(" + str(out[fin]) + ", " + str(percent) + ")\n"
    #     my_output_stream.write(my_str)


    pass

# ------------------------------------------
# FUNCTION my_main
# ------------------------------------------
def my_main(local_False_Cloudera_True,
            my_reducer_input_parameters,
            input_file_example,
            output_file_example
           ):

    # 1. We select the input and output streams based on our working mode
    my_input_stream = None
    my_output_stream = None

    # 1.1: Local Mode --> We use the debug files
    if (local_False_Cloudera_True == False):
        my_input_stream = codecs.open(input_file_example, "r", encoding='utf-8')
        my_output_stream = codecs.open(output_file_example, "w", encoding='utf-8')

    # 1.2: Cloudera --> We use the stdin and stdout streams
    else:
        my_input_stream = sys.stdin
        my_output_stream = sys.stdout

    # 2. We trigger my_reducer
    my_reduce(my_input_stream, my_output_stream, my_reducer_input_parameters)

# ---------------------------------------------------------------
#           PYTHON EXECUTION
# This is the main entry point to the execution of our program.
# It provides a call to the 'main function' defined in our
# Python program, making the Python interpreter to trigger
# its execution.
# ---------------------------------------------------------------
if __name__ == '__main__':
    # 1. Local Mode or Cloudera
    local_False_Cloudera_True = False

    # 2. Debug Names
    input_file_example = "../../my_result/A01 - Part3/2. my_sort_simulation/sort_1.txt"
    output_file_example = "../my_result/A01 - Part3/3. my_reduce_simulation/reduce_sort_1.txt"

    # 3. my_reducer.py input parameters
    # We list the parameters here
    measurement_time = 5

    # We create a list with them all
    my_reducer_input_parameters = [measurement_time]

    # 4. We call to my_main
    my_main(local_False_Cloudera_True,
            my_reducer_input_parameters,
            input_file_example,
            output_file_example
           )
