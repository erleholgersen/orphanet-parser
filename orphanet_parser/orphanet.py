import pandas as pd

from .associated_phenotypes import AssociatedPhenotypesParser
from .functional_consequences import FunctionalConsequencesParser
from .gene_associations import GeneAssociationParser
from .prevalence import PrevalenceParser
from .natural_history import NaturalHistoryParser
from .utils import VERSIONS

from typing import Literal

class OrphanetData:
    """
    Access Orphanet data as pandas data frames. High level utility for convenient access
    to each of the supported data frames.
    
    """
    def __init__(self, version: Literal["2024-07", "2023-12", "2023-06", "2022-12"] = "2024-07"):
        """

        Args:
            version: Data release version.
        
        """
        self.version = version

        self.associated_phenotypes_parser = AssociatedPhenotypesParser(self.version)
        self.functional_consequences_parser = FunctionalConsequencesParser(self.version)
        self.gene_assocationes_parser = GeneAssociationParser(self.version)
        self.prevalence_parser = PrevalenceParser(self.version)
        self.natural_history_parser = NaturalHistoryParser(self.version)

    def associated_phenotypes(self) -> pd.DataFrame:
        """
        Get associated phenotypes data
        """
        return self.associated_phenotypes_parser.parse()
    
    def functional_consequences(self) -> pd.DataFrame:
        """
        Get functional consequences data
        """
        return self.functional_consequences_parser.parse()
    
    def gene_associations(self) -> pd.DataFrame:
        """
        Get gene association data
        """
        return self.gene_assocationes_parser.parse()
    
    def prevalence(self) -> pd.DataFrame:
        """
        Get prevalence data
        """
        return self.prevalence_parser.parse()
    
    def natural_history(self) -> pd.DataFrame:
        """
        Get natural history data
        """
        return self.natural_history_parser.parse()

