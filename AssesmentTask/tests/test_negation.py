import pytest
from src.entity_extraction import extract_entities

def test_negation_handling():
    text = "No signs of pneumonia or diabetes. Prescribed paracetamol."
    output = extract_entities(text)
    assert "pneumonia" not in output["diagnoses"]
    assert "diabetes" not in output["diagnoses"]
    assert "paracetamol" in output["medications"]