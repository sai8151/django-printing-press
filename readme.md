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

[07/May/2024 18:18:12] "GET /marketing-user/client-list/ HTTP/1.1" 200 686
[07/May/2024 18:18:15] "POST /marketing-user/logout/ HTTP/1.1" 200 3428
[07/May/2024 18:18:32] "GET /admin/ HTTP/1.1" 302 0
[07/May/2024 18:18:32] "GET /admin/login/?next=/admin/ HTTP/1.1" 200 4181
[07/May/2024 18:18:41] "POST /marketing-user/logout/ HTTP/1.1" 200 3428
[07/May/2024 18:18:43] "GET /marketing-user/client-list/ HTTP/1.1" 302 0
[07/May/2024 18:18:43] "GET /marketing-user/add-client/ HTTP/1.1" 302 0
Not Found: /accounts/login/
[07/May/2024 18:18:43] "GET /accounts/login/?next=/marketing-user/add-client/ HTTP/1.1" 404 2731
[07/May/2024 18:18:43] "GET /marketing-user/accounts/login/ HTTP/1.1" 200 853
[07/May/2024 18:18:46] "GET /marketing-user/accounts/profile/ HTTP/1.1" 302 0
[07/May/2024 18:18:46] "GET /marketing-user/accounts/login/ HTTP/1.1" 200 853
Not Found: /accounts/login/
[07/May/2024 18:18:49] "GET /accounts/login/?next=/marketing-user/accounts/profile/ HTTP/1.1" 404 2737
[07/May/2024 18:18:51] "GET /marketing-user/accounts/login/ HTTP/1.1" 200 853
[07/May/2024 18:18:51] "GET /marketing-user/accounts/login/ HTTP/1.1" 200 853
[07/May/2024 18:18:55] "GET /marketing-user/accounts/login/ HTTP/1.1" 200 853
[07/May/2024 18:18:57] "GET /marketing-user/accounts/login/ HTTP/1.1" 200 853
[07/May/2024 18:18:57] "GET /marketing-user/accounts/login/ HTTP/1.1" 200 853
[07/May/2024 18:18:57] "GET /marketing-user/accounts/login/ HTTP/1.1" 200 853
/home/zorin/django-printing-press/crm_hrm/myproject/marketing_user/urls.py changed, reloading.
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
May 07, 2024 - 18:21:02
Django version 4.2.11, using settings 'myproject.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.

[07/May/2024 18:21:17] "POST /marketing-user/accounts/login/ HTTP/1.1" 302 0
[07/May/2024 18:21:17] "GET /accounts/profile/ HTTP/1.1" 302 0
[07/May/2024 18:21:17] "GET /marketing-user/accounts/profile/ HTTP/1.1" 200 686
[07/May/2024 18:21:21] "POST /marketing-user/logout/ HTTP/1.1" 302 0
[07/May/2024 18:21:21] "GET / HTTP/1.1" 302 0
[07/May/2024 18:21:21] "GET /index.html/ HTTP/1.1" 200 16980
[07/May/2024 18:21:21] "GET /static/img/id_card_01.jpeg HTTP/1.1" 304 0
[07/May/2024 18:21:21] "GET /static/img/id_card_02.png HTTP/1.1" 304 0
[07/May/2024 18:21:21] "GET /static/img/id_card_03.avif HTTP/1.1" 304 0
[07/May/2024 18:21:29] "GET /marketing-user/ HTTP/1.1" 302 0
[07/May/2024 18:21:29] "GET /marketing-user/accounts/login/ HTTP/1.1" 200 853
[07/May/2024 18:21:32] "GET /admin/ HTTP/1.1" 302 0
[07/May/2024 18:21:32] "GET /admin/login/?next=/admin/ HTTP/1.1" 200 4181
[07/May/2024 18:21:37] "GET /admin/ HTTP/1.1" 302 0
[07/May/2024 18:21:37] "GET /admin/login/?next=/admin/ HTTP/1.1" 200 4181
[07/May/2024 18:27:12] "GET /marketing-user/ HTTP/1.1" 302 0
[07/May/2024 18:27:12] "GET /marketing-user/accounts/login/ HTTP/1.1" 200 853
[07/May/2024 18:27:25] "POST /marketing-user/accounts/login/ HTTP/1.1" 302 0
[07/May/2024 18:27:25] "GET /accounts/profile/ HTTP/1.1" 302 0
[07/May/2024 18:27:25] "GET /marketing-user/accounts/profile/ HTTP/1.1" 200 686
[07/May/2024 18:27:27] "GET /marketing-user/add-client/ HTTP/1.1" 200 2853
[07/May/2024 18:27:30] "GET /marketing-user/client-list/ HTTP/1.1" 200 686
[07/May/2024 18:29:16] "GET /marketing-user/client-list/ HTTP/1.1" 200 3024
[07/May/2024 18:29:26] "GET /marketing-user/add-client/ HTTP/1.1" 200 2853
[07/May/2024 18:29:39] "POST /marketing-user/add-client/ HTTP/1.1" 302 0
[07/May/2024 18:29:39] "GET /marketing-user/client-list/ HTTP/1.1" 200 3065
[07/May/2024 18:29:43] "POST /marketing-user/logout/ HTTP/1.1" 302 0
[07/May/2024 18:29:43] "GET / HTTP/1.1" 302 0
[07/May/2024 18:29:43] "GET /index.html/ HTTP/1.1" 200 16980
[07/May/2024 18:29:43] "GET /index.html/ HTTP/1.1" 200 16980
[07/May/2024 18:30:17] "GET /marketing-user/ HTTP/1.1" 302 0
[07/May/2024 18:30:17] "GET /marketing-user/accounts/login/ HTTP/1.1" 200 853
[07/May/2024 18:31:19] "GET /marketing-user/accounts/login/ HTTP/1.1" 200 853
[07/May/2024 18:31:21] "GET /marketing-user/accounts/login/ HTTP/1.1" 200 853
[07/May/2024 18:31:21] "GET /marketing-user/accounts/login/ HTTP/1.1" 200 853
[07/May/2024 18:31:21] "GET /marketing-user/accounts/login/ HTTP/1.1" 200 853
[07/May/2024 18:31:27] "GET /marketing-user/accounts/login/ HTTP/1.1" 200 853
[07/May/2024 18:31:27] "GET /marketing-user/accounts/login/ HTTP/1.1" 200 853
[07/May/2024 18:31:28] "GET /marketing-user/accounts/login/ HTTP/1.1" 200 853
[07/May/2024 18:31:28] "GET /marketing-user/accounts/login/ HTTP/1.1" 200 853
[07/May/2024 18:31:28] "GET /marketing-user/accounts/login/ HTTP/1.1" 200 853
[07/May/2024 18:31:32] "GET /marketing-user/ HTTP/1.1" 302 0
[07/May/2024 18:31:32] "GET /marketing-user/accounts/login/ HTTP/1.1" 200 853
[07/May/2024 18:31:39] "GET /marketing-user/ HTTP/1.1" 302 0
[07/May/2024 18:31:39] "GET /marketing-user/accounts/login/ HTTP/1.1" 200 853
[07/May/2024 18:31:41] "GET /marketing-user/accounts/login/ HTTP/1.1" 200 853
Not Found: /favicon.ico
[07/May/2024 18:31:41] "GET /favicon.ico HTTP/1.1" 404 2686
[07/May/2024 18:32:26] "GET /marketing-user/accounts/login/ HTTP/1.1" 200 853
[07/May/2024 18:32:26] "GET /marketing-user/accounts/login/ HTTP/1.1" 200 853
[07/May/2024 18:32:27] "GET /marketing-user/accounts/login/ HTTP/1.1" 200 853
[07/May/2024 18:32:27] "GET /marketing-user/accounts/login/ HTTP/1.1" 200 853
[07/May/2024 18:32:27] "GET /marketing-user/accounts/login/ HTTP/1.1" 200 853
^Czorin@zorin-HP-Laptop-14-dq2535tu:~/django-printing-press/crm_hrm/myproject$ python3 manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
May 07, 2024 - 18:32:33
Django version 4.2.11, using settings 'myproject.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.

