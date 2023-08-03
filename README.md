# ToDoList

The todolist project is a simple and intuitive task management application that allows users to create, organize, and track their tasks efficiently.

## Setting up the project

1. Install Python v.3.11 [Python](https://www.python.org/downloads/)

2. Use the package manager [pip](https://pip.pypa.io/en/stable/) to install django (unless you already have it).

```bash
pip install django
```

3. Pull the repository.
4. When using Django, it is necessary to use a virtual environment and set it up as the interpreter.:
```bash
python -m venv <environment_name>
```
* Now activate the virtual environment:

Windows:
```bash
.\environment_name\Scripts\activate
```
macOS/Linux:

```bash
source environment_name/bin/activate
```
* Next step is to set it up as an interpreter. That's how you do it:

Access the interpreter settings and select execution file from the folder where you created your virual environment.
 ```bash
(environment_name->Scripts->python.exe)
```
## Last step
If you completed all of those steps above you can now set up django database. In console prompt paste those 3 commands:

(make sure you are in right directory which includes the manage.py file.)
 ```bash
python manage.py makemigrations # generates the migration files in django.
python manage.py migrate # applies the pending database migrations, making the necessary changes to synchronize the database schema with the current state of the Django models.
python mangage.py loaddata initial_data # loads example data that i prepared
```

Now you can open your browser and paste the url:

[http://127.0.0.1:8000/](http://127.0.0.1:8000/)
## Examples

You can log-in through prepared user:

* username: Jack

* password: password123

Or you can create your own user by clicking link above the log-in section

![image](https://github.com/SzymonGorkiewicz/todolist-django/assets/92310752/adc2a0fb-4e26-4d19-85aa-bfee136f7fcf)


Example gif:
![Animation](https://github.com/SzymonGorkiewicz/todolist-django/assets/92310752/c46ec8cb-2a53-4601-ac3c-61e4dd562a47)

## Contributing

Pull requests are welcome.

