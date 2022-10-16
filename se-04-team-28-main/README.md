# SE-Sprint01-Team28

### Sprint 1:
- Ilyas Benyamna
- Sultan Sadiq Husain Siddiqui
### Sprint 2:
- Zineb Laouzi
- Minyahel Fekadu Haile
### Sprint 3:
- Volen Terziev
- Saad El Jadouri
### Sprint 4:
- Fizza Usman 
- Vahid Menu Nesro 
---
### About the Project - Corona Archive:
```
Corona Archive is a web service for tracking, displaying, evaluating, and archiving of the Corona infections in a particular location. The web service will be accessible to four types of users:

Visitors: Visitors can use the web service to indicate whether they have entered a particular place and when they have done so. In case of infection, visitors will be contacted by authorities.
Places: Places which are frequently visited by people. Place owners will be able to get a QR code - Citizens can scan this QR code to record their presence at that place.
Agency: The agency or the evaluation client can use the web service to generate corona-related reports by collecting data from the database and by registering hospitals and search for visitors.
Hospital: Hospitals can use the web service to mark people as infected and track anyone else that has been in contact with an infected person.
```

### Built with
```
- Python
- HTML
- CSS
- JavaScript
- MySQL
- Flask
```
### File structure
```
    \--se-02-team-28
        \--app
            \--routes
                --agent_routes.py
                --data_routes.py
                --hospital_routes.py
                --place_routes.py
                --visitor_routes.py
            \--static
                \--css
            \--templates
                \--
            --app.py
        \--config
            --db.yaml
        \--sql
            --database.sql
        \--tests
            --tests.py
            --testing.md
        --run.py
        --README.md
        --requirements.txt
        --.gitignore

```
## Getting Started

These instructions are primarily specified for unix based systems
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

    # Inside mysql

    mysql> source database.sql
    mysql> exit

    # update db.yaml in the config folder with your own username and  password, if necessary you can also change the secret key used for bcrypt
    
    $ python3 run.py 
    # for further instructions such as port selection or lan 
    # wide availability use 
    #  FLASK_APP=run.py FLASK_ENV=development FLASK_RUN_CERT=adhoc flask run  --host=0.0.0.0 --port={DESIRED PORT NUMBER}

```
## Sprint 1 Progress

- Created the instructions to initialize the app
- Freezed the requirements using `pip freeze > requirements.txt`
- Created the basic Flask app
- Created a parent html template `templates\layout.html`, the child templates simply extend it, this is done in order to make changes easy to implement and avoid repetition of code (e.g: adding bootstrap). If you want to make any overall changes that will affect all pages, make them in `layout.html`
- Added Bootstrap CSS. We did this because it is easier to style the pages with Bootstrap. There is also the possibility for custom CSS, to be found in the folder `static\main.css`
- Most of the Bootstrap code for styling was copied from the Bootstrap documentation. 
- For the database credentials, a yaml file is used in order no to expose the credentials, and also for simplicity. If one is familiar with JSON, then YAML is simply a superset of JSON.
- Added the ability for visitors to register, an id is created and the necessary validations are performed.
- Added the ability for places to register, along with QR code generation.
- We consider Device ID to be the physical address
- Added the QR Code Scanning page after registering where the webcam is broadcasted
- Added Agent login and logout, with sessions
- Created a css file and styled the page, to make it look simple and as user friendly as possible.

## Run tests
```
    # from the root directory of the project
    $ python3 -m unittest

```
## Sprint 2 Progress

✅ Improved and Implemented better and functional Device_id logic for visitor

✅ Improved and Implemented better and function Device_id logic for place

✅ Corrected and Implemented functional QR scanning

✅ Improved the implementation of all web pages by changing the design and functionality

✅ Improved and Implemented better qr code generation logic

✅ Updated sql database schema with proper indicators for foreign keys and unique values

✅ Implemented logout logic for each individual user type

✅ Implemented Agent visitor look up with proper database display

✅ Implemented Agent place look up with proper database display

✅ Implemented Hospital Visitor lookup

✅ Implemented Hospital Visitor infected / not-infected setting.

✅ Implemented QR code download.

✅ Implemented functional QR scan in logic that records entry and exit times.

✅ Implemented user friendly UI.

✅ Implemented a better and functional visitor hospital registration logic

✅ Removed redundant pages

✅ Improved the Correctness of the code app.py

✅ Improved test cases functionality

✅ Added useful comments

✅ Made proper folder hierarchy


## Sprint 3 Progress

✅ Full overhaul of the Hospital page with improved GUI, more search fields, and convenience
✅ Similar full overhaul for the Agent Search Database page
✅ Functional navigation bar with log out functionality moved to it
✅ Added "About" page and impressum footer
✅ Implemented autodocs
✅ Agent can now view list of hospitals
✅ Registration validation is less stupidly strict
✅ Registration form fields now persist if registration invalid
✅ Unauthorized pages now send you to the corresponding login page
✅ Added more tests and fixed existing ones

GUI
    ✅ Created a consistent style to be used across all pages
    ✅ Refactored the GUI on almost every page to use this style

Code organization
    ✅ Moved CSS code to a single file to remove duplicate code
    ✅ Moved page-specific CSS code to head blocks
    ✅ Used multiline format strings for long queries
    ✅ Made spacing, casing, and naming more consistent
    ✅ Improved quality of comments and added them to complex HTML and JS code

✅ Various bugfixes

## Notable Issues and Tips
- Agent Account
    ```
        Username: agent1
        Password: password
    ```
- Hospital Account
    ```
        Username: BremenNord
        Password: Bremen123
    ```
- The only way to check if users signed in and out at the moment is through mysql by directly observing the VisitorToPlace table


## Sprint 4 Progress
    
    ✅ Implemented a Landing Page and a visually appealing UI
    
    ✅ Implemented and animated a collapsible Navigation Bar to the Website 
    
    ✅ Removed Inline CSS and fixed overly complicated class usage
    
    ✅ Fixed the background design / image of the website
    
    ✅ Fixed Infected Status change error for Hospital user
    
    ✅ Added Javascript to make table transition and appearance smoother
    
    ✅ Fixed the background design / image of the website
    
    ✅ Changed absolute values into relative ones to improve responsiveness on small screens
    
    ✅ Made a feedback form that sends the data users enter to the admin's email
    
    
