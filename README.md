# E-Commerce Product Management System

## Description
This is a simple product management system for an e-commerce website. It allows users to add products, discounts and categories. The system also allows users to view a list of all products, search for a single product as well as get all categories.
## Features
- Add a product 
- Edit a product 
- Delete a product 
- View all products
- View a single product 
- Search for a product by category
- Apply a discount to a product 

## Technologies
- Python
- Django
- Django REST Framework
- PostgreSQL
- Docker
- Poetry

## Setup

Ensure sure you have Docker installed on your machine as we would use it to setup the database.

If you don't have Docker, install [Poetry](https://python-poetry.org/docs/#installation). Then follow the steps below:

### Pre-Setup

1. Clone the repository
2. Make a copy of the `.env.example` file and rename it to `.env`:
```bash
cp .env.example .env
```
3. Update the required fields in the `.env` file.


### Setup

1. Clone the repository
2. Run the following command to start the database:
```bash
docker compose up -d
```
3. Run the following command to install the dependencies:
```bash
poetry install
```
4. Run the following command to start the application:
```bash
poetry run python manage.py runserver
```
5. The application will be available at `http://localhost:8000`

## API Documentation
Here's a link to the [API documentation](https://documenter.getpostman.com/view/23964763/2sAYJ7hzCv)

