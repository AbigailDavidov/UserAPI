# UserAPI
This Python code is a RESTful API with the following CRUD functions:<br>
create_user<br>
get_users<br>
update_user <br>
delete_user<br>
I'v decided to use SQLite as my DB, the class db_sqlite is a generic class for interactions with the DB<br>
The class userActions is a specific class for user API-DB in interactions<br>
I used unittest for testing and logging to track responses, exceptions etc.<br>
Also added basic auth<br>

# How to run the project

Clone the project Repository
```
git clone https://github.com/jod35/Buildndeploy-A-REST-API-With-Flask.git

```

Enter the project folder and create a virtual environment
``` 
$ cd https://github.com/jod35/Build-And-Deploy-A-REST-API-With-Flask 

$ python -m venv env 

```

Activate the virtual environment
``` 
$ source env/bin/actvate #On linux Or Unix

$ source env/Scripts/activate #On Windows 
 
```

Install all requirements

```
$ pip install -r requirements.txt
```

And you are all set
