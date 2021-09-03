# Simple Store

App that shows inventory available in the store

## Version

 Simple Store-V1.0 

## Author

* **mungaijoel**

## Features


As a user of the website you will be able to:

1. Open the app on the web.
2. Sign in
3. Navigate the app.
4. View different new posts.
5. leave a Comment.
6. Log out


## Behaviour Driven Development (BDD)
|Behaviour 	           |    Input 	                 |       Output          |
|----------------------------------------------|:-----------------------------------:|-----------------------------:|       
|Page loads	                           |   USer clicks any link in navbar                            |       Respective content is displayed  |                        |


### Installing

* Step 1:
Clone this repo: git clone . https://git.jambopay.co.ke/interns/simple-store.git
* Step 2:
The repo comes in a zipped or compressed format. Extract to your prefered location and open it.
* Step 3:
open your terminal and navigate to solutions. Add virtual environment and install requirements.txt file  . --  `pip3 install -r requrements.txt`--
* Step 4:
After adding the requirements, add database to the project `psql` add database `CREATE DATABASE (name of database);` then press enter, add user and password to your database.

* Step 5:
Make migrations to update database. Postgres sql . To make migrations run `python manage.py makemigrations` then `python manage.py migrate`
* Step 6:
To run the app, you'll have to run the following commands in your terminal
`python manage.py runserver`

    
## Built With

* Python Django framework
* HTML - For building Mark Up pages/User Interface
* Bootstrap
* CSS - For Styling User Interface


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

Ahmed 