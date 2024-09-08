import pandas as pd

from .base import OrphanetParser
from .utils import get_optional_enum, get_list_field, OrphanetFile

class FunctionalConsequencesParser(OrphanetParser):
    _DATA_FILES = {
        "2024-07": OrphanetFile(
            url="https://storage.googleapis.com/orphanet-parser-data/2024-07/en_funct_consequences.xml",
            known_hash="md5:098ece382cd2de1aa77fda99d42fe120"
            )
        }
    _LIST_FIELDS = ('DisorderDisabilityRelevance', 'DisabilityDisorderAssociation', )

    def parse(self) -> pd.DataFrame:
        doc = self.read_xml(self.data_file.url, self.data_file.known_hash, self._LIST_FIELDS)

        df = []

        for parent in get_list_field(doc['JDBOR'], 'DisorderDisabilityRelevance'):
            disorder = parent['Disorder']
            for association in get_list_field(disorder, 'DisabilityDisorderAssociation'):
                df.append({
                    'orphacode': disorder['OrphaCode'],
                    'expert_link': disorder['ExpertLink']['#text'],
                    'disorder_name': disorder['Name']['#text'],
                    'disorder_type': get_optional_enum(disorder, 'DisorderType'),
                    'disorder_group': get_optional_enum(disorder, 'DisorderGroup'),
                    'disability': get_optional_enum(association, 'Disability'),
                    'frequence_disability': get_optional_enum(association, 'FrequenceDisability'),
                    'temporality_disability': get_optional_enum(association, 'TemporalityDisability'),
                    'severity_disability': get_optional_enum(association, 'SeverityDisability'),
                    'loss_of_ability': association['LossOfAbility'],
                    'type': association['Type'],
                    'defined': association['Defined'],
                    'source_of_validation': parent['SourceOfValidation'],
                    'specific_management': parent['SpecificManagement'],
                    'online': parent['Online'],
                    'annotation_date': parent['AnnotationDate'],
                    'status_disability': get_optional_enum(parent, 'StatusDisability'),
                    'disability_category': get_optional_enum(parent, 'DisabilityCategory')
                    })
    
        return pd.DataFrame(df)
