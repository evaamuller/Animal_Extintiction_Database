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
# %load_ext sql
import os, sys
from dotenv import load_dotenv
load_dotenv()

password = os.getenv("DB_PASSWORD")
os.environ["DATABASE_URL"] = f"mysql+pymysql://root:{password}@localhost/animal_extinction_db"

# %% language="sql"
# # 1. Location
# INSERT INTO Location (location_name, biome, area_sq_km, protection_level) VALUES
# ('Daintree Rainforest', 'Tropical Forest', 1200.50, 'II'),
# ('Great Barrier Reef', 'Marine', 344400.00, 'I'),
# ('Kakadu National Park', 'Wetland', 19804.00, 'II'),
# ('Simpson Desert', 'Desert', 176500.00, 'IV'),
# ('Snowy Mountains', 'Temperate Forest', 6900.00, 'III'),
# ('Tasmanian Wilderness', 'Temperate Forest', 15800.00, 'I'),
# ('Great Victoria Desert', 'Desert', 424400.00, 'VI'),
# ('Murray-Darling Basin', 'Wetland', 1061469.00, 'V');
#
# # 2. Animal
# INSERT INTO Animal (genus_name, species_name, common_name, animal_class, diet, native) VALUES
# ('Phascolarctos', 'cinereus', 'Koala', 'Mammalia', 'Herbivore', TRUE),
# ('Macropus', 'giganteus', 'Eastern Grey Kangaroo', 'Mammalia', 'Herbivore', TRUE),
# ('Ornithorhynchus', 'anatinus', 'Platypus', 'Mammalia', 'Carnivore', TRUE),
# ('Vombatus', 'ursinus', 'Common Wombat', 'Mammalia', 'Herbivore', TRUE),
# ('Sarcophilus', 'harrisii', 'Tasmanian Devil', 'Mammalia', 'Scavenger', TRUE),
# ('Dromaius', 'novaehollandiae', 'Emu', 'Aves', 'Omnivore', TRUE),
# ('Cacatua', 'galerita', 'Sulphur-crested Cockatoo', 'Aves', 'Granivore', TRUE),
# ('Aquila', 'audax', 'Wedge-tailed Eagle', 'Aves', 'Carnivore', TRUE),
# ('Crocodylus', 'porosus', 'Saltwater Crocodile', 'Reptilia', 'Carnivore', TRUE),
# ('Chelonia', 'mydas', 'Green Sea Turtle', 'Reptilia', 'Herbivore', TRUE),
# ('Litoria', 'caerulea', 'Australian Green Tree Frog', 'Amphibia', 'Insectivore', TRUE),
# ('Thylacinus', 'cynocephalus', 'Thylacine', 'Mammalia', 'Carnivore', TRUE),
# ('Panthera', 'tigris', 'Bengal Tiger', 'Mammalia', 'Carnivore', FALSE),
# ('Vulpes', 'vulpes', 'Red Fox', 'Mammalia', 'Omnivore', FALSE),
# ('Oryctolagus', 'cuniculus', 'European Rabbit', 'Mammalia', 'Herbivore', FALSE);
#
# # 3. Endangerment_of_Animal
# # (animal_id references the insert order above, 1-15)
# INSERT INTO Endangerment_of_Animal (animal_id, effect_year, level) VALUES
# (1, 2012, 'VU'),   # Koala - Vulnerable (2012)
# (1, 2022, 'EN'),   # Koala - reclassified Endangered (2022)
# (2, 2020, 'LC'),   # Eastern Grey Kangaroo
# (3, 2016, 'NT'),   # Platypus
# (3, 2020, 'VU'),   # Platypus - later reassessed
# (4, 2000, 'LC'),   # Wombat
# (5, 2008, 'EN'),   # Tasmanian Devil (facial tumour disease impact)
# (8, 2000, 'LC'),   # Wedge-tailed Eagle
# (9, 1996, 'LC'),   # Saltwater Crocodile
# (10, 1982, 'EN'),  # Green Sea Turtle
# (12, 1982, 'EX'),  # Thylacine - Extinct
# (13, 2010, 'EN');  # Bengal Tiger
#
# # 4. Predator_and_Prey
# INSERT INTO Predator_and_Prey (animal_id_predator, animal_id_prey) VALUES
# (8, 1),   # Wedge-tailed Eagle preys on Koala (joeys, rare)
# (8, 2),   # Wedge-tailed Eagle preys on young Kangaroo
# (9, 4),   # Saltwater Crocodile preys on Wombat
# (9, 10),  # Saltwater Crocodile preys on Green Sea Turtle
# (5, 11),  # Tasmanian Devil preys on Tree Frog
# (12, 4),  # Thylacine preys on Wombat (historic)
# (14, 6),  # Red Fox preys on Emu chicks
# (14, 15); # Red Fox preys on Rabbit
#

