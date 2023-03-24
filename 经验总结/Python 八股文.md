* Python

interpreted language is any programming language that executes its statements line by line.

Parent child:
```py
class Child(Parent):
    def __init__(self):
        super().__init__()
```
The super() method allows us to access the inherited methods that cascade to a class object.

`super().__init__()`

Immutable built-in datatypes of Python
Numbers Strings Tuples

Mutable built-in datatypes of Python
List Dictionaries Sets


* How does Python handle memory management?

Python uses private heaps to maintain its memory. So the heap holds all the Python objects and the data structures. This area is only accessible to the Python interpreter; programmers can’t use it.

And it’s the Python memory manager that handles the Private heap. It does the required allocation of the memory for Python objects.
Python employs a built-in garbage collector, which salvages all the unused memory and offloads it to the heap space.

* Def vs. lambda?
Def can hold multiple expressions while lambda is a uni-expression function.


* range([start], stop[, step])
Start: It is the starting no. of the sequence.
Stop: It specifies the upper limit of the sequence.
Step: It is the incrementing factor for generating the sequence.

*argList: list
**kwargs: dict


What does the __ Name __ do in Python?
The __name__ is a unique variable. Since Python doesn’t expose the main() function, so when its interpreter gets to run the script, it first executes the code which is at level 0 indentation.

To see whether the main() gets called, we can use the __name__ variable in an if clause compares with the value “__main__.”

Q-39: What is the difference between pass and continue in Python?
The continue statement makes the loop to resume from the next iteration.

 `ord(char)` in Python takes a string of size one and returns an integer denoting the Unicode

 >>> ord("z")
122


What is GIL in Python language?
Python supports GIL (the global interpreter lock) which is a mutex used to secure access to Python objects, synchronizing multiple threads from running the Python bytecodes at the same time.


How is Python thread safe?
Python ensures safe access to threads. It uses the GIL mutex to set synchronization. If a thread loses the GIL lock at any time, then you have to make the code thread-safe.


* a tuple in Python?
A tuple is a collection type data structure in Python which is immutable.

They are similar to sequences, just like the lists. However, There are some differences between a tuple and list; the former doesn’t allow modifications whereas the list does.

Also, the tuples use parentheses for enclosing, but the lists have square brackets in their syntax.

* exception
```py
while True:
    try:
        value = int(input("Enter an odd number- "))
        if value%2 == 0:
            raise ValueError("Exited due to invalid input!!!")
        else:
            print("Value entered is : %s" % value)
    except ValueError as ex:
        print(ex)
        break
```

* closure

```py

def multiply_number(num):
    def product(number):
        'product() here is a closure'
        return num * number
    return product

num_2 = multiply_number(2)
print(num_2(11))  # 22
print(num_2(24))  # 48

num_6 = multiply_number(6)
print(num_6(1))

```
