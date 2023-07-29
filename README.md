# SHOOD Blog

Live site available [here](https://shoodblog-abf09a84db44.herokuapp.com/). 


## Table of Contents
--------------------------------------

- [Description](#description)
- [User Goals](#user-goals)
- [Site Owner Goals](#site-owner-goals)
- [UX](#ux)
- [Agile Development](#agile-development)
- [Features](#features)
- [Testing](#testing)
- [Technologies](#technologies)
- [Deployment](#deployment)
- [Credits](#credits)

## Description
---------------------------------------

SHOOD Blog, the fourth project for the Code Institute Diploma in Software Development, is a website created using Django with Python, CSS/Bootstrap, and HTML. The site offers role-based permissions for users to access a central database, and users can create an account, book a service, read a blog which includes user authentication and full CRUD functionality for delivery services.

## User Goals
* To create a delivery service booking
* To be able to view edit and cancel bookings
* To view a blog, comment and like posts
* To contact the site owner by sending messages

## Site Owner Goals
* To provide a solution to allow users to book a table online
* To attract more business with a well crafted site
* Provide a modern application with an easy navigation
* Fully responsive and accessible


## UX
*  The blog about SHOOD - the search and comparison engine for grocery shopping and delivery. The blog is dedicated to providing users with all the information they need to know about SHOOD, including how it works, its features and benefits, and how it can help simplify grocery shopping and delivery experience.

### The Sites Ideal User

* The ideal usage of the SHOOD blog is for individuals who are interested in simplifying their grocery shopping and delivery experience. The blog provides valuable information on how to use SHOOD's search and comparison engine to find the best deals and place simultaneous orders from different stores.

## Agile Development

The plan for this project was carried out using the Agile Methodology in Github. User Stories were created using issues on git hub. Each user story explicitly explains the purpose of the issues. Each user story is segmented into acceptance criteria and tasks.


### User Stories
* As a User I can navigate across the site so that I can move to each feature of the site easily (Must have)
* As a Site Owner I can provide a contact us page so that users can get in touch with my business (Must have)
* As a User I can create a booking by selecting a date and time so that I can reserve a delivary service (Must have)
* As a User I can update my booking so that I can choose another available time and date (Must have)
* As a User I can delete my booking so that I can cancel my booking (Must have)
* As a user I can view my booking so that I can remind myself of the date and time I have booked (Must have)
* As a User I am notified so that I know my action of creation, edit, or deletion of a booking has been successful (Must have)
* As a User I can register as prompted so that I can make a booking if I wish book a service (Must have)
* As a User I can register to create an account so that my details are stored for faster booking in future and I can comment and like blog posts (Must have)
* As a user I can login so that I can book a delivery service (Must have)
* As a user I can see my login status so that I know if I am logged in or not (Must have)
* As a User I can view the site's blog so that I can learn additional information and read articles
* As a User I can view blog posts page by page so that I can browse without seeing an overloaded page
* As a User, I can view a list of posts to select one to read
* As a User, I can click on a post to read the full text
* As a User, I can view the number of likes on each post to see which is the most popular
* As a User, I can view comments on an individual post to read the conversation

## Admin / Authorised User
* As an Admin / Authorised User I can log in so that I can access the back end of the site (Must have)
* As an Admin / Authorised User I can manually add a booking so that I can book a delivery service
* As an Admin / Authorised User I can accept or reject bookings
* As an Admin, I can create, read, update, and delete posts to manage my blog content
* As an Admin, I can create draft posts to finish writing the content later
* As an Admin, I can approve or disapprove comments to filter out objectionable comments

Live to the project in Github [here](https://github.com/users/mjrosi/projects/1/views/1).


## Features

#### Home page
* The Front page asks a the visitor of the site to log into view the posts, book a delivery service and contact. 
* If already logged in then it displays My bookings which allows the user to see all their bookings.

<details><summary>See feature images</summary>

![Home Page](/media/images/Screenshot_home_page.png)
</details>

#### Navigation Bar
* The main navigation bar appears at the top of the page, clearly displaying the main navigational links users would require. For sign in and sign up and log out for signed in users.

<details><summary>See feature images</summary>

![Nav Bar](/media/images/Screenshot_navbar_login.png)
![Nav Bar](/media/images/Screenshot_navbar_loggedin.png)
</details>

#### Footer
* A common footer is utilised throughout the site with the links to other SHOOD websites which are my other portfolio projects, about SHOOD Blog and link to social medias.
<details><summary>See feature images</summary>

![footer](/media/images/footer.png)
</details>

#### View post detail
* The user can read the selected blog post
* Registerd user can comment on a blog post
* Registerd user can like a blog post

<details><summary>See feature images</summary>

![Example Post Card](/media/images/postview.png)
</details>

#### Sign up
* Users can sign up in order to like or comment any posts.

<details><summary>See feature images</summary>

![Sign up](/media/images/signup.png)
</details>

#### Sign in
* Users can sign in to their accounts.

<details><summary>See feature images</summary>

![Sign up](/media/images/signin.png)
</details>

#### Book
* Allows the user to book a delivery service using the booking form
* Messages are displayed if the data is not valid such as phone number lenght is too short and the email address is not a valid format

<details><summary>See feature images</summary>

![Book](/media/images/Screenshot_book.png)
![Book](/media/images/Screenshot_book_loggedin.png)
</details>

#### My Bookings
* Allows the users to see all their bookings in a paginated layout, 4 per page

* Status of the booking is displayed, awaiting confirmation and when approved will then change to confirmed status for the users

<details><summary>See feature images</summary>

![My Bookings](/media/images/Screenshot_mybookings.png)
</details>

#### Edit Booking
* Allows the users to edit their bookings

<details><summary>See feature images</summary>

![Edit Bookings](/media/images/Screenshot_editbooking.png)
</details>

#### Cancel Booking
* Allows the users to cancel their bookings
<details><summary>See feature images</summary>

![Cancel Bookings](/media/images/Screenshot_cancelbooking.png)
</details>


#### Contact Us
* Registered users can send messages the site admin?owner via the message form

<details><summary>See feature images</summary>

![Contact Us](/media/images/Screenshot_contactus_loggedin.png)
![Contact Us](/media/images/Screenshot_contactus.png)
</details>

#### 

## Testing

### Testing Strategy
I utilised a manual testing strategy for the development of the site.

#### Testing Overview

Testing was divided into different sections to ensure everything was tested individually with test cases developed for each area.


#### Validator Testing
All code files were validated using suitable validators for the specific language.
HTML & CSS code passed the validation.
There is no JavaScript code to be validated.
Python meets with Pep8 standards except 
* There are some errors regarding line too long- by one character

#### Python Testing
All Custom Python code was manually tested multiple times during and after development.


## Testing User Stories
------

* #### As a User I can navigate across the site so that I can move to each feature of the site easily

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
| Click on the 'Home' link in the navigation bar | Homepage will load| Works as expected |
| Click on the 'Sign Up' link in the navigation bar | Sign up page will load| Works as expected |
| Click on the 'Log in' link in the navigation bar | Login page will load| Works as expected |
| Click on the 'Book' link in the navigation bar | Reservations page will load| Works as expected |
| Click on the 'Contact Us' link in the navigation bar | Contact us page will load| Works as expected |
| Click on the 'My Bookings' link in the navigation bar | Booking list page will load| Works as expected |
| Click on the 'Log out' link in the navigation bar | Logout page will load| Works as expected |


* #### As a Site Owner I can provide a contact us page so that users can get in touch with my business

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
| Click on the 'Contact Us' link in the navigation bar | Contact us page will load| Works as expected |


* #### As a User I can create a booking by selecting a date and time so that I can reserve a delivery service

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
| Click on the 'Book' link in the navigation bar | Find the booking form on the reservations page | Works as expected |


* #### As a User I can update my booking so that I can choose another available time and date

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
| From 'My Bookings' click 'Edit' on booking to be edited| Find the edit booking form loaded  | Works as expected |


* #### As a User I can delete my booking so that I can cancel my table reservation

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
| From 'My Bookings' click 'Cancel' on booking to be cancelled| Find the cancel booking prompt loaded  | Works as expected |


* #### As a user I can view my booking so that I can remind myself of the date and time I have booked

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
| Click on the 'My Bookings' link in the navigation bar | Booking list will display all bookings made| Works as expected |


* #### As an Admin / Authorised User I can log in so that I can access the back end of the site

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
| Visit the [admin page](https://shoodblog-abf09a84db44.herokuapp.com/admin/login/?next=/admin/) | Enter admin login credentials, gain access to back end | Works as expected |


* #### As an Admin / Authorised User I can manually add a booking so that I can book a delivery service

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
| Visit the [admin page](https://shoodblog-abf09a84db44.herokuapp.com/admin/login/?next=/admin/) | Enter admin login credentials, gain access to back end | Works as expected |
| Click on the Bookings button the the left panel, select add booking | Booking form is displayed | Works as expected |


* #### As an Admin / Authorised User I can accept or reject bookings

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
| Visit the [admin page](https://shoodblog-abf09a84db44.herokuapp.com/admin/login/?next=/admin/) | Enter admin login credentials, gain access to back end | Works as expected |
| Click on the Bookings button the the left panel, select a booking id | Booking info is displayed | Works as expected |
| Click Status dropdown | Find different booking status to select and save | Works as expected |


* #### As a User I can I am notified so that I know my action of creation, edit, or deletion of a booking has been successful

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
| From the reservations page, create a booking | A message will be displayed upon completion, Javascript makes it disappear after 3 seconds | Works as expected |
| From the bookings list page, edit a booking | A message will be displayed upon completion, Javascript makes it disappear after 3 seconds | Works as expected |
| From the bookings list page, cancel a booking | A message will be displayed upon completion, Javascript makes it disappear after 3 seconds | Works as expected |


* #### As a User I can register as prompted so that I can make a booking if I wish boo a service

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
| Click on the 'Sign up' link in the navigation bar | Register an account to allow bookings to be made | Works as expected |


* #### As a User I can register to create an account so that my details are stored for faster booking in future

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
| See test 15 | See test 15 | Works as expected |
| Click on the 'Book' link in the navigation bar | Find the booking form with user email inserted automatically | Works as expected |


* #### As a user I can login so that I can book a delivery service

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
| Click on the 'Login' link in the navigation bar | Log in, user now able to book a table | Works as expected |
| Click on the 'Book' link in the navigation bar | Find the booking form on the reservations page | Works as expected |


* #### As a user I can see my login status so that I know if I am logged in or not

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
| While logged in, view navigation bar | Log out button should be visible | Works as expected |




## Technologies

* Python
* Django
    * Django was used as the main python framework in the development of this project.
* Heroku
    * Was used as the cloud based platform to deploy the site on.
* Heroku PostgreSQL
    * Heroku PostgreSQL was used as the database for this project during development and in production.
* Bootstrap 5
    * Bootstrap was used for general layout and spacing requirements for the site.
* Font Awesome
    * Was used for access to the Navvar bars icon for the navigation bar menu.
* CSS
    * CSS was written for a large number of areas on the site to implement custom styling and escape a bootstrap look and feel to the site.
* HTML
    * HTML was used as the base language for the templates created for the site.

#### Packages Used

* Gitpod was used to develop the site
* Git was utilised for version control and transferring files between the code editor and the repository
* GitHub was utilised for storing the files for this project

#### Resources Used

* The Django and Bootstrap documentation was used extensively during development of this project
* The Code Institute reference material was used as a general reference for things that I had previously done during the course.
* Other Resourses we used to help debug and to learn new features not yet covered in the course - Youtube, StackOverflow, GeekForGeeks and Slack.


[Back to the Top](#table-of-contents)

----

## Deployment

The site was deployed via Heroku, and the live link can be found here - [Expensed](https://dashboard.heroku.com/apps/expensed)

### Project Deployment

To deploy the project through Heroku I followed these steps:
* Sign up / Log in to [Heroku](https://www.heroku.com/)
* From the main Heroku Dashboard page select 'New' and then 'Create New App'
* Give the project a name - I entered The-Pantry and select a suitable region, then select create app. The name for the app must be unique.
* This will create the app within Heroku and bring you to the deploy tab. From the submenu at the top, navigate to the resources tab.
* Add the database to the app, in the add-ons section search for 'Heroku Postgres', select the package that appears and add 'Heroku Postgres' as the database
* Navigate to the setting tab, within the config vars section copy the DATABASE_URL to the clipboard for use in the Django configuration.
* Within the django app repository create a new file called env.py - within this file import the os library and set the environment variable for the DATABASE_URL pasting in the address copied from Heroku. The line should appear as os.environ["DATABASE_URL"]= "Paste the link in here"
* Add a secret key to the app using os.environ["SECRET_KEY"] = "your secret key goes here"
* Add the secret key just created to the Heroku Config Vars as SECRET_KEY for the KEY value and the secret key value you created as the VALUE
* In the settings.py file within the django app, import Path from pathlib, import os and import dj_database_url
* insert the line if os.path.isfile("env.py"): import env
* remove the insecure secret key that django has in the settings file by default and replace it with SECRET_KEY = os.environ.get('SECRET_KEY')
* replace the databases section with DATABASES = { 'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))} ensure the correct indentation for python is used.
* In the terminal migrate the models over to the new database connection
* Navigate in a browser to cloudinary, log in, or create an account and log in. 
* From the dashboard - copy the CLOUDINARY_URL to the clipboard
* in the env.py file created earlier - add os.environ["CLOUDINARY_URL"] = "paste in the Url copied to the clipboard here"
* In Heroku, add the CLOUDINARY_URL and value copied to the clipboard to the config vars
* Also add the KEY - DISABLE_COLLECTSTATIC with the Value - 1 to the config vars
* this key value pair must be removed prior to final deployment
* Add the cloudinary libraries to the list of installed apps, the order they are inserted is important, 'cloudinary_storage' goes above 'django.contrib.staitcfiles' and 'cloudinary' goes below it.
* in the Settings.py file - add the STATIC files settings - the url, storage path, directory path, root path, media url and default file storage path.
* Link the file to the templates directory in Heroku TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')
* Change the templates directory to TEMPLATES_DIR - 'DIRS': [TEMPLATES_DIR]
* Add Heroku to the ALLOWED_HOSTS list the format will be the app name given in Heroku when creating the app followed by .herokuapp.com
* In your code editor, create three new top level folders, media, static, templates
* Create a new file on the top level directory - Procfile
* Within the Procfile add the code - web: guincorn PROJECT_NAME.wsgi
* In the terminal, add the changed files, commit and push to GitHub
* In Heroku, navigate to the deployment tab and deploy the branch manually - watch the build logs for any errors.
* Heroku will now build the app for you. Once it has completed the build process you will see a 'Your App Was Successfully Deployed' message and a link to the app to visit the live site.


[Back to the Top](#table-of-contents)

-----

## Credits

All Images used across the site were sourced from either freepik.com, freely available images.
The Navbar bars Icon was taken from font awesome.

I relied heavily on the Code institute course work, particularly the I Think Therefore I Blog walk through projects.

[Back to the Top](#table-of-contents)