[07/May/2024 18:32:36] "GET /marketing-user/accounts/login/ HTTP/1.1" 200 853
[07/May/2024 18:32:40] "GET /marketing-user/ HTTP/1.1" 302 0
[07/May/2024 18:32:40] "GET /marketing-user/accounts/login/ HTTP/1.1" 200 853
[07/May/2024 18:32:58] "GET /marketing-user/accounts/login/ HTTP/1.1" 200 853
[07/May/2024 18:32:59] "GET /marketing-user/accounts/login/ HTTP/1.1" 200 853
[07/May/2024 18:32:59] "GET /marketing-user/accounts/login/ HTTP/1.1" 200 853
[07/May/2024 18:33:00] "GET /marketing-user/accounts/login/ HTTP/1.1" 200 853
[07/May/2024 18:33:00] "GET /marketing-user/accounts/login/ HTTP/1.1" 200 853
[07/May/2024 18:33:00] "GET /marketing-user/accounts/login/ HTTP/1.1" 200 853
[07/May/2024 18:33:00] "GET /marketing-user/accounts/login/ HTTP/1.1" 200 853
[07/May/2024 18:33:40] "GET /marketing-user/accounts/login/ HTTP/1.1" 200 2575
[07/May/2024 18:33:52] "POST /marketing-user/accounts/login/ HTTP/1.1" 302 0
[07/May/2024 18:33:52] "GET /accounts/profile/ HTTP/1.1" 302 0
[07/May/2024 18:33:52] "GET /marketing-user/accounts/profile/ HTTP/1.1" 200 3065
[07/May/2024 18:33:56] "POST /marketing-user/logout/ HTTP/1.1" 302 0
[07/May/2024 18:33:56] "GET / HTTP/1.1" 302 0
[07/May/2024 18:33:56] "GET /index.html/ HTTP/1.1" 200 16980
[07/May/2024 18:33:56] "GET /index.html/ HTTP/1.1" 200 16980
[07/May/2024 18:33:56] "GET /static/img/id_card_01.jpeg HTTP/1.1" 304 0
[07/May/2024 18:33:56] "GET /static/img/id_card_02.png HTTP/1.1" 304 0
[07/May/2024 18:33:56] "GET /static/img/id_card_03.avif HTTP/1.1" 304 0
[07/May/2024 18:46:23] "GET /marketing-user/ HTTP/1.1" 302 0
[07/May/2024 18:46:23] "GET /marketing-user/accounts/login/ HTTP/1.1" 200 2575
[07/May/2024 18:46:40] "POST /marketing-user/accounts/login/ HTTP/1.1" 302 0
[07/May/2024 18:46:40] "GET /accounts/profile/ HTTP/1.1" 302 0
[07/May/2024 18:46:41] "GET /marketing-user/accounts/profile/ HTTP/1.1" 200 32
