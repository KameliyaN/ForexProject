# ForexProject
Forex Project is an app that helps people to learn **forex trading**.Users can also write,read and comment articles/news and see live currency quotes.

[![Python 3.8](https://img.shields.io/badge/python-3.8-green.svg)](https://www.python.org/)
[![Django 3.6](https://img.shields.io/badge/django-3.1-green.svg)](https://www.djangoproject.com/)

## Table of Contents
* [About the Project](#about-the-project)
* [Technologies](#technologies)
* [Getting started](#getting-started)
* [Usage](#usage)

### About the project
 
<img src="static/github/images/home_page.png" height="300"  >

 1. **What is Forex** -> The foreign exchange (also known as FX or forex) market is a global marketplace for exchanging national currencies against one another.Because of the worldwide reach of trade, commerce, and finance, forex markets tend to be the largest and most liquid asset markets in the world.
 1. **Project functionalities:**
    * Roles: 
        * Admin(has full CRUD for all products/content, created by users on the website)
        * Authenticated users(have full CRUD for all of their created content)
        * Unauthenticated users(have only get permissions)
        
    * Public part -> A part of the website, which is accessible by everyone – un/authenticated users
and admins
    * Private part -> Accessible only by authenticated user and admins
    * Admin part -> Accessible only by admins
    * login/register functionality(and forms as well)
    * Form validation
    * Testing (unit testing)
    * Class-based views
    * Extended Django user(Profile,using signals)
    * Decorators and Mixins(checking for user permissions)
    * Bootstrap
    * Crispy forms
    * Requests
    
### Technologies
* [Python 3.8](https://www.python.org/downloads/release/python-380/)
* [Django 3.1](https://www.djangoproject.com/)
* [Bootstrap 4](https://getbootstrap.com/)
### Getting Started
1. Clone the repository to your local machine:\
`git clone https://github.com/KameliyaN/ForexProject.git`

1. Install the requirements:\
`pip install -r requirements.txt`

1. Apply the migrations:\
`python manage.py migrate`

1. Run the development server:\
 `python manage.py runserver`

1. The project will be available at:\
 `127.0.0.1:8000`
 
1. Get a free API Key at: https://currencydatafeed.com/ 
```
 def currencies_live_quotes(request):
    params = {
        'token': 'Put your API Access Token here',
        'currency': 'EUR/USD USD/JPY GBP/USD AUD/USD USD/CAD'
    }
    api_result = requests.get('https://currencydatafeed.com/api/data.php', params)

    api_response = api_result.json()
    currencies = api_response['currency']
    context = {'currencies': currencies}
    return render(request, 'currencies/quotes.html', context) 
```
 
### Usage

* View all latest forex news 
<img src="static/github/images/homepage.png" height="300" alt="">

* View full news(article) with its comments

<img src="static/github/images/article.png" height="300" alt="">

* View all news(articles) of a given user

<img src="static/github/images/alluserarticles.png" height="300" alt="">

* Add/Create news(articles)

<img src="static/github/images/add_news.png" height="300" alt="">

* Edit and delete your news(articles)

<img src="static/github/images/editarticle.png" height="300" alt="">

* Comment news(articles)
* Edit and delete your comments
* View live currency quotes

<img src="static/github/images/live_quotes.png" height="300" alt="">

* View  all currencies list 

<img src="static/github/images/curall.png" height="300" alt="">

* View details for a currency 

<img src="static/github/images/detail_cur.png" height="300" alt="">

* View Useful links organized by categories

<img src="static/github/images/usefulinks.png" height="300" alt="">
