# Comments Web Application
## SPA Application: Comments

## Peculiarities
- Users can leave comments with their name, email address and text.
- Comments can have a nested structure.
- Username Validation: Only letters, numbers and spaces are allowed.
- Email address validation: maximum length 50 characters.
- Comment text validation HTML tags. Checking for correct closing of tags.
- Protection against duplicate comments when replies.
- Ability to sort comments by username, email address and date added.

## Installation and launch
1. Clone the repository
2. Change to the project directory: ```bash cd comments```
3. Create and activate virtual environment: ```bash python3 -m venv venv``` и ```bash source venv/bin/activate``` (или ```bash venv\Scripts\activate``` на Windows)
4. Install dependencies: ```bash pip install -r requirements.txt```
5. Apply migrations: ```bash python manage.py migrate```
6. Start local server: ```bash python manage.py runserver```

## Installing with docker
1. ```bashdocker-compose build --no-cache```
2. ```bashdocker-compose up --detach```

## Running Tests
- You must have dependencies installed!
1. Running tests: ```bashpytest -s -v```