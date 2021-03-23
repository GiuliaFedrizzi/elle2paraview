# elle2paraview
## About the files

*elle2paraview* is a set of scripts that makes it possible to open *.elle* files in ParaView and save figures. It does so by converting them to *.csv* files.

 
 * *elle2csv.py*  looks for .elle files in the current directory and extracts `UNODES` coordinates, `FRACTURES` and `TEMPERATURE` (renamed as *pressure*). It saves all these in a .csv file with the same name as the original .elle file. More sections will be added soon.
 
 * *save-figure-from-csv.py*  is a [ParaView Python](https://kitware.github.io/paraview-docs/latest/python/) script that imports the .csv files in the current directory into Paraview, applies the `table to points` filter, and saves a figure displaying fractures. Saving other features will be added soon (e.g. pressure).
 
 [Here](https://www.paraview.org/Wiki/ParaView/Data_formats#CSV_.28Comma_Separated_Variable.29_files) is more information about how ParaView reads csv files.


## Requirements

* *elle2csv.py* works for **python3** and uses [Pandas](https://pandas.pydata.org/). **You need to install Pandas** before you can run the script.

Note: ParaView Python scripts are very version-dependent. This script has been tested on version 5.4.1 on an Ubuntu 18.04 machine.

## Usage

1. Copy the scripts into the folder with the .elle files you want to convert.
2. You can run *elle2csv.py* in a terminal by typing ```python3 elle2csv.py``` or run it in a Python IDE.
3. To run *save-figure-from-csv.py* type ```pvpython save-figure-from-csv.py```.

## Using only *elle2csv.py* to convert to *csv*
Follow the instructions on the [official documentation](https://www.paraview.org/Wiki/ParaView/Data_formats#CSV_.28Comma_Separated_Variable.29_files) to load *csv* files into ParaView correctly.

