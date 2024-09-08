import pandas as pd

from .base import OrphanetParser
from .utils import get_optional_enum, get_list_field, OrphanetFile
from typing import Literal


class AssociatedPhenotypesParser(OrphanetParser):
    _DATA_FILES = {
        "2024-07": OrphanetFile(
            url="https://storage.googleapis.com/orphanet-parser-data/2024-07/en_product4.xml",
            known_hash="md5:679fd45c9de5d6057945a1c418ab81c2"
            )
        }

    # TODO: move to OrphanetFile class if this becomes problematic
    _LIST_FIELDS = ('HPODisorderAssociation', 'HPODisorderSetStatus')

    def parse(self) -> pd.DataFrame:
        doc = self.read_xml(self.data_file.url, self.data_file.known_hash, self._LIST_FIELDS)

        df = []

        for parent in get_list_field(doc['JDBOR'], 'HPODisorderSetStatus'):
            disorder = parent['Disorder']
            for association in get_list_field(disorder, 'HPODisorderAssociation'):
                df.append({
                    'orphacode': disorder['OrphaCode'],
                    'expert_link': disorder['ExpertLink']['#text'],
                    'disorder_name': disorder['Name']['#text'],
                    'disorder_type': get_optional_enum(disorder, 'DisorderType'),
                    'disorder_group': get_optional_enum(disorder, 'DisorderGroup'),
                    'hpo_id': association['HPO']['HPOId'],
                    'hpo_term': association['HPO']['HPOTerm'],
                    'hpo_frequency': get_optional_enum(association, 'HPOFrequency'),
                    'diagnostic_criteria': get_optional_enum(association, 'DiagnosticCriteria'),
                    'source': parent['Source'],
                    'validation_status': parent['ValidationStatus'],
                    'online': parent['Online'],
                    'validation_date': parent['ValidationDate']
                    })
    
        return pd.DataFrame(df)
