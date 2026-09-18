# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.19.5
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# %%
import sys
# !{sys.executable} -m pip install python-dotenv

# %%
# %load_ext sql

# %%
# Load the database based on environment variables from .env file (for security reasons)
import os, sys
from dotenv import load_dotenv
load_dotenv()

password = os.getenv("DB_PASSWORD")
os.environ["DATABASE_URL"] = f"mysql+pymysql://root:{password}@localhost/animal_extinction_db"

# %% language="sql"
# DROP TABLE IF EXISTS Disease_Outbreaks;
# DROP TABLE IF EXISTS Diseases;
# DROP TABLE IF EXISTS Location_Of_Animal;
# DROP TABLE IF EXISTS Urban_Development;
# DROP TABLE IF EXISTS Natural_Disaster;
# DROP TABLE IF EXISTS Climate;
# DROP TABLE IF EXISTS Population_of_Animal;
# DROP TABLE IF EXISTS Predator_and_Prey;
# DROP TABLE IF EXISTS Endangerment_of_Animal;
# DROP TABLE IF EXISTS Location;
# DROP TABLE IF EXISTS Animal;

# %% language="sql"
#
# CREATE TABLE IF NOT EXISTS Animal (
#     animal_id INT PRIMARY KEY AUTO_INCREMENT,
#     genus_name VARCHAR(100) NOT NULL,
#     species_name VARCHAR(100) NOT NULL,
#     common_name VARCHAR(100),
#     animal_class VARCHAR(15),
#     diet VARCHAR(15),
#     native BOOLEAN DEFAULT TRUE,
#
#     CONSTRAINT unique_animal_name UNIQUE (genus_name,species_name), #combination of genus and species must be unique as it identifies a specific animal
#     CONSTRAINT check_animal_class CHECK (LOWER(animal_class) IN ('mammalia', 'aves', 'reptilia', 'amphibia', 'actinopterygii','elasmobranchii', 'insecta', 'arachnida', 'malacostraca','gastropoda', 'bivalvia', 'annelida')), #put to lower case to avoid case sensitivity issues
#     CONSTRAINT check_diet CHECK (LOWER(diet) IN ('carnivore', 'herbivore', 'omnivore', 'frugivore', 'granivore','foliovore', 'nectarivore', 'insectivore', 'piscivore','myrmecovore', 'detritivore', 'scavenger'))
# );

# %% language="sql"
#
# CREATE TABLE IF NOT EXISTS Endangerment_of_Animal (
#     animal_id INT,
#     effect_year YEAR,
#     level CHAR(2) NOT NULL,
#     PRIMARY KEY (animal_id, effect_year),
#     FOREIGN KEY (animal_id) REFERENCES Animal(animal_id),
#
#     CONSTRAINT check_level CHECK (UPPER(level) IN ('LC', 'NT', 'VU', 'EN', 'CR', 'CD', 'EW', 'EX', 'DD', 'NE')), #put to upper case to avoid case sensitivity issues
#     CONSTRAINT check_effect_year CHECK (effect_year >= 1900) #1900 is the year when The Lacey Act was passed, which was the first federal law protecting wildlife in the US (and worldwide). Moreover, the effect year should not be in the future (enforced by a trigger).
# );
#
# #Methodology for Endangerment Levels:
# #LC - Least Concern
# #NT - Near Threatened
# #VU - Vulnerable
# #EN - Endangered
# #CR - Critically Endangered
# #CD - Conservation Dependent
# #EW - Extinct in the Wild
# #EX - Extinct
# #DD - Data Deficient
# #NE - Not Evaluated

# %% language="sql"
#
# CREATE TABLE IF NOT EXISTS Predator_and_Prey (
#     animal_id_predator INT,
#     animal_id_prey INT,
#     PRIMARY KEY (animal_id_predator, animal_id_prey),
#     FOREIGN KEY (animal_id_predator) REFERENCES Animal(animal_id),
#     FOREIGN KEY (animal_id_prey) REFERENCES Animal(animal_id)
# );

# %% language="sql"
#
# CREATE TABLE IF NOT EXISTS Location (
#     location_id INT PRIMARY KEY AUTO_INCREMENT,
#     location_name VARCHAR(100) UNIQUE NOT NULL,
#     biome VARCHAR(50),
#     area_sq_km FLOAT,
#     protection_level CHAR(2),
#
#     CONSTRAINT biome_check CHECK (LOWER(biome) IN ('tundra', 'taiga', 'temperate forest', 'tropical forest', 'grassland', 'desert', 'wetland', 'marine')), #put to lower case to avoid case sensitivity issues
#     CONSTRAINT protection_level_check CHECK (UPPER(protection_level) IN ('I', 'II', 'III', 'IV', 'V', 'VI')), #put to upper case to avoid case sensitivity issues
#     CONSTRAINT check_area_sq_km CHECK (area_sq_km >= 0) #area cannot be negative
# );
#
# ALTER TABLE Location MODIFY COLUMN protection_level CHAR(3);

