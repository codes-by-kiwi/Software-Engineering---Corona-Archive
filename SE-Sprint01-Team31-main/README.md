# SE-Sprint01-Team31
### Contributors
Sprint 1: 

   * Idris Chendid
 
   * Fizza Usman
### Built with:
   * HTML
   * CSS
   * JAVASCRIPT
   * PYTHON 3  
   * FLASK  
   * MYSQL
### Prerequisites:
   * MySQL
   * Flask

## RUN PROJECT:
 1 clone the repo: git clone https://github.com/Magrawal17/SE-Sprint01-Team31.git \
 2 cd SE-Sprint01-Team31/ \
 3 $ sudo pip3 install virtualenv or $ pip install virtualenv\
 4 $ virtualenv env\
 5 $ source env/bin/activate\
 6 $ pip3 install flask\
 7 $ python3 app.py (run the project)  
 
 Go to this URL once the server has started: 
   * http://127.0.0.1:5000/    

After running app.py and chekcing our progress on the website Run  $ python3 img.py for SQL implementations

## Test Cases:
Run this code once you are entire the environment: 
   * $ python3 tests/test1.py 

It fails the upload and scan pages but it opens successfully when running app.py\
Once the server has started, we can see that the homepage opens successfully, registration and login page opens successfully too and the upload and scan page opens correctly 
without errors. Once a user get registered it is added to the database.

## PROGRESS:
  * We create a home page describing the webservice as a corona archive with links to other pages.
  * Registration page where the user can add his first and last name, email, adress and phone number.
  * User has to choose between being a visitor or place owner using the checkbox provided if not he requests registration.
  * Hospitals request registration to be performed automatically by us.
  * Agent request registration where we have to give them credentials and they have to login with these credentials in the login page.
  * Login page has a link to a scan page where the visitor after login in has to scan the QR code.
  * Added some popup boxes when for example a user uploads a file successfully or when he got registered successfully.
  * Scan.html file for scanning a QR code.
  * Upload page where the user can upload his vaccine pass or his corona test result or may be something else related to his health.
  * We linked our HTML files with python server using flask in the app.py file.
  * We used CSS files and some pictures related to HTML files for designing our website.
  * SQL code: coronaarch.sql related to the database we create a table for user when he performs the registration form, so that when a user get registered he is added to the database with img.py.
  * Frontend devlopped mostly with HTML CSS and backend with python and flask framework that relates HTML files with the server.
