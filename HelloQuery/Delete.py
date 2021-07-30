class Delete:
    def deleteQuery(self, queryList, cursorInstance):
        UserTable = "Karan "
        sqlQuery = " SHOW TABLES "
        cursorInstance.execute(sqlQuery)
        tableList = cursorInstance.fetchall()
        for word in queryList:
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

        Userfield = []
        for word in queryList:
            for field in fields:
                if word == field:
                    Userfield.append(field)
        print(Userfield)
        flag = 0
        if Userfield:
            for word in queryList:
                if word == Userfield[0]:
                    flag = 1

        if flag == 1:
            sqlStatement = "delete  from " + UserTable + " where " + Userfield[-1] + " = " + queryList[-1]
            if cursorInstance.execute(sqlStatement):
                print("Data Deleted Sucessfully.")
            sqlStatement = "select *   from " + UserTable
            cursorInstance.execute(sqlStatement)
            Data = cursorInstance.fetchall()
            for data in Data:
                print(data)

        if flag == 0:
            sqlStatement = "delete  from " + UserTable
            if cursorInstance.execute(sqlStatement):
                print("Data Deleted Sucessfully.")
            sqlStatement = "select *   from " + UserTable
            cursorInstance.execute(sqlStatement)
            Data = cursorInstance.fetchall()
            for data in Data:
                print(data)
