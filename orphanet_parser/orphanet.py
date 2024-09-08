import pandas as pd

from .associated_phenotypes import AssociatedPhenotypesParser
from .functional_consequences import FunctionalConsequencesParser
from .gene_associations import GeneAssociationParser
from .prevalence import PrevalenceParser
from .natural_history import NaturalHistoryParser
from .utils import VERSIONS

class OrphanetData:
    """
    Access Orphanet data as pandas data frames. High level utility for convenient access
    to each of the supported data frames.
    
    """

    def __init__(self, version: VERSIONS = "2024-07"):
        self.version = version

        self.associated_phenotypes_parser = AssociatedPhenotypesParser(self.version)
        self.functional_consequences_parser = FunctionalConsequencesParser(self.version)
        self.gene_assocationes_parser = GeneAssociationParser(self.version)
        self.prevalence_parser = PrevalenceParser(self.version)
        self.natural_history_parser = NaturalHistoryParser(self.version)

    def associated_phenotypes(self) -> pd.DataFrame:
        return self.associated_phenotypes_parser.parse()
    
    def functional_consequences(self) -> pd.DataFrame:
        return self.functional_consequences_parser.parse()
    
    def gene_associations(self) -> pd.DataFrame:
        return self.gene_assocationes_parser.parse()
    
    def prevalence(self) -> pd.DataFrame:
        return self.prevalence_parser.parse()
    
    def natural_history(self) -> pd.DataFrame:
        return self.natural_history_parser.parse()

