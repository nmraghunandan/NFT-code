# NFT-code
This code is a Flask web application for a image boxes listing and management system. It allows users to register, login, view images, and manage their cart. Here is an overview of each block of code:

1. Importing modules and setting up the Flask application:
   - The code begins with importing necessary modules, including Flask, SQLite3, and os.
   - The Flask application is created, and a secret key is set for session management.
   - An upload folder is specified for storing images.
2. Database setup:
   - The code connects to an SQLite database file named 'main.db'.
   - Two tables, 'users' and 'datafiles', are created if they don't already exist.
   - The 'users' table stores user details, including name, phone, email, password, address, and coupon code.
   - The 'datafiles' table is used to store box IDs, images, and corresponding links.
3. Routing and View Functions:
   - Multiple routes are defined using the `@app.route` decorator for different pages of the website, such as home, contact, product, about, etc.
   - Each route corresponds to a view function, which is responsible for rendering the appropriate HTML template.
   - The functions interact with the database, retrieve necessary data, and pass it to the templates for rendering.
4. Register and Login Functionality:
   - The `/register` route handles user registration. It captures user input from the registration form and inserts the data into the 'users' table in the database.
   - The `/login` route handles user login. It checks the entered email and password against the database and creates a session for the logged-in user.
5. Cart Management:
   - The `/go_to_cart` route handles adding selected boxes to the cart. It receives the selected box IDs and processes the form data, such as images and links, to store them in the 'datafiles' table.
   - The `/cart` route renders the cart template and displays the selected box IDs.
6. Vendor Profile and Activity:
   - The `/vendorprofile` and `/activity` routes handle displaying vendor profiles and activity pages, respectively.
7. Additional Functionality:
   - The code includes routes for admin, contact, referral, about, widget, and manage pages, which render the respective templates.
   - The code also includes functions for uploading images and displaying them on the homepage.
