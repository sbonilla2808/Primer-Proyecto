ANWERS


1- What are 4 data types present in python?

   INT
   BOOL
   STR
   FLOAT

2- What function is used to know the data type of a variable?
 
   TYPE ()

3-What is the difference between / and //?

   use a / is for division to return decimal numbers

   using two // in a division serves so that the answer of the division is in    whole numbers

4- What does the function pow(a, b) do?

    It is for calculating the power rise of a number. 
    (a) is the base of the number that will rise to power
    (b) is the exponent

5- What does the function round(a, b) do?

rounds to the given number of digits and returns the floating point number, if no number of digits to round is given, rounds the number to the nearest integer.

6- What does the function bin(a, b) do?

   Return the binary representation of an integer

7- What does the function hex(a, b) do?

   Returns the hexadecimal representation of an integer

8- What does it mean that a variable is immutable?

   means that if the value can change, the object is called mutable, while if the value cannot change, the object is called immutable

9- If a=[0,1,2,3,4] and a[0]=0, what's the value of a[-1]?

    the value is (4)

10- What does the operator in do?

    in returns True if the specified value is found in the sequence. Otherwise it     returns False.


11- What is operator precedence?

    Python operators have a set precedence order, which determines which operators       are evaluated first in a potentially ambiguous expression.


12- How is different an expression from a statement? 1.What is an augmented operator? write a code block with an example.

    declarations are anything that can make up a line (or lines) of Python code.     Note that expressions are also statements.

    expressions contain only identifiers, literals, and operators, where operators     include arithmetic and boolean operators, the call operator function of () the     subscription operator [], and the like, and can be reduced to some kind of     "value", which can be any object


13- What is string concatenation? write a code block with an example.

    allow you to assign a value to a variable.  example:  r=5; r = r+10
                                                          print(r)                                                                       
                                                          answer: 15

14- What is escape sequence and why is it used?

      Concatenation can be defined as the integration of two strings into one       object.     example:  x = "El monto de mi cuenta de banco es de "
                                                                                                                 y = 100 000
                                                                                                                 print(x + str (y))     
                             
                                                                                                                answer: "El monto de mi cuenta de banco es de 100 000"     

15- What's a formatted strin`? write a code block with an example.

Escape sequences allow you to include special characters in strings. To do this, simply add a backslash (\) before the character you want to escape.

16- Given the string "sinorita", how would you extract all vowels from it using only string indexes?

f-strings are constructed like a normal Python string, but preceded by an f or F. This makes it possible to interpolate code by enclosing it in curly braces ( {} ) within the string. Resulting in a text string.    EXAMPLE:  
                                                            #Formated Strings
                                                             name = "Placido"
                                                             lastname = "Bonilla"
                                                             age = 21
                                                             print(f"Hello {name} {lastname}. You are {age} years old and do you like spearfishing\n")

                                                             
17- What's a builtin function? write a code block with two of them and explain what are they doing.

    1. Take a string from the user and store it in a variable.
    2. Initialize a count variable to 0.
    3. Use a for loop to loop through the characters in the string.
    4. Use an if statement to check if the character is a vowel or not and            increment the count variable if it is a vowel.
    5. Print the total number of vowels in the string.   

EXAMPLE: string=raw_input("Enter string:")
         vowels=0
         for i in string:
         if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
            vowels=vowels+1
         print("Number of vowels are:")
         print(vowels)


18- What are thruthy and falsey values? Why are they important?

Words like file(), print(), round(), open(), range(), input(), may be familiar to you, i.e. functions provided by the language itself that can be executed by referencing (calling) them. Example:

    Input: The input() function is a data entry function that allows users to enter data of various types from standard input (typically corresponding to keyboard     input).

    Round: The round() function rounds a float number to a given precision in decimal digits (default 0 digits). This always returns a float number. The precision may     be negative.

   Example 1:         name = input('What is your name?\n')
                      input("Hello. How are you %s. \n" % name)

              #INPUT: receive and save your name to use when referring to you.

   Example 2:        r = 7.2; r = r+ 7.2
                     print(round(r))

              #ROUND: is rounding my operation of 7.2 + 7.2 to give as a result: 14

19- Why is it important type conversion?

yes, they are values.
True is very important because it represents a truth and False because it represents a lie.

20- How are different dictionaries from lists?

List is a collection of index value pairs like array in c++. The list indices are integers starting at 0.

    The dictionary is a hash structure of key and value pairs. Dictionary keys can be of any data type.

21- How are different tuples from lists?

Lists have a number of additional functions that allow extensive handling of the values ​​they contain. Based on this definition, it can be said that lists are dynamic, while tuples are static.
the content of the lists can be modified during the execution of the program while for the tuples it is not possible to alter their content.

22- How are different sets from lists?

A set is an unordered collection of non-repeating values. Python sets are analogous to mathematical sets. The set type is mutable: once a set has been created, it can be modified.

A list in Python is a data structure made up of an ordered sequence of objects. Elements of a list can be accessed by their index, where 0 is the index of the first element. ... Via indexes, the elements of a list can be changed on the spot.







