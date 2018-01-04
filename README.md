# Schrödinger's cat

`scat` is a `cat` clone which, for every line in the files passed to it, has
roughly a 50/50 chance -of printing that line. Oh, and it has kind of a crappy
name...

## Features

* Supports line numbering with `-n` and `-b` flags. Numbers correspond to lines
  in the original file
* Behaves just like `cat` when provided multiple files (line numbers reset)
* Behaves just like `cat` when run without arguments (uses stdin)

## Use cases
* Find some

## Examples

If you run:
```
scat -b zen_of_python.txt
```

the output might be:
```
     5  Complex is better than complicated.
     7  Sparse is better than dense.
    11  Errors should never pass silently.
    13  In the face of ambiguity, refuse the temptation to guess.
    14  There should be one-- and preferably only one --obvious way to do it.
    16  Now is better than never.
    17  Although never is often better than *right* now.
```

but it could also be:
```
     1  The Zen of Python, by Tim Peters

     2  Beautiful is better than ugly.
     3  Explicit is better than implicit.
     4  Simple is better than complex.
     6  Flat is better than nested.
     7  Sparse is better than dense.
    10  Although practicality beats purity.
    12  Unless explicitly silenced.
    13  In the face of ambiguity, refuse the temptation to guess.
    15  Although that way may not be obvious at first unless you're Dutch.
    19  If the implementation is easy to explain, it may be a good idea.
    20  Namespaces are one honking great idea -- let's do more of those!
```
