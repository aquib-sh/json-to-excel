# json-to-excel
Python script which merges many JSON files into one Excel with easy to read format and then again seperates those JSON files back from Excel.

## Windows Users
1> You need to have python 3.8.6 installed on your system
   you can download the appropriate verson from here
   https://www.python.org/downloads/

2> install python from installer you need to keep in mind
   that it should be in your path
   there would come an option while installing such as add python to path
   you should check this option

3> to install the necassary required modules
   you can go on cmd and type
   
   pip install openpyxl pandas xlrd

4> then you can run the script by navigating to that directory from cd command
	and
   if you want to export the JSON files to excel then use python j2e.py --export-excel
	and
   if you want to export excel file to JSON then use python j2e.py --export-json

5> remember that the all JSON files should be provided in input directory

6> data would be saved as a .xlsx file inside excel directory which is present inside outputs

7> i have highlighted the directory and file names in the script if u need to change it in the future(not recommended)


## Mac and Linux Users
1> you need to have python 3.8.6 installed on your system
   you can download the appropriate verson from by
   sudo apt install python3

2> sudo apt install python3-pip 

3> to install the necassary required modules
   you can go on cmd and type

   pip3 install openpyxl pandas

4> then you can run the script by navigating to that directory from cd command
	and
   if you want to export the JSON files to excel then use python3 j2e.py --export-excel
	and
   if you want to export excel file to JSON then use python3 j2e.p --export-json

5> remember that the all JSON files should be provided in input directory

6> data would be saved as a .xlsx file inside excel directory which is present inside outputs

7> i have highlighted the directory and file names in the script if u need to change it in the future(not recommended)
