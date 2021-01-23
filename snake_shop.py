# imports
import time
from PyQt5 import uic, QtCore, QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

# create default
hello = """
    |        |   |---------   |            |            |_________|
    |        |   |            |            |            |         |
    |        |   |            |            |            |         |
    |--------|   |---------   |            |            |         |
    |        |   |            |            |            |         |
    |        |   |            |            |            |         |
    |        |   |---------   |_________   |_________   |_________|
"""

description = """
This program is designed to buy skins. 
Your balance is formed from the points received. 
That is, the number of points you have received for all the time is summed up and divided by 10. 
(number of points / 10). 
For the received balance, you can buy skins. 
In the menu, you can check your balance and buy skins if you have enough balance.
"""

buy_text = """
1. Cyber snake (default skin (you have this skin)).
2. Rainbow skin. Price: 2 units.
3. The classic skin. Price: 4 units.
4. Skin of the USSR. Price: 10 units.
"""

info_about_file_in_skin = """
1. Cyber snake.
2. Rainbow skin.
3. The classic skin.
4. Skin of the USSR.
"""


# parse info about skins
def parse():
    # read
    f_read_skin = open('D:\\pythonProject\\main\\skins\\my_skin.txt')
    info_in_file_my_skin = f_read_skin.read()
    info_in_file_my_skin_split = info_in_file_my_skin.splitlines()

    # print
    print(info_about_file_in_skin)
    print('')
    print(f'Your purchased skins: {info_in_file_my_skin_split[0]}')
    print(f'Your non purchased skins: {info_in_file_my_skin_split[1]}')


# processing the balance
def processing_balance(price):
    # read
    f_total_point = open('D:\\pythonProject\\main\\mm\\total_point.txt')
    info_in_file_total_point = (f_total_point.read())

    # processing
    balance_for_buy = float(info_in_file_total_point) - float(price)
    print(f'You bought this skin, now your balance: {balance_for_buy}')
    time.sleep(5)
    path_total_balance = 'D:\\pythonProject\\main\\mm\\total_point.txt'

    # write
    f_total_balance = open(path_total_balance, 'w')
    f_total_balance.write(str(balance_for_buy))


# opening the skin
def open_skin(name_of_file, number_of_skin):
    # opening the skin
    print(name_of_file)

    # read and write info
    path_for_opening_skin = f'D:\\pythonProject\\main\\skins\\oll skins\\{name_of_file}.txt'
    print(path_for_opening_skin)
    file_for_opening_skin = open(path_for_opening_skin, 'w')
    file_for_opening_skin.write(str(number_of_skin))


