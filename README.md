# Welcome

## Getting started

To begin with the project start by making a cone of the repository.

```bash
# Cloning Repository
git clone git@github.com:Sharif15/MiniLang.git
# Stepping into the file
cd MiniLang
```

## Setting up the python environmnet 

Set up your vertual environment using this command : 

```bash
python -m venv .env

source .env/bin/activate
```

## Branching 

To start wroking create your own branch 

```bash
# Replace your-name with the name you want for the branch
git checkout -b your-name
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

# Warning 

Be sure to pull the latest branch often before you start your work to stay uptodate

```bash
git pull origin main
```