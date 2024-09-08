import pandas as pd
import xmltodict
import pooch


from typing import Tuple
from typing import Literal

class OrphanetParser:

    _DELIMETER = '; '

    def __init__(self, version: Literal["2024-07"] = "2024-07"):
        self.version = version
        self.data_file = self._DATA_FILES[version]

    @staticmethod
    def read_xml(file_url: str, known_hash: str, list_fields: Tuple[str]) -> dict:
        """
        Read ISO-8859-1 encoded XML file and parse to dictionary
        """
        file_path = pooch.retrieve(url=file_url, known_hash=known_hash)

        with open(file_path, encoding='iso-8859-1') as f:
            doc = xmltodict.parse(
                f.read(), 
                encoding='iso-8859-1',
                force_list=list_fields
                )

        return doc
    
    def parse(self) -> pd.DataFrame:
        raise NotImplementedError("Must be implemented by child classes")
