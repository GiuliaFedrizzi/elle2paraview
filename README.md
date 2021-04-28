# elle2paraview
## About the files

*elle2paraview* is a set of scripts that makes it possible to open [*.elle* files](http://elle.ws/) in ParaView and save figures. It does so by converting them to *.csv* files.

 
 * *elle2csv.py*  looks for .elle files in the current directory and extracts the unodes' `coordinates`, `fractures`, `pressure` (stored under *temperature*), `Young's Modulus` and `porosity` (originally stored under *dislocation density*). It saves all these in a .csv file with the same name as the original .elle file.
 
 * *save-figure-from-csv.py*  is a [ParaView Python](https://kitware.github.io/paraview-docs/latest/python/) script that imports the .csv files in the current directory into Paraview, applies the `Table to points` filter, and saves 3 figures displaying **fractures**, **pressure** field and **porosity** distribution respectively. Most of this file was written with ParaView's automatic scripting, the [Trace Recorder](https://www.paraview.org/Wiki/ParaView_and_Python#Trace_Recorder).
 * *save-animation-from-csv.py*: same as above, but works with **ParaView 5.9.0**

* *clearAll* is a bash script that deletes ALL the *.elle* files generated by an *Elle* experiment that start with 'my_exp' (the standard name) and ALL the *.csv* files. Use with caution!

 [Here](https://www.paraview.org/Wiki/ParaView/Data_formats#CSV_.28Comma_Separated_Variable.29_files) is more information about how ParaView reads csv files.


## Requirements

* *elle2csv.py* works for **python3** and uses [Pandas](https://pandas.pydata.org/). **You need to install Pandas** before you can run the script.
* *save-figure-from-csv.py* is compatible with version 5.4.1 of ParaView and seems to run with **Python2** (with the *paraview.simple* module).
* *save-animation-from-csv.py* is compatible with version 5.9.0 of ParaView.

Note: ParaView Python scripts are very version-dependent. The scripts have been tested on an Ubuntu 18.04 machine.

## Usage

1. Copy the scripts into the folder with the .elle files you want to convert.
2. You can run *elle2csv.py* in a terminal by typing ```python3 elle2csv.py``` or run it in a Python IDE.
3. To run *save-figure-from-csv.py* type ```python2 save-figure-from-csv.py```or ```pvpython save-figure-from-csv.py```.

### Display csv files in ParaView

Follow the instructions on the [official documentation](https://www.paraview.org/Wiki/ParaView/Data_formats#CSV_.28Comma_Separated_Variable.29_files) to load *csv* files into ParaView correctly.

