from VoiceRecognisation import VoiceRecognisation


class Drop:
    def dropQuery(self,queryList,cursorInstance,Instance):

        flag=0
        print(queryList)
        for word in queryList:
            if word == 'table' or word == 'Table':
                flag=1

        if flag == 1:
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

            print("Really want to drop Table.\n1.Yes\n2.No")
            Condition = VoiceRecognisation.speech("VoiceRecognisation","answer:-")
            if Condition == 'Yes' or Condition == 'yes':

                sqlQuery = "drop table " + UserTable
                cursorInstance.execute(sqlQuery)

            sqlQuery = " SHOW TABLES "
            cursorInstance.execute(sqlQuery)
            tableList = cursorInstance.fetchall()
            for table in tableList:
                print(table)

        if flag == 0:
            UserDatabase = "Karan"
            sqlQuery = " SHOW databases "
            Instance.execute(sqlQuery)
            DatabaseList = Instance.fetchall()
            for word in queryList:
                for Database in DatabaseList:
                        if Database['Database'] == word:
                            UserDatabase=word
            print("Your Database")
            print(UserDatabase)
            print("Really want to drop database.\n1.Yes\n2.No")
            Condition = VoiceRecognisation.speech("VoiceRecognisation","answer:-")
            if Condition == 'Yes' or Condition == 'yes':

                sqlQuery = "drop database " + UserDatabase
                print(sqlQuery)
                cursorInstance.execute(sqlQuery)

            sqlQuery = " SHOW Databases "
            cursorInstance.execute(sqlQuery)
            DatabaseList = cursorInstance.fetchall()
            for DB in DatabaseList:
                print(DB)

