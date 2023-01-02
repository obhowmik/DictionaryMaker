#NatDictionary by Suman
import sys, os
from PyQt6 import uic #QtSql, QtCore, QtGui
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from dataconnections import *
sys.dont_write_bytecode = True

# get the directory of this script
path = os.path.dirname(os.path.abspath(__file__))

#debug control..Comment out all "if DEBUG:" statements for production for performance issues
DEBUG = False #True
if DEBUG:print('DEBUGGING')

NatDictionaryUI, NatDictionaryBase = uic.loadUiType(
    os.path.join(path, 'DictionaryMaker.ui'))

class NatDictionary(NatDictionaryUI, NatDictionaryBase):

    def __init__(self, fileInfo, parent=None):
        NatDictionaryBase.__init__(self, parent)
        self.setupUi(self)

        #initialize combo and table population
        self.languPopul()
        self.typeePopul()
        self.lettrPopul()
        self.cllasPopul()
        self.grammPopul()
        self.tablePopul()

        #connect single table cell clicked to the details
        self.ttable.cellClicked.connect(self.cell_single_clicked)
        #double click on a cell of the table widget to perform actions
        self.ttable.cellDoubleClicked.connect(self.cell_double_clicked)

        #connect CLEAR pushbutton to corresponding method
        self.pb_clear.clicked.connect(self.clear_button_clicked)
        #connect ADD Transaction pushbutton to corresponding method
        self.pb_adda.clicked.connect(self.adda_button_clicked)
        #connect EDIT Transaction pushbutton to corresponding method
        self.pb_edit.clicked.connect(self.edit_button_clicked)
        #connect DELETE Transaction pushbutton to corresponding method
        self.pb_delt.clicked.connect(self.delt_button_clicked)

        #reset to all
        self.pb_resettoall.clicked.connect(self.reset_filters_to_all)

        #refresh table push button
        self.pb_rfrh.clicked.connect(self.tablePopul)
        #connect pb_savenote pushbutton to corresponding method
        self.pb_savenote.clicked.connect(self.savenote_button_clicked)

    #Retreives the language information for each item in the database and compiles it into a combo
    def languPopul(self):

        #add the filter all value
        self.langu_f.addItem("All")

        #fetching and populating data
        cn.execute("SELECT * FROM langu")

        #get the entire table data in cursor
        cur=cn.fetchall()
        for i,row in enumerate(cur): #pick rows one at a time, i = row no
            for j,val in enumerate(row): #pick comlumns one at a time, j = column no
                self.langu.addItem(str(val))
                self.langu_f.addItem(str(val))

    #Retreives the type information for each item in the database and compiles it into a combo
    def typeePopul(self):
        #add the filter all value
        self.typee_f.addItem("All")

        #fetching and populating data
        cn.execute("SELECT * FROM typee")

        #get the entire table data in cursor
        cur=cn.fetchall()
        for i,row in enumerate(cur): #pick rows one at a time, i = row no
            for j,val in enumerate(row): #pick comlumns one at a time, j = column no
                self.typee.addItem(str(val))
                self.typee_f.addItem(str(val))

    #Retreives the letter information for each item in the database and compiles it into a combo
    def lettrPopul(self):
        #add the filter all value
        self.lettr_f.addItem("All")

        #fetching and populating data
        cn.execute("SELECT lettr FROM lettr")

        #get the entire table data in cursor
        cur=cn.fetchall()
        for i,row in enumerate(cur): #pick rows one at a time, i = row no
            for j,val in enumerate(row): #pick comlumns one at a time, j = column no
                self.lettr.addItem(str(val))
                self.lettr_f.addItem(str(val))

    #Retreives the class information for each item in the database and compiles it into a combo
    def cllasPopul(self):
        #add the filter all value
        self.cllas_f.addItem("All")

        #fetching and populating data
        cn.execute("SELECT cllas FROM cllas")

        #get the entire table data in cursor
        cur=cn.fetchall()
        for i,row in enumerate(cur): #pick rows one at a time, i = row no
            for j,val in enumerate(row): #pick comlumns one at a time, j = column no
                self.cllas.addItem(str(val))
                self.cllas_f.addItem(str(val))

    #Retreives the grammar information for each item in the database and compiles it into a combo
    def grammPopul(self):
        #fetching and populating data
        cn.execute("SELECT gramm FROM gramm")

        #get the entire table data in cursor
        cur=cn.fetchall()
        for i,row in enumerate(cur): #pick rows one at a time, i = row no
            for j,val in enumerate(row): #pick comlumns one at a time, j = column no
                self.gramm.addItem(str(val))

    #Populates the main table with data
    def tablePopul(self):

        #delete all previous data 1st
        self.ttable.clearContents()
        self.ttable.setRowCount(0)
        self.ttable.setColumnCount(0)

        #determining colcount
        self.ttable.setColumnCount(13)

        #determine Horizontal Header Labels
        self.ttable.setHorizontalHeaderLabels(str("PK;Ltr;Langu;Type;Word;Meaning;Trick;Root1;Root2;Gramr;Class;Example;Remks;").split(";"))

        #find current selected text of the combos
        cst_langu_f = str(self.langu_f.currentText())
        cst_typee_f = str(self.typee_f.currentText())
        cst_lettr_f = str(self.lettr_f.currentText())
        cst_cllas_f = str(self.cllas_f.currentText())

        #base select string
        counttstring = "SELECT COUNT(*) FROM natdictionary"
        selectstring = "SELECT * FROM natdictionary"

        #construct beginning of the where string
        if cst_langu_f != "All" or cst_typee_f != "All" or cst_lettr_f != "All" or cst_cllas_f != "All":
            wherestring = " WHERE"
        else:
            wherestring = ""

        #langu where determination
        if cst_langu_f != "All":
            wherestring = wherestring + " langu =  \'" + cst_langu_f + "'"

        #typee where determination
        if cst_typee_f != "All":
            if len(wherestring) > 6:
                wherestring = wherestring + " AND typee =  \'" + cst_typee_f + "'"
            else:
                wherestring = wherestring + " typee =  \'" + cst_typee_f + "'"

        #lettr where determination
        if cst_lettr_f != "All":
            if len(wherestring) > 6:
                wherestring = wherestring + " AND lettr =  \'" + cst_lettr_f + "'"
            else:
                wherestring = wherestring + " lettr =  \'" + cst_lettr_f + "'"

        #cllas where determination
        if cst_cllas_f != "All":
            if len(wherestring) > 6:
                wherestring = wherestring + " AND cllas =  \'" + cst_cllas_f + "'"
            else:
                wherestring = wherestring + " cllas =  \'" + cst_cllas_f + "'"

        counttstring = counttstring + wherestring
        selectstring = selectstring + wherestring
        if DEBUG:print("counttstring is: " + counttstring)
        if DEBUG:print("selectstring is: " + selectstring)
        #rowcount determination & setting
        #rowcount = cn.execute("SELECT COUNT(*) FROM natdictionary").fetchone()[0]
        rowcount = cn.execute(counttstring).fetchone()[0]
        self.ttable.setRowCount(rowcount)

        #fetching and populating data
        cn.execute(selectstring)

        #get the entire table data in cursor
        cur=cn.fetchall()
        for i,row in enumerate(cur): #pick rows one at a time, i = row no
            for j,val in enumerate(row): #pick comlumns one at a time, j = column no
                self.ttable.setItem(i, j, QTableWidgetItem(str(val)))
                #print i,j,val
        #conn.close()

        counttstring = "SELECT COUNT(*) FROM natdictionary"
        wordcount = cn.execute(counttstring).fetchone()[0]
        if wordcount is None:wordcount = 0
        print (wordcount)
        #wordcount = 12
        self.le_wordcount.setText(str(wordcount))

        self.ttable.setSortingEnabled(True)
        self.ttable.sortItems(5, Qt.SortOrder.AscendingOrder) # column 1(date), Qt.DescendingOrder
        #self.ttable.rowHeight(20)
        self.ttable.resizeColumnsToContents()

    def clear_button_clicked(self):
        self.msgl.setText("Clearing...")
        self.pykey.clear()
        self.wordd.clear()
        self.meani.clear()
        self.examp.clear()
        self.trick.clear()
        self.root1.clear()
        self.root2.clear()
        self.remks.clear()

    def adda_button_clicked(self):
        self.msgl.setText("Howdy.")

        ilangu = str(self.langu.currentText())  #01
        itypee = str(self.typee.currentText())  #02
        iwordd = str(self.wordd.text())         #03
        imeani = str(self.meani.text())         #04
        ilettr = str(self.lettr.currentText())  #05
        icllas = str(self.cllas.currentText())  #06
        iexamp = str(self.examp.text())         #07
        itrick = str(self.trick.text())         #08
        iroot1 = str(self.root1.text())         #09
        iroot2 = str(self.root2.text())         #10
        igramm = str(self.gramm.currentText())  #11
        iremks = str(self.remks.text())         #12


        Auto_lettr = iwordd[0]
        uppercase_auto_lettr = Auto_lettr.upper()
                #prepare the input array
        t = (ilangu, itypee, iwordd, imeani, uppercase_auto_lettr, icllas, iexamp, itrick, iroot1, iroot2, igramm, iremks)
        cn.execute("INSERT INTO natdictionary (langu, typee, wordd, meani, lettr, cllas, examp, trick, root1, root2, gramm, remks) VALUES (?,?,?,?,?,?,?,?,?,?,?,?)",(t[0],t[1],t[2],t[3],t[4],t[5],t[6],t[7],t[8],t[9],t[10],t[11]))
        conn.commit()         #inserts data into database
        #conn.close()


        self.tablePopul()

    def delt_button_clicked(self):
        self.msgl.setText("Howdy....We are Deleting")

        if self.pykey.text() == "":
            self.msgl.setText("Not Found pkey...")
            return

        ipykey = str(self.pykey.text())         #00
        ipykey_i = int(ipykey)

        if ( ipykey_i > 0 ):
            self.msgl.setText("Found valid pkey...")
        else:
            self.msgl.setText("Not Found valid pkey...")
            return

        result = QMessageBox.question(self,
                                            "Confirm Delete...",
                                            "Are you sure you want to delete ? the PK " + ipykey,
                                            QMessageBox.StandardButton.Yes| QMessageBox.StandardButton.No)

        if result == QMessageBox.StandardButton.Yes:
            cn.execute("DELETE FROM natdictionary WHERE pykey=?", (ipykey_i, ))
            conn.commit()
            self.msgl.setText("Deleted..." + ipykey  + "...")
            self.clear_button_clicked()
            self.tablePopul()

    def edit_button_clicked(self):
        self.msgl.setText("Howdy.")

        ipykey = str(self.pykey.text())         #00
        ipykey_i = int(ipykey)
        ilangu = str(self.langu.currentText())  #01
        itypee = str(self.typee.currentText())  #02
        iwordd = str(self.wordd.text())         #03
        imeani = str(self.meani.text())         #04
        ilettr = str(self.lettr.currentText())  #05
        icllas = str(self.cllas.currentText())  #06
        iexamp = str(self.examp.text())         #07
        itrick = str(self.trick.text())         #08
        iroot1 = str(self.root1.text())         #09
        iroot2 = str(self.root2.text())         #10
        igramm = str(self.gramm.currentText())  #11
        iremks = str(self.remks.text())         #12

                #prepare the input array
        t = (ilangu, itypee, iwordd, imeani, ilettr, icllas, iexamp, itrick, iroot1, iroot2, igramm, iremks)
        cn.execute("UPDATE natdictionary SET langu=? ,typee=? ,wordd=? ,meani=? ,lettr=? ,cllas=? ,examp=? ,trick=? ,root1=? ,root2=? ,gramm=? ,remks=? WHERE pykey=?", (t[0],t[1],t[2],t[3],t[4],t[5],t[6],t[7],t[8],t[9],t[10],t[11],ipykey_i))
        conn.commit()
        self.msgl.setText("Edited..." + ipykey  + "..." + iwordd)
        self.tablePopul()

    def cell_single_clicked(self,m,n):
        self.msgl.setText("Howdy..You clicked.")
        #user selected row m, column n

        #get the primary key
        currPyKey = self.ttable.item(m,0).text()
        thisCurrPyKey = int(currPyKey) #convert to int for support
        self.intCurrPyKey = thisCurrPyKey

        rowcount = cn.execute("SELECT COUNT(*) FROM natdictionary_detls WHERE pykey = ? ", (thisCurrPyKey,)).fetchone()[0]
        if rowcount == 0:
            #prepare the input array
            idetls = "Eample:"
            cn.execute("INSERT INTO natdictionary_detls (pykey, detls) VALUES (?,?)", (thisCurrPyKey,idetls))
            conn.commit()

        #fetching the details value and populating data
        cn.execute("SELECT detls FROM natdictionary_detls WHERE pykey = ? ", (thisCurrPyKey,))
        row = cn.fetchone()

                #populate the value now in the details pane
        self.detls.setPlainText(row[0])

    def cell_double_clicked(self,m,n):
        #user selected row(m), column(n)
        if self.ttable.item(m, 0) is not None: cpykey = self.ttable.item(m,0).text()    #pykey
        ###############################
        if self.ttable.item(m, 1) is not None: clettr = self.ttable.item(m,1).text()    #lettr
        if self.ttable.item(m, 2) is not None: clangu = self.ttable.item(m,2).text()    #langu
        if self.ttable.item(m, 3) is not None: ctypee = self.ttable.item(m,3).text()    #Type
        if self.ttable.item(m, 4) is not None: cwordd= self.ttable.item(m,4).text()     #word
        if self.ttable.item(m, 5) is not None: cmeani = self.ttable.item(m,5).text()    #meani
        if self.ttable.item(m, 6) is not None: ctrick = self.ttable.item(m,6).text()    #trick
        if self.ttable.item(m, 7) is not None: croot1 = self.ttable.item(m,7).text()    #root1
        if self.ttable.item(m, 8) is not None: croot2 = self.ttable.item(m,8).text()    #root2
        if self.ttable.item(m, 9) is not None: cgramm = self.ttable.item(m,9).text()    #gramr
        if self.ttable.item(m, 10) is not None: ccllas = self.ttable.item(m,10).text()  #cllas
        if self.ttable.item(m, 11) is not None: cexamp = self.ttable.item(m,11).text()  #examp
        if self.ttable.item(m, 12) is not None: cremks = self.ttable.item(m,12).text()  #remks

        self.pykey.setText(cpykey) #pykey

        #find the combo index to be set for langu
        index = self.langu.findText(clangu, Qt.MatchFlag.MatchFixedString)
        if index >= 0:
            self.langu.setCurrentIndex(index)

        #find the combo index to be set for typee
        index = self.typee.findText(ctypee, Qt.MatchFlag.MatchFixedString)
        if index >= 0:
            self.typee.setCurrentIndex(index)

        self.wordd.setText(cwordd) #wordd
        self.meani.setText(cmeani) #meani

        #find the combo index to be set for lettr
        index = self.lettr.findText(clettr, Qt.MatchFlag.MatchFixedString)
        if index >= 0:
            self.lettr.setCurrentIndex(index)

        #find the combo index to be set for cllas
        index = self.cllas.findText(ccllas, Qt.MatchFlag.MatchFixedString)
        if index >= 0:
            self.cllas.setCurrentIndex(index)

        self.examp.setText(cexamp)   #examp
        self.trick.setText(ctrick)   #trick
        self.root1.setText(croot1)   #root1
        self.root2.setText(croot2)   #root2

        #find the combo index to be set for gramm
        index = self.gramm.findText(cgramm, Qt.MatchFlag.MatchFixedString)
        if index >= 0:
            self.gramm.setCurrentIndex(index)

        self.remks.setText(cremks) #remks

    def savenote_button_clicked(self):
        idetls = str(self.detls.toPlainText())
        thisCurrPyKey =  self.intCurrPyKey
        cn.execute("UPDATE natdictionary_detls SET detls = ? WHERE pykey = ?", (idetls, thisCurrPyKey))
        conn.commit()
        self.msgl.setText("Update seems succesful...Switch back and forth to verify")

    def reset_filters_to_all(self):

        talls = "All"

        #find the combo index to be set for langu_f
        index = self.langu_f.findText(talls, Qt.MatchFlag.MatchFixedString)
        if index >= 0:
            self.langu_f.setCurrentIndex(index)

        #find the combo index to be set for typee
        index = self.typee_f.findText(talls, Qt.MatchFlag.MatchFixedString)
        if index >= 0:
            self.typee_f.setCurrentIndex(index)

        #find the combo index to be set for lettr
        index = self.lettr_f.findText(talls, Qt.MatchFlag.MatchFixedString)
        if index >= 0:
            self.lettr_f.setCurrentIndex(index)

        #find the combo index to be set for cllas
        index = self.cllas_f.findText(talls, Qt.MatchFlag.MatchFixedString)
        if index >= 0:
            self.cllas_f.setCurrentIndex(index)

        self.tablePopul()