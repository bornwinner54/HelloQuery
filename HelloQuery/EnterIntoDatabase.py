from VoiceRecognisation import VoiceRecognisation
from DBConnection import DBConnection
import pyttsx3
engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty(rate, 175)

class EnterIntoDatabase:
    UserDatabase=""
    def enterDatabase(self):
        Instance=DBConnection.connection("DBConnection")
        sqlQuery = "SHOW DATABASES"

        Instance.execute(sqlQuery)

        databaseList = Instance.fetchall()
        for databases in databaseList:
            print(databases)

        Database=VoiceRecognisation.speech("VoiceRecognisation","Enter Your Database  Name")
        #Database='Yash'
        flag=0
        for db in databaseList:
            if db['Database'] == Database:
                print("Database exist")
                flag=1

        if flag == 0:
            #Condition=VoiceRecognisation.speech("VoiceRecognisation","Want To Create database.")
            Condition='yes'
            if Condition == 'Yes' or Condition == 'yes':
                sqlStatement = "CREATE DATABASE " + Database
                Instance.execute(sqlStatement)
            flag=1

        if flag == 1:
            engine.say("Enter Into Database Succefully...")
            print("Enter Into Database Succefully...")
        return Database