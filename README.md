# Assignment: Lunar Phase App

1) Please create a simple Django project with only two views: the login screen and a page displaying 
   the current lunar phase (accessible upon logging in).

2) The design of the pages and the information representation is unimportant and will not be assessed. 
   The "lunar phase" page can either be text-based or have some graphics in it, 
   the implementation is fully up to you.
   
3) Use Postgres as the DB backend. Choose an application server and, possibly, a web server of your liking 
   (Django built-in server, or Nginx/uwsgi, or whatever else).
   
4) The user should be able to log in with an email and password. Don't add the "forgot password" option 
   or any other features - just the "email/password" prompt and a "submit" button.
   
5) The whole web app (all it's services) should be containerized with Docker (and/or Compose).
   
6) Please create a repository on either Github, Gitlab or Bitbucket. It can be a public project or a private one.
   
7) Add a shell script run.sh to the repo. The script should launch the container(s) on the local system, 
   so that the website is accessible at 127.0.0.1:80 locally. 
   Assume that I have Docker and Compose installed on my Linux machine already.
   
8) I should already have a user account (with my email) when the system runs. 
   Please set some default password for my account.
   
9) The idea is that I should be able to clone the repository, simply run the shell script and observe the result 
   in the browser, without having to do any additional manipulations.
   

# Solution

This is a minimalistic possible solution, and it implements all the requirements.

### Running the App in Docker container

1) Clone the project repository.

2) Go to project root directory (the one that contains Dockerfile)

3) Run the script by issuing **./run.sh** command, 
or if you are running Docker as a power user, run **sudo ./run.sh** command
   
4) When you have done with the app, do not forget to stop application docker containers
```
    docker-compose down
```

5) Application super user account, will allow you to move forwards with the app.

- Login Email: admin@example.com

- Login Password: admin123

**Note:**

After running the script **run.sh** you will notice that there is a directory called _data
in the project directory. This is because we applied volume mapping in our
**docker-compose.yml** script. Specifically, 

```
services:
  db:
  ...
    volumes:
    - './_data/pgdata:/var/lib/postgresql/data/pgdata'
```

This was done in order to save initial migrations and create the super user account.
It was a necessary step in order to fulfill the requirement number 9) and let
the user to run the application directly from the shell script.
