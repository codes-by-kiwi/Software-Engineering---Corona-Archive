# README file

### Contributors

Sprint 1

- Shubham Kumar Chaurasia
- Mahmoud El Bergui

## File Structure

```
\--SE-Sprint01-Team30
    \--database
        --database.db           # holds the portable database
        \--init_db.py           # initializes the schema.sql file
    \--schema
        --schema.sql            # holds all the queries
    \--tests
        --conftest.py           # configuration for tests
        --test.py               # all tests for the app
    \--static
        \--css                  # All the CSS Files used
        --                      # contains images and static files
    \--templates
        \--                     # All HTML files
    -- app.py                   # Main flask app
    -- README.md
    -- requirements.txt         # Required dependencies to run this program
    -- .gitignore

```

## First clone the gitrepository to run

#Go inside root of the directory where you can see app.py
install Virtual Env(Or you can create a virtual environment by any way you like)

```
sudo pip3 install virtualenv
```

# Create virtual environment

$ virtualenv env

# Start virtual environment

$ source env/bin/activate

# Install all the dependencies

$ pip3 install -r requirements.txt

# Enter into /database folder

```
$ python3 init_db.py
```

```
$ sqlite3 database.db

```

- set environment variable

```
$set FLASK_APP=app.py
```

if you want to turn on the debugger mode (to see changes on refresh)

```
$export FLASK_ENV=development
```

# Go to the root directory

$ flask run

# For Documentation

Please see into the project root directory file named 'Project Design.pdf'

#After entring the data from the Registration of any Pages. The data can be seen by

- Enter into /database

```
  $sqlite3 database.db
```

-- Once the sqlite3>> terminal is open, type the queries

```
select * from Visitor;
```

```
select * from Places;

```

```
select * from Agent;

```

```

select * from Hospital;

```

## Sprint 1 achievements

1. Created database.db and init_db.py and store and run queries.

2. Maintained schema into schema.sql

3. Maintained .gitignore

4. Made static files all well documented and self explanitory

5. Made README.md.

6. Made templates for each pages.

7. Made register options for all visitor, places, agent, hospitals.

8. Checked successfully entry of data to the database.

9. Commented and made everything proper for next team to continue

10. Tests configuration has been done.

```

```
# Sprint 2

### Contributors

- Fizza Usman
- Denisa Checiu

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

### File Structure

```
\--SE-Sprint01-Team30
    \--database
        --database.db           # holds the portable database
        \--init_db.py           # initializes the schema.sql file
    \--schema
        --schema.sql            # holds all the queries
    \--tests
        --conftest.py           # configuration for tests
        --test.py               # all tests for the app
    \--static
        \--css                  # All the CSS Files used
        \--vaccuploads          # all the vaccination uploads go into this file
            --                  # contains the vaccination uploads
        \--client
            \--img              # all the files that can be downloaded go into this file
            --                  # contains images that the client can download from the website and the R code for the graph
        --                      # contains images and static files
    \--templates
        \--                     # All HTML files
    -- app.py                   # Main flask app
    -- README.md
    -- requirements.txt         # Required dependencies to run this program
    -- .gitignore

```

## Getting started

The following instructions will enable you to get a copy of the project we created, up and running on your local machine for development and testing purposes. Proceed further to see which software you need to instal and how to do it.

### Pre-requisities
* [sqlite3](https://www.sqlite.org/download.html)
After downloading the files, add them in a folder titled 'sqlite' in 'C:'.
Sometimes it still gives some errors (for Windows), to be sure that it works, add the path for sqlite3 manually:
```
PATH=%PATH%;c:\sqlite
```
* Flask
```
pip install Flask
```
* Virtual Env
```
sudo pip3 install virtualenv
```

## Updated Installation Guide

```
# clone the repository
git clone 

# go to the location of your folder containing the repository
cd se-sprint02-team30/

# Create virtual environment
$ virtualenv env

# Start virtual environment - for Linux and Mac users
$ source env/bin/activate
# Start virtual enviroment for Windows users
# env/Scripts/activate

# Install all the dependencies
$ pip install -r requirements.txt

# Enter database folder
cd database

# Initialize database
python3 init_db.py
sqlite3 database.db

# Set environment variable
set FLASK_APP=app.py

# You can also turn on the debugger mode (to see changes on refresh) - for Linux and Mac users
export FLASK_ENV=development
# For Windows users
#set FLASK_ENVIROMENT=development

# Go back to the root directory
cd .. 

# Run python script
flask run

# Open http://127.0.0.1:5000 in your browser to explore the web service.
```

### Contributions in Sprint 2

✅ Updated SQL file - added the Innob engine for all tables; altered table `visitortoplaces` to drop the QRcode and device_ID and add citizen_id and place_id as foreign keys, also added a primary key for the table; changed attribute infected to be of type boolean as required; as visitors can choose to input email and or phone number, we changed the attributes to not be mandatory to input(same for device_id); added contact attribute for 'places'; made QRcode not mandatory to input in the beginning (dropped the NOT NULL attibute), as place owners don't have it when they register.

✅ Added fake instances for the database. 

✅ Made the more info button work - it takes us to the 'moreinfo' page.

✅ Created 'moreinfo' page which has a guide on how to use the web service.

✅ Made option to download image from the website

✅ Created a page where users can add their COVID vaccination certificate, in image or pdf format. Once they upload it it loads into the 'vaccuploads' folder.

✅ Made a daily death rate corona chart in R.

✅ Created the hospital Registration page.

✅ Made the hospital registration button work, from the 'option' page.

✅ Made a QR code generator for bussiness owner - they just enter their bussiness name and a unique code is generated. (they can also download it, per the feature implemented above).

✅ Created 2 functional buttons in the moreinfo page, which lead to the new pages created : QRcodegenerator and uploadImage (vaccination certificate upload). -- later on this can be developed so only logged in users can access them.

✅ Added a button to the navbar (Guide) which takes them to the more infopage.

✅ Created a test cases python script, included test for each template created, including the already existing register pages.

