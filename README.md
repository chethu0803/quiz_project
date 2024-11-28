Installation

Follow these steps to get the project up and running locally:

Prerequisites

Ensure that you have the following installed:

   Python 3.x: Download Python
   
   pip: Python package manager (usually comes with Python).
   
   Git (optional for version control): Download Git

Steps

1.Clone the repository:

     git clone https://github.com/chethu0803/quiz_project.git

2.Navigate to the project directory:

     cd quiz_project

3.Create a virtual environment (optional but recommended):

     python3 -m venv env

4.Activate the virtual environment:

On Windows:

     env\Scripts\activate
  
On macOS/Linux:

     source env/bin/activate

5.Install the dependencies:

     pip install -r requirements.txt

6.Run database migrations:

To set up the database and tables:

     python manage.py migrate

7.Create a superuser (optional, for admin access):

     python manage.py createsuperuser

Use the below superuser credentials,if you dont want to create one:

      Email: test@gmail.com

  
      Password: Acertest
  

8.Start the development server:

     python manage.py runserver

9.Access the app: Open a browser and go to http://127.0.0.1:8000/ to access the quiz application.

For admin access, go to http://127.0.0.1:8000/admin/ and log in with the superuser credentials.








