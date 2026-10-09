# Animal Extinction Database

## Project Overview
- The Database is modelling the relationships between variables tied to Animal Extinction in Australia.
- Motivation behind this database was to assemble together information that could inform stakeholders about the possible causes of extinction of particular animals and to track the numbers and development or such species in time.

Tasks that were conducted each week are recorded in the table below with corresponding files.

| Week | Task | Outcome |
|----------|----------|----------|
| 1    | Problem definition | [societal_problem_definition](docs/societal_problem_definition.pdf)|
| 2    | Schema definition - defining the entities, attributes, PKs, FKs, normalization to 3NF | [ERD](docs/erd.pdf) , [normalization](docs/normalization.pdf)|
| 3    | Database implementation in code - definition and example queries | see directory [sql](sql)|
| 4    | Stakeholder video | [pitch_video](docs/pitch_video.mov)|
| 5    | Real data integration - finding, cleaning and inserting data | see [data](data) for .csv files and [data_info](data/datasets_info.md) for information about the datasets; [tsx_preprocess](sql/tsx_preprocessing.ipynb) and [tssl_preprocess](sql/threatened_species_preprocessing.ipynb) for files cleaning and transforming the datasets; and [data_insertion](sql/data_insertion.ipynb) for actual data insertion into the database |
| 6    | Feedback implementation, additional queries | [feedback](docs/feedback_implementation.md) , [queries_week_6](sql/queries_week_6.ipynb)|

## Files
- `requirements.txt` - Python packages needed to run the notebooks
### sql:
- `sql/db_definition.ipynb` - Defines the database schema in code, implements constraints and triggers
- `sql/db_interaction.ipynb` - Inserts mock data and showcases a few interactions with the database - UPDATE, INSERT, DELETE queries
- `sql/db_queries.ipynb` - Example SELECT queries
- `sql/data_insertion.ipynb` - Insertion of the real world data
- `sql/threatened_species_preprocessing.ipynb` - Preprocessing of the tssl dataset
- `sql/tsx_preprocessing.ipynb` - Preprocessing of the tsx dataset
- `sql/queries_week_6.ipynb` - Contains additional example queries from the final week of the project

### data:
- `data/datasets_info.md` - information about the real-world datasets - sources, what they contain, what data was used and justification why they are disjoint
- `data/raw/tsx.csv` - raw tsx data
- `data/raw/threatened_species_state_lists.csv` - raw tssl data
- `data/processed/tsx_cleaned.csv` - preprocessed tsx dataset that includes only the data relevant to our database
- `data/processed/threatened_species_state_lists_cleaned.csv` - preprocessed tssl dataset

### supporting files:
- `docs/societal_problem_definition.pdf` - Defines the problem the database is addressing, the scope and the stakeholders
- `docs/erd.pdf` - Schema definition
- `docs/normalization.pdf` - Records our normalization procedure and provides further description of the modeled entities
- `docs/pitch_video.mov` - Stakeholder video that describes the project in a non-technical way
- `docs/feedback_implementation.md` - Records changes made based on the feedback our group received
- `docs/limitations_future_work.md` - Addresses limitations of the current state of this database and outlines intended future improvements
- `docs/recorded_changes.md`- Comments on the changes made to the schema and addresses normalization after the insertion of the real-world data 

## How to run / reconstruct the database

**Requirements**
- Python <version 3.13> and Jupyter (VS Code with the Jupyter extension works)
- MySQL - check for appropriate version for your OS: here developed and tested with MySQL 26.7.0 on macOS
- Python packages: `pandas`, `SQLAlchemy`, `PyMySQL` (the database connector), `jupysql`, `python-dotenv` (install with `pip install -r requirements.txt`)

**Steps**

Run the notebooks in this order. Each step depends on the previous one:

1. Create database. In MySQL : `CREATE DATABASE animal_extinction_db;`
2. `sql/db_definition.ipynb`: creates the tables
3. `sql/db_interaction.ipynb`: inserts the mock data into the tables
4. `sql/data_insertion.ipynb`: loads the cleaned data from `data/processed/` into the database.
5. `sql/db_queries.ipynb`: executes example queries
6. `sql/queries_week_6.ipynb`: executes additional example queries

**Configuration**

Before running, create a file named `.env` in the `sql/` folder. It must contain `DB_PASSWORD=your_password`, where `your_password` is your own MySQL password. The notebooks read it in their first cell and connect as `root` on `localhost` to the database `animal_extinction_db`. If your MySQL setup uses a different user or host, change `root` and `localhost` in the connection line of the first cell of each notebook. The password is kept in this file instead of in the notebooks, so it is not uploaded to GitHub.

**Resetting**
`db_definition.ipynb` drops and recreates the tables, so you can start over by running it again. (the database `animal_extinction_db` must already exist)
    
## Data Sources
Mock data was generated by Claude AI. Note that mock data was kept to ensure that all of our sample queries returned results.
For details on real-world data sources please see [datasets_info](data/datasets_info.md).

## Database dump
A full MySQL dump (schema, triggers and data) is available on Zenodo: <[DOI link](https://doi.org/10.5281/zenodo.23261431)> but also in the `database_dump/` folder : [animal_extinction_database.sql](database_dump/animal_extinction_database.sql).


To restore it : 
1. Create an empty database. In MySQL : `CREATE DATABASE animal_extinction_db;` (you may chose a different name)

2. Restore the database using the SQL dump: `mysql -u root -p animal_extinction_db < database/animal_extinction_database.sql` Replace `root` with your MySQL username and `animal_extinction_db` with your chosen database name, if different. Run the command from the project's root directory. Your MySQL password will be asked as input.

## How we worked
All authors contributed comparably to the project. We had issues with version control with Jupyter notebook files and thus, we mostly worked together in person and uploaded everything at once. We do recognize that this is not ideal and in the future we would ensure that we have everything set up correctly.

## Authors
- **Irina-Cezara Iacob**
- **Klára Albertová**
- **Eva Artemis Müller**
