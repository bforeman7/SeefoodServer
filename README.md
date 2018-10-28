# SEEFOOD SERVER
#### CEG 4110
##### Nathan Dunn, Brandon Hulbert, Brandon Foreman

## Setting Up Local / Development Environment
1. Install [Python 2](https://www.python.org/downloads/release/python-2715/) and configure your [Windows environment](http://www.aaronstannard.com/how-to-setup-a-proper-python-environment-on-windows/)
2. Install and configure Virualenv (What is [Virtualenv](https://virtualenv.pypa.io/en/latest/) ?) This is NOT required but is RECOMMENDED:
    * `pip install virtualenv`
    * `cd ~/`
    * `mkdir {choose-your-directory-name}`
    * `cd {your-directory}`
    * `mkdir {choose-your-directory-name}`
    * `virtualenv seefood-env -p C:\Python27\python.exe`   
    * To start Virtualenv: `seefood-env/Scripts/activate`
    * To stop Virtualenv: `seefood-env/Scripts/deactivate`
3. Install python dependencies (within project root directory): `pip install -r requirements.txt`
4. Run flask server: `python run.py`
5. In your favorite Browser, navigate to http://127.0.0.1:5000 to be welcomed by the server