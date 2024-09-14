# Welcome to orphanet-parser

A Python package for accessing versioned data from Orphanet in pandas data frame format. All data was obtained from the [Orphadata_aggregated](https://github.com/Orphanet/Orphadata_aggregated/) repository.

Currently only a subset of the Engligh-language data is supported. 

## Versions

We currently support all releases since December 2022. Versions are named by their month of release. The table shows the size of each dataset in different versions.

|Dataset                    |2024-07    |2023-12    |2023-06    |2022-12    |
|:--------------------------|----------:|----------:|----------:|----------:|
|Phenotypes                 |114,050    |112,599    |111,765    |112,689    |
|Functional consequences    |34,904     |34,938     |34,670     |33,926     |
|Gene associations          |8164       |8351       |8301       |8248       |
|Prevalence                 |15,982     |15,982     |15,978     |15,916     |
|Natural history            |6872       |6795       |6638       |6650       |

## Future work

- Disorder classifications
- Linearization of disorders
- Ontologies