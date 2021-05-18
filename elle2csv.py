"""
Converting elle files to csv to be read in paraview
Giulia Fedrizzi, February-May 2021
"""
import os
import pandas as pd
import glob

def search_string_in_file(file_name, string_to_search):
    """Search for the given string in file and return lines containing that string"""
    line_number = 0
    with open(file_name, 'r') as read_obj:      # Open the file in read only mode   
        for line in read_obj:            # Read all lines in the file one by one
            # For each line, check if line contains the string
            line_number += 1
            if string_to_search in line:
                # save the line where the word has been found
                line_of_result=line_number
                break  # found the string? -> stop searching and exit the loop
        # Return the line number where the result was found
        return line_of_result 

def save_the_right_lines(file_name,section):
    """get the list of number of lines to read: lines_list[0] is the fist line to save, lines_list[1] the last. Save all of the lines in between:"""
    lines_to_read = list(range(lines_list[0],lines_list[1]-1)) 
    if section == "UNODES":
        minimumLine =min(lines_to_read)  # start here
    else:
        minimumLine =min(lines_to_read) + 1     # need to skip the first line (it defines the default values)
    maximumLine = max(lines_to_read) # end here
    rangeLines = maximumLine - minimumLine + 1     # number of lines between start and end (included)
    # save lines in the range determined by minimumLine and maximumLine:
    dFconverted = pd.read_csv(file_name,skiprows=minimumLine, nrows=rangeLines,delim_whitespace=True,header=None) # to do : add string_to_search as header
    return(dFconverted)

"""
Big loop over every elle file in the current directory:
"""
for file_to_convert in sorted(glob.glob("*.elle")):  # find files with elle extension in the current folder, sorted by name
    if file_to_convert.startswith("res"): # EXCLUDE those that start with "res"
        continue
    if file_to_convert.startswith("my_experiment001") or file_to_convert.startswith("my_experiment002"):
        continue
    converted_file_name=file_to_convert.replace(".elle","") # extract the name without file extension
    # TEST: are the files already converted?
    if os.path.isfile(converted_file_name+".csv"):
        print("File \'"+converted_file_name+ ".csv\' already exists. Exiting to avoid overwriting.")
        continue

    print("Converting "+str(file_to_convert)) # letting know which file is being opened

    complete_list_of_things_to_search=["LOCATION","UNODES","CONC_A","U_FRACTURES","U_PHASE","U_TEMPERATURE","U_DIF_STRESS","U_MEAN_STRESS","U_DENSITY","U_YOUNGSMODULUS","U_ENERGY","U_DISLOCDEN","U_VISCOSITY","U_ATTRIB_A"]
    # what I need to find in the elle file: every couple is the start and the end of the section I need to save. 
    #e.g. from "UNODES" to "CONC_A" means I am going to save all the lines after "LOCATION" until "CONC_A".
    for ind,section in enumerate(complete_list_of_things_to_search):   # ind is the index, section is the name of the section (e.g. "LOCATION")
        if section in ["UNODES", "U_FRACTURES", "U_TEMPERATURE","U_DENSITY","U_YOUNGSMODULUS","U_DISLOCDEN"]:        # sections we want to save
            things_to_search=complete_list_of_things_to_search[ind:ind+2]  # search for this section and the next (start and stop of the search process)
            lines_list=[] # initialising some useful variables
            for x in things_to_search:    # now things_to_search changes every time with every 'section'
                # call the function that searches the words (x) in the file
                line_of_results = search_string_in_file(file_to_convert,x)
                # append the newly found result
                lines_list.append(line_of_results)
            line_number=lines_list[0]   # line where to start
            lines_to_write=[]
            # --------------------------
            # RUN SAVE RIGHT LINES
            convertedDf = save_the_right_lines(file_to_convert,section) # run function with input: elle file and section to save
            # --------------------------
            
            # Create a dataframe for each section, assign the correct header and merge it with the previous one
            if section == "UNODES":     # needs to assign headers: x,y,z
                #myDf = pd.read_csv(converted_file_name+".txt",delim_whitespace=True,header=None) # create pandas dataframe
                myDf = convertedDf
                myDf.columns = ["id","x coord", "y coord"] # assign headers
                myDf['z coord'] = 0       # add a third column for the z coordinate (set to 0, we are in 2D)
                myDf["id"]=myDf["id"].astype('int64',errors='raise') # need to change the type of "id" column to merge later

            elif section == "U_FRACTURES":  # create a second pandas dataframe
                #fracDf = pd.read_csv(converted_file_name+".txt",delim_whitespace=True,header=None)
                fracDf = convertedDf
                fracDf.columns = ["id","Fractures"] # assign headers
                fracDf["id"]=fracDf["id"].astype('int64',copy=True,errors='raise')
                # merge UNODES with FRACTURES based on their index ("id")
                mergedDf = myDf.merge(fracDf,how="left",left_on="id",right_on="id")#,suffixes=["_L","_R"])  
            elif section == "U_TEMPERATURE":
                pressDf =convertedDf
                pressDf.columns = ["id","Pressure"] # assign headers
                pressDf["id"]=pressDf["id"].astype('int64',copy=True,errors='raise') # need to change the type in order to merge by id
                mergedDf = mergedDf.merge(pressDf,how="left",left_on="id",right_on="id") # merge with previous dataframe
            elif section == "U_YOUNGSMODULUS":
                youngsDf = convertedDf
                youngsDf.columns = ["id","Young's Modulus"] # assign headers
                youngsDf["id"]=youngsDf["id"].astype('int64',copy=True,errors='raise') # need to change the type in order to merge by id
                mergedDf = mergedDf.merge(youngsDf,how="left",left_on="id",right_on="id") # merge with previous dataframe
            elif section == "U_DISLOCDEN":  # = porosity
                poroDf = convertedDf
                poroDf.columns = ["id","Porosity"] # assign headers
                poroDf["id"]=poroDf["id"].astype('int64',copy=True,errors='raise') # need to change the type in order to merge by id
                mergedDf = mergedDf.merge(poroDf,how="left",left_on="id",right_on="id") # merge with previous dataframe
            elif section == "U_DENSITY": # = counter for broken bonds
                sectionDf = convertedDf
                sectionDf.columns = ["id","Broken Bonds"] # assign headers
                sectionDf["id"]=sectionDf["id"].astype('int64',copy=True,errors='raise') # need to change the type in order to merge by id
                mergedDf = mergedDf.merge(sectionDf,how="left",left_on="id",right_on="id") # merge with previous dataframe
                
            else:
                raise ValueError(str(section) + " did not match any valid option")
            

        if ind==len(complete_list_of_things_to_search)-1:  # if we reached the last thing to search: stop. Don't search anymore.
            break
    
    # save the csv file
    mergedDf.to_csv(converted_file_name+".csv",index=False)
    print(converted_file_name+".csv created")
