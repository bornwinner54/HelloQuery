
class Select:
    def selectQuery(self,queryList,cursorInstance):
        UserTable="Karan "
        sqlQuery=" SHOW TABLES "
        cursorInstance.execute(sqlQuery)
        tableList=cursorInstance.fetchall()
        for word in queryList:
            for table in tableList:
                for t in table:
                    if word == t:
                        UserTable = t

        sqlStatement = "select * from "+UserTable
        cursorInstance.execute(sqlStatement)
        Data=cursorInstance.fetchall()
        for data in Data:
            print(data)