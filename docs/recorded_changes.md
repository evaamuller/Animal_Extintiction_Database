# Changes made after real-world data insertion

## Schema changes
Generally, we aimed to make minimal changes to the schema and instead did extensive preprocessing to ensure the data meets the constraints defined by our schema. Still, one change was made:

| Entity affected | Attribute changed | Change made | Reason |
|-----------------|-------------------|-------------|--------|
| Animal | `BOOLEAN NATIVE DEFAULT TRUE` | Removed `DEFAULT TRUE` | The real-world datasets contain no information on whether an animal is native, so we cannot automatically assume that it is |

This change is reflected in our [ERD](/docs/erd.pdf) as well.

## Normalization
As mentioned above, we did extensive preprocessing to ensure the inserted data was in the correct format and also normalized. This process was done using pandas DataFrames, where we could visually inspect that at least a limited number of rows were in the correct format. We also checked for missing values and incorrect formatting. However, extensive testing on the final cleaned data was not done, so the authors acknowledge that there may be a normalization violation that the work done did not reveal. This is a potential limitation and something that should be addressed in the future.