# %% language="sql"
#
# CREATE TABLE IF NOT EXISTS Population_of_Animal (
#     animal_id INT,
#     location_id INT,
#     population_year YEAR,
#     population_size INT NOT NULL,
#     PRIMARY KEY (animal_id, location_id, population_year),
#     FOREIGN KEY (animal_id) REFERENCES Animal(animal_id),
#     FOREIGN KEY (location_id) REFERENCES Location(location_id),
#
#     CONSTRAINT check_population_year CHECK (population_year >= 1900),#First scientific monitoring of animal populations in Australia started in the 1900s, and the population year cannot be in the future.
#     CONSTRAINT check_population_size CHECK (population_size >= 0) #population size cannot be negative
# );

# %% language="sql"
# CREATE TABLE IF NOT EXISTS Climate(
#     record_date DATE,
#     location_id INT,
#     temperature_min_celsius FLOAT,
#     temperature_max_celsius FLOAT,
#     rainfall_mm FLOAT,
#     PRIMARY KEY (record_date, location_id),
#     FOREIGN KEY (location_id) REFERENCES Location(location_id),
#
#     CONSTRAINT check_temperature_min CHECK (temperature_min_celsius >= -100 AND temperature_min_celsius <= 60), #Temperature range on Earth is from -89.2°C to 56.7°C, but we allow a bit more for extreme cases.
#     CONSTRAINT check_temperature_max CHECK (temperature_max_celsius >= -100 AND temperature_max_celsius <= 60),
#     CONSTRAINT check_rainfall_mm CHECK (rainfall_mm >= 0), #Rainfall cannot be negative
#     CONSTRAINT check_min_max_temperature CHECK (temperature_min_celsius <= temperature_max_celsius)  #Minimum temperature cannot be greater than maximum temperature
# );

# %% language="sql"
#
# CREATE TABLE IF NOT EXISTS Natural_Disaster (
#     disaster_id INT PRIMARY KEY AUTO_INCREMENT,
#     disaster_type VARCHAR(50),
#     disaster_year YEAR NOT NULL, #it doe not make sense to have a disaster without a year (we would not be able to infer causality), thus we make it NOT NULL
#     location_id INT,
#     disaster_area_sq_km FLOAT,
#     FOREIGN KEY (location_id) REFERENCES Location(location_id),
#
#     CONSTRAINT check_disaster_year CHECK (disaster_year >= 1750), #Natural disaster year cannot be in the future (enforced by triggers) and we put 1750 as a lower limit (given Australia's colonization year is 1788) so unreasonable values are not entered.
#     CONSTRAINT check_disaster_area_sq_km CHECK (disaster_area_sq_km >= 0) #Disaster area cannot be negative
# );

# %% language="sql"
# CREATE TABLE IF NOT EXISTS Urban_Development (
#     development_name VARCHAR(100) PRIMARY KEY, #name of the urban development project can be used for querying the database, thus it make sence to be the primary key as it will speed up queries and avoid duplicates.
#     location_id INT,
#     development_type VARCHAR(100),
#     development_year YEAR,
#     development_area_sq_km FLOAT,
#     FOREIGN KEY (location_id) REFERENCES Location(location_id),
#
#     CONSTRAINT check_development_year CHECK (development_year >= 1750), #Urban development year cannot be in the future (enforced by triggers) and we put 1500 as a lower limit (given Australia's colonization year is 1788) so unreasonable values are not entered.
#     CONSTRAINT check_development_area_sq_km CHECK (development_area_sq_km >= 0) #Development area cannot be negative
# );

# %% language="sql"
# CREATE TABLE IF NOT EXISTS Diseases (
#     disease_id INT PRIMARY KEY AUTO_INCREMENT,
#     disease_name VARCHAR(100) NOT NULL UNIQUE, #disease name should be unique as it identifies a specific disease
#     disease_type VARCHAR(100) 
# );

