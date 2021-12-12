# kirbyonweb.dev website

## About

This repository contains the source code for my portfolio website. I made this website using the django framework. 


## Features

Generally the main porpose of the website is to show a public portfolio. The website should demonstrate my different web development skills. This will be in the form of demo apps.

### Blog
Other than being a regular blog, this is probably the largest and long-running demo. It has the following basic features

- each blog article will have a body and a separate preview
- blog articles can be categorized into one or many category tags. blogs in a category can be listed.
- each blog article has a thumbnail image


## installation

Installation will require internet connection since the applications are downloaded.

This site runs on python3 and uses Django. It uses a separate uploads directory that is served statically by a web server.

By default Django uses sqlite3 as a default database. This site uses postgresql, it should not be a big issue to use a different database ( except for specific apps )

### Virtual Environment
using a virtual environment will isolate the application from the rest of the host. There maybe different ways to install the virtualenv in different distribuions. In centos stream it is installed like this ( requires root privilege )
```
# yum install virtualenv
```

create your working directory and create the virtual environment there ( as your normal less-privileged user )
```
$ mkdir /your/working/directory
$ cd /your/working/directory
```
setup your virtual environment binaries. we will name the directory `django-env`
```
$ virtualenv django-env
```

this will install the basic apps needed to run a python application in isolation. the two important binaries that will be used is python and pip . It will output something like this
```
Using base prefix '/usr'
New python executable in /your/working/directory/django-env/bin/python3.6
Also creating executable in /your/working/directory/django-env/bin/python
Installing setuptools, pip, wheel...done.
```

activate the virtual environment. Activating the virtual environment is done everytime you will do anything with the application since this is the environemnt where is will run. Take note of this command
```bash
$ source django-env/bin/activate
```

your command promt should look something like this. take note of the (django-env)
```
(django-env) [user@host directory]$ 
```
from here you can now install all needed applications

### Installing the Django Framework

install Django via pip
```
$ pip install django
```
it should output something like this
```
Collecting django
  Downloading Django-3.2.10-py3-none-any.whl (7.9 MB)
     |████████████████████████████████| 7.9 MB 8.2 MB/s            
Collecting sqlparse>=0.2.2
  Using cached sqlparse-0.4.2-py3-none-any.whl (42 kB)
Collecting pytz
  Using cached pytz-2021.3-py2.py3-none-any.whl (503 kB)
Collecting asgiref<4,>=3.3.2
  Using cached asgiref-3.4.1-py3-none-any.whl (25 kB)
Collecting typing-extensions
  Downloading typing_extensions-4.0.1-py3-none-any.whl (22 kB)
Installing collected packages: typing-extensions, sqlparse, pytz, asgiref, django
Successfully installed asgiref-3.4.1 django-3.2.10 pytz-2021.3 sqlparse-0.4.2 typing-extensions-4.0.1
```

Since were installing the required libraries, we might as well install the libraries required by the website

- gunicorn - used to serve the python application in production ( read more in gunicorn )
- Pillow - a fork of Python Imaging Library. this is used in image uploads
- psycopg2 - postgresql database adapter



Since we are using `psycopg2` we should install `libpq-devel` library and `gcc` in the system in order to compile the library
```
# yum search libpq-devel
# yum install gcc
```
install `psycopg2-binary`
```
pip install psycopg2-binary
```
Output should look like this
```
Collecting psycopg2-binary
  Downloading psycopg2_binary-2.9.2-cp36-cp36m-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (3.0 MB)
     |████████████████████████████████| 3.0 MB 773 kB/s            
Installing collected packages: psycopg2-binary
Successfully installed psycopg2-binary-2.9.2
```

