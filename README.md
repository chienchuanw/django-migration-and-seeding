# Django Migration and Seeding
This repository contains a Django project that demonstrates how to perform database migrations and seed initial data using fixtures. This project follows the steps outlined in [Ardho's article on Medium](https://medium.com/@ardho/migration-and-seeding-in-django-3ae322952111).  
Meanwhile you can also find instructions of django-seed [here](https://github.com/mstdokumaci/django-seed).  

## Table of Contents

- [Django Migration and Seeding](#django-migration-and-seeding)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Setup](#setup)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)

## Introduction

Database migration and seeding are essential parts of the development workflow in Django. This project demonstrates how to:
- Perform database migrations.
- Seed initial data into the database.
- Revert seeded data without affecting non-seeded data.

## Setup

Follow these steps to set up the project on your local machine.

### Prerequisites

- Python 3.6+
- Django 3.0+
- Git

### Installation
1. Clone the repository:

    ```bash
    git clone git@github.com:chienchuanw/django-migration-and-seeding.git 
    cd django-migration-and-seeding
    ```

2. Create and activate a virtual environment:

    ```bash
    poetry shell
    ```

3. Install the dependencies:

    ```bash
    poetry install
    ```



