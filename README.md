# Animal Extinction Database

## 1. Overview
- The Database is modelling the relationships between variables tied to Animal Extinction in Australia.
- Motivation behind this database was to assemble together information that could inform stakeholders about the possible causes of extinction of particular animals and to track the numbers and development or such species in time.

## 2. Database Schema
- The database models the following entities that were indentified to be connected to the issues based on available literature.
  - Animal
  - Location
  - Endangerment_of_Animal
  - Population_of_Animal
  - Predator_and_Prey
  - Climate
  - Natural_Disaster
  - Urban_Development
  - Diseases
  - Disease_Outbreaks
  - Location_Of_Animal
- Multiple CHECK constraints are applied throughout the database definition to ensure basic logic is complied with. For example we ensure the years fall into a specific time frame we found reasonable in the given context or that for example population of an animal is not a negative number.

## 3. Tech Stack
To run and interact with this database, following software and packages are required:
- MySQL
- Python (pymysql / JupySQL)
- Jupyter Notebook
- dotenv library was used to hide sql credentials

## 4. Setup / Installation
- Install prerequisites (MySQL server, Python version)
- Clone the repo
- Set up your own local database on MySQL 
- Connect the database to the notebook with your MySQL credentials

## 5. Usage
- Four parts are provided:
    1) [DB_Definition](SQL/DB_Definition.ipynb)
        - Notebook where the entities are created along with constraints and triggers
    2) [DB_Interaction](SQL/DB_Interaction.ipynb)
        - Notebook intended for adding and modifying data mock data
    3) [DB_Queries](SQL/DB_Queries.ipynb)
        - Code for database querying
    4) [Data_Insertion](SQL/Data_Insertion.ipynb)
        - Notebook intended for adding and modifying data mock data

## 6. Data Sources

## 7. Supporting files
- Definition of the problem [Problem Statement](Supporting%20files/Societal%20problem%20definition.pdf)
- Entity Relationship Diagram that defines the schema [ERD](Supporting%20files/ERD.pdf)
- Data Modelling explains modeling choices and normalisation [Data Modeling](Supporting%20files/Data%20Modelling.pdf)
- Pitch Video [Pitch](Supporting%20files/Animal%20Extinction%20Video.mov)

## 8. Authors
- **Irina Iacob**
- **Klára Albertová**
- **Eva Artemis Müller**
