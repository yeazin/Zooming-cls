<div align="center">
<img src="readme/logo.png" width="120px">

<h1> Zooming cls ( Google Classroom Clone )</h2>
<img src="readme/home.png">
<hr>





[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
 [![git](https://badgen.net/badge/icon/git?icon=git&label)](https://git-scm.com) [![Visual Studio](https://badgen.net/badge/icon/visualstudio?icon=visualstudio&label)](https://visualstudio.microsoft.com) [![Docker](https://badgen.net/badge/icon/docker?icon=docker&label)](https://https://docker.com/)
 </div>
<br>
Clone the repository using the following command

```bash
git clone github.com/yeazin/Zooming-cls.git
# After cloning, move into the directory having the project files using the change directory command
cd Zooming-cls
```
Create a virtual environment where all the required python packages will be installed

```bash
# Use this on Windows
python -m venv env
# Use this on Linux and Mac
python3 -m venv env
```
Activate the virtual environment

```bash
# Windows
.\env\Scripts\activate
# Linux and Mac
source env/bin/activate
```
Install all the project Requirements
```bash
pip install -r requirements.txt
```
-Apply migrations and create your superuser (follow the prompts)
```bash
# apply migrations and create your database
python manage.py migrate

# Create a user with manage.py
python manage.py createsuperuser
```

Run the development server

```bash
# run django development server
python manage.py runserver
```
