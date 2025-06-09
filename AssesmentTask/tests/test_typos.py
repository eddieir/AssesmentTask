import pytest
from src.entity_extraction import extract_entities

def test_typo_handling():
    text = "Diagnosed with myocarial infarcton and underwent angoplasty."
    output = extract_entities(text)
    assert "myocardial infarction" in output["diagnoses"]
    assert "angioplasty" in output["procedures"]