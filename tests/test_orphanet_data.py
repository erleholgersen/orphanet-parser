import pytest
from orphanet_parser import OrphanetData

CONSTANT_COLUMNS = [
    'orphacode',
    'expert_link', 
    'disorder_name', 
    'disorder_type', 
    'disorder_group'
    ]

@pytest.fixture
def parser():
    return OrphanetData("2024-07")

def test_natural_history(parser):
    df = parser.natural_history()

    assert len(df) == 6872
    assert len(df['orphacode'].unique()) == len(df)
    assert all(x in df.columns for x in CONSTANT_COLUMNS)
    
    custom_columns = ['average_age_of_onset', 'type_of_inheritance']
    assert all(x in df.columns for x in custom_columns)

def test_gene_associations(parser):
    df = parser.gene_associations()
    assert len(df) == 8164
    assert all(x in df.columns for x in CONSTANT_COLUMNS)

    parser_prev = OrphanetData(version="2023-12")
    df_prev = parser_prev.gene_associations()
    assert len(df_prev) == 8351

    smn_df = df[ df['gene_symbol'] == 'SMN1' ]
    assert len(smn_df) == 4

    EXPECTED_DISORDERS = [ f'Proximal spinal muscular atrophy type {x}' for x in range(1, 5) ] 
    assert sorted(EXPECTED_DISORDERS) == sorted(smn_df['disorder_name'])

    custom_columns = [
        'association_type', 'association_status', 'gene_symbol', 'gene_name', 'gene_type', 'external_references', 'source_of_validation'
        ]
    assert all(x in df.columns for x in custom_columns)

def test_functional_consequences(parser):
    df = parser.functional_consequences()

    assert all(x in df.columns for x in CONSTANT_COLUMNS)
    assert len(df) == 34904 

    custom_columns = [
        'disability', 'disability_category', 'reason_for_not_applicable', 'frequence_disability', 'temporality_disability', 'severity_disability', 'loss_of_ability', 'type', 'defined', 'source_of_validation', 'specific_management', 'annotation_date', 'status_disability',
        ]
    assert all(x in df.columns for x in custom_columns)

def test_prevalence(parser):
    df = parser.prevalence()

    assert all(x in df.columns for x in CONSTANT_COLUMNS)
    assert len(df) == 15982

    custom_columns = [
        'prevalence_source', 'prevalence_type', 'prevalence_qualification', 'prevalence_class', 
        'prevalence_geographic', 'prevalence_validation_status'
        ]
    assert all(x in df.columns for x in custom_columns)

def test_associated_phenotypes(parser):
    df = parser.associated_phenotypes()
    
    assert all(x in df.columns for x in CONSTANT_COLUMNS)
    assert len(df) == 114050

    custom_columns = ['hpo_id', 'hpo_term', 'hpo_frequency', 'diagnostic_criteria', 'source']
    assert all(x in df.columns for x in custom_columns)
  
    

