## Usama Bin Nadeem
#### Backend Level 1 Evaluation
<hr/>
<br/>

## Functions

<br/>

> Fibonacci (Q1)

``` python
def fibonacci(num_of_terms=1):
    output = []
    for idx in range(num_of_terms):
        if idx == 0 or idx == 1:
            output.append(1)
        else:
            output.append(output[idx - 1] + output[idx - 2])
    return output
```

<br/>

> What is the difference between a parameter and an argument? (Q2)


A parameter is like a variable that is defined on the function whereas an argument is the actual value that is passed to a function.

``` python
 #bar is the parameter
 def foo(bar):
     print(bar)

 # Hello World is the argument passed to the function foo
 foo('Hello World') 
```

<br/>

> All functions in Python by default return? (Q3)


All functions by default return **None**

<br/>

> What are keyword arguments and when should we use them? (Q4)


Keyword arguments are used when we want to pass an arbitrary number of arguments to a function. They are mostly used when we want to pass named arguments.

<br/>

> How can we make a parameter of a function optional? (Q5)


``` python
def optional_param_sum(foo=10, bar=20):
    return foo + bar

# this function could be called without arguments and would return 30
optional_param_sum()
# returns 30 by default

# or one could pass one of these parameters
optional_param_sum(30)
# returns 50 (here foo=30 and bar=20)
```

<br />

> What happens when we prefix a parameter with an asterisk (*)? (Q6)


Prefixing a parameter with an asterisk means that this function might be called with a list as an argument. Using * means we are unpacking (extracting) all the values inside that function


<br/>

> What about two asterisks (**)? (Q7)

Two asterisks are used to unpack the arguments that are passed in the form of a dictionary unlike as a list

<br/>

> Write a function that prints all the prime numbers between 0 and limit where the limit is a parameter. (Q8)

<br/>

## Control Flow

<br/>

> What is the difference between ```10 / 3``` and ```10 // 3```?

10/3 would do a normal division and return 3.333... whereas 10//3 would do a **floor** division returning 3. Floor division truncates the decimals and returns the value to the left of decimal

<br/>

> What is the result of ```10 ** 3```?

**1000** (x ** y ==> x^y so 10^3 == 1000)

<br/>

> Given ```(x = 1)```, what will be the value of x after we run ```(x += 2)```?

x would be equal to **3**

<br/>

> How can we round a number?

Using Python's builtin function ```round()```. Accepts optional second parameter for number of decimal places to round to.

<br/>

> What is the result of ```float(1)```?

**1.0**

<br/>

> What is the result of ```bool(“False”)```?

**True**

<br/>

> What are the falsy values in Python?

- ```[]``` (empty lists)
- ```{}``` (empty dictionaries)
- ```set()``` (empty sets)
- ```""``` (empty strings)
- ```0, 0.0``` (zeroes)
- ```None``` (null values)
- ```False``` (false boolean value)

<br/>

> What is the result of ```10 == “10”```?

**False**

<br/>

> What is the result of ```“bag” > “apple”```?

**True**

<br/>

> What is the result of ```not(True or False)```?

**False**

<br/>

> Under what circumstances does the expression 18 <= age < 65 evaluate to True?

If age is greater than equal to 18 or strictly lesser than 65

<br/>

> What does ```range(1, 10, 2)``` return?

```[1,3,5,7,9]```

<br/>


> Name 3 iterable objects in Python.

- Lists
- Strings
- Tuples
- Dictionaries

<br/>