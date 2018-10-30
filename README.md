# SEEFOOD SERVER
#### CEG 4110
##### Nathan Dunn, Brandon Hulbert, Brandon Foreman

## Setting Up Local / Development Environment (Linux)
2. Install and configure Virualenv (What is [Virtualenv](https://virtualenv.pypa.io/en/latest/) ?) This is NOT required but is RECOMMENDED:
    * `pip install virtualenv`
    * `cd SeefoodServer/`
    * `virtualenv seefood-venv --python=python2.7`  
    * To start Virtualenv: `source seefood-venv/bin/activate`
    * To stop Virtualenv: `deactivate`
3. Install python dependencies (within project root directory && virtualenv activated): `pip install -r requirements.txt`
4. Run flask server (with virtualenv activated): `python run.py`
5. In your favorite Browser, navigate to http://0.0.0.0:5000 to be welcomed by the server