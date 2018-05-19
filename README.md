# ibm_project_dir
<a href="http://imgur.com/VUMzbMm"><img src="http://i.imgur.com/VUMzbMm.png" title="source: imgur.com" /></a>

# Project setup
1. Install Docker and Docker Compose.
2. Clone this repo to your computer and navigate to the <b>ibm_project_dir</b>.
3. Makemigrations: `sudo docker-compose run web python manage.py makemigrations`.
4. Migrate: `sudo docker-compose run web python manage.py migrate`.
5. Create Superuser: `sudo docker-compose run web python manage.py createsuperuser`.
6. Run tests: `sudo docker-compose run web python manage.py test`.
7. Runserver: `sudo docker-compose up`.
8. Access the application at: `http://127.0.0.1:8000/my-tasks/`.
9. Due Date format should be: `05/16/2018-22:00`
10. Access back-end at: `http://127.0.0.1:8000/admin/`.

