import pytest
from src.entity_extraction import extract_entities

def test_multiple_entities():
    text = "Patient was diagnosed with diabetes, hypertension, and given aspirin and metformin."
    output = extract_entities(text)
    assert set(output["diagnoses"]) == {"diabetes", "hypertension"}
    assert set(output["medications"]) == {"aspirin", "metformin"}