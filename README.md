# json-to-excel
python script which merges many JSON files into one Excel with easy to read format and then again seperates those JSON files back from Excel.

## Windows Users
1> YOU NEED TO HAVE PYTHON 3.8.6 INSTALLED ON YOUR SYSTEM
   YOU CAN DOWNLOAD THE APPROPRIATE VERSON FROM HERE
   https://www.python.org/downloads/

2> INSTALL PYTHON FROM INSTALLER YOU NEED TO KEEP IN MIND
   THAT IT SHOULD BE IN YOUR PATH
   THERE WOULD COME AN OPTION WHILE INSTALLING SUCH AS ADD PYTHON TO PATH
   YOU SHOULD CHECK THIS OPTION

3> TO INSTALL THE NECASSARY REQUIRED MODULES
   YOU CAN GO ON CMD AND TYPE
   
   pip install openpyxl pandas xlrd

4> THEN YOU CAN RUN THE SCRIPT BY NAVIGATING TO THAT DIRECTORY FROM cd command
	AND
   IF YOU WANT TO EXPORT THE JSON FILES TO EXCEL THEN USE python j2e.py --export-excel
	AND
   IF YOU WANT TO EXPORT EXCEL FILE TO JSON THEN USE python j2e.py --export-json

5> REMEMBER THAT THE ALL JSON FILES SHOULD BE PROVIDED IN input DIRECTORY

6> DATA WOULD BE SAVED AS A .xlsx FILE inside excel DIRECTORY WHICH IS PRESENT INSIDE outputs

7> I HAVE HIGHLIGHTED THE DIRECTORY AND FILE NAMES IN THE SCRIPT IF U NEED TO CHANGE IT IN THE FUTURE(NOT RECOMMENDED)


## Mac and Linux Users
1> YOU NEED TO HAVE PYTHON 3.8.6 INSTALLED ON YOUR SYSTEM
   YOU CAN DOWNLOAD THE APPROPRIATE VERSON FROM BY
   sudo apt install python3

2> sudo apt install python3-pip 

3> TO INSTALL THE NECASSARY REQUIRED MODULES
   YOU CAN GO ON CMD AND TYPE

   pip3 install openpyxl pandas

4> THEN YOU CAN RUN THE SCRIPT BY NAVIGATING TO THAT DIRECTORY FROM cd command
	AND
   IF YOU WANT TO EXPORT THE JSON FILES TO EXCEL THEN USE python3 j2e.py --export-excel
	AND
   IF YOU WANT TO EXPORT EXCEL FILE TO JSON THEN USE python3 j2e.p --export-json

5> REMEMBER THAT THE ALL JSON FILES SHOULD BE PROVIDED IN input DIRECTORY

6> DATA WOULD BE SAVED AS A .xlsx FILE inside excel DIRECTORY WHICH IS PRESENT INSIDE outputs

7> I HAVE HIGHLIGHTED THE DIRECTORY AND FILE NAMES IN THE SCRIPT IF U NEED TO CHANGE IT IN THE FUTURE(NOT RECOMMENDED)
