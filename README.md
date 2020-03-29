# Fullthrottle Labs' Problem Statement

Design and implement a Django application with User and ActivityPeriod models, write
a custom management command to populate the database with some dummy data, and design
an API to serve that data in the json format.
You should use the following API FORMAT -     

        {
            "ok": true,
            "members": [{
                    "id": "W012A3CDE",
                    "real_name": "Egon Spengler",
                    "tz": "America/Los_Angeles",
                    "activity_periods": [{
                            "start_time": "Feb 1 2020  1:33PM",
                            "end_time": "Feb 1 2020 1:54PM"
                        },
                        {
                            "start_time": "Mar 1 2020  11:11AM",
                            "end_time": "Mar 1 2020 2:00PM"
                        },
                        {
                            "start_time": "Mar 16 2020  5:33PM",
                            "end_time": "Mar 16 2020 8:02PM"
                        }
                    ]
                },
                {
                    "id": "W07QCRPA4",
                    "real_name": "Glinda Southgood",
                    "tz": "Asia/Kolkata",
                    "activity_periods": [{
                            "start_time": "Feb 1 2020  1:33PM",
                            "end_time": "Feb 1 2020 1:54PM"
                        },
                        {
                            "start_time": "Mar 1 2020  11:11AM",
                            "end_time": "Mar 1 2020 2:00PM"
                        },
                        {
                            "start_time": "Mar 16 2020  5:33PM",
                            "end_time": "Mar 16 2020 8:02PM"
                        }
                    ]
                }
            ]
        }

# List of Libraries and Packages used in Django

• django 3.0
• python 3.7.3
• django-rest-framework
• Faker 
• gunicorn whitenoise psycopg2
• random
• MDBootstrap 
• HEROKU(Deployment)

# Deployment
This project is deployed on Heroku web service. You can check it out here

    https://fullthrottle-django-app.herokuapp.com/
# Structure
I have structured my project as shown below
- fullthrottle_app
    - models.py             --- creating models for User and ActivityPeriods 
    - views.py/api.py       --- creating bussiness logic for processing the data from database 
    - serializers.py        --- creating serialised data from DB using DRF methods
    - urls.py               --- creating and redirecting processed data into templates 
- fullthrottle_project
    - settings.py           --- configuring apps,templates,static files to current django project
- templates                 --- Contain HTML files
- db.sqlite3                --- database used is sqlite3
- manage.py

# Project Overview

The main functionality of this challenge is as follows : 

•  Generate or Bulk creation of Users and allotment of Activity period to each User and populate the data in database using Custom Management Command in Django.
•  Display the JSON format of the populated data by using Django-rest-framework and list all the users with respect to activity period,timezone,start time,endtime.
•  Custom Management command is served through two ways:
 - Can be accessed through COMMAND LINE ARGS 

        python manage.py <throttle_command> <args>
           
    Command name - throttle_command
    argument     - 5 (int)
 (OR)
- Can be accessed services a particular URL
 
        https://fullthrottle-django-app.herokuapp.com/throttle-command/

# Application
Open the application : 
    
    https://fullthrottle-django-app.herokuapp.com/
### Usage
#### 1. To populate or Generate data by URL: 

Enter the number of users to be created as arguments
• Numbers - Enter the number of users you wish to generate in the DB
• Randomly Users,start time,end time,time zone are alloted to each user and will be stored in the DB.

#### 2. To populate or Generate data using Command Line : 
Enter the number of users to be created as arguments
• Numbers - Enter the number of users you wish to generate in the DB using command line
• Randomly Users,start time,end time,time zone are alloted to each user and will be stored in the DB.
### 3. To view the API serving the above conditions check the url :      
    
    https://fullthrottle-django-app.herokuapp.com/api/list/ 

## Run Scripts
#### Using Command Line
    python manage.py throttle_command 5
    
Command name - throttle_command
argument     - 5 (int)

#### Using Browser
#### Step 1 

    https://fullthrottle-django-app.herokuapp.com/
  
  Display Home page of the Django-challenge 
  
#### Step 2


    https://fullthrottle-django-app.herokuapp.com/throttle-command/
    
 Generates Bulk Data for Users and Activity Period 
    
#### Step 3 

    https://fullthrottle-django-app.herokuapp.com/api/list
    
Display the List of Users and assigned activity period in JSON format

References:
https://docs.djangoproject.com/en/3.0/
https://www.django-rest-framework.org/topics/documenting-your-api/




