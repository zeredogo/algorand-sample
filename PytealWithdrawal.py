from pyteal import *

#create a withdrawal transaction

def Bank_Account(receiver):
    is_payment = Txn.type_enum() ==TxnType.payment
    is_singletransaction = Global.group_size() == int(1)
    is_receiver = Txn.receiver() == Addr(receiver)
    no_closeout_address =