# main window
class MainWindow(QMainWindow):
    # init
    def __init__(self):
        # init
        super().__init__()

        # load ui
        uic.loadUi('D:\\pythonProject\\main\\snake_shop.ui', self)

        # Title
        self.setWindowTitle('Snake Shop')

        # buttons
        self.menu_pas.clicked.connect(self.show_old_menu)
        self.descrip_.clicked.connect(self.show_description)
        self.balance_.clicked.connect(self.show_balance)
        self.check_my_skins.clicked.connect(self.show_my_skins)
        self.buy_.clicked.connect(self.show_buying_process)

    # show old menu
    def show_old_menu(self):
        # show menu
        print(hello)
        time.sleep(0.5)

        print('MENU')
        time.sleep(0.5)

        print('1. Description')
        time.sleep(0.5)

        print('2. Check balance')
        time.sleep(0.5)

        print('3. View my skins')
        time.sleep(0.5)

        print('4. Buy\n')
        time.sleep(0.5)

        # input
        input_number = input('Enter the number: ')

        # check
        # Description
        if input_number == '1':
            # print
            print(description)
            time.sleep(120)

        # Check balance
        elif input_number == '2':
            # read
            f_total_point = open('D:\\pythonProject\\main\\mm\\total_point.txt')
            info_in_file_total_point_ = (f_total_point.read())
            print(f'Your balance: {info_in_file_total_point_}')
            time.sleep(120)

        # View my skins
        elif input_number == '3':
            # start parse
            parse()

        # Buy skins
        elif input_number == '4':
            # read
            f_total_point = open('D:\\pythonProject\\main\\mm\\total_point.txt')
            info_in_file_total_point_ = (f_total_point.read())
            print(buy_text)

            # ###
            number_skin = input('Enter the number of the skin you want to buy: ')

            # if
            # cyber_snake
            if number_skin == '1':
                print('You have this skin')
                time.sleep(120)

            # rainbow
            elif number_skin == '2':
                if 2 <= float(info_in_file_total_point_):
                    # processing the balance
                    processing_balance(2.0)

                    # start func
                    open_skin('rage', 1)

                else:
                    print('Error')
                    time.sleep(120)

            # classic skin
            elif number_skin == '3':
                if 4 <= float(info_in_file_total_point_):
                    # processing the balance
                    processing_balance(4.0)

                    # start func
                    open_skin('classic', 1)
                else:
                    print('Error')
                    time.sleep(120)

            # USSR skin
            elif number_skin == '4':
                if 10 <= float(info_in_file_total_point_):
                    # processing the balance
                    processing_balance(10.0)

                    # start func
                    open_skin('ussr', 1)
                else:
                    print('Error')
                    time.sleep(120)

    # show description
    def show_description(self):
        self.ex_1 = Desc()
        self.ex_1.show()

    # show balance
    def show_balance(self):
        self.ex_2 = CheckBalance()
        self.ex_2.show()

    # show my skins
    def show_my_skins(self):
        self.ex_3 = CheckMySkins()
        self.ex_3.show()

    # show buying process
    def show_buying_process(self):
        self.ex_4 = BuySkins()
        self.ex_4.show()


# description
class Desc(MainWindow):
    # init
    def __init__(self):
        # init
        super().__init__()

        # load ui
        uic.loadUi('D:\\pythonProject\\main\\desc.ui', self)

        # Title
        self.setWindowTitle('Description')


# check balance
class CheckBalance(MainWindow):
    # init
    def __init__(self):
        # init
        super().__init__()

        # load ui
        uic.loadUi('D:\\pythonProject\\main\\balance.ui', self)

        # Title
        self.setWindowTitle('My balance')

        # buttons
        self.descrip_.clicked.connect(self.show_balance_)

    # show balace
    def show_balance_(self):
        f_total_point_ = open('D:\\pythonProject\\main\\mm\\total_point.txt')
        info_in_file_total_point__ = (f_total_point_.read())
        self.pprint_text.append(f'Your balance: {info_in_file_total_point__}')


# check skins which we have
class CheckMySkins(MainWindow):
    # init
    def __init__(self):
        # init
        super().__init__()

        # load ui
        uic.loadUi('D:\\pythonProject\\main\\view_my_skin.ui', self)

        # Title
        self.setWindowTitle('My skins')

        # buttons
        self.descrip_.clicked.connect(self.show_my_skins_)

    # show skins
    def show_my_skins_(self):
        # print
        self.pprint_text.append(info_about_file_in_skin)

        # read
        f_read_skin = open('D:\\pythonProject\\main\\skins\\my_skin.txt')
        info_in_file_my_skin_ = f_read_skin.read()
        info_in_file_my_skin_split_ = info_in_file_my_skin_.splitlines()

        # print
        self.pprint_text.append(f'Your purchased skins: {info_in_file_my_skin_split_[0]}')
        self.pprint_text.append(f'Your non purchased skins: {info_in_file_my_skin_split_[1]}')


