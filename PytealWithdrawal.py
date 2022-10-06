from pyteal import *

#create a withdrawal transaction

def Bank_Account(receiver):
    is_payment = Txn.type_enum() ==TxnType.payment
    is_singletransaction = Global.group_size() == int(1)
    is_receiver = Txn.receiver() == Addr(receiver)
    no_closeout_address = Txn.close_remainder_to() == Global.zero_address()
    no_rekeying = Txn.close_remainder_to() == Global.zero_address()
    acceptable_fee = Txn.fee() <= Int(1000)
    return And(
        is_payment,
        is_singletransaction,
        is_receiver,
        no_closeout_address,
        no_rekeying,
        acceptable_fee
    )

    if __name__ == "__main__":
        program = Bank_Account("then you write the address you generated here")
        print(compileteal(program, main.Application))