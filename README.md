# orphanet-parser

Pythonic interface to key data from Orphanet. Data was obtained from the [Orphadata](https://github.com/Orphanet/Orphadata_aggregated/tree/master) GitHub repository. The goal of the Python interface is to provide access to pandas data frames, without having to parse XML files. 

The package only supports English-language data, and currently does not provide access to ontologies or disease linearization data. 

## Dataset schemas

All information is obtained from Orphanet. To the extent possible, 

### Prevalence

One row represents one prevalence estimate. A disorder may have multiple prevalence estimates.

|Column                         |Description                        |
|:------------------------------|:----------------------------------|
|orphacode                      |Unique identifier of disorder      |
|expert_link                    |Link to Orphanet page for disase   |
|disorder_name                  |Most generally accepted name of disorder   |
|disorder_group                 |Hierarchical level of the clinical entity. Can be either "Group of disorders", "Disorder", or "Subtype of disorder"    |
|prevalence_source              |Source of information for prevalence estimate|
|prevalence_type                |One of "Point prevalence", "birth prevalence", "lifelong prevalence", "incidence", and "cases/families" |
|prevalence_qualification       |One of "Value and Class", "Only class", "Case", and "Family"
|prevalence_class               |Estimated prevalence. One of ">1 / 1,000", "1-5 / 10,000", "6-9 / 10,000", "1-9 / 100,000", "1-9 / 1,000,000", "<1 /1,000,000", "Not yet documented", and "Unknown"    |
|prevalence_geographic          |Geographic area of prevalence type |
|prevalence_validation_status   |One of "Validated", and "Not yet validated"    |

### Natural history



|Column                         |Description                        |
|:------------------------------|:----------------------------------|
|orphacode                      |Unique identifier of disorder      |
|expert_link                    |Link to Orphanet page for disase   |
|disorder_name                  |Most generally accepted name of disorder   |
|disorder_group                 |Hierarchical level of the clinical entity. Can be either "Group of disorders", "Disorder", or "Subtype of disorder"    |
|average_age_of_onset           |Groups corresponding to estimated average age of onset: "Antenatal", "Neonatal", "Infancy", 
"Childhood",
"Adolescence", "Adult", "Elderly", "All ages" and "No data available". If more than one age of onset is provided, they are semicolon-separated and alphabetically sorted.
|type_of_inheritance            |

### Gene associations


|Column                         |Description                        |
|:------------------------------|:----------------------------------|
|orphacode                      |Unique identifier of disorder      |
|expert_link                    |Link to Orphanet page for disase   |
|disorder_name                  |Most generally accepted name of disorder   |
|disorder_group                 |Hierarchical level of the clinical entity. Can be either "Group of disorders", "Disorder", or "Subtype of disorder"    |
|hpo_id                         |
|hpo_term                       |
|hpo_frequency                  |
|diagnostic_criteria            |
|source                         |
|validation_status              |
|online                         |
|validation_date                |


### Associated phenotypes

|Column                         |Description                        |
|:------------------------------|:----------------------------------|
|orphacode                      |Unique identifier of disorder      |
|expert_link                    |Link to Orphanet page for disase   |
|disorder_name                  |Most generally accepted name of disorder   |
|disorder_group                 |Hierarchical level of the clinical entity. Can be either "Group of disorders", "Disorder", or "Subtype of disorder"    |
|hpo_id                         |
|hpo_term                       |
|hpo_frequency                  |
|diagnostic_criteria            |
|source                         |
|validation_status              |
|online                         |
|validation_date                |


### Functional consequences 

|Column                         |Description                        |
|:------------------------------|:----------------------------------|
|orphacode                      |Unique identifier of disorder      |
|expert_link                    |Link to Orphanet page for disase   |
|disorder_name                  |Most generally accepted name of disorder   |
|disorder_group                 |Hierarchical level of the clinical entity. Can be either "Group of disorders", "Disorder", or "Subtype of disorder"    |
|disability                     |
|frequence_disability           |
|temporality_disability         |
|severity_disability            |
|loss_of_ability                |
|type                           |
|defined                        |
|source_of_validation           |
|specific_management            |
|online                         |
|annotation_date                |
|status_disability              |
|disability_category            |

## Versions

Size of different datasets by version.

|Dataset                    |2024-07    |2023-12    |2023-06    |2022-12    |
|:--------------------------|----------:|----------:|----------:|----------:|
|Phenotypes                 |114050     |112599     |111765     |112689     |
|Functional consequences    |34904      |34938      |34670      |33926      |
|Gene associations          |8164       |8351       |8301       |8248       |
|Prevalence                 |15982      |15982      |15978      |15916      |
|Natural history            |6872       |6795       |6638       |6650       |

## Future work

- Disorder classifications
- Linearization of disorders
- Ontologies