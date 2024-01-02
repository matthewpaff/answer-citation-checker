"""Original case templates with independently supplied expected results."""
import copy
import re

TEMPLATES = [('validate repeated known source markers without judging answer truth', {'answer': 'See [a{n}] and [a{n}].', 'sources': ['a{n}', 'b{n}']}, {'valid': True, 'used': ['a{n}'], 'unknown': [], 'unused_sources': ['b{n}'], 'occurrences': 2}), ('report source markers absent from the supplied catalog', {'answer': 'See [missing].', 'sources': ['a{n}']}, {'valid': False, 'used': ['missing'], 'unknown': ['missing'], 'unused_sources': ['a{n}'], 'occurrences': 1}), ('require a source marker when citation mode is enabled', {'answer': 'No marker.', 'sources': []}, {'valid': False, 'used': [], 'unknown': [], 'unused_sources': [], 'occurrences': 0}), ('allow uncited text when the explicit policy permits it', {'answer': 'No marker.', 'sources': [], 'require_citation': False}, {'valid': True, 'used': [], 'unknown': [], 'unused_sources': [], 'occurrences': 0}), ('reject repeated source catalog IDs', {'answer': '[a{n}]', 'sources': ['a{n}', 'a{n}']}, None)]


def make_case(index):
    description, source, expected = copy.deepcopy(TEMPLATES[index % len(TEMPLATES)])
    def fill(value):
        if isinstance(value, str):
            if re.fullmatch(r"@i[+]\d+", value):
                return index + int(value[3:])
            return value.replace("{n}", str(index))
        if isinstance(value, list):
            return [fill(item) for item in value]
        if isinstance(value, dict):
            return {fill(key): fill(item) for key, item in value.items()}
        return value
    case = {"id": "citations-{:04d}".format(index), "description": description, "input": fill(source)}
    case.update({"expected_error": True} if expected is None else {"expected": fill(expected)})
    return case
