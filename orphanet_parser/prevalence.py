import pandas as pd

from .base import BaseParser
from .utils import get_optional_enum, get_list_field, OrphanetFile

class PrevalenceParser(BaseParser):
    _DATA_FILES = {
        "2024-07": OrphanetFile(
            url="https://storage.googleapis.com/orphanet-parser-data/2024-07/en_product9_prev.xml",
            known_hash="md5:e47834377343211f3e71c829f635cc3b"
            ),
        "2023-12": OrphanetFile(
            url="https://storage.googleapis.com/orphanet-parser-data/2023-12/en_product9_prev.xml",
            known_hash="md5:02b822e722433e356da5878decf0377d"
            ),
        "2023-06": OrphanetFile(
            url="https://storage.googleapis.com/orphanet-parser-data/2023-06/en_product9_prev.xml",
            known_hash="md5:21861f5863ddeb666e582778ad7fe73d"
            ),
        "2022-12": OrphanetFile(
            url="https://storage.googleapis.com/orphanet-parser-data/2022-12/en_product9_prev.xml",
            known_hash="md5:be9724d186f84ab6d1756305376dfd0c"
            ),
        }
    _LIST_FIELDS = ('Disorder', 'Prevalence')

    def parse(self) -> pd.DataFrame:
        """
        Get prevalence information as a data frame.
        
        """
        doc = self.read_xml(self.data_file.url, self.data_file.known_hash, self._LIST_FIELDS)

        disorder_df = []
        for disorder in get_list_field(doc['JDBOR'], 'Disorder'):
            for prevalence in get_list_field(disorder, 'Prevalence'):
                disorder_df.append({
                    'orphacode': disorder['OrphaCode'],
                    'expert_link': disorder['ExpertLink']['#text'],
                    'disorder_name': disorder['Name']['#text'],
                    'disorder_type': get_optional_enum(disorder, 'DisorderType'),
                    'disorder_group': get_optional_enum(disorder, 'DisorderGroup'),
                    'prevalence_source': prevalence['Source'],
                    'prevalence_type': get_optional_enum(prevalence, 'PrevalenceType'),
                    'prevalence_qualification': get_optional_enum(prevalence, 'PrevalenceQualification'),
                    'prevalence_class': get_optional_enum(prevalence, 'PrevalenceClass'),
                    'prevalence_geographic': get_optional_enum(prevalence, 'PrevalenceGeographic'),
                    'prevalence_validation_status': get_optional_enum(prevalence, 'PrevalenceValidationStatus')
                    })

        return pd.DataFrame(disorder_df)