# check skins which we have
class BuySkins(MainWindow):
    # init
    def __init__(self):
        # init
        super().__init__()

        # load ui
        uic.loadUi('D:\\pythonProject\\main\\buy_skins.ui', self)

        # Title
        self.setWindowTitle('Buy skins')

        # buttons
        self.buy_button.clicked.connect(self.buy_skins_new_menu)

        # print
        self.pprint_text.append(info_about_file_in_skin)

    # buy
    def buy_skins_new_menu(self):
        # get number
        number_skin = self.input_number_of_skin.text()

        # ###
        print(number_skin)

        # read
        f_total_point_ = open('D:\\pythonProject\\main\\mm\\total_point.txt')
        info_in_file_total_point_ = (f_total_point_.read())

        # if
        # cyber_snake
        if number_skin == '1':
            self.pprint_text.append('You have this skin =)')

        # rainbow
        elif number_skin == '2':
            if 2 <= float(info_in_file_total_point_):
                # processing the balance
                balance_for_buy_ = float(info_in_file_total_point_) - float(2)
                self.pprint_text.append(f'You bought skin: 2. Rainbow skin.')
                self.pprint_text.append(f'Now your balance: {balance_for_buy_}')
                time.sleep(5)
                path_total_balance = 'D:\\pythonProject\\main\\mm\\total_point.txt'

                # write
                f_total_balance = open(path_total_balance, 'w')
                f_total_balance.write(str(balance_for_buy_))

                # opening the skin
                name_of_file_ = 'rage'
                number_of_skin_ = 1
                self.pprint_text.append(name_of_file_)

                # read and write info
                path_for_opening_skin_ = f'D:\\pythonProject\\main\\skins\\oll skins\\{name_of_file_}.txt'
                self.pprint_text.append(path_for_opening_skin_)
                file_for_opening_skin_ = open(path_for_opening_skin_, 'w')
                file_for_opening_skin_.write(str(number_of_skin_))

            else:
                self.pprint_text.append('Error')
                time.sleep(120)

        # classic skin
        elif number_skin == '3':
            if 4 <= float(info_in_file_total_point_):
                # processing the balance
                balance_for_buy_ = float(info_in_file_total_point_) - float(4)
                self.pprint_text.append(f'You bought skin: 3. The classic skin.')
                self.pprint_text.append(f'Now your balance: {balance_for_buy_}')
                time.sleep(5)
                path_total_balance = 'D:\\pythonProject\\main\\mm\\total_point.txt'

                # write
                f_total_balance = open(path_total_balance, 'w')
                f_total_balance.write(str(balance_for_buy_))

                # opening the skin
                name_of_file_ = 'classic'
                number_of_skin_ = 1
                self.pprint_text.append(name_of_file_)

                # read and write info
                path_for_opening_skin_ = f'D:\\pythonProject\\main\\skins\\oll skins\\{name_of_file_}.txt'
                self.pprint_text.append(path_for_opening_skin_)
                file_for_opening_skin_ = open(path_for_opening_skin_, 'w')
                file_for_opening_skin_.write(str(number_of_skin_))

            else:
                self.pprint_text.append('Error')
                time.sleep(120)

        # USSR skin
        elif number_skin == '4':
            if 10 <= float(info_in_file_total_point_):
                # processing the balance
                balance_for_buy_ = float(info_in_file_total_point_) - float(10)
                self.pprint_text.append(f'You bought skin: 4. Skin of the USSR.')
                self.pprint_text.append(f'Now your balance: {balance_for_buy_}')
                time.sleep(5)
                path_total_balance = 'D:\\pythonProject\\main\\mm\\total_point.txt'

                # write
                f_total_balance = open(path_total_balance, 'w')
                f_total_balance.write(str(balance_for_buy_))

                # opening the skin
                name_of_file_ = 'ussr'
                number_of_skin_ = 1
                self.pprint_text.append(name_of_file_)

                # read and write info
                path_for_opening_skin_ = f'D:\\pythonProject\\main\\skins\\oll skins\\{name_of_file_}.txt'
                self.pprint_text.append(path_for_opening_skin_)
                file_for_opening_skin_ = open(path_for_opening_skin_, 'w')
                file_for_opening_skin_.write(str(number_of_skin_))

            else:
                self.pprint_text.append('Error')
                time.sleep(120)


# except
def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


# start app
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())
