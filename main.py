from enum import Enum
numbers = {}

class Commands(Enum):
    EXIT = 0
    VAR = 1
    ADD = 2
    SUB = 3
    MUL = 4
    DIV = 5
    PRINT = 6
    ALL = 7
    IF = 8
    THEN = 9
    OTHERWISE = 10

class Operators(Enum):
    M = '>'     #More
    L = '<'     #Less
    E = '=='    #Equal
    ME = '>='   #More or Equal
    LE = '<='   #Less or Equal
    NE = '!='   #Not Equal

def cmd_add(parts):
    if len(parts) < 3:
        print("Not enough variables")
        return False
    if parts[1] not in numbers:
        print(f"Variable {parts[1]} not found")
        return False

    result = int(numbers[parts[1]])
    for var in parts[2:]:
        if var in numbers:
            result += int(numbers[var])
        else:
            print(f"Variable {var} not found")
            return True
    else:
        print(result)

def cmd_sub(parts):
    if len(parts) < 3:
        print("Not enough variables")
        return False
    if parts[1] not in numbers:
        print(f"Variable {parts[1]} not found")
        return False

    result = int(numbers[parts[1]])
    for var in parts[2:]:
        if var in numbers:
            result -= int(numbers[var])
        else:
            print(f"Variable {var} not found")
            return True
    else:
        print(result)

def cmd_mul(parts):
    if len(parts) < 3:
        print("Not enough variables")
        return False
    if parts[1] not in numbers:
        print(f"Variable {parts[1]} not found")
        return False

    result = int(numbers[parts[1]])
    for var in parts[2:]:
        if var in numbers:
            result *= int(numbers[var])
        else:
            print(f"Variable {var} not found")
            return True
    else:
        print(result)

def cmd_div(parts):
    if len(parts) < 3:
        print("Not enough variables")
        return False
    if parts[1] not in numbers:
        print(f"Variable {parts[1]} not found")
        return False

    result = int(numbers[parts[1]])
    for var in parts[2:]:
        if var in numbers:
            value = int(numbers[var])
            if value == 0:
                print("You can't divide by zero")
                return True
            result /= value
        else:
            print(f"Variable {var} not found")
            return True
    else:
        print(result)

def cmd_print(parts):
    if len(parts) < 2:
        print("Not enough variables")
        return False

    if parts[1] == Commands.ALL.name:
        for name, value in numbers.items():
            print(f"{name} = {value}")
        return False
            
    for varname in parts[1:]:
        if varname in numbers:
            print(f"{varname} = {numbers[varname]}")
        else:
            print(f"{varname} not found")
            return True

#IF-THEN STATEMENT LOGIC
def cmd_if_otherwise(parts):
    if len(parts) < 5 or parts[4] != Commands.THEN.name:
        print("Syntax error in IF statement")
        return False
    
    then_index = parts.index(Commands.THEN.name)
    otherwise_index = parts.index(Commands.OTHERWISE.name) if Commands.OTHERWISE.name in parts else None

    var1 = parts[1]
    op = parts[2]
    var2 = parts[3]

    if var1 not in numbers or var2 not in numbers:
        print("Variable not found in IF statement")
        return True

    val1 = int(numbers[var1])
    val2 = int(numbers[var2])

    ops = {
        Operators.M.value: lambda a, b: a > b,
        Operators.L.value: lambda a, b: a < b,
        Operators.E.value: lambda a, b: a == b,
        Operators.ME.value: lambda a, b: a >= b,
        Operators.LE.value: lambda a, b: a <= b,
        Operators.NE.value: lambda a, b: a != b
    }

    if op not in ops:
        print("Invalid operator for IF statement")
        return False

    condition_true = ops[op](val1, val2)

    if otherwise_index is not None:
        then_command = parts[then_index + 1 : otherwise_index]
        otherwise_command = parts[otherwise_index + 1:]
    else:
        then_command = parts[then_index + 1:]
        otherwise_command = None

    if condition_true:
        handle_command(then_command)
    elif otherwise_command:
        handle_command(otherwise_command)
    
def handle_command(parts):
    if parts[0] == Commands.VAR.name:
        numbers.update({parts[1] : parts[2]})

    elif parts[0] == Commands.ADD.name:
        cmd_add(parts)

    elif parts[0] == Commands.SUB.name:
        cmd_sub(parts)

    elif parts[0] == Commands.MUL.name:
        cmd_mul(parts)

    elif parts[0] == Commands.DIV.name:
        cmd_div(parts)

    elif parts[0] == Commands.PRINT.name:
        cmd_print(parts)

    elif parts[0] == Commands.EXIT.name:
        print("GOODBYE")
        return True
    else:
        print("No such command")
        return False

def run():
    while True:
        line = input(">>> ")
        parts = line.split()

        if parts[0] == Commands.IF.name:
            cmd_if_otherwise(parts)
        else:
            if handle_command(parts):
                break

run()
