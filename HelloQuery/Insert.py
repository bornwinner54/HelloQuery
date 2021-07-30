from VoiceRecognisation import VoiceRecognisation


class Insert:
    def insertQuery(self,querylist,cursorInstance):
        UserTable="Karan"
        sqlQuery = " SHOW TABLES "
        cursorInstance.execute(sqlQuery)
        tableList = cursorInstance.fetchall()
        for word in querylist:
            for table in tableList:
                for t in table:
                    if word == t:
                        UserTable = t

        print(UserTable)
     
        sqlQuery = "desc " + UserTable
        cursorInstance.execute(sqlQuery)
        FieldList = cursorInstance.fetchall()
        fields = []
        for data in FieldList:
            fields.append(data[0])
        print(fields)

        intcount=len(fields)
        count=0
        values=[]
        while (intcount > 0):
            field = VoiceRecognisation.speech("VoiceRecognisation", "Value for "+ fields[count] + ":-")
            values.append(field)
            intcount=intcount-1
            count=count+1

        #values=['1','mahesh','mahesh','rushikesh']

        print(values)
        str_join = " ' , ' ".join(values)
        FinalString= str_join + ' '


        sqlQuery = "insert into " + UserTable + " values ( '" + FinalString + "' )"
        cursorInstance.execute(sqlQuery)
        sqlStatement = "select *   from " + UserTable
        cursorInstance.execute(sqlStatement)
        Data = cursorInstance.fetchall()
        for data in Data:
            print(data)