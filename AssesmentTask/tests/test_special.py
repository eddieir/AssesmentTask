import pytest
from src.entity_extraction import extract_entities

def test_special_characters():
    text = "José Rodríguez, 72 y/o, prescribed “metformín”."
    output = extract_entities(text)
    assert output["patient_name"] == "José Rodríguez"
    assert "metformin" in output["medications"]