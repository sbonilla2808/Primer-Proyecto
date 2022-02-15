                ANWERS


 1- What are 4 data types present in python?

 'int'
 'bool'
 'str'
 'float'

 2- What function is used to know the data type of a variable?
 
 'type'() 


 3-What is the difference between '/' and '//'?

 use a '/' is for division to return decimal numbers

 using two '//' in a division serves so that the answer of the division is in whole numbers

 4- What does the function 'pow'(a, b) do?

    It is for calculating the 'power' rise of a number. 
    '(a)' is the 'base' of the number that will rise to power
    '(b)' is the 'exponent'

 5- What does the function 'round(a, b)' do?

 rounds to the given number of digits and returns the floating point number, if no number of digits to round is given, rounds the number to the nearest integer.

 6- What does the function 'bin(a, b)' do?

 Return the binary representation of an integer

 7- What does the function 'hex(a, b)' do?

  Returns the 'hexadecimal' representation of an integer

 8- What does it mean that a variable is 'immutable'?

   means that if the value can change, the object is called mutable, while if the value cannot change, the object is called 'immutable'

 9- If 'a=[0,1,2,3,4]' and 'a[0]=0', what's the value of 'a[-1]'?

    the value is '(4)'

 10- What does the operator 'in' do?

    'in' returns 'True' if the specified value is found in the sequence. Otherwise it returns 'False'.

 11- What is operator precedence?

    Python operators have a set precedence order, which determines which operators are  evaluated first in a potentially ambiguous expression.
 
 12- How is different an "expression" from a 'statement'? 1.What is an augmented operator? write a code block with an example.
 
 An 'expression' evaluates to a value. An 'expression' is something that can be reduced to a value. A statement is an instruction that the Python interpreter can execute.   When you write a "statement" on the command line, Python executes it and displays the result, if any. The result of a print statement is a value.

  What is an augmented operator?
  Augmented assignment operators combine the impact of an arithmetic operator with an assignment operator.
  EXAMPLE: 
         a = 5 
         b = 10
         c = 15

         a += b 
         print(a)                  Answer: '15'


  13- What is 'string' 'concatenation'? write a code block with an example.

   Concatenation can be defined as the integration of two strings into one object. 

   EXAMPLE:
          x = 'El monto de mi cuenta de banco es de '
          y = '100000'
          print(x + str (y))

 14- What is escape sequence and why is it used?

    Escape sequences let us embed characters in strings that can't even be easily typed from a keyboard. The character '\' and one or more characters following it          are changed to a single character in the final string.
                            

 15- What's a formatted strin? write a code block with an example.

   String formatting is also known as string interpolation. It is the process of inserting a custom string or variable into a predefined text

   'f-strings' are constructed like a normal Python 'string', but preceded by an f or F. This makes it possible to interpolate code by enclosing it in curly braces     
   ( {} ) within the string. Resulting in a text string
                                                      Example:
                                                             #Formated Strings
                                                             name = 'Placido'
                                                             lastname = 'Bonilla'
                                                             age = '21'
                                                             print(f"Hello {name} {lastname}. You are {age} years old and do you like spearfishing\n")


 16- Given the string 'sinorita', how would you extract all vowels from it using only string indexes?

     selfish = 'sinorita'
     #selfish= '01234567'
     print(selfish[1:8:2])                              Answer: 'ioia'

  17- What's a 'builtin function'? write a code block with two of them and explain what are they doing.
   
      Words like 'file()', 'print()', 'round()', 'open()', 'range()', 'input()', may be familiar to you, i.e. functions provided by the language itself that can be       executed by referencing 'calling' them. Example:

    'Input': The 'input'() function is a data entry function that allows users to enter data of various types from standard input (typically corresponding to keyboard                input).

    'Round': The 'round'() function rounds a float number to a given precision in decimal digits (default 0 digits). This always returns a float number. The precision may             be negative.

   Example 1:         name = input('What is your name?\n')
                      input("Hello. How are you %s. \n" % name)

              'INPUT': 'receive' and save your name to use when referring to you.

   Example 2:        r = 7.2; r = r+ 7.2
                     print(round(r))

              'ROUND': is 'rounding' my operation of '7.2 + 7.2' to give as a result: '14'

  18- What are 'thruthy' and 'falsey' values? Why are they important?

      They are 'values'
      
      Returns 'True' when the argument 'x' is 'true', 'False' otherwise.
      These values ​​are especially important for conditional expressions and loops, they are values ​​that can represent binary logical values.
      It is normally used in programming, statistics, electronics, mathematics (Boolean algebra), etc.

  19- Why is it important 'type conversion'?
 
      Is important because it allows us to convert an object from one "data type" to another 'data type'. Implicit type conversion is done automatically by the Python       interpreter. Python avoids data loss in implicit 'type conversion'.

  20- How are different 'dictionaries' from 'lists'?

      'List' is a collection of index value pairs like array in c++. The list indices are integers starting a '0'.

      The 'dictionary' is a hash structure of key and value pairs. Dictionary keys can be of any data type.

  21- How are different "tuples" from "lists"?

      'Lists' have a number of additional functions that allow extensive handling of the values ​​they contain. Based on this definition, it can be said that lists are       dynamic, while tuples are static.
      The content of the lists can be modified during the execution of the program while for the 'tuples' it is not possible to alter their content.

  22- How are different 'sets' from 'lists'?

      A 'set' is an unordered collection data type that is iterable, mutable, and has no duplicate elements. Python's set class represents the mathematical notion of a       'set'.

      'Lists' are like dynamically sized arrays, declared in other languages ​​(vector in C++ and ArrayList in Java). Lists don't have to always be homogeneous, which       makes it the most powerful tool in Python.














