STANDART_PATTERNS = [
    "<major:int>.<minor:int>.<patch:int>-<build_name>.<build_number:int>",
    "<major:int>.<minor:int>.<patch:int>-<build_name>",
    "<major:int>.<minor:int>-<build_name>",
    "<major:int>.<minor:int>.<patch:int>",
    "<major:int>.<minor:int>",
    "<major:int>"
]
STANDART_VARIATIONS = {"build_name": ["", "alpha", "beta", "debag", "pre-release", "release"]}
STANDART_VERSION_DATA = {
    "major": 0,
    "minor": 0,
    "patch": 0,
    "build_name": "",
    "build_number": 0
}