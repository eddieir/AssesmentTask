import pytest
from src.entity_extraction import extract_entities

def test_html_tag_noise():
    text = "<div>Mr. John Smith, 67, admitted with chest pain</div>"
    output = extract_entities(text)
    assert output["patient_name"] == "John Smith"
    assert "chest pain" in output["diagnoses"]