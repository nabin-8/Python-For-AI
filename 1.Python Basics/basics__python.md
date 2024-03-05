### Variables in Python
// https://docs.python-guide.org

name="Nabin" # Assigning value to a variable

in the memory

```mermaid
classDiagram
    class Memory Objec {
        type: string
        value: "Nabin"
        Refrence Count: 1
    }

    class Name {
        name="Nabin"
    }

    Memory Objec <|-- Name

```

like wise when we store:
age=22

```mermaid
classDiagram
    class Memory Objec {
        type: Number
        value: 22
        Refrence Count: 1
    }

    class age {
        age=22
    }

    Memory Objec <|-- age

```

#### Mutable and immutable variables in Python
``` mermaid
    flowchart LR
    A(Immutable) ---B(integers)
    A(Immutable) ---C(floats)
    A(Immutable) ---D(complex numbers)
    A(Immutable) ---E(Booleans)
    A(Immutable) ---F(Strings)
    A(Immutable) ---G(Tuples)

    N(Mutable) ---NA(Lists)
    N(Mutable) ---NC(Dictionaries)
    N(Mutable) ---ND(Sets)


```

#### Keywords in Python

<pre>
    False               class               from                or
    None                continue            global              pass
    True                def                 if                  raise
    and                 del                 import              return
    as                  elif                in                  try
    assert              else                is                  while
    async               except              lambda              with
    await               finally             nonlocal            yield
    break               for                 not
</pre>

#### Comments in Python
``` python
# This is a comment. It will be ignored by the interpreter.
"""This is also a comment, but it's a docstring, which provides documentation to other programmers reading your code."""

```

#### Input Output
``` python
# To get input from user:
name = input("Enter your name: ")
print("Hello, " + name)
```