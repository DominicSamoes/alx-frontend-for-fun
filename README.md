# Markdown to HTML

## Description

Markdown is awesome! All your README.md are made in Markdown. 

---

## General Requirements
* All your files will be interpreted/compiled on Ubuntu 18.04 LTS using python3 (version 3.7 or higher)
* The first line of all your files should be exactly #!/usr/bin/python3
* A README.md file, at the root of the folder of the project, is mandatory
* Your code should use the PEP 8 style (version 1.7.*)
* All your files must be executable
* All your modules should be documented: python3 -c 'print(__import__("my_module").__doc__)'
* Your code should not be executed when imported (by using if __name__ == "__main__":)

---

# Tasks

[0. Start a script](./markdown2html.py)

* Write a script markdown2html.py that takes an argument 2 strings:

	- First argument is the name of the Markdown file
	- Second argument is the output file name

* Requirements:

	- If the number of arguments is less than 2: print in STDERR Usage: ./markdown2html.py README.md README.html and exit 1
	- If the Markdown file doesn’t exist: print in STDER Missing <filename> and exit 1
	- Otherwise, print nothing and exit 0




---

### Author
* **Dominic Samo** - (https://github.com/DominicSamoes)
