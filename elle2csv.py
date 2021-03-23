"""
Converting elle files to csv to be read in paraview
Giulia Fedrizzi, February-March 2021
search for letters in regex:
    letters:       [a-zA-Z]
    words:         [a-zA-Z]+
    words, no 'e': [a-d,f-z,A-D,F-Z]+
"""
import sys
import os
import pandas as pd
import glob 
fracturesTF=True; pressureTF=True; difStressTF=True  # TO DO: let the user decide what to save

""" #remove already existing files
if os.path.isfile("converted.csv"):
    os.remove("converted.csv")
"""

def search_string_in_file(file_name, string_to_search):
    """Search for the given string in file and return lines containing that string"""
    line_number = 0
    # Open the file in read only mode
    with open(file_name, 'r') as read_obj:
        # Read all lines in the file one by one
        for line in read_obj:
            # For each line, check if line contains the string
            line_number += 1
            if string_to_search in line:
                # save the line where the word has been found
                line_of_result=line_number
                break
        # Return the line number where the result was found
        return line_of_result 


def save_the_right_lines(file_name):
    """get the list of number of lines to read: lines_list[0] is the fist line to save, lines_list[1] the last. Save all of the lines in between:"""
    lines_to_read = list(range(lines_list[0],lines_list[1]-1)) 
    minimumLine =min(lines_to_read)
    maximumLine = max(lines_to_read)

    
    my_elle_file = open(file_name)
    my_converted_elle_file = open(converted_file_name+".txt","w+")
    for position, line in enumerate(my_elle_file): # iterate over each line and its index
        if position >= minimumLine and position <= maximumLine: # write lines from min to max lines
            my_converted_elle_file.write(line)
   
    my_elle_file.close()
    my_converted_elle_file.close()

"""
Find where the sections start and end
"""
for file_to_convert in glob.glob("[!res]*.elle"):  # find files with elle extension in the current folder, EXCLUDE those that start with "res"
    converted_file_name=file_to_convert.replace(".elle","") # extract the name without file extension
    # TEST: are the files already converted
    """
    if os.path.isfile(converted_file_name+".csv"):
    #    os.remove(converted_file_name+".txt")
        print("File \'"+converted_file_name+ ".csv\' already exists. Exiting to avoid overwriting.")
        sys.exit()
    """
    print("Converting "+str(file_to_convert)) # letting know which file is being opened

    complete_list_of_things_to_search=["LOCATION","UNODES","CONC_A","U_FRACTURES","U_PHASE","U_TEMPERATURE","U_DIF_STRESS","U_MEAN_STRESS","U_DENSITY","U_YOUNGSMODULUS","U_ENERGY"]
    # what I need to find in the elle file: every couple is the start and the end of the section I need to save. 
    #e.g. from "LOCATION" to "CONC_A" means I am going to save all the lines after "LOCATION" until "CONC_A".
    for ind,section in enumerate(complete_list_of_things_to_search):   # ind is the index, section is the name of the section (e.g. "LOCATION")
        if section in ["UNODES", "U_FRACTURES", "U_TEMPERATURE"]:        # sections we want to save
            things_to_search=complete_list_of_things_to_search[ind:ind+2]  # search for this section and the next (start and stop of the search process)
            lines_list=[] # initialising someuseful variables
            for x in things_to_search:    # now things_to_search changes every time with every 'section'
                # call the function that searches the words (x) in the file
                line_of_results = search_string_in_file(file_to_convert,x)
                # append the newly found result
                lines_list.append(line_of_results)
            line_number=lines_list[0]   # line where to start
            lines_to_write=[]
            save_the_right_lines(file_to_convert) # run function

            if section == "UNODES":     # needs to assign headers: x,y,z
                myDf = pd.read_csv(converted_file_name+".txt",delim_whitespace=True,header=None) # create pandas dataframe
                myDf.columns = ["id","x coord", "y coord"] # assign headers
                myDf['z coord'] = 0       # add a third column for the z coordinate (set to 0, we are in 2D)
                myDf["id"]=myDf["id"].astype('int64',errors='raise') # need to change the type of "id" column to merge later
            if section == "U_FRACTURES":  # create a second pandas dataframe
                fracDf = pd.read_csv(converted_file_name+".txt",delim_whitespace=True,header=None)#,delimiter=' ')
                fracDf.drop(fracDf.index[[0]],inplace=True) # drop the first row (that says "default = 0")
                fracDf.columns = ["id","Fractures"] # assign headers
                #fracDf.to_csv('fractures.csv',index=False)   # save a .csv to check
                print(fracDf.dtypes)
                fracDf["id"]=fracDf["id"].astype('int64',copy=True,errors='raise')
                # merge UNODES with FRACTURES based on their index ("id")
                mergedDf = myDf.merge(fracDf,how="left",left_on="id",right_on="id")#,suffixes=["_L","_R"])  
            if section == "U_TEMPERATURE":
                pressDf = pd.read_csv(converted_file_name+".txt",delim_whitespace=True,header=None)
                pressDf.drop(pressDf.index[[0]],inplace=True) # drop the first row (that says "default = 0")
                pressDf.columns = ["id","Pressure"] # assign headers
                #pressDf.to_csv('pressDf.csv',index=False)   # save a .csv to check
                pressDf["id"]=pressDf["id"].astype('int64',copy=True,errors='raise')
                mergedDf = mergedDf.merge(pressDf,how="left",left_on="id",right_on="id")

        if ind==len(complete_list_of_things_to_search)-1:  # if we reached the last thing to search: stop. Don't search anymore.
            break
        #else:                # sections we don't care about
        #    pass
    os.remove(converted_file_name+".txt")
    
    # save the csv file
    mergedDf.to_csv(converted_file_name+".csv",index=False)
    print(converted_file_name+".csv created")
