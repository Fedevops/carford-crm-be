carford-crm-be
Project = CRM system for customer and car registration.

# To run this project:

    Using Docker image:
    1 - Build the image (in the project root)
    docker build -t backend-carford .

    2 - Run the image:
    docker run -p 8000:8000 backend-carford

# Manual run
    1 - Create a virtual environment:
    python3.11 -m venv venv

    2 - Activate virtual environment:
    source venv/bin/activate

    3 - Install dependencies:
    pip install -r requirements.txt

    4 - Perform migrations (in the project root)
    python3 manage.py makemigrations

    5 - Generate the necessary tables
    python3 manage.py migrate

    6 - Run the project
    python3 manage.py runserver

# Run Tests
    python manage.py test
# Check test coverage report (90%)
    coverage report

# Check API documentation
    http://localhost:8000/api/docs