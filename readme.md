zorin@zorin-HP-Laptop-14-dq2535tu:~/django-printing-press/crm_hrm$ django-admin startproject myproject
zorin@zorin-HP-Laptop-14-dq2535tu:~/django-printing-press/crm_hrm$ cd myproject
zorin@zorin-HP-Laptop-14-dq2535tu:~/django-printing-press/crm_hrm/myproject$ python3 manage.py startapp user_management
zorin@zorin-HP-Laptop-14-dq2535tu:~/django-printing-press/crm_hrm/myproject$ python3 manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

zorin@zorin-HP-Laptop-14-dq2535tu:~/django-printing-press/crm_hrm/myproject$ python3 manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying sessions.0001_initial... OK

  zorin@zorin-HP-Laptop-14-dq2535tu:~/django-printing-press/crm_hrm/myproject$ python3 manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
May 06, 2024 - 16:41:10
Django version 4.2.11, using settings 'myproject.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.


zorin@zorin-HP-Laptop-14-dq2535tu:~/django-printing-press/crm_hrm/myproject$ python3 manage.py createsuperuser
Username (leave blank to use 'zorin'): 
Email address: saikiranreddy8151@gmail.com
Password: 
Password (again): 
Superuser created successfully.

zorin@zorin-HP-Laptop-14-dq2535tu:~/django-printing-press/crm_hrm/myproject$ python3 manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
May 06, 2024 - 16:45:19
Django version 4.2.11, using settings 'myproject.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.


zorin@zorin-HP-Laptop-14-dq2535tu:~/django-printing-press/crm_hrm/myproject$ python3 manage.py makemigration
s user_management
Migrations for 'user_management':
  user_management/migrations/0001_initial.py
    - Create model UserProfile

zorin@zorin-HP-Laptop-14-dq2535tu:~/django-printing-press/crm_hrm/myproject$ python3 manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions, user_management
Running migrations:
  Applying user_management.0001_initial... OK

zorin@zorin-HP-Laptop-14-dq2535tu:~/django-printing-press/crm_hrm/myproject$ python3 manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
May 06, 2024 - 16:52:25
Django version 4.2.11, using settings 'myproject.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.

zorin@zorin-HP-Laptop-14-dq2535tu:~/django-printing-press/crm_hrm/myproject$ python3 manage.py startapp marketing_user

