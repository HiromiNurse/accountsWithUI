# Form implementation generated from reading ui file 'banking.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(560, 450)
        Dialog.setMinimumSize(QtCore.QSize(560, 450))
        Dialog.setMaximumSize(QtCore.QSize(560, 450))
        self.button_Account = QtWidgets.QPushButton(parent=Dialog)
        self.button_Account.setGeometry(QtCore.QRect(380, 190, 91, 41))
        self.button_Account.setObjectName("button_Account")
        self.button_SavingAccount = QtWidgets.QPushButton(parent=Dialog)
        self.button_SavingAccount.setGeometry(QtCore.QRect(280, 190, 91, 41))
        self.button_SavingAccount.setObjectName("button_SavingAccount")
        self.label_AccountInformation = QtWidgets.QLabel(parent=Dialog)
        self.label_AccountInformation.setGeometry(QtCore.QRect(290, 250, 250, 190))
        self.label_AccountInformation.setMaximumSize(QtCore.QSize(290, 250))
        self.label_AccountInformation.setObjectName("label_AccountInformation")
        self.button_Withdraw = QtWidgets.QPushButton(parent=Dialog)
        self.button_Withdraw.setGeometry(QtCore.QRect(0, 250, 81, 31))
        self.button_Withdraw.setObjectName("button_Withdraw")
        self.entry_Withdraw = QtWidgets.QLineEdit(parent=Dialog)
        self.entry_Withdraw.setGeometry(QtCore.QRect(90, 250, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.entry_Withdraw.setFont(font)
        self.entry_Withdraw.setObjectName("entry_Withdraw")
        self.button_Deposite = QtWidgets.QPushButton(parent=Dialog)
        self.button_Deposite.setGeometry(QtCore.QRect(0, 290, 81, 31))
        self.button_Deposite.setObjectName("button_Deposite")
        self.entry_Deposit = QtWidgets.QLineEdit(parent=Dialog)
        self.entry_Deposit.setGeometry(QtCore.QRect(90, 290, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.entry_Deposit.setFont(font)
        self.entry_Deposit.setObjectName("entry_Deposit")
        self.button_SetBalance = QtWidgets.QPushButton(parent=Dialog)
        self.button_SetBalance.setGeometry(QtCore.QRect(0, 330, 81, 31))
        self.button_SetBalance.setObjectName("button_SetBalance")
        self.entry_SetBalance = QtWidgets.QLineEdit(parent=Dialog)
        self.entry_SetBalance.setGeometry(QtCore.QRect(90, 330, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.entry_SetBalance.setFont(font)
        self.entry_SetBalance.setObjectName("entry_SetBalance")
        self.button_SetName = QtWidgets.QPushButton(parent=Dialog)
        self.button_SetName.setGeometry(QtCore.QRect(0, 370, 81, 31))
        self.button_SetName.setObjectName("button_SetName")
        self.entry_SetName = QtWidgets.QLineEdit(parent=Dialog)
        self.entry_SetName.setGeometry(QtCore.QRect(90, 370, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.entry_SetName.setFont(font)
        self.entry_SetName.setObjectName("entry_SetName")
        self.button_Confirm = QtWidgets.QPushButton(parent=Dialog)
        self.button_Confirm.setGeometry(QtCore.QRect(0, 410, 81, 31))
        self.button_Confirm.setObjectName("button_Confirm")
        self.entry_Login_First = QtWidgets.QLineEdit(parent=Dialog)
        self.entry_Login_First.setGeometry(QtCore.QRect(90, 10, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.entry_Login_First.setFont(font)
        self.entry_Login_First.setText("")
        self.entry_Login_First.setObjectName("entry_Login_First")
        self.entry_Login_Last = QtWidgets.QLineEdit(parent=Dialog)
        self.entry_Login_Last.setGeometry(QtCore.QRect(90, 60, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.entry_Login_Last.setFont(font)
        self.entry_Login_Last.setText("")
        self.entry_Login_Last.setObjectName("entry_Login_Last")
        self.entry_Login_Pin = QtWidgets.QLineEdit(parent=Dialog)
        self.entry_Login_Pin.setGeometry(QtCore.QRect(360, 10, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.entry_Login_Pin.setFont(font)
        self.entry_Login_Pin.setText("")
        self.entry_Login_Pin.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.entry_Login_Pin.setClearButtonEnabled(False)
        self.entry_Login_Pin.setObjectName("entry_Login_Pin")
        self.button_login = QtWidgets.QPushButton(parent=Dialog)
        self.button_login.setGeometry(QtCore.QRect(290, 60, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.button_login.setFont(font)
        self.button_login.setObjectName("button_login")
        self.label_create_new = QtWidgets.QLabel(parent=Dialog)
        self.label_create_new.setGeometry(QtCore.QRect(0, 120, 111, 16))
        self.label_create_new.setObjectName("label_create_new")
        self.label_enter_pin = QtWidgets.QLabel(parent=Dialog)
        self.label_enter_pin.setGeometry(QtCore.QRect(280, 10, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_enter_pin.setFont(font)
        self.label_enter_pin.setObjectName("label_enter_pin")
        self.label_last_name = QtWidgets.QLabel(parent=Dialog)
        self.label_last_name.setGeometry(QtCore.QRect(10, 60, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_last_name.setFont(font)
        self.label_last_name.setObjectName("label_last_name")
        self.label_first_name = QtWidgets.QLabel(parent=Dialog)
        self.label_first_name.setGeometry(QtCore.QRect(10, 10, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_first_name.setFont(font)
        self.label_first_name.setObjectName("label_first_name")
        self.label_first_name_2 = QtWidgets.QLabel(parent=Dialog)
        self.label_first_name_2.setGeometry(QtCore.QRect(10, 140, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_first_name_2.setFont(font)
        self.label_first_name_2.setObjectName("label_first_name_2")
        self.entry_register_Last = QtWidgets.QLineEdit(parent=Dialog)
        self.entry_register_Last.setGeometry(QtCore.QRect(90, 190, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.entry_register_Last.setFont(font)
        self.entry_register_Last.setText("")
        self.entry_register_Last.setObjectName("entry_register_Last")
        self.entry_register_First = QtWidgets.QLineEdit(parent=Dialog)
        self.entry_register_First.setGeometry(QtCore.QRect(90, 140, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.entry_register_First.setFont(font)
        self.entry_register_First.setText("")
        self.entry_register_First.setObjectName("entry_register_First")
        self.entry_register_Pin = QtWidgets.QLineEdit(parent=Dialog)
        self.entry_register_Pin.setGeometry(QtCore.QRect(360, 140, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.entry_register_Pin.setFont(font)
        self.entry_register_Pin.setText("")
        self.entry_register_Pin.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.entry_register_Pin.setClearButtonEnabled(False)
        self.entry_register_Pin.setObjectName("entry_register_Pin")
        self.label_last_name_2 = QtWidgets.QLabel(parent=Dialog)
        self.label_last_name_2.setGeometry(QtCore.QRect(10, 190, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_last_name_2.setFont(font)
        self.label_last_name_2.setObjectName("label_last_name_2")
        self.label_enter_pin_2 = QtWidgets.QLabel(parent=Dialog)
        self.label_enter_pin_2.setGeometry(QtCore.QRect(280, 140, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_enter_pin_2.setFont(font)
        self.label_enter_pin_2.setObjectName("label_enter_pin_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.button_Account.setText(_translate("Dialog", "Account"))
        self.button_SavingAccount.setText(_translate("Dialog", "Saving Account"))
        self.label_AccountInformation.setText(_translate("Dialog", "Account Information"))
        self.button_Withdraw.setText(_translate("Dialog", "Withdraw"))
        self.entry_Withdraw.setText(_translate("Dialog", "Withdraw Amount"))
        self.button_Deposite.setText(_translate("Dialog", "Deposite"))
        self.entry_Deposit.setText(_translate("Dialog", "Deposite Amount"))
        self.button_SetBalance.setText(_translate("Dialog", "Set Balance"))
        self.entry_SetBalance.setText(_translate("Dialog", "Balance Amount"))
        self.button_SetName.setText(_translate("Dialog", "Set Name"))
        self.entry_SetName.setText(_translate("Dialog", "New Name"))
        self.button_Confirm.setText(_translate("Dialog", "Confirm"))
        self.button_login.setText(_translate("Dialog", "Login"))
        self.label_create_new.setText(_translate("Dialog", "Create New Account"))
        self.label_enter_pin.setText(_translate("Dialog", "Enter Pin"))
        self.label_last_name.setText(_translate("Dialog", "Last Name"))
        self.label_first_name.setText(_translate("Dialog", "First Name"))
        self.label_first_name_2.setText(_translate("Dialog", "First Name"))
        self.label_last_name_2.setText(_translate("Dialog", "Last Name"))
        self.label_enter_pin_2.setText(_translate("Dialog", "Enter Pin"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())
