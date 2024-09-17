# Data Schemas

Details of data frames returned by orphanet-parser. All data is parsed from XML files provided by Orphanet, and column names are preserved (as snake case) to the extent possible. 

For more detailed information on the datasets, see the [Orphadata free access product description](https://www.orphadata.com/docs/OrphadataFreeAccessProductsDescription.pdf).

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


|Column                         |Description                        |<div style="width:210px">Values</div>|
|:------------------------------|:----------------------------------|:----------------------|
|orphacode                      |Unique identifier of disorder      |`int`                  |
|expert_link                    |Link to Orphanet page for disase   |`str`                  |
|disorder_name                  |Most generally accepted name of disorder   |`str`          |
|disorder_group                 |Hierarchical level of the clinical entity |`"Group of disorders"`</br>`"Disorder"`</br> `"Subtype of disorder"` 
|association_type               |Gene-disease relationship|`"Biomarker tested in"`</br>`"Candidate gene tested in"`</br>`"Disease-causing germline mutation(s) (gain of function) in"`</br>`"Disease-causing germline mutation(s) (loss of function) in"`</br>`"Disease-causing germline mutation(s) in"`</br>`"Disease-causing somatic mutation(s) in"`</br>`"Major susceptibility factor in"`</br>`"Modifying germline mutation in"`</br>`"Part of a fusion gene in"`</br>`"Role in the phenotype of"` |
|association_status             |Gene-disease association status    |`"Validated"`</br>`"Not validated"`    |
|gene_symbol                    |HGNC-approved gene symbol  |`str`      |
|gene_name                      |Full gene name     |`str`|
|gene_type                      |Gene type  |`"gene with protein product"`</br>`"Non-coding RNA"`</br>`"Disorder-associated locus"`|
|external_references            |List of references in HGNC, OMIM, GenAtlas and UniProtKB, Ensembl, Reactome and IU-PHAR associated with a given gene|`str`|
|source_of_validation           |Listed reference for a given source associated with a gene|`str`|

## Associated phenotypes

|Column                         |Description                        |<div style="width:210px">Values</div>|
|:------------------------------|:----------------------------------|:------------------|
|orphacode                      |Unique identifier of disorder      |`int`|
|expert_link                    |Link to Orphanet page for disase   |`str`|
|disorder_name                  |Most generally accepted name of disorder   |`str`|
|disorder_group                 |Hierarchical level of the clinical entity.   |`"Group of disorders"`</br>`"Disorder"`</br> `"Subtype of disorder"` |
|hpo_id                         |
|hpo_term                       |
|hpo_frequency                  |
|diagnostic_criteria            |
|source                         |
|validation_status              |
|online                         |
|validation_date                |


## Functional consequences 

|Column                         |Description                        |<div style="width:210px">Values</div>|
|:------------------------------|:----------------------------------|:------------------|
|orphacode                      |Unique identifier of disorder      |`int`|
|expert_link                    |Link to Orphanet page for disase   |`str`|
|disorder_name                  |Most generally accepted name of disorder   |`str`|
|disorder_group                 |Hierarchical level of the clinical entity.   |`"Group of disorders"`</br>`"Disorder"`</br> `"Subtype of disorder"` |
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