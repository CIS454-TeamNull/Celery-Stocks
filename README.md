# Celery-Stocks
Inventory Management for Restaurants

## Notes for Team Null:

git clone this repo

enter the directory and create your own branch to make your changes in

git checkout -b your_name_dev

Install virtualenv with pip install virtualenv

https://www.liquidweb.com/kb/how-to-setup-a-python-virtual-environment-on-windows-10/

Then create a python virtual environment with: python -m venv venv

Activate the venv with: source venv/bin/activate

then install python modules with: pip install -r requirements.txt 

now you can run the Flask application

flask run

or 

FLASK_APP=main.py SECRET_KEY=keyhere flask --debug run

Now you can load the site on your machine, default: http://localhost:5000
or http://127.0.0.1:5000 depending on if your system has localhost defined

# Read the tutorial

https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world

###### Docker Notes
Build the Docker image with: docker build -t celery:latest .  

Make sure Flask app is stopped, run Docker container with: docker run -p5000:80 celery

###### Helpful tutorials:

https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world

http://getskeleton.com/

https://sqldocs.org/sqlite/introduction/

