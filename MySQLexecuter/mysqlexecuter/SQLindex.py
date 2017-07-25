import msvcrt

import MySQLexecuter.mysqlexecuter.functions


class Index(object):

    def __init__(self):
        self.func = MySQLexecuter.mysqlexecuter.functions.Functions()

    def filt(self, data):
        if str(type(data)) == "<class 'list'>":
            for d in data:
                print(d)
        elif str(type(data)) == "<class 'tuple'>":
            data = list(data)
            for d in data:
                d = str(d).replace("(", '').replace("'", '').replace(')', '').replace(',', '')
                print(d)

    def inputPWD(self):
        chars = []
        while True:
            try:
                next_char = msvcrt.getch().decode(encoding='utf-8')
            except:
                print('Input failed')
            if next_char in '\n\r':
                break
            elif next_char == '\b':
                if len(chars) > 0:
                    del chars[-1]
                    msvcrt.putch('\b'.encode(encoding='utf-8'))
                    msvcrt.putch(' '.encode(encoding='utf-8'))
                    msvcrt.putch('\b'.encode(encoding='utf-8'))
            else:
                chars.append(next_char)
                msvcrt.putch('*'.encode(encoding='utf-8'))
        return ''.join(chars)

    def do_sql(self, password, db_name=None, tb_name=None):
        ask = '''
            **__Thanks for using python's mysql-executor__**
            Enter the number to tell me what is your order.
            1. SHOW DATABASE
            2. SHOW TABLE
            3. SHOW COLUMN
            4. INSERT DATA
            5. DELETE DATA
            6. VIEW DATA 
            7. CHANGE DATABASE AND TABLE * still working on, not available\n'''
        switcher = {
            1: self.func.showDatabase,
            2: self.func.showTable,
            3: self.func.showColumn,
            4: self.func.insertData,
            5: self.func.deleteData,
            6: self.func.viewDetail,
        }

        self.func.connectDB(password, db_name)
        input_data = int(input(ask))
        if input_data in range(1, 3):
            self.filt(switcher.get(input_data)())
        elif input_data in range(3, 7):
            self.filt(switcher.get(input_data)(tb_name))
        else:
            print('Wrong number! Please enter a valid number.')

        self.func.disconnectDB()


if __name__ == '__main__':
    bot = Index()
    print("Please input your password:")
    password = bot.inputPWD()
    print('\nPassword confirmed')
    db_name = input("What is the database's name?\n")
    tb_name = input("What is the table's name? (press enter if you don't want to fill this)\n")
    while True:
        bot.do_sql(password, db_name, tb_name)
        a = input('Press Enter to continue, input "exit" to exit\n')
        if a == "exit":
            print('Bye~')
            break
