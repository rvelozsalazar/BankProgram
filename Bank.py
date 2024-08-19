# **********************************************************************************************************
# Author:           Richard Veloz Salazar
# Lab:              Lab 4
# Date:             08/10/2023
# Description:      This program is a simple banking system that allows users to interact with their accounts.
#                   Users can open accounts, withdraw money, deposit money, and view their account balances.
#                   The program provides a user-friendly interface for managing banking transactions.
# Input:            The program prompts the user for various inputs, including:
#                   - Menu options (1 to 4) for different actions.
#                   - Name when opening an account.
#                   - Initial account balance when opening an account.
#                   - Account number for withdrawals and deposits.
#                   - Amounts for withdrawals and deposits.
# Output:           The program provides the following outputs:
#                   - Display of menu options to the user.
#                   - Prompts, messages, and status updates for various actions.
#                   - Display of account information, including account numbers and balances.
#                   - Notifications for successful and unsuccessful transactions.
# Sources:          Lab 4 specifications.
# ***********************************************************************************************************


# !/usr/bin/env python3
import random
import valid as v
from message import exit_message


def main():
    print("Welcome to my Banking System Program")
    name_list = []
    account_list = []
    account_bal_list = []

    option = 0
    while option != 4:
        # Displaying menu options.
        banking_menu = ["1. Open Account", "2. Withdraw Money", "3. Deposit Money", "4. Quit"]
        for option in banking_menu:
            print(option)
        user_input = False

        # validation for user input
        while not user_input:
            try:
                option = v.get_integer("Please enter an option: ")
                if 0 < option < 5:
                    user_input = True
                else:
                    print("\nPlease enter a number between 1 and 4.\n")
                    for option in banking_menu:
                        print(option)
            except ValueError:
                print("\nError --- Please enter a number between 1 to 4 only\n")
                for option in banking_menu:
                    print(option)

        # Option 1: Open Account
        if option == 1:
            open_account(name_list, account_list, account_bal_list)

        # Option 2: Withdraw Money
        elif option == 2:
            cash_out(name_list, account_list, account_bal_list)

        # Option 3: Deposit Money
        elif option == 3:
            add_money(name_list, account_list, account_bal_list)

        # Option 4: Quit
        elif option == 4:
            exit_message()
            break


def open_account(name_list, account_list, account_bal_list):
    name = v.get_string("Please enter your name: ")
    print("Your name: ", name)
    name_list.append(name)
    account_number = random.randint(1000, 9999)
    print("Your account number: ", account_number)
    account_balance = v.get_real(f"Please enter initial account balance for account number {account_number}: ")
    account_list.append(account_number)
    account_bal_list.append(account_balance)
    print(f"Account successfully opened for {name} "
          f"with account number {account_number} and initial balance of", "$", format(account_balance, ".2f"))

    return name_list, account_list, account_bal_list


def cash_out(name_list, account_list, account_bal_list):
    account_number = int(input("Enter your account number: "))
    if account_number in account_list:
        index = account_list.index(account_number)
        withdrawal_amount = float(input("Enter withdrawal amount: "))
        if withdrawal_amount <= account_bal_list[index]:
            account_bal_list[index] -= withdrawal_amount
            print("Withdrawal successful."
                  "An amount of ", "$", format(withdrawal_amount, ".2f"), " is removed from your account ",
                  account_number, sep="")
            print("")
            print("Your current balance is ", "$", format(account_bal_list[index], ".2f"), sep="")
            print("")
        else:
            print("Unfortunately you don't have sufficient funds in your account.", name_list[index])
            print("Your balance after your current transaction is ", "$",
                  format(account_bal_list[index], ".2f"), sep="")
            print("")
    else:
        print("\n Sorry that account number does not exist \n")
    return name_list, account_list, account_bal_list


def add_money(name_list, account_list, account_bal_list):
    account_number = int(input("\nEnter your account number: "))
    if account_number in account_list:
        index = account_list.index(account_number)
        deposit_amount = float(input("Enter the amount you want to deposit: "))
        if deposit_amount > 0:
            account_bal_list[index] += deposit_amount
            print("Deposit successful."
                  "An amount of ", "$", format(deposit_amount, ".2f"), " is added to your account ",
                  account_number, sep="")
            print("Your current balance is ", "$", format(account_bal_list[index], ".2f"), sep="")
        else:
            print("ERROR --- Please enter a positive number", name_list[index])
            print("Your balance after your current transaction is ", "$",
                  format(account_bal_list[index], ".2f"), sep="")
            print("")
    else:
        print("\n Sorry that account number does not exist \n")
    return name_list, account_list, account_bal_list


if __name__ == "__main__":
    main()
