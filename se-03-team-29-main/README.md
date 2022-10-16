## SE-Sprint01-Team29

# README file for Corona Archive Web Service

### Contributors

Sprint 1

- Denisa Checiu
- Zineb Laouzi

## Project Description

Corona Archive is a web service for tracking, displaying, evaluating, and
archiving of the Corona infections in a particular location. The web service will be accessible to
four types of users:

- Visitors: Citizens or visitors can use the web service to indicate whether they have
  entered a particular place and when they have done so.
- Places: Places which are frequently visited by people, such as clubs, pubs, restaurants,
  cinemas etc. can use the web service to get access to a QR code, which uniquely
  identifies their place. Citizens can scan this QR code to record their presence at that
  place.
- Agency: The agency or the evaluation client can use the web service to generate coronarelated reports by collecting data from the database.
- Hospital: Hospitals can use the web service to mark people as infected and track anyone
  else that has been in contact with an infected person.

### Tools used

- HTML
- CSS
- JavaScript
- MySQL
- Flask
- Python3

## File Structure

```
\--se-sprint03-team29
    \-- app
        \-- models
            \--             # model python files
        \-- routes
            \--             # route python files
        \-- static
            \-- css
                \--         # css files
            \-- images
            \-- js
        \-- templates
            \--             # all HTML files
        \-- utils
    \-- config
        -- db.yaml
    \-- sql
        -- setup.sql
    \-- tests
        \-- unittests
            -- app_factory.py
            -- tests.py
    -- Project Design.pdf
    -- README.md
    -- requirements.txt
    -- run.py
```

## Getting started

The following instructions will enable you to get a copy of the project we created, up and running on your local machine for development and testing purposes. Proceed further to see which software you need to instal and how to do it.

## Prerequisites

- Mysql (both client and server)
  - If libbysqlclient-dev is missing you can install it with
  ```
      sudo apt-get install python-dev default-libmysqlclient-dev libssl-dev
  ```
- Virtualenv
- Latest version of pip or pip3 (important to get latest required packages)

on linux (if your are using python 3):
sudo pip3 install virtualenv

## Installation Guide

```
#clone the repo

    $ cd se-02-team-28

    $ virtuaenv env

    $ source env/bin/activate

    $ pip3 install -r requirements.txt

    $ cd sql

    $ mysql -u {ENTER USERNAME WITH DATABASE PRIVELEGES} -p

    # after starting mysql

    mysql> source setup.sql
    mysql> exit

    # update db.yaml in the config folder with your own username and  password, if necessary you can also change the secret key used for bcrypt

    $ python3 run.py
    # for further instructions such as port selection or lan wide availability use the command below
    # FLASK_APP=run.py FLASK_ENV=development FLASK_RUN_CERT=adhoc flask run  --host=0.0.0.0 --port={DESIRED PORT NUMBER}
```

## Run tests

```
    # from the root directory of the project
    $ python3 -m unittest

```

