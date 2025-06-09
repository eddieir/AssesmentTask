import pytest
from src.entity_extraction import extract_entities

def test_ambiguous_language():
    text = "The patient was possibly suffering from a heart event."
    output = extract_entities(text)
    assert "heart event" not in output.get("diagnoses", [])