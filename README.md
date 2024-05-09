URL Checker



URL Checker is a simple Django web application that allows users to check the availability of URLs and store records of these URLs. The application provides a user-friendly interface to manage and monitor URLs.

Features
Check the availability of URLs and store records with the status.
Display a list of checked URLs with their statuses.
Add new URLs for checking.
Delete URLs from the list.
Automatically update the status of URLs at regular intervals.
View statistics on the number of available and unavailable URLs.
User-friendly interface with validation for input URLs.
Prerequisites
Python (3.x)
Django (3.x)
Installation
Clone the repository:
bash
Copy code
git clone https://github.com/your-username/url-checker.git
Navigate to the project directory:
bash
Copy code
cd url-checker
Install dependencies:
bash
Copy code
pip install -r requirements.txt
Usage
Run migrations to create the database schema:
bash
Copy code
python manage.py migrate
Start the development server:
bash
Copy code
python manage.py runserver
Open your web browser and go to http://127.0.0.1:8000/ to access the application.
Use the provided interface to add URLs for checking and monitor their statuses.
Contributing
Contributions are welcome! If you find any issues or have suggestions for improvement, please open an issue or create a pull request on GitHub.

License
This project is licensed under the MIT License - see the LICENSE file for details.
