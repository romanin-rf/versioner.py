from vbml import Pattern
from typing import Dict, Any, List
# * Local Imports
try:
    from .Functions import get_patterns, handling_variations, is_equal_keys, parse_version_data
    from .Exceptions import ParsingError, ParsingKeysError
    from .Units import STANDART_PATTERNS, STANDART_VARIATIONS, STANDART_VERSION_DATA
except:
    from Functions import get_patterns, handling_variations, is_equal_keys, parse_version_data
    from Exceptions import ParsingError, ParsingKeysError
    from Units import STANDART_PATTERNS, STANDART_VARIATIONS, STANDART_VERSION_DATA

# ! Version Class
class Version:
    def __init__(
        self,
        version: str,
        version_data: Dict[str, int]
    ) -> None:
        self.version = version
        self.version_data = version_data
        self.hash_data = [hash(i) for i in self.version_data.values()]
    
    def __str__(self) -> str: return self.version
    def __repr__(self) -> str: return f"{self.__class__.__name__}('{self.__str__()}')"
    def similar_to(self, version) -> bool: return is_equal_keys(self.version_data, version.version_data)
    def __eq__(self, other) -> bool:
        if self.similar_to(other):
            return min([(i[0] == i[1]) for i in list(zip(self.hash_data, other.hash_data))])
        raise ParsingKeysError()
    def __lt__(self, other) -> bool:
        if self.similar_to(other):
            return max([(i[0] < i[1]) for i in list(zip(self.hash_data, other.hash_data))])
        raise ParsingKeysError()
    def __gt__(self, other) -> bool:
        if self.similar_to(other):
            return max([(i[0] > i[1]) for i in list(zip(self.hash_data, other.hash_data))])
        raise ParsingKeysError()
    def __ne__(self, other) -> bool: return not self.__eq__(other)
    def __le__(self, other) -> bool: return self.__lt__(other) or self.__eq__(other)
    def __ge__(self, other) -> bool: return self.__gt__(other) or self.__eq__(other)

# ! Versioner Class
class Versioner:
    def __init__(
        self,
        **kwargs
    ) -> None:
        self.version_data: Dict[str, Any] = kwargs.get("version_data", STANDART_VERSION_DATA)
        self.patterns: List[Pattern] = get_patterns(kwargs.get("patterns", STANDART_PATTERNS))
        self.variations: Dict[str, List[str]] = kwargs.get("variations", STANDART_VARIATIONS)
    
    def parse(self, string: str) -> Version:
        vd, pvd = self.version_data.copy(), parse_version_data(string, self.patterns)
        if pvd is not None:
            vd.update(pvd)
            vd = handling_variations(vd, self.variations)
            return Version(string, vd)
        raise ParsingError()
