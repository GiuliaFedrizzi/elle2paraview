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

def porosityDiff(oldfile,idName,mergedDf):
    poroDiffDf = pd.read_csv(oldfile,delimiter=',',usecols=["id","Porosity"])  # get the porosity values from old file
    poroDiffDf["Porosity"] = mergedDf["Porosity"] - poroDiffDf["Porosity"] # dataframe with difference in porosity from initial porosity distribution
    poroDiffDf.columns = ["id",idName]  # rename column from Porosity to Porosity Variation
    mergedDf = mergedDf.merge(poroDiffDf,how="left",left_on="id",right_on="id") # merge with previous dataframe
    return mergedDf
    
    

count=0; first_file=''
"""
Big loop over every elle file in the current directory:
"""
for file_to_convert in sorted(glob.glob("*.elle")):  # find files with elle extension in the current folder, sorted by name
    if file_to_convert.startswith("res"): # EXCLUDE those that start with "res"
        continue
    if file_to_convert.startswith("my_experiment001") or file_to_convert.startswith("my_experiment002"): # ignore first two files
        continue
    converted_file_name=file_to_convert.replace(".elle","") # extract the name without file extension
    # TEST: are the files already converted?
    if os.path.isfile(converted_file_name+".csv"):
        print("File \'"+converted_file_name+ ".csv\' already exists. Exiting.")
        if count == 0:
            first_file = converted_file_name+".csv"
            
        count +=1
        prev_file = converted_file_name+".csv"
        continue
    print("Converting "+str(file_to_convert)+"...") # letting know which file is being opened

    complete_list_of_things_to_search=["LOCATION","UNODES","CONC_A","U_FRACTURES","U_PHASE","U_TEMPERATURE","U_DIF_STRESS","U_MEAN_STRESS","U_DENSITY","U_YOUNGSMODULUS","U_ENERGY","U_DISLOCDEN","U_VISCOSITY","U_ATTRIB_A","U_ATTRIB_B","U_ATTRIB_C"]
    # what I need to find in the elle file: every couple is the start and the end of the section I need to save. 
    #e.g. from "UNODES" to "CONC_A" means I am going to save all the lines after "LOCATION" until "CONC_A".
    for ind,section in enumerate(complete_list_of_things_to_search):   # ind is the index, section is the name of the section (e.g. "LOCATION")
        if section in ["UNODES", "U_FRACTURES", "U_TEMPERATURE","U_DENSITY","U_YOUNGSMODULUS","U_DISLOCDEN","U_VISCOSITY","U_ENERGY","U_ATTRIB_B"]:        # sections we want to save
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
            if convertedDf.size == 0 and section != "U_FRACTURES" and section != "U_DENSITY":   #  skip empty sections, except for fractures
                print("WARNING! Empty section: "+section)
                continue
            else:
                # Create a dataframe for each section, assign the correct header and merge it with the previous one
                if section == "UNODES":     # needs to assign headers: x,y,z
                    #myDf = pd.read_csv(converted_file_name+".txt",delim_whitespace=True,header=None) # create pandas dataframe
                    mergedDf = convertedDf
                    mergedDf.columns = ["id","x coord", "y coord"] # assign headers
                    mergedDf['z coord'] = 0       # add a third column for the z coordinate (set to 0, we are in 2D)
                    mergedDf["id"]=mergedDf["id"].astype('int64',errors='raise') # need to change the type of "id" column to merge later
                    
                elif section == "U_FRACTURES":  # create a second pandas dataframe
                    if convertedDf.size == 0:    # if it's empty (no fractures), add a column of zeros.
                        mergedDf['Fractures'] = 0   # It's useful because Paraview won't show "Fractures" as an option if they are only avail. in a later file  
                        print("No fractures in this timestep!")
                    else:    
                        fracDf = convertedDf
                        fracDf.columns = ["id","Fractures"] # assign headers
                        fracDf["id"]=fracDf["id"].astype('int64',copy=True,errors='raise')
                        #mergedDf2=mergedDf # need a second copy for merging later
                        # merge UNODES with FRACTURES based on their index (the column called "id")
                        mergedDf = mergedDf.merge(fracDf,how="left",left_on="id",right_on="id").fillna(0)  
                        #mergedDf["Fractures"] = convertedDf.iloc[:,1]  # doesn't work, need to use 'merge'
                elif section == "U_TEMPERATURE":
                    mergedDf["Pressure"] = convertedDf.iloc[:,1]
                elif section == "U_YOUNGSMODULUS":
                    mergedDf["Young's Modulus"] = convertedDf.iloc[:,1]
                elif section == "U_DISLOCDEN":  # = porosity
                    mergedDf["Porosity"] = convertedDf.iloc[:,1]

                    # calculate difference in porosity from first file
                    if count >0:          # if there are already csv files:
                        if len(first_file) == 0:
                            raise ValueError("Couldn't find the first file")
                        # calculate difference
                        mergedDf = porosityDiff(first_file,"Porosity Variation Global",mergedDf)
                        # difference with previous tstep
                        mergedDf = porosityDiff(prev_file,"Porosity Variation",mergedDf)
                    else:
                        mergedDf['Porosity Variation Global'] = 0   # It's useful because Paraview won't show it as an option if they are only present in a later file  
                        mergedDf['Porosity Variation'] = 0   # It's useful because Paraview won't show it as an option if they are only present in a later file  
                        print("This is the first file")
                    
                elif section == "U_DENSITY": # = counter for broken bonds
                    if convertedDf.size == 0:    # if it's empty (no fractures), add a column of zeros.
                        mergedDf['Broken Bonds'] = 0   # It's useful because Paraview won't show it as an option if they are only present in a later file  
                    else:
                        BrDb = convertedDf
                        BrDb.columns = ["id","Broken Bonds"] # assign headers
                        BrDb["id"]=BrDb["id"].astype('int64',copy=True,errors='raise')
                        # merge with old dataframe based on their index (the column called "id")
                        mergedDf = mergedDf.merge(BrDb,how="left",left_on="id",right_on="id").fillna(0)
                        
                #elif section == "U_DIF_STRESS":
                #    mergedDf["U_DIF_STRESS"] = convertedDf.iloc[:,1]
                #elif section == "U_MEAN_STRESS":
                #    mergedDf["Solid Pressure"] = convertedDf.iloc[:,1]
                elif section == "U_ENERGY":
                    mergedDf["Y Velocity"] = convertedDf.iloc[:,1]
                elif section == "U_ATTRIB_B":
                    mergedDf["Permeability"] = convertedDf.iloc[:,1]
                elif section == "U_VISCOSITY":
                    convertedDf.columns = ["id","Healing"] # assign headers
                    convertedDf["id"]=convertedDf["id"].astype('int64',copy=True,errors='raise') # need to change the type in order to merge by id
                    mergedDf = mergedDf.merge(convertedDf,how="left",left_on="id",right_on="id").fillna(1) # merge with previous dataframe
                else:
                    raise ValueError(str(section) + " did not match any valid option")
                
        if ind==len(complete_list_of_things_to_search)-1:  # if we reached the last thing to search: stop. Don't search anymore.
            break
    
    # save the csv file
    mergedDf.to_csv(converted_file_name+".csv",index=False)
    print(converted_file_name+".csv created")
    if count == 0:
        first_file = converted_file_name+".csv"
        count +=1
    prev_file = converted_file_name+".csv"
    
