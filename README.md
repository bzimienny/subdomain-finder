# subdomain-finder
Tool for search dns subdomains with dictionaries. 
# Installation
First you need to clone repository.
```linux
git clone https://github.com/bzimienny/subdomain-finder.git
```
Next you need to move to the cloned repository.
```linux
cd subdomain-finder
```
Setup python:
``` python
python -m venv myvenv
  ###########
 ###Linux###
###########
source ./myvenv/bin/activate
  ###########
 ##Windows##
###########
./myvenv/bin/activate

pip install requests

```
# How to use
To run you need type "main.py" with python.
## Options
-d "name" domain_name - choose dictionary
for egzample:
```linux
python main.py -d example_dictionary.txt google.pl
```