finally instlal the libraries
```
$ pip install gunicorn Pillow psycopg2
```
it will output something like this
```
Collecting gunicorn
  Using cached gunicorn-20.1.0-py3-none-any.whl (79 kB)
Collecting Pillow
  Using cached Pillow-8.4.0-cp36-cp36m-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (3.1 MB)
Collecting psycopg2
  Using cached psycopg2-2.9.2.tar.gz (380 kB)
  Preparing metadata (setup.py) ... done
Requirement already satisfied: setuptools>=3.0 in ./django-env/lib/python3.6/site-packages (from gunicorn) (59.5.0)
Building wheels for collected packages: psycopg2
  Building wheel for psycopg2 (setup.py) ... done
  Created wheel for psycopg2: filename=psycopg2-2.9.2-cp36-cp36m-linux_x86_64.whl size=519715 sha256=0000000000cbf508898bbb24769053000829a1fd9df5df203027ec0000000000
  Stored in directory: /home/XXXXX/.cache/pip/wheels/cc/0e/26/00000000006b5c907dcc92678f878745c6d0fd650000000000
Successfully built psycopg2
Installing collected packages: psycopg2, Pillow, gunicorn
Successfully installed Pillow-8.4.0 gunicorn-20.1.0 psycopg2-2.9.2
```

### create the django app
```bash
$ django-admin startproject blogsite
```
to deploy the files in this repository into the blogsite, we will nedd install `wget` and `unzip` since it is not installed by default

```bash
# yum install wget unzip
```
now go to the  blogsite and download the project

```bash
$ cd blogsite
$ wget https://github.com/kirbykirbydev/kirby-agudelo-portfolio-site/archive/refs/heads/master.zip
$ unzip master.zip
```

this will create a subdirectory `kirby-agudelo-portfolio-site-master`. go to the directory and copy everything back to the upper directory. then delete this later.

```bash
$ cd kirby-agudelo-portfolio-site-master
$ cp -rf * ../.
$ cd ..
```

delete source files
```bash
$ rm -rf kirby-agudelo-portfolio-site-master kirby-agudelo-portfolio-site-master.zip
```

**system variables**

the aplication loads some configuration via system envoronment variables. these can be executed in the current bash environment
```bash
export blog_debug_mode=True
export blog_secret_key=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
export blog_db_engine=django.db.backends.postgresql_psycopg2
export blog_db_host=XXXXXXXXX
export blog_db_user=XXXXXXXXXXX
export blog_db_name=XXXXXXXXXXX
export blog_db_pass=XXXXXXXXXXX
export blog_media_root=XXXXXXXXXXXXXXXXXXXXXXXXXX
export blog_static_root=XXXXXXXXXXXXXXXXXX
export blog_static_url=XXXXXXXXXXXXXXXXXXXXX
```

there are many ways to load load configuration variables to the systsm but the shortest way is to just execute them via bash.

these commands can be saved in an executable bash script ( for example `blog_config.sh`) 
and then run the script using the source command ( to load the variables directly to the current environment
```bash
$ source blog_config.sh
```

finally test if the site will run

```bash
$ python manage.py runserver 127.0.0.1:8000
```

in production mode `gunicorn` is used to run the site. i have created a script to execute this

```bash
#!/bin/bash


WORKING_DIR=/your/working/directory
LOG_FILE=$WORKING_DIR/blogsite.log
PID_FILE=$WORKING_DIR/gunicorn_blogsite.pid

source ./load_blogsite_cfg.sh

cd $WORKING_DIR
source django-env/bin/activate
cd blogsite
gunicorn blogsite.wsgi:application --bind 0.0.0.0:8000 --daemon --log-file=$LOG_FILE --pid=$PID_FILE
```

**configuring nginx for proxy and static files**

configuring proxy and static files
currently the website is usinig nginx as the proxy web server but it should not matter which proxy server is used.

config file /etc/nginx/nginx.conf
in nginx the only important configuration so far is what port to listen to and what is the server name

```

http {

  # ...
  # other configs here
  # ...
  server {

        listen       80;
        listen       [::]:80;
        server_name  www.kirbyonweb.dev ;

        # Load configuration files for the default server block.
        include /etc/nginx/default.d/*.conf;

        error_page 404 /404.html;
            location = /40x.html {
        }

        error_page 500 502 503 504 /50x.html;
            location = /50x.html {
        }
  }

  # ...
  # other configs here
  # ...

}
```


and then the specific configuration in /etc/nginx/default.d/blogsite.conf


```
root /where/your/static/files/are;

# all url paths that start with /static/ are forwarded to load the files in the root
location ~ ^/static/ {
    rewrite ^/static/(.+)$ /$1 last;
}

# the blog site starts with /blog
location /blog {
    proxy_pass http://127.0.0.1:8000 ;

}

#the website home has no url path
location ~ ^/$ {
    proxy_pass http://127.0.0.1:8000 ;
}
```
