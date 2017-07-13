# Schrödinger's cat

A `cat` clone which, for every line in the files passed to it, has 50/50 chance
of printing that line.

## Features

* Supports `-b` and `-n` flags. Numbers correspond to lines in the original file.
* Behaves just like `cat` when provided multiple files (line numbers reset)
* Behaves just like `cat` when run without arguments (uses stdin)

## Use cases
* Find some
