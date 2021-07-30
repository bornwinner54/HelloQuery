
from VoiceRecognisation import VoiceRecognisation


class Truncate:
    def truncateQuery(self,queryList,cursorInstance):
        flag = 0
        print(queryList)
        UserTable = " Karan"
        sqlQuery = " SHOW TABLES "
        cursorInstance.execute(sqlQuery)
        tableList = cursorInstance.fetchall()
        for word in queryList:
            for table in tableList:
                for t in table:
                    if word == t:
                        UserTable = t
        print(UserTable)

        print("Really want to Truncate Table.\n1.Yes\n2.No")
        Condition = VoiceRecognisation.speech("VoiceRecognisation","Answer:-")
        if Condition == 'Yes' or Condition == 'yes':
            sqlQuery = "truncate table " + UserTable
            cursorInstance.execute(sqlQuery)

        sqlQuery = " select * from  "+UserTable
        cursorInstance.execute(sqlQuery)
        tableList = cursorInstance.fetchall()
        print(tableList)