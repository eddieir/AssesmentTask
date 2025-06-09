import pytest
from src.entity_extraction import extract_entities

def test_correctness_unit():
    """
    Unit Test: Validate individual components of the system.
    """
    input_text = "Mr. John Smith, a 67-year-old male, was admitted with chest pain and diagnosed with myocardial infarction. He was prescribed aspirin and underwent an angioplasty."
    expected_output = {
        "patient_name": "John Smith",
        "age": 67,
        "gender": "male",
        "diagnoses": ["myocardial infarction", "chest pain"],
        "procedures": ["angioplasty"],
        "medications": ["aspirin"]
    }
    assert extract_entities(input_text) == expected_output, "Unit test failed for correctness."

def test_correctness_integration():
    """
    Integration Test: Test the system end-to-end with predefined inputs and outputs.
    """
    input_text = "Ms. Jane Doe, 50, was diagnosed with diabetes and hypertension. She takes metformin and lisinopril."
    expected_output = {
        "patient_name": "Jane Doe",
        "age": 50,
        "gender": "female",
        "diagnoses": ["diabetes", "hypertension"],
        "medications": ["metformin", "lisinopril"]
    }
    assert extract_entities(input_text) == expected_output, "Integration test failed for correctness."

def test_correctness_edge_case():
    """
    Edge Case Test: Test unusual or ambiguous inputs.
    """
    input_text = "Patient J. Smith, 45, presented with fever and was prescribed ibuprofen."
    expected_output = {
        "patient_name": "J. Smith",
        "age": 45,
        "gender": None,
        "diagnoses": ["fever"],
        "medications": ["ibuprofen"]
    }
    assert extract_entities(input_text) == expected_output, "Edge case test failed for correctness."

def test_completeness():
    """
    Completeness Test: Ensure all relevant entities are extracted without omissions.
    """
    input_text = "Ms. Jane Doe, 50, was diagnosed with diabetes and hypertension. She takes metformin and lisinopril."
    expected_output = {
        "patient_name": "Jane Doe",
        "age": 50,
        "gender": "female",
        "diagnoses": ["diabetes", "hypertension"],
        "medications": ["metformin", "lisinopril"]
    }
    assert len(extract_entities(input_text)) == len(expected_output), "Completeness test failed."

def test_reliability_stress():
    """
    Stress Test: Test the system with long and complex narratives.
    """
    input_text = (
        "Mr. John Smith, a 67-year-old male, was admitted with chest pain and diagnosed with myocardial infarction. "
        "He was prescribed aspirin and underwent an angioplasty. Later, he was diagnosed with hypertension and prescribed lisinopril. "
        "Ms. Jane Doe, 50, was diagnosed with diabetes and hypertension. She takes metformin and lisinopril."
    )
    expected_output = {
        "patient_name": "John Smith",
        "age": 67,
        "gender": "male",
        "diagnoses": ["myocardial infarction", "chest pain", "hypertension"],
        "procedures": ["angioplasty"],
        "medications": ["aspirin", "lisinopril"]
    }
    assert extract_entities(input_text) == expected_output, "Stress test failed for reliability."