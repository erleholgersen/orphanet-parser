import pandas as pd

from .base import BaseParser
from .utils import get_optional_enum, get_list_field, OrphanetFile

class GeneAssociationParser(BaseParser):
    _DATA_FILES = {
        "2024-07": OrphanetFile(
            url="https://storage.googleapis.com/orphanet-parser-data/2024-07/en_product6.xml",
            known_hash="md5:958785cf6ae24bfe5bc662eec09be5dd"
            ),
        "2023-12": OrphanetFile(
            url="https://storage.googleapis.com/orphanet-parser-data/2023-12/en_product6.xml",
            known_hash="md5:5a9e4259fd4d37627f632e4d51f6e3a2"
            ),
        }
    _LIST_FIELDS = ('Disorder', 'DisorderGeneAssociation', 'ExternalReference', 'Locus', 'Synonym', )

    def parse(self) -> pd.DataFrame:
        doc = self.read_xml(self.data_file.url, self.data_file.known_hash, self._LIST_FIELDS)

        df = []

        for disorder in get_list_field(doc['JDBOR'], 'Disorder'):
            for association in get_list_field(disorder, 'DisorderGeneAssociation'):
                gene = association['Gene']
                external_references = get_list_field(gene, 'ExternalReference')
                df.append({
                    'orphacode': disorder['OrphaCode'],
                    'expert_link': disorder['ExpertLink']['#text'],
                    'disorder_name': disorder['Name']['#text'],
                    'disorder_type': get_optional_enum(disorder, 'DisorderType'),
                    'disorder_group': get_optional_enum(disorder, 'DisorderGroup'),
                    'association_type': get_optional_enum(association, 'DisorderGeneAssociationType'),
                    'association_status': get_optional_enum(association, 'DisorderGeneAssociationStatus'),
                    'gene_symbol': gene['Symbol'],
                    'gene_name': gene['Name']['#text'],
                    'gene_type': get_optional_enum(gene, 'GeneType'),
                    # TODO: sort? 
                    'external_references': self._DELIMETER.join(f'{x["Source"]}: {x["Reference"]}' for x in external_references),
                    'source_of_validation': association['SourceOfValidation']
                    })
    
        return pd.DataFrame(df)
