## Usama Bin Naeem
#### Backend Level 1 Evaluation
<hr/>
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