```
## Sprint 1 Changes Done

✅ Detailed README file, regarding project description, pre-requisities and installation

✅  Provided requirments (rqt.txt) file

✅  Python script which tests the functionality of our web service (api.py)

✅ SQL database containing tables for the four types of users (Visitors, Places, Agents, Hospitals), plus one which will help the agents (VisitorsToPlaces)

✅ Landing page, which lets you choose which one of the 4 types of users you represent

✅ Sign-up and log-in page for visitors

✅ Sign-up and log-in page for places

✅ Log-in page for agents

✅ Log-in page for hospitals

✅ Page for visitors (accessible after they log-in) to sign the QR code of a place, and have their time there recorded and displayed at the end

✅ Page for place-owners (accessible after they log-in) to have a QR code generated for their bussiness and the possibility to download the QR code

✅ Page for hospital officials (accessible after they log-in) to visualize the entire list of visitors registered in our database (in the form of a python script which generates a html page containing the table of full visitors registered in the database)

We started the project from scratch, closely following the Project Design documentation provided. We were able to created full frontend and (partial) backend integration. At this stage, someone can access the web service through the landing page, where they choose which type of user they are, and log-in to their account(or sign-up if allowed or necessary). Based on which type of user they are, they will be able to: scan the QR code of a place (visitors), get a unique QR code for their bussiness (place owners) or visualize certain lists of users and places (agents, hospital officials).


##sprint 2 changes made:
###contributors:
-Sultan Sadiq Husain Siddiqui
-Saad El Jadouri

### Errors and Problems that we encountered and solved:

-1.Upon following the instructions rcieved and running the program through python3  app.py, we got an ERROR 404:URL NOT FOUND error in our localhost.
 - upon careful examination of the code, we found out that this was because of the lack of an app route.
 -the user had to manually enter the name of the HTML page that they wanted to access in the URL to go to the app.
  Realizing that for a user, who doesnot have the access to the source code, will not
  know the name of any HTML pages and the website is technically useless to him/her.
  solution implemented:
  We added an approute to solve this issue, allowing users to acess the website without having to know the name sof any html pages.

 2. SQL error:Acess Denied 'Root@Localhost'
 -This was another error that we faced. Due to this error we could not do anything related to the database of the project. we could not login nor
  could we sign in.
  solution Implemented:
  They had used root, which provides unlimited access and hence is not allowed by  mysql servers. TO solve this we had to reinstall the mysql
  server at our local machine and we created and centered a new user and used that user credintials, granted the new user all accesses to solve the
  problem.

3.Hrefs not working:ERROR
 - The Visitor login and signup pages had links that would allow a user to go from one page to the another, however they were not working.
  solution Implemented:
   realized that this was because of a problems with the app routs. We rewrote the app routes for both this pages and also re did the
  linking to make it work.

 4. SQL Table Errors:
 We could not use the signup visitors page and the sign up place pages due to sql errors, and mismatches.
 solution Implemented:
  rewrote- the sql code for two tables: visitors and places and rewrote the central queries for these two tables in the app.py file to make
 them work.

5.Queries not working:
- Almost all the queries in the app routes had one problem or the otehr, from  wrong table names, getting wrong inputs with mismatching
names from the forms, wrong column names and error:Not allowed for methods.
Solution Implemented:
- we rewrote the queries and made sure to view the tables and columns before writing the queries.

6. Qr code error:
-The qr code was not being generated for the place owner, eventhought the javascript file  was present.
solution Implemented:
-Realized this was due to text wrap errors, where the javascript file linking was being understtod as a app route. Introduced text wrapping to fix this
 error.


NOTE:PLEASE SIGN IN THE SQL USING THE GIVEN CREDIANTALS FOR THE BACKEND TO WORK PROPERLY.YOU CAN CHANGE THJE USERNAME AND PASSWORD FROM THE APP.PY
      BUT MAY REQUIRE YOUR TO REINSTALL YOUR MYSQL.

 ##Furthur Additions made:

✅ Implemented a Central homepage, through which a user can choose to login or signup as a visitor, login as an agent, sign-in as a hospital staff,          regsiter a place or login in to his place account. we also used an API to fetch current corona numbers in germany and displayed it in the homepage to
   make the website more informative.
✅  Added the Hospital Landing page, which was not provided.
✅  Implemented the idea of sessions for agents and Hospitals. Using the idea of sessions we implemented these things:
    - If a agent is already logged in and he tries to login, he is directly taken to the agent page and not the login page.
    -If a hospital is already logged in and tries to login again the hospital admisntrator is taken to the hospital page.
    - If a agent is not in the session(basically not logged in) and tries to register a hospital he is taken to the agent login page. Through
      this we esnure that only an agent can register a hospital.
    - Understanding that an agent and a hospital have important taks, and a random person can abuse their power, both the agent and the hospital
      can now logout of the session through their respective pages.
✅  Added a hospital registration page, through which an agent can register a hospital.
✅ Added an Agent homepage, through which an agent after logging in can choose to register a hospital, search through the database for visitors or
   logout.
✅ Added the visitor search page through which the agent can search for visitors using their username and if found details would be displayed.
✅ constructed the sql query and the approute  for the agent to search the database for Visitors.
✅ added a link to go back to the homepage from every page to make the website more user friendly.
✅ Renamed the name of the sql file making it shorter and easier to use.
✅ added a test file test_sprint_02_29.py for the unit testing of the code.


p.s:DOnt forget to use the provided credientials for the mwsql login.


To conclude, we recieved a simple website with simple login HTML pages from the first sprint. We for this sprint, fixed the backend, and added furthur frontend components to give the website a more complete strucutre. Almost 70% of the projects is now finished with only some work reuqired for the visitor qr scanning, hospitals choosing who in positive and who is not for the other sprints.


Sprint 03

- Minyahel Haile
- Usman Fizza

Sprint 03 changes made

🚩 Errors encountered and fixed

The app we received lacked structure, a good ui and functionality among other things so most of our energy was spent on trying to figure out a way to update things if possible, in the end most of the code was not reusable.

1. Packages that were not specified in the requirements were used and the program wouldn't run off the bat
    - Identified the required packages and removed unnecessary ones

2. Only 1 button out of 6 on the homepage worked, with the others leading to invalid routes
    - Identified the proper routes and the proper hrefs and updated the buttons and links

3. Login routes didn't specify who they were for and a generic "user" name was given
    - Identified the broken routes and gave the necessary fixes

4. Signup routes didn't specify who they were for
    - Identified for whom the routes were and renamed them

5. There were routes that made no sense such as the already user route which is not connected to anything else
    - Deleted these unnecesary routes

6. All of the login and signup logic for visitor and place was different from what was given in the specification
    - Updated the required fields for visitor and place

7. Project had two flask applications where one was in the tests foler
    - Removed the unnecessary app

8. Encountered multiple python files that were in no way connected to each other
    - Removed the unnecessary files

9. Many routes didn't work as they either had improper naming or something else missing

10. There was no trace of error handling

11. The UI was unintuitive and lacked structure
    - designed a whole new UI

🔵 All in all, the app was very hard to work with with all the code in a single file where the route naming and function naming made it impossible to know what was happening.

The Additions we made to the project

✅ Organized the code into respective packages and modules for easier file structure understanding
✅ Renamed most of the files to something that was easy to understand
✅ Separated the routes into respective modules where each module contained only files that were related to a specific user type
✅ Encapsulated all database operations under respective user type classes with class methods for required interfaces
✅ Added error handling to all database interactions for a more robust backend
✅ Renamed routes to something that was easy to understand while at the same time filling gaps to which routes were missing from the original project
✅ Updated the database structure to have more suitable datatypes for multiple fields
✅ Updated the database to improve the types and logic of the device id and qr code for visitor and place, also updated the logic of VisitorsToPlaces table to have a primary key made from the unique setting qr code and device id
✅ Implemented device_id and qr code logic with randomly generated uuid values
✅ Implemented the scanning in logic with the corresponding dynamic route
✅ Implemented route protection on all routes
✅ Implemented error handling on all routes
✅ Implemented json based interaction between endpoints and the front end for easy to understand communication between the backend and the frontend
✅ Implemented a whole new UI with better styling and functionality
✅ Implemented input checking for logging and registration forms
✅ Implemented visitor lookup page for agent with pop-up modals for infected visitors to check place history
✅ Implemented place lookup page for agent with pop-up modals for place visitor history checking
✅ Implemented hospital registration page for agent that checks for a unique username and generates a password
✅ Implemented filtering buttons for agent that show either infected or all visitors
✅ Implemented visitor lookup page for hospital with pop-up modals for setting the infection status of a visitor
✅ Implemented visitor dashboard that shows the checkin history, the checked in places and the visitor information
✅ Implemented a checkin page where a visitor scans to check into a place
✅ Implemented a timer that times how long a visitor has been at a place
✅ Implemented safe guards that prevent a visitor from checking into two places at the same time
✅ Implemented a logout account feature for visitor
✅ Implemented a dashboard for place owner displaying the qr
✅ Implemented qr downloading feature for a place
✅ Implemented logout for place
✅ Implemented responsive layouts for visitor and place pages for mobile devices
✅ Greatly reduced the need for many different html files by utilizing javascript and ajax for providing a single page application feel
✅ Wrote unit tests for testing route endpoints
✅ Wrote manual tests for tests that test the dom elements

Notable Issues and Tips
- Agent Account
        Username: agent1
        Password: password
- Hospital Account
        Username: hospital1
        Password: password

- You have to be on the same network to use on multiple devices
- To scan using a smart phone, make sure to start the server with the FLASK_RUN_CERT=adhoc option, this will start the server over https enabling you scan
- You can create a new hospital account using agent

```
