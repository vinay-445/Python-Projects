logo="""
  ___        _        ____                      
 / _ \ _   _(_)____  / ___| __ _ _ __ ___   ___ 
| | | | | | | |_  / | |  _ / _` | '_ ` _ \ / _ \
| |_| | |_| | |/ /  | |_| | (_| | | | | | |  __/
 \__\_\\__,_|_/___|  \____|\__,_|_| |_| |_|\___|
"""
quiz = {
    "questions": [
        {
            "question": "What is the output of the following code?\n\nprint(2 ** 3)",
            "options": {
                "a": "5",
                "b": "6",
                "c": "8",
                "d": "9"
            },
            "answer": "c"
        },
        {
            "question": "Which of the following is a mutable data type in Python?",
            "options": {
                "a": "Tuple",
                "b": "List",
                "c": "String",
                "d": "Integer"
            },
            "answer": "b"
        },
        {
            "question": "How do you start a comment in Python?",
            "options": {
                "a": "//",
                "b": "/*",
                "c": "#",
                "d": "--"
            },
            "answer": "c"
        },
        {
            "question": "What does the 'len' function do?",
            "options": {
                "a": "Adds elements to a list",
                "b": "Returns the number of items in an object",
                "c": "Removes elements from a list",
                "d": "None of the above"
            },
            "answer": "b"
        },
        {
            "question": "Which keyword is used to define a function in Python?",
            "options": {
                "a": "function",
                "b": "def",
                "c": "func",
                "d": "define"
            },
            "answer": "b"
        },
        {
            "question": "What is the output of the following code?\n\nprint(3 + 4 * 2)",
            "options": {
                "a": "14",
                "b": "11",
                "c": "10",
                "d": "None of the above"
            },
            "answer": "b"
        },
        {
            "question": "Which of the following is a Python tuple?",
            "options": {
                "a": "[1, 2, 3]",
                "b": "{1, 2, 3}",
                "c": "(1, 2, 3)",
                "d": "{1: 'a', 2: 'b', 3: 'c'}"
            },
            "answer": "c"
        },
        {
            "question": "How can you access the last element of a list `my_list`?",
            "options": {
                "a": "my_list[0]",
                "b": "my_list[-1]",
                "c": "my_list[len(my_list)]",
                "d": "my_list[last]"
            },
            "answer": "b"
        },
        {
            "question": "What does the `append()` method do in Python?",
            "options": {
                "a": "Removes the last element of a list",
                "b": "Adds a new element at the end of a list",
                "c": "Returns the length of a list",
                "d": "Sorts the elements of a list"
            },
            "answer": "b"
        },
        {
            "question": "Which of the following statements will create a dictionary in Python?",
            "options": {
                "a": "d = {1, 2, 3}",
                "b": "d = {1: 'a', 2: 'b', 3: 'c'}",
                "c": "d = (1, 2, 3)",
                "d": "d = [1, 2, 3]"
            },
            "answer": "b"
        },
        {
            "question": "What is the output of `print('Python'.lower())`?",
            "options": {
                "a": "PYTHON",
                "b": "python",
                "c": "Python",
                "d": "pYTHON"
            },
            "answer": "b"
        },
        {
            "question": "Which of the following is the correct way to define a class in Python?",
            "options": {
                "a": "class MyClass:",
                "b": "MyClass class:",
                "c": "define MyClass:",
                "d": "function MyClass:"
            },
            "answer": "a"
        },
        {
            "question": "What is the output of `print(type(3.14))`?",
            "options": {
                "a": "<class 'int'>",
                "b": "<class 'float'>",
                "c": "<class 'double'>",
                "d": "<class 'decimal'>"
            },
            "answer": "b"
        },
        {
            "question": "Which of the following is used to handle exceptions in Python?",
            "options": {
                "a": "try-except",
                "b": "try-catch",
                "c": "catch-except",
                "d": "try-finally"
            },
            "answer": "a"
        },
        {
            "question": "What will be the output of the following code?\n\nx = [1, 2, 3]\ny = x\ny.append(4)\nprint(x)",
            "options": {
                "a": "[1, 2, 3]",
                "b": "[1, 2, 3, 4]",
                "c": "[4, 1, 2, 3]",
                "d": "[1, 2, 3, 4, 4]"
            },
            "answer": "b"
        },
        {
            "question": "What will be the output of the following code?\n\nprint(10 // 3)",
            "options": {
                "a": "3",
                "b": "3.33",
                "c": "3.0",
                "d": "4"
            },
            "answer": "a"
        },
        {
            "question": "Which method is used to remove whitespace from both ends of a string?",
            "options": {
                "a": "strip()",
                "b": "trim()",
                "c": "cut()",
                "d": "remove()"
            },
            "answer": "a"
        },
        {
            "question": "How do you check if a key exists in a dictionary?",
            "options": {
                "a": "key in dict",
                "b": "dict.has_key(key)",
                "c": "dict.contains(key)",
                "d": "key.exists(dict)"
            },
            "answer": "a"
        },
        {
            "question": "Which of the following is a valid way to create a set in Python?",
            "options": {
                "a": "set = {1, 2, 3}",
                "b": "set = [1, 2, 3]",
                "c": "set = (1, 2, 3)",
                "d": "set = {1: 'a', 2: 'b'}"
            },
            "answer": "a"
        },
        {
            "question": "What will be the output of the following code?\n\nprint('Python'[::-1])",
            "options": {
                "a": "nohtyP",
                "b": "Python",
                "c": "Pytnoh",
                "d": "Error"
            },
            "answer": "a"
        },
        {
            "question": "Which operator is used to check if two values are equal in Python?",
            "options": {
                "a": "=",
                "b": "==",
                "c": "===",
                "d": "!="
            },
            "answer": "b"
        },
        {
            "question": "What does the `pop()` method do when used on a dictionary?",
            "options": {
                "a": "Removes a key-value pair",
                "b": "Removes the last element",
                "c": "Adds a new key-value pair",
                "d": "Returns the dictionary size"
            },
            "answer": "a"
        },
        {
            "question": "How do you define a class method in Python?",
            "options": {
                "a": "@classmethod",
                "b": "@method",
                "c": "def method_name(cls):",
                "d": "def class_method():"
            },
            "answer": "a"
        },
        {
            "question": "Which of the following functions is used to get the type of an object in Python?",
            "options": {
                "a": "type()",
                "b": "object()",
                "c": "isinstance()",
                "d": "class()"
            },
            "answer": "a"
        },
        {
            "question": "What will be the output of the following code?\n\nprint(5 % 2)",
            "options": {
                "a": "1",
                "b": "2",
                "c": "0",
                "d": "5"
            },
            "answer": "a"
        },
        {
            "question": "Which function is used to read a line from a file in Python?",
            "options": {
                "a": "read()",
                "b": "readline()",
                "c": "getline()",
                "d": "fetch()"
            },
            "answer": "b"
        },
        {
            "question": "What does the `enumerate()` function do in Python?",
            "options": {
                "a": "Adds index to an iterable",
                "b": "Converts an iterable to a dictionary",
                "c": "Sorts an iterable",
                "d": "Filters an iterable"
            },
            "answer": "a"
        },
        {
            "question": "How can you merge two dictionaries in Python 3.9 and above?",
            "options": {
                "a": "dict1.update(dict2)",
                "b": "dict1 + dict2",
                "c": "dict1.merge(dict2)",
                "d": "dict1 | dict2"
            },
            "answer": "d"
        },
        {
            "question": "What is the purpose of the `__init__` method in Python classes?",
            "options": {
                "a": "Initialize instance variables",
                "b": "Define class variables",
                "c": "Define a class method",
                "d": "Initialize class-level attributes"
            },
            "answer": "a"
        },
        {
            "question": "What will be the output of the following code?\n\nprint([x**2 for x in range(4)])",
            "options": {
                "a": "[0, 1, 4, 9]",
                "b": "[0, 1, 2, 3]",
                "c": "[0, 1, 4, 16]",
                "d": "[1, 4, 9]"
            },
            "answer": "a"
        }
    ]
}
