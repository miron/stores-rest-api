# Stores REST Api

This is built with Flask, Flask-RESTful, Flask-JWT and Flask-SQLAlchemy.

deploy on Ubuntu WSL:

sudo apt install software-properties-common  
sudo add-apt-repository ppa:deadsnakes/ppa  
sudo apt install python3.9  
sudo apt install python3.9-venv  
sudo apt install postgresql  
sudo service postgresql start  
sudo -i -u postgres  
createuser streetyogi # same as in Linux  
createdb streetyogi  
su streetyogi  
python3.9 -m venv env   
source env/bin/activate  
pip install -r requirements  
set database password in app.py <pwd>  
pyuwsgi -http 127.0.0.1:8000 --master -p4 -w app:app  




