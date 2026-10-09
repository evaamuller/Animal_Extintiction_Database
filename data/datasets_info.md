# Real data integration

2 data sources were identified to be inserted into our database.

Both of the datasets were preprocessed and converted to "cleaned" .csv files to only include data relevant to our database and in the correct format to avoid conflicts with our schema - see [TSSL_preprocessing](/sql/threatened_species_preprocessing.ipynb) and [TSX_preprocessing](/sql/tsx_preprocessing.ipynb) for details.

## TSX dataset

The index is managed by the NCRIS-funded Terrestrial Ecosystem Research Network (TERN) project at The University of Queensland and supported by the Australian Government Department of Climate Change, Energy, the Environment and Water (DCCEEW).

All TSX data available at [TSX](https://tsx.org.au/tsx/) are openly accessible and are licensed under a Creative Commons – Attribution 4.0 International licence (CC BY 4.0).

Publication date of the data: 25-11-2025

The dataset contains:

1) 193,500 yearly population values (1950–2022) from 25,164 monitored time series, for 217 animal species and 178 plant taxa. Plants are left out in our database as we focus only on animals.

2) Per value the data contains: species, site, region, unit of measurement (there are 103 different possible units), year and the population 

3) There are 15,724 monitoring sites in 346 regions


## Threatened Species State Lists

Publication date of the data: 28-08-2026

This dataset in available at [TSSL](https://data.gov.au/data/dataset/threatened-species-state-lists) under the Creative Commons Attribution 3.0 Australia license.

The dataset contains:

1) 2,222 species, of which 700 are animals and 1,522 plants. Plants are left out in our database as we focus only on animals.

2) Per value the data cointains: scientific name, common name, threatened status, genus, species, subspecies, class, family, and a Yes/- column for each state or territory where it occurs.

## Dataset properties
After cleaning the datasets and identifying relevant data (see [data_insertion](sql/data_insertion.ipynb)) following properties were identified:

| Dataset             | TSX                                                                  | TSSL                                                                                                  |
|---------------------|----------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------|
| Attributes included | `Scientific Name`, `Common Name`, `Class`, `State`, `Level` and year columns | `Scientific Name`, `Common Name`, `Threatened status`, `Kingdom`, `Class`, `Date extracted` and state columns |
| Number of rows      | 141                                                                  | 700                                                                                                   |
| Number of columns   | 79                                                                   | 24                                                                                                    |

The datasets intersect in only 5 animals, and do not share all of the attributes, thus they are disjoint.
