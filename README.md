# KMicroblog
Microblogging application

## Installation & usage
Create and switch to a virtual environment (not required, but highly recommended):
```
python -m venv venv


On Linux/OSX:

source venv/bin/activate

On Windows:

.\venv\Scripts\activate
```

Install dependencies:
```
pip install -r requirements.txt
```

Create a .env file: (*Make sure that you will modify it with your settings.*)
```
cp .env.template .env
```

Migrate database changes:
```
python manage.py migrate
```

Create a superuser (optional):
```
python manage.py createsuperuser
```

And finally, run the development server:
```
python manage.py runserver
```

## Deployment
*TBA*

## To-do list
- [x] ~~MySQL / MariaDB support~~ Now deprecated. Use PostgreSQL or SQLite instead.
- [ ] Authentication
    * [x] Log in / out
    * [x] Account creation
    * [ ] Account deletion
    * [ ] Password change
    * [ ] Password reset
- [ ] Upvotes, downvotes
- [x] Post tags
- [ ] Post images
- [ ] Comments
    * [ ] with images
- [ ] Some decent CSS
- [ ] Change the way that the posts are added (Celery?)
- [ ] Mod / admin tools
    * [ ] Post deletion feature, mods' PSAs, etc.
    * [ ] User / IP bans
- [x] Captcha
- [ ] REST API
- [ ] Search by post content / tags (ElasticSearch)

### Optional to-dos
- [ ] Page caching (Redis)
- [ ] Automatic spam removal (very long words, "aaaaaaaaaaa", ...)
- [ ] LaTeX
- [ ] Bots
- [ ] Mobile app (Flutter)

### 2020 to-dos
- [ ] Flash messages
- [x] PostgreSQL support
- [x] Add flake8 config file
- [ ] Use Docker for deployment