# %% language="sql"
#
# DELETE FROM Population_of_Animal;  # Clear existing data
#
# # 5. Population_of_Animal
# INSERT INTO Population_of_Animal (animal_id, location_id, population_year, population_size) VALUES
# (1, 1, 2010, 15000),
# (1, 1, 2020, 9800),
# (2, 5, 2015, 250000),
# (2, 5, 2022, 300000),
# (3, 5, 2018, 30000),
# (3, 5, 2023, 22000),
# (5, 6, 2005, 140000),
# (5, 6, 2020, 25000),
# (8, 4, 2015, 12000),
# (9, 3, 2019, 100000),
# (10, 2, 2000, 85000),
# (10, 2, 2021, 45000),
# (12, 6, 1901, 5000),
# (12, 6, 1936, 0),
# (6, 7, 2018, 630000);

# %% language="sql"
# # 6. Climate
# INSERT INTO Climate (record_date, location_id, temperature_min_celsius, temperature_max_celsius, rainfall_mm) VALUES
# ('2023-01-15', 1, 22.5, 33.0, 210.4),
# ('2023-01-15', 4, 18.0, 45.2, 0.0),
# ('2023-06-15', 6, 2.1, 11.5, 85.6),
# ('2023-06-15', 3, 15.0, 32.0, 45.2),
# ('2022-12-01', 2, 24.0, 31.5, 150.0),
# ('2022-07-20', 5, -3.5, 6.0, 60.8),
# ('2021-03-10', 7, 20.0, 40.0, 5.1),
# ('2020-11-05', 8, 16.5, 34.0, 22.3);

# %% language="sql"
# # 7. Natural_Disaster
# INSERT INTO Natural_Disaster (disaster_type, disaster_year, location_id, disaster_area_sq_km) VALUES
# ('Bushfire', 2019, 6, 1200.50),   # Black Summer bushfires, Tasmania
# ('Bushfire', 2020, 5, 800.25),    # Snowy Mountains bushfires
# ('Drought', 2018, 8, 50000.00),   # Murray-Darling Basin drought
# ('Flood', 2022, 3, 3000.00),      # Kakadu flooding
# ('Cyclone', 2011, 2, 15000.00);   # Cyclone affecting Great Barrier Reef

# %% language="sql"
# # 8. Urban_Development
# INSERT INTO Urban_Development (development_name, location_id, development_type, development_year, development_area_sq_km) VALUES
# ('Cairns Coastal Expansion', 1, 'Residential', 1995, 45.30),
# ('Murray Basin Irrigation Scheme', 8, 'Agricultural', 1970, 3200.00),
# ('Snowy Hydro Expansion', 5, 'Infrastructure', 1965, 120.75),
# ('Darwin Port Development', 3, 'Industrial', 2015, 18.60),
# ('Alice Springs Growth Corridor', 4, 'Residential', 2005, 60.00);

# %% language="sql"
# # 9. Diseases
# INSERT INTO Diseases (disease_name, disease_type) VALUES
# ('Devil Facial Tumour Disease', 'Cancer'),
# ('Chlamydia', 'Bacterial'),
# ('Chytrid Fungus', 'Fungal'),
# ('Avian Influenza', 'Viral'),
# ('Toxoplasmosis', 'Parasitic');

# %% language="sql"
# # 10. Disease_Outbreaks
# INSERT INTO Disease_Outbreaks (disease_id, animal_id, location_id, outbreak_year, disease_mortality_percent) VALUES
# (1, 5, 6, 1996, 70.50),   # DFTD in Tasmanian Devils
# (1, 5, 6, 2010, 85.00),
# (2, 1, 1, 2015, 30.25),   # Chlamydia in Koalas
# (3, 11, 5, 2005, 60.00),  # Chytrid fungus in tree frogs
# (4, 6, 7, 2020, 15.75),   # Avian influenza in Emus
# (5, 2, 5, 2018, 5.50);    # Toxoplasmosis in Kangaroos

# %% language="sql"
#
# # 11. Location_Of_Animal
# INSERT INTO Location_Of_Animal (animal_id, location_id) VALUES
# (1, 1), (1, 5),
# (2, 5), (2, 7), (2, 8),
# (3, 5), (3, 6),
# (4, 5), (4, 6),
# (5, 6),
# (6, 4), (6, 7), (6, 8),
# (7, 1), (7, 3),
# (8, 4), (8, 5), (8, 7),
# (9, 3), (9, 1),
# (10, 2),
# (11, 5), (11, 1),
# (15, 8);
