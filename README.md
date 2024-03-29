# openCV-Basic

Belajar opencv dari dasar
1. Install Virtual Environment Linux
    - `$ sudo apt-get install python3-pip`
    - `$ sudo pip3 install virtualenv`
2. Install Virtual Environment Windows
    - `$ pip install virtualenv`
    - `$ virtualenv env`
    - `$ cd env/Script`
    - `$ activate.bat`
3. Create Virtual Environment namely Env 
    - `$ python -m venv Env`
    or
    - `$ virtualenv .venv`
4. Go to Env 
    - `$ Env\Scripts\activate.bat`
    or 
    - `$ source .venvUbuntu/bin/activate`
5. Check pip list `$ pip list`. If need to upgrade, please upgrade first. `$ python.exe -m pip install --upgrade pip`
6. Check again `$ pip list`
7. Install Numpy `$ pip install numpy`. Check again `$ pip list`
8. Install opencv `$ pip install opencv-contrib-python`
9. How to check opencv already installed:

- Type `$ python`
- Type `import cv2`
- Type `cv2.__version__`

> NB: if point no 6 not work, try `$ pip install opencv-contrib-python-headless` or `$ pip install opencv-python`.

10. Install matplotlib `$ pip install matplotlib`
11. Install `$ sudo apt install python3-tk` if matplotlib can't show()



///////////////////////////////////////////////////////////////////////////////////
# Step 1: Update your repositories
sudo apt-get update

# Step 2: Install pip for Python 3
sudo apt-get install build-essential libssl-dev libffi-dev python-dev
sudo apt install python3-pip

# Step 3: Use pip to install virtualenv
sudo pip3 install virtualenv 

# Step 4: Launch your Python 3 virtual environment, here the name of my virtual environment will be env3
virtualenv -p python3 env3

# Step 5: Activate your new Python 3 environment. There are two ways to do this
. env3/bin/activate # or source env3/bin/activate which does exactly the same thing

# you can make sure you are now working with Python 3
python -- version
# this command will show you what is going on: the python executable you are using is now located inside your virtualenv repository
which python 

# Step 6: code your stuff

# Step 7: done? leave the virtual environment
deactivate



# 23_Face_Detection
1. Download [trained classifier XML file](https://raw.githubusercontent.com/opencv/opencv/master/data/haarcascades/haarcascade_frontalface_default.xml)
2. Save it to your project directory
