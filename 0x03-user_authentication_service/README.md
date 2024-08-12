0x03. User authentication service
Back-end
Authentification

Task 0: User Model
Objective: Create a SQLAlchemy model named User for a users table.

Attributes:

id: Integer primary key.
email: Non-nullable string.
hashed_password: Non-nullable string.
session_id: Nullable string.
reset_token: Nullable string.
File: user.py

Task 1: Create User
Objective: Implement the add_user method in the DB class to add a new user to the database.

Method:

Accepts two arguments: email and hashed_password.
Saves the user to the database and returns a User object.
File: db.py

Task 2: Find User
Objective: Implement the find_user_by method in the DB class to find a user by arbitrary keyword arguments.

Handling:

Raises NoResultFound if no user is found.
Raises InvalidRequestError if invalid query arguments are provided.
File: db.py

Task 3: Update User
Objective: Implement the update_user method in the DB class to update a user's attributes.

Handling:

Finds the user using find_user_by.
Updates the user's attributes with the given keyword arguments.
Commits changes to the database.
Raises ValueError if invalid attributes are passed.
File: db.py

Task 4: Hash Password
Objective: Implement a _hash_password method to hash a password using bcrypt.

Output: Returns the hashed password as bytes.

File: auth.py

Task 5: Register User
Objective: Implement the register_user method in the Auth class.

Functionality:

Registers a new user by hashing the password and saving the user to the database.
Raises ValueError if the user already exists.
File: auth.py

Task 6: Basic Flask App
Objective: Set up a basic Flask application.

Route:

GET /: Returns {"message": "Bienvenue"} as JSON.
File: app.py

Task 7: Register User Endpoint
Objective: Implement the /users route in Flask to register a user.

Endpoint:

POST /users: Registers a user with form data email and password.
If successful, returns {"email": "<email>", "message": "user created"}.
If the user already exists, returns {"message": "email already registered"} with a 400 status code.
File: app.py

General Setup and Requirements
Environment:

Ubuntu 18.04 LTS using Python 3.7.
SQLAlchemy 1.3.x.
Use bcrypt for password hashing.
Coding Standards:

Follow pycodestyle for code styling.
Ensure all files end with a newline.
Document all modules, classes, and functions.
