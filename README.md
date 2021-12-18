# Django Profile manager

## Screenshots

#### Login
![](https://i.ibb.co/rcNRCKF/Capture3.png)

#### Profile
![](https://i.ibb.co/JCnCV9n/Capture1.png)

#### Email modification
![](https://i.ibb.co/MfJxxDk/Capture2.png)

## How to install

> git clone https://github.com/ayoubmn/django_mng.git

in project route

> docker compose up

an error may occur due to migration 

>docker-compose run web python3 ProfileManager/manage.py makemigrations --name first

then

>docker-compose run web python3 ProfileManager/manage.py migrate
 

