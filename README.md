# SimpleLang

SimpleLang is extremely simple python-based language. Further I'll cover every command and operator

## Commands

1. **EXIT** - used when user wants to terminate the program
    >>> `EXIT`
2. **VAR** - used when user wants to declare a new variable
    >>> `VAR X 5`
3. **ADD** - used when user wants to add two or more numbers
    >>> `ADD X Y`
4. **SUB** - used when user wants to subtract two or more numbers
    >>> `SUB X Y`
5. **MUL** - used when user wants to multiply two or more numbers
    >>> `MUL X Y`
6. **DIV** - used when user wants to divide two or more numbers
    >>> `DIV X Y`
7. **PRINT** - used when user wants to print out one or more numbers
    >>> `PRINT X`
7.1. **ALL** - used when user wants to print out all variables, inlcluding names and values
    >>> `PRINT ALL`
8. **IF** - never used alone

8.1 **THEN** - used in IF-THEN statement
    >>> `IF X < Y THEN ADD X Y`

8.2 **OTHERWISE** - used in IF-THEN-OTHERWISE statement
    >>> `IF X < Y THEN ADD X Y OTHERWISE SUB X Y`

## Operators

1. `>` - More
2. `<` - Less
3. `==` - Equal
4. `>=` - More or Equal
5. `<=` - Less or Equal
6. `!=` - Not Equal
