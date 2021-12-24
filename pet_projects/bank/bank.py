import pandas as pd
import argparse
from datetime import datetime as dt
import shlex
# from prettytable import from_csv # for the grid
# from io import StringIO # for the grid


class Bank():
    def __init__(self, client):
        self.client = client
        self.balance = 0.0

    def deposit(self, client, amount, description):
        global DF
        if amount <= 0:
            print("It's impossible")
            return None
        self.balance += amount
        DF = DF.append({
            'Date': dt.today().replace(microsecond=0),
            'Description': description,
            'Withdrawals': '',
            'Deposits': amount,
            'Balance': self.balance}, ignore_index=True)
        print('Deposit operation was successful!')

    def withdraw(self, client, amount, description):
        global DF
        if amount <= 0:
            print("It's impossible")
            return None
        if amount > self.balance:
            print('Your balance is ${:.2f}'.format(self.balance))
            return None
        self.balance -= amount
        DF = DF.append({
            'Date': dt.today().replace(microsecond=0),
            'Description': description,
            'Withdrawals': amount,
            'Deposits': '',
            'Balance': self.balance}, ignore_index=True)
        print('Withdrawal operation was successful!')

    def show_bank_statement(self, client, since, till):
        global DF
        if len(DF) < 1:
            print("You don't have any operations!")
            return None
        try:
            if (DF[DF['Date'] >= since].index[0]) == 0:
                prev_balance = 0
            else:
                prev_balance = list(DF[DF['Date'] < since]['Balance'])[-1]
        except BaseException:
            print('Incorrect datetime!')
            return None
        res = pd.DataFrame([['', 'Previous Balance', '', '', float(prev_balance)]],
            columns=[
            'Date',
            'Description',
            'Withdrawals',
            'Deposits',
            'Balance'])
        df = DF[(since <= DF['Date']) & (DF['Date'] <= till)]
        df = pd.concat([res, df])
        total_with, total_dep, last_balance = pd.to_numeric(df['Withdrawals'], errors='coerce').sum(
        ), pd.to_numeric(df['Deposits'], errors='coerce').sum(), list(df['Balance'])[-1]
        df = df.append({'Date': '',
                        'Description': 'Totals',
                        'Withdrawals': total_with,
                        'Deposits': total_dep,
                        'Balance': last_balance},
                       ignore_index=True)

        pd.set_option('display.max_colwidth', None)
        pd.set_option('display.float_format', '${:.2f}'.format)

        print(df.to_string(index=False))  # string version without grid
        # print(df.to_markdown()) # pandas version with grid and without $
        # print(from_csv(StringIO(df.to_csv(index=False)))) # csv with grid and without $


def make_parse():  # this is a string parsing for the arguments
    str_for_parse = input()
    parser.add_argument('method', type=str, help='method')
    parser.add_argument('--client', type=str, help='client')
    parser.add_argument('--amount', type=float, help='amount')
    parser.add_argument('--description', type=str, help='description')
    parser.add_argument('--since', type=str, help='since')
    parser.add_argument('--till', type=str, help='till')
    return str_for_parse


if __name__ == '__main__':
    print('Service started!')

    DF = pd.DataFrame(
        columns=[
            'Date',
            'Description',
            'Withdrawals',
            'Deposits',
            'Balance'])

    methods = ['deposit', 'withdraw', 'show_bank_statement']
    bank_client = None
    while True:
        parser = argparse.ArgumentParser()
        args = parser.parse_args(shlex.split(make_parse()))
        # arguments in the Namespace
        if bank_client is None:
            bank_client = Bank(args.client)
            client_name = args.client
        if  args.method not in methods:
            break
        if client_name != args.client:
            print('Your client name is incorrect!')
            continue
        if args.method == 'deposit':
            bank_client.deposit(args.client, args.amount, args.description)
        elif args.method == 'withdraw':
            bank_client.withdraw(args.client, args.amount, args.description)
        elif args.method == 'show_bank_statement':
            bank_client.show_bank_statement(
                args.client,
                dt.strptime(
                    args.since,
                    '%Y-%m-%d %H:%M:%S'),
                dt.strptime(
                    args.till,
                    '%Y-%m-%d %H:%M:%S'))
