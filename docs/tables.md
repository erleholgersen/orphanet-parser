# Data Schemas

Details of data frames returned by orphanet-parser. All data is parsed from XML files provided by Orphanet, and column names are preserved (as snake case) to the extent possible. We currently do not sanitize the data, so some inconsistencies present in the Orphanet XML files persist (e.g. yes/no vs y/n for booleans).

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

One row represents one disorder/phenotype pair. A disorder may have multiple associated phenotypes.

|Column                         |Description                        |<div style="width:210px">Values</div>|
|:------------------------------|:----------------------------------|:------------------|
|orphacode                      |Unique identifier of disorder      |`int`|
|expert_link                    |Link to Orphanet page for disase   |`str`|
|disorder_name                  |Most generally accepted name of disorder   |`str`|
|disorder_group                 |Hierarchical level of the clinical entity.   |`"Group of disorders"`</br>`"Disorder"`</br> `"Subtype of disorder"` |
|hpo_id                         |Unique identifying number assigned by HPO to a given phenotype|`str`|
|hpo_term                       |Preferred name of HPO phenotype|`str`|
|hpo_frequency                  |Estimated frequency of phenotype within disorder|`"Obligate (100%)"`</br>`"Very frequent (99-80%)"`</br>`"Frequent (79-30%)"`</br>`"Occasional (29-5%)"`</br>`"Very rare (<4-1%)"`</br>`"Excluded (0%)"`|
|diagnostic_criteria            |Indicator of phenotype being a pathognomonic sign or a diagnostic criterion in disorder   |`"Diagnostic criterion"`</br>`"Pathognomonic sign"`|
|source                         |Reference                          |`str`|


## Functional consequences 

One row represents one disorder/functional consequence pair. A disorder may have multiple functional consequences.

|Column                         |Description                        |<div style="width:210px">Values</div>|
|:------------------------------|:----------------------------------|:------------------|
|orphacode                      |Unique identifier of disorder      |`int`|
|expert_link                    |Link to Orphanet page for disase   |`str`|
|disorder_name                  |Most generally accepted name of disorder   |`str`|
|disorder_group                 |Hierarchical level of the clinical entity.   |`"Group of disorders"`</br>`"Disorder"`</br> `"Subtype of disorder"` |
|disability                     |Name of disability|`str`|
|disability_category            |Category of disability|`“Activity limitation/participation restriction”`</br>`“No functional disability”`</br>`“Not applicable”`|
|reason_for_not_applicable      |If category is not applicable, the identified reason|`“Hypervariable functioning”`</br>`“Early death-causing disease”`</br>`“Not applicable for another reason”`|
|frequence_disability           |Frequency of the functional consequence in the given population|`"very frequent"`</br>`"frequent"`</br>`"occasional"`|
|temporality_disability         |Temporality of the functional consequence in the given population|`“permanent limitation/restriction”`</br> `“transient limitation/restriction”`</br>`“delayed acquisition”`|
|severity_disability            |Severity of the functional consequence in the given population|`“low”`</br>`“moderate”`</br>`“severe”`</br>`“complete”`</br>`“Unspecified”`|
|loss_of_ability                |Defined as a progressive and definitive loss of a skill or ability over the course of the disease|`"yes"`</br>`"no"`|
|type                           |Disability (functional consequence) or environmental factor|`"Disability"`</br>`"Environmental factor"`|
|defined                        |Indicator for severity, temporality, and frequency being defined|`"y"`</br>`"n"`|
|source_of_validation           |Source of validation of the given clinical entity’s annotation|`str`|
|specific_management            |If specific management protocol is known for the given disease, this field will indicate “y” for yes and all the annotations will have been conducted considering this specific management protocol.|`"y"`</br>`"n"`|
|annotation_date                |Date of annotation|`str`|
|status_disability              |Status of the validation of the given clinical entity’s annotation|`"Validated"`</br>`"Not validated"`|
