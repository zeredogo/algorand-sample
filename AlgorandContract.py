from pyteal import *

program = App.globalPut(Bytes("mykey"). Int(50))
print (compileTeal(program, Mode.Application))