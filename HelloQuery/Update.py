
class Update:
    def updateQuery(self,querylist,cursorInstance):
        print(querylist)

        sqlQuery = " SHOW TABLES "
        cursorInstance.execute(sqlQuery)
        tableList = cursorInstance.fetchall()
        '''for word in querylist:
            for table in tableList:
                for t in table:
                    if word == t:
                        UserTable = t'''
        UserTable = 'Karan'
        print(UserTable)

        sqlQuery = "desc "+UserTable
        cursorInstance.execute(sqlQuery)
        FieldList = cursorInstance.fetchall()
        fields = []
        for data in FieldList:
            fields.append(data[0])
        print(fields)
        Userfield=[]
        for word in querylist:
            for field in fields:
                if word == field:
                    Userfield.append(field)
        print(Userfield)

        count=0
        for word in querylist:
            count = count + 1
            if word == "Where":
                print(word)
                break
        print(count)
        #sqlStatement = "update " + UserTable + " set " + Userfield[0] +"= 'akya' "+ " where " + Userfield[-1] +"= 1"
        sqlStatement = "update " + UserTable + " set " + Userfield[0] + " = " +"'" +querylist[count-2]+"'" + " where " + Userfield[
            -1] + " = " + querylist[-1]
        print(sqlStatement)
        cursorInstance.execute(sqlStatement)
        sqlStatement = "select * from "+UserTable +" where "+ Userfield[-1] + "  = " + querylist[-1]
        cursorInstance.execute(sqlStatement)
        Data = cursorInstance.fetchall()
        print(Data)
