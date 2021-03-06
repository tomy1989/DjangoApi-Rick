### Features

- Loading rick and morty characters from https://rickandmortyapi.com/
- Check between multiple character if they identical
- Get compare result to csv file
- Python django
- Vue.js
- Swagger https://app.swaggerhub.com/apis/tomy1989/RicknMorty/1.0.0

# Rick and Morty compare tool

![](https://www.pngall.com/wp-content/uploads/4/Rick-And-Morty-PNG-Clipart-180x180.png)

![](https://img.shields.io/badge/-tomy%20poliakov-orange) ![](https://img.shields.io/npm/v/npm) ![](https://img.shields.io/pypi/pyversions/django)


**Table of Contents**

+ [Features](#features)
- [Rick and Morty compare tool](#rick-and-morty-compare-tool)
- [Configure backend (Django)](#configure-backend--django)
- [Configure front (Vue)](#configure-front--vue)
      - [Project setup (install needed packages)](#project-setup--install-needed-packages)
      - [Compiles and hot-reloads for development](#compiles-and-hot-reloads-for-development)
      - [Compiles and minifies for production](#compiles-and-minifies-for-production)
      - [Lints and fixes files](#lints-and-fixes-files)
      - [Customize configuration](#customize-configuration)
    + [Some Images](#some-images)
    + [Some usefull information](#some-usefull-information)
    + [End](#end)


Configure backend (Django)
====
Backend files you can find in /APi

Make sure you have **python3.9+** installed
otherwise you will need to install Json1 [click](https://code.djangoproject.com/wiki/JSON1Extension) for more information


Python installation you can find [here](https://www.python.org/downloads/)


venv folder = enviroment that have been used
turn on enviroment when in folder API (not must)
```
venv\Scripts\activate
```
In API/api can find file req.txt

Make sure you have pip installed
can use this command to install all needed packages:
####Pip install from requirements file, code

req.txt = requirements.txt`$ pip install -r /path/to/requirements.txt`

 if you not have pip installed you can follow instuction [here](https://www.geeksforgeeks.org/how-to-install-pip-on-windows/) for installing

#### Run django server
```python
python manage.py runserver
```

Configure front (Vue)
====
Front files you can find in /FRONT

Make sure you have **Node.js** installed
otherwise you will need to install [click for install](https://nodejs.org/en/download/) 

Also make sure you have npm on machine if not you can find more information [here](https://docs.npmjs.com/cli/v7/configuring-npm/install#using-a-node-version-manager-to-install-node-js-and-npm)

Go to vue project /FRONT/Rick_Morty_Web
#### Project setup (install needed packages)
```
npm install
```
Congratulation everything should be installed ;)
#### Compiles and hot-reloads for development
```
npm run serve
```

#### Compiles and minifies for production
```
npm run build
```

#### Lints and fixes files
```
npm run lint
```

#### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).

### Some Images

![](https://i.imgur.com/rbm2Pct.png)

> Home page.

![](https://i.imgur.com/6hcnNiI.png)

> Multi search optional.

![](https://i.imgur.com/P1StDKh.png)

> Identical result popup.

![](https://i.imgur.com/iOJKRsz.png)

> Csv result.

![](https://i.imgur.com/a8lYUAh.png)

> Characters view.

![](https://i.imgur.com/KUwxf1Q.png)

> Characters card information.


### Some usefull information


for containerize the project with Docker i have this 2 documentation:
for django - https://docs.docker.com/samples/django/ and for vue - https://v2.vuejs.org/v2/cookbook/dockerize-vuejs-app.html but i was not sure if need to make one image or two, i read somewhere that the right way is 2 images, i was not sure how to make i would like to get know from you how i should make it work.

backend should be on port 8000 and front on 8080
if port already in use it can run on different ports when you run it the program show you on which port its run take a look at that to make sure everything right if backend run on diffrent port need to change it in EventService.js file to make front access to backend


### End