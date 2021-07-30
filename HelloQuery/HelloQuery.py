import os
import webbrowser

import pyttsx3

from Create import Create
from DBConnection import DBConnection
from Delete import Delete
from Drop import Drop
from EnterIntoDatabase import EnterIntoDatabase
from Insert import Insert
from Select import Select
from Truncate import Truncate
from Update import Update
from VoiceRecognisation import VoiceRecognisation
x=1
if x==1:

    engine = pyttsx3.init()
    rate = engine.getProperty('rate')
    engine.setProperty(rate, 50)



    AdminName = VoiceRecognisation.speech("VoiceRecognisation", "Please Enter Your Name")
    # AdminName='Rushikesh'
    if AdminName == 'Prasanna' or AdminName == 'Karan' or AdminName == 'Rushikesh':
        engine.say("Admin Verified")
        print("Admin Verified")
        engine.say("...Welcome MySql Database...")
        engine.runAndWait()
        allQueries = ["Select", "Insert", "Update", "Delete", "Drop", "Truncate", "Create", "select", "insert",
                      "update",
                      "delete", "drop", "truncate", "create"]

        try:

            Instance = DBConnection.connection("DBConnection")
            Database = EnterIntoDatabase.enterDatabase("EnterIntoDatabase")
            connectionInstance = DBConnection.connectionWithDatabase("DBConnection", Database)
            cursorInstance = connectionInstance.cursor()
            Repetation = 1
            while Repetation:
                userQuery = VoiceRecognisation.speech("VoiceRecognisation", "Enter Your Query")
                # userQuery = "Delete From Table school where Id = 2"
                userQuery = userQuery.title()
                queryList = userQuery.split()
                condition = ""
                for word in queryList:
                    for query in allQueries:
                        if query == word:
                            condition = query

                if condition == "Select" or condition == "select":
                    Select.selectQuery("Select", queryList, cursorInstance)
                elif condition == "Update" or condition == "update":
                    Update.updateQuery("Update", queryList, cursorInstance)
                elif condition == "Insert" or condition == "insert":
                    Insert.insertQuery("Insert", queryList, cursorInstance)
                elif condition == "Delete" or condition == "delete":
                    Delete.deleteQuery("Delete", queryList, cursorInstance)
                elif condition == "Drop" or condition == "drop":
                    Drop.dropQuery("Drop", queryList, cursorInstance, Instance)
                elif condition == "Truncate" or condition == "truncate":
                    Truncate.truncateQuery("Truncate", queryList, cursorInstance)
                elif condition == "Create" or condition == "create":
                    Create.createQuery("Create", queryList, cursorInstance)

                if userQuery == 'Quit' or userQuery == 'quit' or userQuery == 'Stop' or userQuery == 'stop' or userQuery == 'Exit' or userQuery == 'exit' or userQuery == 'Bass':
                        Repetation = 0



        except Exception as e:

            print("Exeception occured:{}".format(e))

        finally:
            engine.say("Thank You")
            print("Thank You")
            connectionInstance.commit()
            cursorInstance.close()
            Instance.close()

    else:

        #engine.say("pehli fursat mein nikal")
        engine.say("Access Denied.")
        print("Access Denied")
        engine.runAndWait()
else:
    print("Error In opening UI.")
