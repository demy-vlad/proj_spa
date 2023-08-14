# Comments Web Application
## Peculiarities
- Users can leave comments with their name, email address and text.
- Comments can have a nested structure.
- Username Validation: Only letters, numbers and spaces are allowed.
- Email address validation: maximum length 50 characters.
- Comment text validation HTML tags. Checking for correct closing of tags.
- Protection against duplicate comments when replies.
- Ability to sort comments by username, email address and date added.
2. Change to the project directory: ```bashcd comments```


## Installation and launch
```bash
1. Clone the repository
2. Change to the project directory: `cd comments`
3. Create and activate virtual environment: `python3 -m venv venv` и `source venv/bin/activate` (или `venv\Scripts\activate` на Windows)
4. Install dependencies: `pip install -r requirements.txt`
5. Apply migrations: `python manage.py migrate`
6. Start local server: `python manage.py runserver`
```

## Installing with docker
```bash
1. `docker-compose build --no-cache`
2. `docker-compose up --detach`
```

## Running Tests
- You must have dependencies installed!
```bash
1. Running tests: `pytest -s -v`
```