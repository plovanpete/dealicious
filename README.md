# Dealicious
Find Deals where ever you go!


# Learning:

## How to create a Server and App with Django:

Django is a website creator that uses Python and can implement HTML code to its websites!
To get started, we must download Django, and then afterwards, create a folder for the Django website.
Afterwards, type in 'django-admin startproject (Insert Name Here)' in the command prompt to see the created framework of the project.
Then, navigate inside that folder that was created, and use the command, "python manage.py runserver" to start up a local server!

Use localhost:(numberhere) to access to your local server. (Ctrl + C ends the server!)

To create an app, use the command "python manage.py startapp (Insert Name Here)" to create an app!

## How to allow your HTML Website onto Django!
Now that we created an app, we may begin with making a website!

This is needed, so you must create a directory for your html either by using the cmd "mkdir (Insert Name Here)" or adding a new folder! (inside the apps folder)

Afterwards, create an html file, with once again, either by using the cmd "echo (Insert message here) > (Insert Name Here).html to create an html file, or you could just completely create and convert a file by using an IDE to create one for you!

Now that your HTML file has been created, one must go back to the settings.py inside your inner folder of your main project folder. (Not by Command Prompt, open the .py file!)

1. Add a import os under the line "from pathlib import Path" this allows specification of paths in the templates.
2. Go down till you see TEMPLATES with a blank DIRS list, this is what we are going to need!
3. Inside the DIRS[] type os.path.join(BASE_DIR, (AppFolder/HTMLFolder))

Now that's made, let's get started on how to respond the server with a webpage!

## How to allow Users to "View" the request from the server!
1. Go to your views.py located in your folder with admin.py, apps.py, models.py, etc.
2. Create a simple function, like def myview(insertYourVarNameHere) and return a render(request, (Your HTML file in Strings Here!))
We DO NOT need to specify the path since we already did it in the previous steps!

Now that we've set the views that can allow the User to access it (not quite), we may begin the next step (if you want to navigate to another route), which is creating a Route to the server!

## How to create a route in Django!
1. Make a copy of views and rename it to urls(recommended) [Located inside the folder with apps.py]
2. insert a line with "from django.urls import path" this allows us to specify the route!
3. insert a line under that with "from .import views" to allow our recent views.py to this new python file!
4. This is MOST IMPORTANT! make a list, urlpatterns and put the path() function inside it, like this: urlpatterns = [path()]
5. inside the path function, you can choose the route like path('myview/', views.myview)

## How to create a route in Django, Part 2!
1. Yay, we finished making the urls.py! But wait! We must now go back to the other urls.py inside the folder with asgi.py and wsgi.py!
2. On the line, "from django.urls import path" add the include function by adding a comma and include, like so: "from django.urls import path, include"
3. Add a path function, with your route, path('app/', include('app.urls')), to add your site to the urlpatterns!
4. We made a website, YIPEEE!!!
5. run the server and check up on your local server, localhost:(yournumber)/app/views (this is a template, not really real!)
6. you may choose to get rid of the /views by going to your urls.py located in your app folder and leaving an empty string instead of myview/


## Editing your webpage, with CSS style and HTML structure!
1. Go back to your folder with your apps, and 
