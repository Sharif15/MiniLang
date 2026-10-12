# Welcome

## Team member
Sharif Islam <br> 
Angel Castillo <br> 
Wendy Hielo <br>

## Getting started

To begin with the project start by making a clone of the repository.

```bash
# Cloning Repository
git clone git@github.com:Sharif15/MiniLang.git
# Stepping into the file
cd MiniLang
```

## Testing & Running the Interpreter

### Running Unit Tests:

To run the given test suite use the following command: 

```bash
python -m unittest tests.test_interpreter
```

### Running the Interpreter:

To run the interpreter on a MiniLang program file, use the following command format:

```bash
python -m main.py [--debug] <path_to_your_source_code_file>
```

The `--debug` flag enables the Debug/Display mode.

Example run:
```bash
python main.py tests\test01_basic.mini
```

## Instructions for Development:

### Branching 

To start wroking create your own branch 

```bash
# Replace your-name with the name you want for the branch
git checkout -b your-name
# Add your name to this readme file
git add .
git commit -m "New branch"
git push -u origin your-name
```

For anyother time your can use: 

```bash 
# To step into your branch
git checkout your-name
```

and all other git operation is the same 

### Warning !!!

Be sure to pull the latest branch often before you start your work to stay uptodate

```bash
git pull origin main
```