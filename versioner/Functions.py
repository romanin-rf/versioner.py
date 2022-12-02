from vbml import Pattern, Patcher
from typing import List, Iterable, Dict, Any, TypeVar, Optional

KEY = TypeVar("KEY", int, float, str)

def get_patterns(patterns_strings: Iterable[str]) -> List[Pattern]:
    return [Pattern(i) for i in patterns_strings]

def handling_variations(version_data: Dict[str, Any], variations: Dict[str, List[str]]) -> Dict[str, int]:
    version_data_keys = list(version_data.keys())
    for i in variations:
        if i in version_data_keys:
            if version_data[i] in variations[i]:
                version_data[i] = variations[i].index(version_data[i])
    return version_data

def is_equal_keys(a: Dict[KEY, Any], b: Dict[KEY, Any]) -> bool:
    if (len(a) == len(b)):
        if (len(a) > 0) and (len(b) > 0):
            return min([i[0]==i[1] for i in list(zip(list(a.keys()), list(b.keys())))])
        return True
    return False

def parse_version_data(version: str, patterns: Iterable[Pattern]) -> Optional[Dict[str, Any]]:
    p = Patcher()
    for pattern in patterns:
        if type(data:=p.check(pattern, version)) == dict:
            return data