# %% language="sql"
# CREATE TABLE IF NOT EXISTS Disease_Outbreaks(
#     outbreak_id INT PRIMARY KEY AUTO_INCREMENT,
#     disease_id INT, 
#     animal_id INT, 
#     location_id INT,
#     outbreak_year YEAR,
#     disease_mortality_percent DECIMAL(4,2), # mortality is a percentage (4 digits in total, 2 after the decimal point)
#
#     FOREIGN KEY (disease_id) REFERENCES Diseases(disease_id),
#     FOREIGN KEY (animal_id) REFERENCES Animal(animal_id),
#     FOREIGN KEY (location_id) REFERENCES Location(location_id),
#
#     CONSTRAINT check_outbreak_year CHECK (outbreak_year >= 1750), #Outbreak year cannot be in the future (enforced by triggers) and we put 1750 as a lower limit (given Australia's colonization year is 1788) so unreasonable values are not entered.
#     CONSTRAINT check_disease_mortality_percent CHECK (disease_mortality_percent >= 0 AND disease_mortality_percent <= 100) #Mortality percentage cannot be negative or greater than 100
# );

# %% language="sql"
# CREATE TABLE IF NOT EXISTS Location_Of_Animal(
#     animal_id INT,   
#     location_id INT,
#     
#     PRIMARY KEY (animal_id, location_id),
#     FOREIGN KEY (animal_id) REFERENCES Animal(animal_id),
#     FOREIGN KEY (location_id) REFERENCES Location(location_id)
# );

# %% language="sql"
#
# #triggers to enforce that the years in tables cannot be in the future
#
# CREATE TRIGGER IF NOT EXISTS trg_endangerment_insert
# BEFORE INSERT ON Endangerment_of_Animal
# FOR EACH ROW
# BEGIN
#     IF NEW.effect_year > YEAR(CURDATE()) THEN
#         SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'effect_year cannot be in the future';
#     END IF;
# END;

# %% language="sql"
# CREATE TRIGGER IF NOT EXISTS trg_endangerment_update
# BEFORE UPDATE ON Endangerment_of_Animal
# FOR EACH ROW
# BEGIN
#     IF NEW.effect_year > YEAR(CURDATE()) THEN
#         SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'effect_year cannot be in the future';
#     END IF;
# END;

# %% language="sql"
# CREATE TRIGGER IF NOT EXISTS trg_population_insert
# BEFORE INSERT ON Population_of_Animal
# FOR EACH ROW
# BEGIN
#     IF NEW.population_year > YEAR(CURDATE()) THEN
#         SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'population_year cannot be in the future';
#     END IF;
# END;

# %% language="sql"
# CREATE TRIGGER IF NOT EXISTS trg_population_update
# BEFORE UPDATE ON Population_of_Animal
# FOR EACH ROW
# BEGIN
#     IF NEW.population_year > YEAR(CURDATE()) THEN
#         SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'population_year cannot be in the future';
#     END IF;
# END;

# %% language="sql"
# CREATE TRIGGER IF NOT EXISTS trg_disaster_insert
# BEFORE INSERT ON Natural_Disaster
# FOR EACH ROW
# BEGIN
#     IF NEW.disaster_year > YEAR(CURDATE()) THEN
#         SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'disaster_year cannot be in the future';
#     END IF;
# END;

# %% language="sql"
# CREATE TRIGGER IF NOT EXISTS trg_disaster_update
# BEFORE UPDATE ON Natural_Disaster
# FOR EACH ROW
# BEGIN
#     IF NEW.disaster_year > YEAR(CURDATE()) THEN
#         SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'disaster_year cannot be in the future';
#     END IF;
# END;

# %% language="sql"
# CREATE TRIGGER IF NOT EXISTS trg_development_insert
# BEFORE INSERT ON Urban_Development
# FOR EACH ROW
# BEGIN
#     IF NEW.development_year > YEAR(CURDATE()) THEN
#         SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'development_year cannot be in the future';
#     END IF;
# END;

# %% language="sql"
# CREATE TRIGGER IF NOT EXISTS trg_development_update
# BEFORE UPDATE ON Urban_Development
# FOR EACH ROW
# BEGIN
#     IF NEW.development_year > YEAR(CURDATE()) THEN
#         SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'development_year cannot be in the future';
#     END IF;
# END;

# %% language="sql"
# CREATE TRIGGER IF NOT EXISTS trg_outbreak_insert
# BEFORE INSERT ON Disease_Outbreaks
# FOR EACH ROW
# BEGIN
#     IF NEW.outbreak_year > YEAR(CURDATE()) THEN
#         SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'outbreak_year cannot be in the future';
#     END IF;
# END;

# %% language="sql"
# CREATE TRIGGER IF NOT EXISTS trg_outbreak_update
# BEFORE UPDATE ON Disease_Outbreaks
# FOR EACH ROW
# BEGIN
#     IF NEW.outbreak_year > YEAR(CURDATE()) THEN
#         SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'outbreak_year cannot be in the future';
#     END IF;
# END;
