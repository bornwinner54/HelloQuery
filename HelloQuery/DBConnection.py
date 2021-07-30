import pymysql

class DBConnection:


    def connection(self):
        databaseServerIP = "localhost"

        databaseUserName = "root"

        databaseUserPassword = ""

        cusrorType = pymysql.cursors.DictCursor

        connectionInstance = pymysql.connect(host=databaseServerIP, user=databaseUserName,
                                             password=databaseUserPassword,

                                             cursorclass=cusrorType)
        cursorInstance = connectionInstance.cursor()
        return cursorInstance



    def connectionWithDatabase(self,DatabaseName):

        cusrorType = pymysql.cursors.DictCursor
        dbName=DatabaseName
        connectionInstance=pymysql.connect("localhost", "root", "", DatabaseName)
        return connectionInstance

