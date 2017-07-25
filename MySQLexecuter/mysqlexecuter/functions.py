import pymysql


class Functions(object):

    def connectDB(self, password, db_name=None):
        try:
            global connection, cursor
            connection = pymysql.connect('localhost', 'root', password, db_name)
            cursor = connection.cursor()
            return connection, cursor
        except Exception:
            print('connect failed')

    def disconnectDB(self):
        connection.close()

    def showDatabase(self):
        cursor.execute('SHOW DATABASES')
        data = cursor.fetchall()
        return data

    def showTable(self):
        cursor.execute('SHOW TABLES')
        data = cursor.fetchall()
        return data

    def showColumn(self, tb_name):
        sql = 'SHOW COLUMNS FROM %s' % tb_name
        cursor.execute(sql)
        rough_data = cursor.fetchall()
        data = []
        for rd in rough_data:
            data.append(rd[0])
        return data

    def insertData(self, tb_name):
        column = self.showColumn(tb_name)
        input_data = []
        for c in column:
            input_data.append(input(c + '?'))
        input_data = str(tuple(input_data))
        sql = 'INSERT INTO %s VALUES %s' % (tb_name, input_data)
        try:
            cursor.execute(sql)
            return 'Insertion succeeded!'
        except Exception:
            return 'Insertion failed!'

    def deleteData(self, tb_name):
        data = self.viewDetail(tb_name)
        print(self.showColumn(tb_name))
        for d in range(0, len(data)):
            print('%d. %s' % (d+1, data[d]))
        row = input('Which row do you want to delete?\n')
        sql = 'DELETE FROM %s WHERE id = %s' % (tb_name, row)
        try:
            cursor.execute(sql)
            return 'Deletion succeeded!'
        except Exception:
            return 'Deletion failed!'

    def viewDetail(self, tb_name):
        detail = input('Any details?\n')
        if detail == '':
            detail = '*'
        sql = 'SELECT %s FROM %s ' % (detail, tb_name)
        cursor.execute(sql)
        data = cursor.fetchall()
        return data
