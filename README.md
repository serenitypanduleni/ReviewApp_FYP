
# W1889280 - Serenity Pedro

## Table of Contents
- [References](#references)
- [Installation](#installation)


## References 
Mele, A.(2025). Django 5 By Example Fith Edition. Birmingham. Packt Publishing Ltd

Stein, C.(2024). Django 5 Cookbook. India. GitforGits

LearnDjango by Will Vincent - https://learndjango.com/courses/django-for-professionals/introduction/

Django Documentation - https://docs.djangoproject.com/en/6.0/


## Installation

1. Clone the repository 
`git clone https://github.com/serenitypanduleni/ReviewApp_FYP.git`

2. Change into the application directory 
`cd ReviewApp`

2. Create and activate virtual environment
`python3 -m venv .venv'
`source .venv/bin/activate'

3. Install the required dependencies 
`pip install -r requirements.txt`

4. Run the migrations 
`python3 manage.py migrate`

5. Create a superuser
`python3 manage.py createsuperuser`

5. Load the json data into the appliaction
`python3 manage.py loaddata appdata.json`

7. Run the server
`python3 manage.py runserver`


