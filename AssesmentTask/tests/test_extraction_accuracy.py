import pytest
from src.entity_extraction import extract_entities

@pytest.mark.parametrize("input_text, expected", [
    ("John Smith, 67, underwent angioplasty and received aspirin.", {
        "patient_name": "John Smith",
        "age": 67,
        "procedures": ["angioplasty"],
        "medications": ["aspirin"]
    }),
])
def test_extraction_accuracy(input_text, expected):
    result = extract_entities(input_text)
    for key, expected_value in expected.items():
        assert set(result.get(key, [])) == set(expected_value)