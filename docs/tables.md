# Data Schemas

Details of data frames returned by orphanet-parser.

## Prevalence

One row represents one prevalence estimate. A disorder may have multiple prevalence estimates.

|Column                         |Description                        |<div style="width:210px">Values</div>|
|:------------------------------|:----------------------------------|:------------------|
|orphacode                      |Unique identifier of disorder      |`int`|
|expert_link                    |Link to Orphanet page for disase   |`str`|
|disorder_name                  |Most generally accepted name of disorder   |`str`|
|disorder_group                 |Hierarchical level of the clinical entity.   |`"Group of disorders"`</br>`"Disorder"`</br> `"Subtype of disorder"` |
|prevalence_source              |Source of information for prevalence estimate|`str`|
|prevalence_type                |Type of prevalence estimate|`"Point prevalence"`</br>`"birth prevalence"`</br>`"lifelong prevalence"`</br>`"incidence"`</br>`"cases/families"`|
|prevalence_qualification       ||`"Value and Class"` </br>`"Only class"` </br>`"Case"` </br>`"Family"`|
|prevalence_class               |Estimated prevalence |`">1 / 1,000"`</br>`"1-5 / 10,000"`</br>`"6-9 / 10,000"`</br>`"1-9 / 100,000"`</br>`"1-9 / 1,000,000"`</br>`"<1 /1,000,000"`</br>`"Not yet documented"`</br>`"Unknown"`|
|prevalence_geographic          |Geographic area of prevalence type |`str`|
|prevalence_validation_status   |Validation status  |`"Validated"`</br>`"Not yet validated"`|



## Natural history

One row represents one disorder, and contains information on the age of onset and type of inheritance.

|Column                         |Description                        |<div style="width:210px">Values</div>|
|:------------------------------|:----------------------------------|:----------------------|
|orphacode                      |Unique identifier of disorder      |`int`                  |
|expert_link                    |Link to Orphanet page for disase   |`str`                  |
|disorder_name                  |Most generally accepted name of disorder   |`str`          |
|disorder_group                 |Hierarchical level of the clinical entity |`"Group of disorders"`</br>`"Disorder"`</br> `"Subtype of disorder"` 
|average_age_of_onset           |Groups corresponding to estimated average age of onset.</p>If more than one age of onset is provided, they are alphabetically sorted and semicolon-separated.|`"Antenatal"`</br>`"Neonatal"`</br>`"Infancy"`</br>`"Childhood"`</br>`"Adolescence"`</br>`"Adult"`</br>`"Elderly"`</br>`"All ages"`</br>`"No data available"`|
|type_of_inheritance            |Type of inheritance.</p>If more than one age of onset is provided, they are alphabetically sorted and semicolon-separated.|`"Autosomal dominant"`</br>`"Autosomal recessive"`</br>`"Multigenic/multifactorial"`</br>`"Mitochondrial inheritance"`</br>`"X-linked dominant"`</br>`"X-linked recessive"`</br>`"Not applicable"`</br>`"No data available"`</br>`"Unknown"`|

## Gene associations

One row represents one association between a gene and disorder.


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


## Associated phenotypes

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


## Functional consequences 

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