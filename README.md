# About:
Welcome to DictionaryMaker!
DictionaryMaker is a program that builds on a QtDesigner GUI to make a Python program that allows you to create your own personal dictionary!

* Developed by Olivia Bhowmik
* Email: developer.olivia.bhowmik@gmail.com
* License: MIT
* Version: 1.0.0
* Technology: QtDesigner, Python 3 and Sqlite

# Images:
## Game Mode
![The Application Window](images/DictionaryPic.PNG)

# Files:
| File Name | Description |
| --------- | ----------- |
| DictionaryMaker.py | Main file that runs the game |
| natdictionary.py | Contains the classes and functions that run the program |
| dataconnections.py | Connects the program to the database |
| DictionaryDB.db | Database file that contains all the dictionary data |
| DictionaryMaker.ui | UI file that contains the entire application GUI, made with QtDesigner |
| olida.ui | Main UI file where sub-applications can be added |

# Main File:
* The program imports all relevant files and technology
* It sets up the GUI window and loads it with information from the dictionary database

# Connections File:
* Establishes a connection with the Sqlite database and makes a cursor

# Dictionary Prepper File(natdictionary):
* Uploads and imports all relevant files and technologies
* Creates the NatDictionary class that will actually organize and load dictionary data as well as install the dictionary functionality (add, edit, delete e.t.c)
* In the first init function, the program initializes categories that will be filtered with or edited in the dictionary. It also creates actions for single or double clicking on the table as well as actions for pressing any buttons on the GUI.
* The next few functions (languPopul, typeePopul, lettrPopul, cllasPopul and grammPopul) retrieve their respective information from the sqlite database (language of the word e.t.c.) and compiles all the information from the categories that will display on the main table to a couple cursors, one cursor for each category.
* The biggest function, tablePopul is responsible for actually composing the entire main table using the individual cursors that were previously made. It starts by clearing away the data that was previously displayed on the main table, creating headers for every category and connecting with the combos/cursors that were created for them. Then it decides what data to display on the main table using two strings called the wherestring and countstring. Through a series of if statements that determine the current filter conditions, the program dynamically builds the database retrieval statement to make sure that only the relevant data is retrieved. After taking into account all the category information and the filters, the function populates the main table with data.
* The function clear_button_clicked detects when the user pushes the clear button and deletes any information displayed in the category message boxes on top.
* The adda_button_clicked function inserts the information from the category display boxes into the word database if the Add button is clicked by the user. It calls tablePopul at the end to redisplay the table with the new data.
* The delt_button_clicked function checks whether the user currently has a pre-existing word selected, and if they do, it removes that word from the database.
* The def edit_button_clicked function assigns a variable to the text in all the different QLineEdit widgets for the word that is currently selected. It then uploads those changes to the database.
* The def_cell_single_clicked function detects which word the user clicked on and reads the primary key (pykey) of that word. It then uses the pykey to search a corresponding database of extra information on the word. If the word clicked has any extra information attached, it displays the info on the QTextEdit widget to the side of the main table.
* The def_cell_double_clicked function identifies which word the user clicked on using the pykey. It checks whether there is any information under the different categories for the word and if there is, it displays the info on the QLineEdit widgets on top.
* def_savenote_button_clicked checks whether a word is selected and if it is, it uploads any extra information in the QTextEdit widget to the separate details database.
* Finally the def reset_filters_to_all function goes through all the dropdown filters (QComboBoxes) and manually sets them to the “All” option.


# Future Plans:
Below are some of the ideas I want to implement in the future:
* Implement word search functionality.
* Make the wordcount display how many words are filtered instead of the total words existing.

# Installing the Game:
* First make sure to have Python Version 3 installed on your device from https://www.python.org/
* For admin purposes the user can download the DB Browser for Sqlite and QtDesigner but it isn't necessary to run the program.
* Open the main file "DictionaryMaker.py" through a Python editor and run

# Using the Application:
* In order to select or edit a word the user needs to double click on it
* The rest of the application is fairly self-explanatory
