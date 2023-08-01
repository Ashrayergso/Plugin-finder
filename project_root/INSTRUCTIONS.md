# Instructions

## Setup

1. Clone the repository to your local machine.
2. Navigate to the project root directory in your terminal.
3. Install the required Python packages by running `pip install -r requirements.txt`.

## Database Setup

1. Make sure you have PostgreSQL installed and running on your machine.
2. Create a new PostgreSQL database for the project.
3. Update the `DATABASES` configuration in the `settings.py` file with your database name, user, and password.

## Running the Application

1. Apply the database migrations by running `python manage.py migrate`.
2. Start the Django development server by running `python manage.py runserver`.
3. Open your web browser and navigate to `http://localhost:8000` to view the application.

## Using the Application

1. On the home page, click the "Scan for Plugins" button to start scanning for audio plugin units on your Mac.
2. Once the scan is complete, a table will be displayed with the name, version, creator, and installation date of each plugin.
3. Click the "Look Online" button next to a plugin to search for it online.
4. Click the "Check Version" button next to a plugin to check if it is the most recent version.

## Running Tests

1. Run the test suite by executing `python manage.py test`.

## Troubleshooting

If you encounter any issues while setting up or using the application, please refer to the `README.md` file for additional information.