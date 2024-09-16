# Tutorials

The `OrphanetData` class provides access to all the individual data frames. By default, the latest version is used, currently `"2024-07"`.

```python
import pandas as pd
from orphanet_parser import OrphanetData

orphanet = OrphanetData()
```

The following sections walk through examples of analyses one might want to do with the orphanet-parser package. 

## Finding disorders associated with a gene

Imagine we are interested in finding information about disorders associated with a particular disease. We can query the gene associations data by gene symbol.

```python
gene_df = orphanet.gene_associations()
smn1_disorders = gene_df[ gene_df['gene_symbol'] == 'SMN1' ].copy()
```

In the case of SMN1, there are four associated disorders: Proximal spinal muscular atrophy type 1-4. These are all classified as subtypes of a disorder, and are caused by germline mutations in the SMN1 gene.

```python
smn1_disorders
```

|   orphacode | expert_link                                                        | disorder_name                           | disorder_type    | disorder_group      | association_type                        | association_status   | gene_symbol   | gene_name                             | gene_type                 | external_references                                                                                                     | source_of_validation   |
|------------:|:-------------------------------------------------------------------|:----------------------------------------|:-----------------|:--------------------|:----------------------------------------|:---------------------|:--------------|:--------------------------------------|:--------------------------|:------------------------------------------------------------------------------------------------------------------------|:-----------------------|
|       83330 | http://www.orpha.net/consor/cgi-bin/OC_Exp.php?lng=en&Expert=83330 | Proximal spinal muscular atrophy type 1 | Clinical subtype | Subtype of disorder | Disease-causing germline mutation(s) in | Assessed             | SMN1          | survival of motor neuron 1, telomeric | gene with protein product | Ensembl: ENSG00000172062; Genatlas: SMN1; HGNC: 11117; OMIM: 600354; Reactome: Q16637; SwissProt: Q16637; ClinVar: SMN1 | 20301526[PMID]         |
|       83419 | http://www.orpha.net/consor/cgi-bin/OC_Exp.php?lng=en&Expert=83419 | Proximal spinal muscular atrophy type 3 | Clinical subtype | Subtype of disorder | Disease-causing germline mutation(s) in | Assessed             | SMN1          | survival of motor neuron 1, telomeric | gene with protein product | Ensembl: ENSG00000172062; Genatlas: SMN1; HGNC: 11117; OMIM: 600354; Reactome: Q16637; SwissProt: Q16637; ClinVar: SMN1 | 20301526[PMID]         |
|       83420 | http://www.orpha.net/consor/cgi-bin/OC_Exp.php?lng=en&Expert=83420 | Proximal spinal muscular atrophy type 4 | Clinical subtype | Subtype of disorder | Disease-causing germline mutation(s) in | Assessed             | SMN1          | survival of motor neuron 1, telomeric | gene with protein product | Ensembl: ENSG00000172062; Genatlas: SMN1; HGNC: 11117; OMIM: 600354; Reactome: Q16637; SwissProt: Q16637; ClinVar: SMN1 | 20301526[PMID]         |
|       83418 | http://www.orpha.net/consor/cgi-bin/OC_Exp.php?lng=en&Expert=83418 | Proximal spinal muscular atrophy type 2 | Clinical subtype | Subtype of disorder | Disease-causing germline mutation(s) in | Assessed             | SMN1          | survival of motor neuron 1, telomeric | gene with protein product | Ensembl: ENSG00000172062; Genatlas: SMN1; HGNC: 11117; OMIM: 600354; Reactome: Q16637; SwissProt: Q16637; ClinVar: SMN1 | 20301526[PMID]         |

