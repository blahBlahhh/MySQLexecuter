import pymysql


class Functions(object):

    def connectDB(self, password, db_name=None):
        try:
            connection = pymysql.connect('localhost', 'root', password, db_name)
            cursor = connection.cursor()
            return connection, cursor
        except Exception:
            print('connect failed')

    def showDatabase(self, password):
        connection, cursor = self.connectDB(password, 'information_schema')
        cursor.execute('SHOW DATABASES')
        data = cursor.fetchall()
        connection.close()
        return data

    def showTable(self, db_name, password):
        connection, cursor = self.connectDB(password, db_name)
        cursor.execute('SHOW TABLES')
        data = cursor.fetchall()
        connection.close()
        return data

    def showColumn(self, db_name, tb_name, password):
        connection, cursor = self.connectDB(password, db_name)
        sql = 'SHOW COLUMNS FROM %s' % tb_name
        cursor.execute(sql)
        rough_data = cursor.fetchall()
        connection.close()
        data = []
        for rd in rough_data:
            data.append(rd[0])
        return data

    def insertData(self, db_name, tb_name, password):
        connection, cursor = self.connectDB(password, db_name)
        column = self.showColumn(db_name, tb_name, password)
        input_data = []
        for c in column:
            input_data.append(input(c + '?'))
        input_data = str(tuple(input_data))
        sql = 'INSERT INTO %s VALUES %s' % (tb_name, input_data)
        try:
            cursor.execute(sql)
            connection.close()
            return 'Insertion succeeded!'
        except Exception:
            connection.close()
            return 'Insertion failed!'

    def deleteData(self, db_name, tb_name, password):
        connection, cursor = self.connectDB(password, db_name)
        data = self.viewDetail(db_name, tb_name, password)
        print(self.showColumn(db_name, tb_name, password))
        for d in range(0, len(data)):
            print('%d. %s' % (d+1, data[d]))
        row = input('Which row do you want to delete?\n')
        sql = 'DELETE FROM %s WHERE id = %s' % (tb_name, row)
        try:
            cursor.execute(sql)
            connection.close()
            return 'Deletion succeeded!'
        except Exception:
            connection.close()
            return 'Deletion failed!'

    def viewDetail(self, db_name, tb_name, password):
        detail = input('Any details?\n')
        if detail == '':
            detail = '*'
        connection, cursor = self.connectDB(password, db_name)
        sql = 'SELECT %s FROM %s ' % (detail, tb_name)
        cursor.execute(sql)
        data = cursor.fetchall()
        connection.close()
        return data
