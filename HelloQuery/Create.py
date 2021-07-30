import pymysql
import speech_recognition as sr
from VoiceRecognisation import VoiceRecognisation
from DBConnection import DBConnection


class Create:
    def createQuery(self, queryList, cursorInstance):
        sqlQuery = " SHOW TABLES "
        cursorInstance.execute(sqlQuery)
        tableList = cursorInstance.fetchall()
        for Table in tableList:
            print(Table)

        print(queryList)
        count = 0
        flag = 0
        for word in queryList:
            count = count + 1
            if word == 'Table' or word == 'table':
                flag = 1
                break

        fields = []
        if flag == 1:
            try:
                Table=queryList[count]
            except:
                Table= VoiceRecognisation.speech("VoiceRecognisation", "Enter Table Name:-")

        else:
            Table = VoiceRecognisation.speech("VoiceRecognisation", "Enter Table Name:-")
        number = VoiceRecognisation.speech("VoiceRecognisation", "how many fields you want to add:-")
        intcount= int(number)
        #intcount=2

        while (intcount > 0):
            field = VoiceRecognisation.speech("VoiceRecognisation", "Enter Your Field")
            fields.append(field)
            intcount=intcount-1

        print(fields)
        str_join = " varchar(50) ,".join(fields)
        FinalString= str_join + ' varchar(50) '

        sqlQuery = "create table "+ Table + " ( " + FinalString + ")"
        result=cursorInstance.execute(sqlQuery)

        if result:
            print("Table Created Succesfully.")
        else:
            print("Table Did not Created")


        sqlStatement = "Desc " + Table
        print(sqlStatement)
        cursorInstance.execute(sqlStatement)
        Data = cursorInstance.fetchall()
        for data in Data:
            print(data)

        Condition = VoiceRecognisation.speech("VoiceRecognisation", "Want to enter Primary Key:-")
        if Condition == 'Yes' or Condition == 'yes':
            print(fields)
            field = VoiceRecognisation.speech("VoiceRecognisation", "Enter field Name")

            sqlQuery = "Alter  table " + Table + " add primary key (" + field +")"

            cursorInstance.execute(sqlQuery)
