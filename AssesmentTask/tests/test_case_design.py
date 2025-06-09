import pytest
from src.entity_extraction import extract_entities

# Core Positive Test Cases
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

# Abbreviation Test Cases
def test_abbreviation_handling():
    text = "Pt. J. Smith, 67, was admitted with HTN and Rx: ASA"
    output = extract_entities(text)
    assert "hypertension" in output["diagnoses"]
    assert "aspirin" in output["medications"]

# Typographical Error Test Cases (Fuzzy Matching)
def test_typo_handling():
    text = "Diagnosed with myocarial infarcton and underwent angoplasty."
    output = extract_entities(text)
    assert "myocardial infarction" in output["diagnoses"]
    assert "angioplasty" in output["procedures"]

# Negation Test Cases
def test_negation_handling():
    text = "No signs of pneumonia or diabetes. Prescribed paracetamol."
    output = extract_entities(text)
    assert "pneumonia" not in output["diagnoses"]
    assert "diabetes" not in output["diagnoses"]
    assert "paracetamol" in output["medications"]

# Ambiguous Language Test Cases
def test_ambiguous_language():
    text = "The patient was possibly suffering from a heart event."
    output = extract_entities(text)
    assert "heart event" not in output.get("diagnoses", [])

# Multiple Entities Test Cases
def test_multiple_entities():
    text = "Patient was diagnosed with diabetes, hypertension, and given aspirin and metformin."
    output = extract_entities(text)
    assert set(output["diagnoses"]) == {"diabetes", "hypertension"}
    assert set(output["medications"]) == {"aspirin", "metformin"}

# Missing or Incomplete Data Test Cases
def test_incomplete_data():
    text = "Prescribed medication."
    output = extract_entities(text)
    assert "medications" in output
    assert output.get("patient_name") is None
    assert output.get("age") is None
    assert output.get("gender") is None

# Unicode and Special Characters Test Cases
def test_special_characters():
    text = "José Rodríguez, 72 y/o, prescribed “metformín”."
    output = extract_entities(text)
    assert output["patient_name"] == "José Rodríguez"
    assert "metformin" in output["medications"]

# Noise Injection/Format Disturbance Test Cases
def test_html_tag_noise():
    text = "<div>Mr. John Smith, 67, admitted with chest pain</div>"
    output = extract_entities(text)
    assert output["patient_name"] == "John Smith"
    assert "chest pain" in output["diagnoses"]