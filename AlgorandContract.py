from pyteal import *

program = App.globalPut(Bytes("mykey"). Int(50))
program
print (compileTeal(program, Mode.Application))