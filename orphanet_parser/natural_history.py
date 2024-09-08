import pandas as pd

from .base import BaseParser
from .utils import get_optional_enum, get_list_field, OrphanetFile


class NaturalHistoryParser(BaseParser):
    _DATA_FILES = {
        "2024-07": OrphanetFile(
            url="https://storage.googleapis.com/orphanet-parser-data/2024-07/en_product9_ages.xml",
            known_hash="md5:5043cc5b517e35b062cd29db18f39554"
            ),
        "2023-12": OrphanetFile(
            url="https://storage.googleapis.com/orphanet-parser-data/2023-12/en_product9_ages.xml",
            known_hash="md5:a422899975163e185dccff8aae152321"
            )
        }
    _LIST_FIELDS = ('Disorder', 'AverageAgeOfOnset', 'TypeOfInheritance')

    def parse(self) -> pd.DataFrame:
        doc = self.read_xml(self.data_file.url, self.data_file.known_hash, self._LIST_FIELDS)

        df = []
        for disorder in get_list_field(doc['JDBOR'], 'Disorder'):
            age_of_onset = [ x['Name']['#text'] for x in get_list_field(disorder, 'AverageAgeOfOnset') ]
            type_of_inheritance = [ x['Name']['#text'] for x in get_list_field(disorder, 'TypeOfInheritance') ] 

            df.append({
                'orphacode': disorder['OrphaCode'],
                'expert_link': disorder['ExpertLink']['#text'],
                'disorder_name': disorder['Name']['#text'],
                'disorder_type': get_optional_enum(disorder, 'DisorderType'),
                'disorder_group': get_optional_enum(disorder, 'DisorderGroup'),
                'average_age_of_onset': self._DELIMETER.join(sorted(age_of_onset)),
                'type_of_inheritance': self._DELIMETER.join(sorted(type_of_inheritance))
                })

        return pd.DataFrame(df)