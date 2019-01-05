# SEEFOOD SERVER
#### CEG 4110
##### Nathan Dunn, Brandon Hulbert, Brandon Foreman

## Setting Up Development Environment (Linux)
1. Install and configure Virualenv (What is [Virtualenv](https://virtualenv.pypa.io/en/latest/) ?) This is NOT required but is RECOMMENDED:
    * `pip install virtualenv`
    * `cd SeefoodServer/`
    * `virtualenv seefood-venv --python=python2.7`  
    * To start Virtualenv: `source seefood-venv/bin/activate`
    * To stop Virtualenv: `deactivate`
2. Install python dependencies (within project root directory && virtualenv activated): `pip install -r requirements.txt`

#### Setting Up Database
1. Install PostgreSQL and Dependencies: `sudo apt-get install postgresql postgresql-contrib libpq-dev`
2. Connect to PostgreSQL: `sudo -i -u postgres psql` 
3. Alter user credentials to meet flask configurations: `ALTER USER postgres WITH ENCRYPTED PASSWORD 'password';`
3. Create the database: `CREATE DATABASE seefood_db;`
4. Run flask to create database(in project root dir): `python run.py`
5. Reconnect to PostgreSQL (step 2)
6. Change to created database: `\c seefood_db`
7. Verify image table was created: `select * from images`

## Run in Production / Deployment
* clone the repository in EC2 instance
* Follow steps [here](https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-uswgi-and-nginx-on-ubuntu-18-04), from Digital Ocean

## Testing API with Postman
* Download [Postman](https://www.ceos3c.com/open-source/install-postman-ubuntu-18-04/) 
* Ask a team member to be added to the Seefood workspace
* In the top right of the screen, click on the dropdown titled *no environment* and select *Seefood-Development*
* The endpoints that can be tested are located under the folder *Seefood-API* on the left side of the screen
* **Make sure the server is running** and test the endpoints accordingly. Instructions on how to test each endpoints are located in their description.

Additional documentation for the full application and server:
https://docs.google.com/document/d/1sWhShVgpn9bVdvPXGpjd1iFVIYPWAeU967ElWOJ5Omw/edit?usp=sharing