The `source_of_validation` column contains the reference for the association. In this case, all four associations were described in [GeneReviews](https://pubmed.ncbi.nlm.nih.gov/20301526/).

The natural history dataset contains more information about the inheritance pattern and age of onset of each of these disorders. The `orphacode` is a unique disorder identifier and can be used for merging.

```python
natural_history_df = orphanet.natural_history()
smn1_natural_history = pd.merge(smn1_disorders[['orphacode', 'disorder_name']], natural_history_df, how='left', validate='1:1')
smn1_natural_history
```

|   orphacode | disorder_name                           | expert_link                                                        | disorder_type    | disorder_group      | average_age_of_onset                  | type_of_inheritance   |
|------------:|:----------------------------------------|:-------------------------------------------------------------------|:-----------------|:--------------------|:--------------------------------------|:----------------------|
|       83330 | Proximal spinal muscular atrophy type 1 | http://www.orpha.net/consor/cgi-bin/OC_Exp.php?lng=en&Expert=83330 | Clinical subtype | Subtype of disorder | Infancy; Neonatal                     | Autosomal recessive   |
|       83419 | Proximal spinal muscular atrophy type 3 | http://www.orpha.net/consor/cgi-bin/OC_Exp.php?lng=en&Expert=83419 | Clinical subtype | Subtype of disorder | Adolescent; Adult; Childhood; Infancy | Autosomal recessive   |
|       83420 | Proximal spinal muscular atrophy type 4 | http://www.orpha.net/consor/cgi-bin/OC_Exp.php?lng=en&Expert=83420 | Clinical subtype | Subtype of disorder | Adult                                 | Autosomal recessive   |
|       83418 | Proximal spinal muscular atrophy type 2 | http://www.orpha.net/consor/cgi-bin/OC_Exp.php?lng=en&Expert=83418 | Clinical subtype | Subtype of disorder | Infancy                               | Autosomal recessive   |

The spinal muscular atrophy subtypes are numbered by the age of onset, with type 1 manifesting in infancy and type 4 in adulthood. All four subtypes have autosomal recessive inheritance.

We can also get prevalence estimates for each by cross-referencing the prevalence dataset. A disorder may have multiple prevalence estimates, and each is represented by a row. 

```python
prevalence_df = orphanet.prevalence()
smn1_prevalence = pd.merge(smn1_disorders[['orphacode', 'disorder_name']], prevalence_df, how='left', validate='1:m')
smn1_prevalence
```

|   orphacode | disorder_name                           | expert_link                                                        | disorder_type    | disorder_group      | prevalence_source            | prevalence_type     | prevalence_qualification   | prevalence_class   | prevalence_geographic   | prevalence_validation_status   |
|------------:|:----------------------------------------|:-------------------------------------------------------------------|:-----------------|:--------------------|:-----------------------------|:--------------------|:---------------------------|:-------------------|:------------------------|:-------------------------------|
|       83330 | Proximal spinal muscular atrophy type 1 | http://www.orpha.net/consor/cgi-bin/OC_Exp.php?lng=en&Expert=83330 | Clinical subtype | Subtype of disorder | ORPHANET                     | Annual incidence    | Value and class            | 1-9 / 1 000 000    | Europe                  | Not yet validated              |
|       83330 | Proximal spinal muscular atrophy type 1 | http://www.orpha.net/consor/cgi-bin/OC_Exp.php?lng=en&Expert=83330 | Clinical subtype | Subtype of disorder | ORPHANET                     | Point prevalence    | Class only                 | 1-9 / 100 000      | Europe                  | Not yet validated              |
|       83419 | Proximal spinal muscular atrophy type 3 | http://www.orpha.net/consor/cgi-bin/OC_Exp.php?lng=en&Expert=83419 | Clinical subtype | Subtype of disorder | 1483045[PMID]                | Prevalence at birth | Value and class            | 1-9 / 1 000 000    | Italy                   | Validated                      |
|       83419 | Proximal spinal muscular atrophy type 3 | http://www.orpha.net/consor/cgi-bin/OC_Exp.php?lng=en&Expert=83419 | Clinical subtype | Subtype of disorder | 28676062[PMID]_ORPHANET      | Point prevalence    | Class only                 | 1-9 / 1 000 000    | Europe                  | Validated                      |
|       83420 | Proximal spinal muscular atrophy type 4 | http://www.orpha.net/consor/cgi-bin/OC_Exp.php?lng=en&Expert=83420 | Clinical subtype | Subtype of disorder | ORPHANET                     | Annual incidence    | Class only                 | Unknown            | Europe                  | Validated                      |
|       83420 | Proximal spinal muscular atrophy type 4 | http://www.orpha.net/consor/cgi-bin/OC_Exp.php?lng=en&Expert=83420 | Clinical subtype | Subtype of disorder | ORPHANET                     | Point prevalence    | Class only                 | Unknown            | Europe                  | Validated                      |
|       83418 | Proximal spinal muscular atrophy type 2 | http://www.orpha.net/consor/cgi-bin/OC_Exp.php?lng=en&Expert=83418 | Clinical subtype | Subtype of disorder | 10677857[PMID]_1483045[PMID] | Prevalence at birth | Value and class            | 1-9 / 100 000      | Europe                  | Validated                      |
|       83418 | Proximal spinal muscular atrophy type 2 | http://www.orpha.net/consor/cgi-bin/OC_Exp.php?lng=en&Expert=83418 | Clinical subtype | Subtype of disorder | 28676062[PMID]_ORPHANET      | Point prevalence    | Class only                 | 1-9 / 100 000      | Worldwide               | Validated                      |

There are different types of prevalence estimates, as indicated by the `prevalence_type` column. 

```python
phenotypes = orphanet.associated_phenotypes()
smn1_phenotypes = pd.merge(smn1_disorders[['orphacode', 'disorder_name']], phenotypes, how='left', validate='1:m')
```

The functional consequences data contains information on clinician-reported consequences of the disease. 

```python
func_consequences = orphanet.functional_consequences()
smn1_func_consequences = pd.merge(smn1_disorders[['orphacode', 'disorder_name']], func_consequences, how='inner', validate='1:m')
```

|   orphacode | disorder_name                           | expert_link                                                        | disorder_type    | disorder_group      | disability                                                                             | frequence_disability   | temporality_disability   | severity_disability   | loss_of_ability   | type                 | defined   | source_of_validation                 | specific_management   | online   | annotation_date       | status_disability   | disability_category                           |
|------------:|:----------------------------------------|:-------------------------------------------------------------------|:-----------------|:--------------------|:---------------------------------------------------------------------------------------|:-----------------------|:-------------------------|:----------------------|:------------------|:---------------------|:----------|:-------------------------------------|:----------------------|:---------|:----------------------|:--------------------|:----------------------------------------------|
|       83419 | Proximal spinal muscular atrophy type 3 | http://www.orpha.net/consor/cgi-bin/OC_Exp.php?lng=en&Expert=83419 | Clinical subtype | Subtype of disorder | Learning to write                                                                      | Occasional             | Acquisition delay        | Low                   | n                 | Disability           | y         | Dr Emmanuelle SALORT CAMPANA[Expert] | n                     | y        | 2022-11-01 00:00:00.0 | Not validated       | Activity limitation/participation restriction |
|       83419 | Proximal spinal muscular atrophy type 3 | http://www.orpha.net/consor/cgi-bin/OC_Exp.php?lng=en&Expert=83419 | Clinical subtype | Subtype of disorder | Learning to write                                                                      | Occasional             | Permanent limitation     | Low                   | y                 | Disability           | y         | Dr Emmanuelle SALORT CAMPANA[Expert] | n                     | y        | 2022-11-01 00:00:00.0 | Not validated       | Activity limitation/participation restriction |
|       83419 | Proximal spinal muscular atrophy type 3 | http://www.orpha.net/consor/cgi-bin/OC_Exp.php?lng=en&Expert=83419 | Clinical subtype | Subtype of disorder | Writing                                                                                |                        |                          |                       | y                 | Disability           | n         | Dr Emmanuelle SALORT CAMPANA[Expert] | n                     | y        | 2022-11-01 00:00:00.0 | Not validated       | Activity limitation/participation restriction |
|       83419 | Proximal spinal muscular atrophy type 3 | http://www.orpha.net/consor/cgi-bin/OC_Exp.php?lng=en&Expert=83419 | Clinical subtype | Subtype of disorder | Speaking                                                                               | Occasional             | Permanent limitation     | Low                   | y                 | Disability           | y         | Dr Emmanuelle SALORT CAMPANA[Expert] | n                     | y        | 2022-11-01 00:00:00.0 | Not validated       | Activity limitation/participation restriction |
|       83419 | Proximal spinal muscular atrophy type 3 | http://www.orpha.net/consor/cgi-bin/OC_Exp.php?lng=en&Expert=83419 | Clinical subtype | Subtype of disorder | Producing messages in sign language                                                    |                        |                          |                       | y                 | Disability           | n         | Dr Emmanuelle SALORT CAMPANA[Expert] | n                     | y        | 2022-11-01 00:00:00.0 | Not validated       | Activity limitation/participation restriction |
|       83419 | Proximal spinal muscular atrophy type 3 | http://www.orpha.net/consor/cgi-bin/OC_Exp.php?lng=en&Expert=83419 | Clinical subtype | Subtype of disorder | Producing nonverbal messages                                                           |                        |                          |                       | y                 | Disability           | n         | Dr Emmanuelle SALORT CAMPANA[Expert] | n                     | y        | 2022-11-01 00:00:00.0 | Not validated       | Activity limitation/participation restriction |
|       83419 | Proximal spinal muscular atrophy type 3 | http://www.orpha.net/consor/cgi-bin/OC_Exp.php?lng=en&Expert=83419 | Clinical subtype | Subtype of disorder | Writing messages                                                                       |                        |                          |                       | y                 | Disability           | n         | Dr Emmanuelle SALORT CAMPANA[Expert] | n                     | y        | 2022-11-01 00:00:00.0 | Not validated       | Activity limitation/participation restriction |
|       83419 | Proximal spinal muscular atrophy type 3 | http://www.orpha.net/consor/cgi-bin/OC_Exp.php?lng=en&Expert=83419 | Clinical subtype | Subtype of disorder | Using communication devices                                                            |                        |                          |                       | y                 | Disability           | n         | Dr Emmanuelle SALORT CAMPANA[Expert] | n                     | y        | 2022-11-01 00:00:00.0 | Not validated       | Activity limitation/participation restriction |
|       83419 | Proximal spinal muscular atrophy type 3 | http://www.orpha.net/consor/cgi-bin/OC_Exp.php?lng=en&Expert=83419 | Clinical subtype | Subtype of disorder | Standing                                                                               |                        |                          |                       | y                 | Disability           | n         | Dr Emmanuelle SALORT CAMPANA[Expert] | n                     | y        | 2022-11-01 00:00:00.0 | Not validated       | Activity limitation/participation restriction |
|       83419 | Proximal spinal muscular atrophy type 3 | http://www.orpha.net/consor/cgi-bin/OC_Exp.php?lng=en&Expert=83419 | Clinical subtype | Subtype of disorder | Sitting                                                                                |                        |                          |                       | y                 | Disability           | n         | Dr Emmanuelle SALORT CAMPANA[Expert] | n                     | y        | 2022-11-01 00:00:00.0 | Not validated       | Activity limitation/participation restriction |



## Visualizing prevalence estimates

```
prevalence_df = orphanet.prevalence()
```