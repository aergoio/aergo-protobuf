#!/usr/bin/python3
"""
This takes the output of `git diff -w -U0` on stdin,
iterates through the lines to build a table of changes,
and outputs it according to our defined format.
"""

import sys
assert sys.version_info >= (3, 7), 'Requires at least Python version 3.7'

import fileinput
import re
from dataclasses import field as _field, dataclass
from typing import Dict, Union

@dataclass
class Field:
    name: str
    typ: str
    number: int
    addOrRemove: str

    def __str__(self):
        if self.typ:
            return '%s (type: %s, fieldNo: %d)' % (self.name, self.typ, self.number)
        return '%s (%d)' % (self.name, self.number)

@dataclass
class RpcField:
    name: str
    input: str
    output: str
    new: bool
    addOrRemove: str

    def __str__(self):
        return '%s (arg: %s, ret: %s)' % (self.name, self.input, self.output)

@dataclass
class Symbol:
    name: str
    typ: str
    addOrRemove: str
    fields: Dict[str, Union[Field, RpcField]] = _field(default_factory=dict)

    def __str__(self):
        return '%s' % (self.name)

@dataclass
class ProtoFile:
    name: str
    symbols: Dict[str, Symbol] = _field(default_factory=dict)

table: Dict[str, ProtoFile] = dict()
currentFile = None
currentSymbol = None

skipNewSymbolFields = True  # show a new symbol's fields or not


# Iterate diff and create intermediate representation
for line in fileinput.input():
    filename = re.match(r'^\+\+\+ b/proto/(.*?)$', line)
    if filename:
        currentFile = filename.groups()[0]
        if not currentFile in table:
            table[currentFile] = ProtoFile(name=currentFile)
        #print("FILE = %s" % currentFile)

    if not currentFile:
        continue

    changedSymbol = re.match(r'^@@ .*? @@ ([^\s]*?) ([^\s]*?) {', line)
    if changedSymbol:
        (symbolType, currentSymbol) = changedSymbol.groups()
        if not currentSymbol in table[currentFile].symbols:
            table[currentFile].symbols[currentSymbol] = Symbol(name=currentSymbol, typ=symbolType, addOrRemove='')
        #print("SYMBOL = %s" % currentSymbol)

    newSymbol = re.match(r'^([+-])([^\s]*?) ([^\s]*?) {', line)
    if newSymbol:
        (addRemove, symbolType, currentSymbol) = newSymbol.groups()
        if not currentSymbol in table[currentFile].symbols:
            table[currentFile].symbols[currentSymbol] = Symbol(name=currentSymbol, typ=symbolType, addOrRemove=addRemove)
        #print("SYMBOL = %s" % currentSymbol)

    if not currentSymbol:
        continue
    
    rpcMethod = re.match(r'^([+-])\s*rpc ([^\s]*?)\s*\((.*?)\) returns \((.*?)\) {', line)
    if rpcMethod:
        (addRemove, fieldName, rpcInput, rpcOutput) = rpcMethod.groups()
        table[currentFile].symbols[currentSymbol].fields[addRemove + fieldName] = RpcField(name=fieldName, input=rpcInput, output=rpcOutput, new=False, addOrRemove=addRemove)
        #print("FIELD = %s" % fieldName)

    fieldMatch = re.match(r'^([+-])\s*(.*?)\s*([^\s]*?)\s*\=\s*(\d+);', line)
    if fieldMatch:
        (addRemove, fieldType, fieldName, fieldNumber) = fieldMatch.groups()
        table[currentFile].symbols[currentSymbol].fields[addRemove + fieldName] = Field(name=fieldName, typ=fieldType, number=int(fieldNumber), addOrRemove=addRemove)
        #print("FIELD = %s" % fieldName)

    #print(line)

def isUnchanged(table, symbol, field):
    # Check if identical entry exists with opposite change direction
    # If so, nothing about this field (except comments, whitespace) has changed
    reverseAddRemove = '+' if field.addOrRemove == '-' else '-'
    otherField = table[fileName].symbols[symbol.name].fields.get(reverseAddRemove + field.name, None)
    return otherField and str(otherField) == str(field)

# Iterate intermediate representation and output format
for fileName, protofile in table.items():
    printedLines = 0
    for symbol in protofile.symbols.values():
        if symbol.addOrRemove != '':
            print("%s %s::%s" % (symbol.addOrRemove, fileName, symbol))
            printedLines += 1
            if symbol.addOrRemove == '-' or skipNewSymbolFields:
                continue
        for field in symbol.fields.values():
            if isUnchanged(table, symbol, field):
                continue
            print("%s %s::%s::%s" % (field.addOrRemove, fileName, symbol.name, field))
            printedLines += 1
    if printedLines > 0:
        print()