## Social-library project

### Project Description
* A social online library where user can upload,read,download books.

* Here user cannot delete uploaded files only admin have the previlege.

* Anyone can signup and make an user and read the books.

### How to Install and Run the project

* Run this command to clone and run in local server
```
 git clone https://github.com/Abhi-1298/E-library.git
 ```

* Create an Enviornment 
```
 python3 -m venv env_name
```
* Activate Environment -
```
 ./env/scripts/activate
 ```
* Install all Dependencies 
```
pip install requirements.txt
```
* Database Migrations
```
 python3 manage.py makemigratoins
```
* To apply Sql query
```
python3 manage.py migrate
```
* To Run Server 
```
python3 manage.py runserver
```
