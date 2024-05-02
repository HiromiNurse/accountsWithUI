from PyQt6.QtWidgets import *
from gui import *
from accounts import *
import csv

"""
Make it so the bottom section is hidden until someone is logged in as a user.
Or registered.
"""

class Logic(QMainWindow, Ui_Dialog):
    current_user = Account('holder')

    def __init__(self) -> None:
        """
        Function Create an instance window and connect buttons to functions
        """
        super().__init__()
        self.setupUi(self)

        self.button_Confirm.hide()

        self.accounts = {}
        self.read_from_file()

        self.button_login.clicked.connect(lambda: self.login())

        self.button_Account.clicked.connect(lambda: self.create_account())
        self.button_SavingAccount.clicked.connect(lambda: self.create_saving())

        self.button_Deposite.clicked.connect(lambda: self.deposit_button())
        self.button_Withdraw.clicked.connect(lambda: self.withdraw_button())

        self.button_SetName.clicked.connect(lambda: self.set_name_button())
        self.button_Confirm.clicked.connect(lambda: self.confirm_button())
        self.button_SetBalance.clicked.connect(lambda: self.set_balance_button())

    def login(self):
        first_name = self.entry_Login_First.text().lower().strip()
        last_name = self.entry_Login_Last.text().lower().strip()
        name = f"{first_name} {last_name}"
        try:
            pin_number = int(self.entry_Login_Pin.text())
        except ValueError:
            self.label_AccountInformation.setText("Pin Number must be a number")
        else:
            if name in self.accounts.keys():
                if pin_number == self.accounts[name][3]:
                    self.change_account(name)
                else:
                    self.label_AccountInformation.setText("Invalid Login. Try Again.")
            else:
                self.label_AccountInformation.setText("Invalid Login. Try Again.")

                self.entry_Login_Pin.clear()
                self.entry_Login_Last.clear()
                self.entry_Login_First.clear()

    def create_account(self) -> None:
        """
        Function On create account button click, creates an account with $0 and the
        name entered into the entry at the top right
        """
        name = f"{self.entry_register_First.text().strip().lower()} {self.entry_register_Last.text().strip().lower()}"
        try:
            pin_number = int(self.entry_register_Pin.text().strip())
        except ValueError:
            self.label_AccountInformation.setText("Pin Number must be a number")
        else:
            self.accounts[name] = [0, 'checking', 0, pin_number]
            self.change_account(name)

            self.entry_register_Pin.clear()
            self.entry_register_Last.clear()
            self.entry_register_First.clear()

    def create_saving(self) -> None:
        """
        Function On create saving account button click, creates a saving account with $100 and the
        name entered into the entry at the top right
        """
        name = f"{self.entry_register_First.text().strip().lower()} {self.entry_register_Last.text().strip().lower()}"
        try:
            pin_number = int(self.entry_register_Pin.text().strip())
        except ValueError:
            self.label_AccountInformation.setText("Pin Number must be a number")
        else:
            self.accounts[name] = [100, 'saving', 0, pin_number]
            self.change_account(name)

            self.entry_register_Pin.clear()
            self.entry_register_Last.clear()
            self.entry_register_First.clear()

    def deposit_button(self) -> None:
        """
        Function Adds the value in the entry next to the deposit button to the current selected
        account's balance. Also applies interest to saving accounts every 5 deposits
        """
        amount = self.entry_Deposit.text()
        try:
            amount = float(amount)
        except ValueError:
            self.entry_Deposit.setText("Enter a number")
        except TypeError:
            self.entry_Deposit.setText("Enter a number")
        else:
            try:
                if Logic.current_user.get_name() != "holder":
                    Logic.current_user.deposit(amount)
                    if Logic.current_user.atype == "saving":
                        self.accounts[Logic.current_user.get_name()][2] += 1
                    self.update_accounts()
                else:
                    self.entry_Deposit.setText("Select an account")
            except ChildProcessError:
                self.entry_Deposit.setText("Invalid amount")

    def withdraw_button(self) -> None:
        """
        Function Subtracts the value in the entry next to the withdraw button from the current
        selected account's balance
        """
        amount = self.entry_Withdraw.text()
        try:
            amount = float(amount)
        except ValueError:
            self.entry_Withdraw.setText("Enter a number")
        except TypeError:
            self.entry_Withdraw.setText("Enter a number")
        else:
            try:
                if Logic.current_user.get_name() != "holder":
                    Logic.current_user.withdraw(amount)
                    self.update_accounts()
                else:
                    self.entry_Withdraw.setText("Select an account")
            except ChildProcessError:
                self.entry_Withdraw.setText("Invalid amount")

    def set_balance_button(self) -> None:
        """
        Function Set's the selected account's balance to the value entered into the
        entry next to the set balance button
        """
        amount = self.entry_SetBalance.text()
        try:
            amount = float(amount)
        except ValueError:
            self.entry_SetBalance.setText(f"Enter number above {Logic.current_user.MINIMUM}")
        except TypeError:
            self.entry_SetBalance.setText(f"Enter number above {Logic.current_user.MINIMUM}")
        else:
            try:
                if Logic.current_user.get_name() != 'holder':
                    Logic.current_user.set_balance(amount)
                    self.update_accounts()
                else:
                    self.entry_SetBalance.setText("Select an account")
            except ChildProcessError:
                self.entry_SetBalance.setText(f"Invalid amount")

    def set_name_button(self) -> None:
        """
        Function Shows the confirmation button for changing account name
        """
        self.button_Confirm.show()

    def confirm_button(self) -> None:
        """
        Function Changes the selected account's name to the string entered into the entry
        next to the set name button
        """
        self.button_Confirm.hide()
        old_name = Logic.current_user.get_name()
        new_name = self.entry_SetName.text().lower().strip()
        self.accounts[new_name] = self.accounts.pop(old_name)
        Logic.current_user.set_name(new_name)
        self.update_text()

    def update_text(self) -> None:
        """
        Function Updates the text displayed in the top right label
        """
        name = Logic.current_user.get_name()
        balance = self.accounts[name][0]
        atype = self.accounts[name][1]
        if atype == 'checking':
            text = (f"Account Owner's Name: {name}\n"
                    f"Account Balance: {balance:.2f}\n"
                    f"Account Type: {atype}")
        else:
            deposit_count = self.accounts[name][2]
            text = (f"Account Owner's Name: {name}\n"
                    f"Account Balance: {balance:.2f}\n"
                    f"Account Type: {atype}\n"
                    f"Deposit Count: {deposit_count}\n"
                    f"Every 5 deposits, interest is applied\n"
                    f"Minimum Balance: {SavingAccount.MINIMUM}")
        self.label_AccountInformation.setText(text)

    def update_accounts(self) -> None:
        """
        Function Updates account information stored in the accounts dict
        """
        name = Logic.current_user.get_name()
        balance = Logic.current_user.get_balance()
        atype = Logic.current_user.atype
        pin_number = self.accounts[name][3]
        if atype == "saving":
            deposit_count = Logic.current_user.get_deposit_count()
            self.accounts[name] = [balance, atype, deposit_count, pin_number]
        else:
            self.accounts[name] = [balance, atype, 0, pin_number]
        self.update_text()

    def change_account(self, name) -> None:
        """
        Function Changes the current selected account
        :param name: name of the account being switched to
        """
        del Logic.current_user
        atype = self.accounts[name][1]
        if atype == 'checking':
            Logic.current_user = Account(name, self.accounts[name][0])
        else:
            Logic.current_user = SavingAccount(name, self.accounts[name][2])
            Logic.current_user.get_balance()
        self.update_text()

    def read_from_file(self) -> None:
        """
        Function Reads info from the accounts.csv file and stores it in the
        accounts dict
        """
        with open('accounts.csv', 'r') as input_file:
            for line in input_file:
                line = line.strip().split(',')
                name = line[0]
                balance = float(line[1])
                atype = line[2]
                deposit_count = int(line[3])
                pin_number = int(line[4])
                self.accounts[name] = [balance, atype, deposit_count, pin_number]

    def closeEvent(self, event) -> None:
        """
        Function Override the default close sequence to include saving the new accounts to the file
        """
        with open('accounts.csv', 'w', newline="") as output_file:
            content = csv.writer(output_file)
            for name, values in self.accounts.items():
                content.writerow([name, values[0], values[1], values[2], values[3]])
        event.accept()
