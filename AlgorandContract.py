from pyteal import *

program = App.globalPut(Bytes("mykey"). Int(50))
program = App.globalGet(Bytes)
print (compileTeal(program, Mode.Application))                                                                                                                           