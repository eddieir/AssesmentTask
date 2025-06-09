import pytest
from src.entity_extraction import extract_entities

def test_positive_case():
    text = "Mr. John Smith, a 67-year-old male, was admitted with chest pain and diagnosed with myocardial infarction. He was prescribed aspirin and underwent an angioplasty."
    output = extract_entities(text)
    assert output["patient_name"] == "John Smith"
    assert output["age"] == 67
    assert output["gender"] == "male"
    assert "myocardial infarction" in output["diagnoses"]
    assert "chest pain" in output["diagnoses"]
    assert "aspirin" in output["medications"]
    assert "angioplasty" in output["procedures"]