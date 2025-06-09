import pytest
from src.entity_extraction import extract_entities

def test_completeness_basic():
    """
    Basic Completeness: Ensure all entities are extracted.
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
    assert len(extract_entities(input_text)) == len(expected_output), "Basic completeness test failed."

def test_completeness_multiple_entities():
    """
    Multiple Diagnoses/Medications/Procedures: Ensure all entities are extracted.
    """
    input_text = "Ms. Jane Doe, 50, was diagnosed with diabetes, hypertension, and asthma. She takes metformin, lisinopril, and albuterol. She underwent a CT scan and a lung biopsy."
    expected_output = {
        "patient_name": "Jane Doe",
        "age": 50,
        "gender": "female",
        "diagnoses": ["diabetes", "hypertension", "asthma"],
        "medications": ["metformin", "lisinopril", "albuterol"],
        "procedures": ["CT scan", "lung biopsy"]
    }
    assert len(extract_entities(input_text)) == len(expected_output), "Multiple entities completeness test failed."

def test_completeness_nested_sentences():
    """
    Nested or Complex Sentences: Ensure all entities are extracted.
    """
    input_text = "Mr. John Smith, a 67-year-old male with a history of hypertension and diabetes, was admitted with chest pain. He was diagnosed with myocardial infarction and prescribed aspirin. He underwent an angioplasty."
    expected_output = {
        "patient_name": "John Smith",
        "age": 67,
        "gender": "male",
        "diagnoses": ["hypertension", "diabetes", "chest pain", "myocardial infarction"],
        "procedures": ["angioplasty"],
        "medications": ["aspirin"]
    }
    assert len(extract_entities(input_text)) == len(expected_output), "Nested sentences completeness test failed."

def test_completeness_missing_information():
    """
    Missing or Partial Information: Ensure the system handles missing entities gracefully.
    """
    input_text = "Patient, 45, was admitted with fever and prescribed ibuprofen."
    expected_output = {
        "patient_name": None,
        "age": 45,
        "gender": None,
        "diagnoses": ["fever"],
        "medications": ["ibuprofen"]
    }
    assert len(extract_entities(input_text)) == len(expected_output), "Missing information completeness test failed."

def test_completeness_ambiguous_entities():
    """
    Ambiguous Entities: Ensure the system handles overlapping or ambiguous entities.
    """
    input_text = "Dr. John Smith, a 45-year-old male, was diagnosed with chest pain and prescribed aspirin. His son, also named John Smith, was diagnosed with a fever."
    expected_output = {
        "patient_name": "John Smith",
        "age": 45,
        "gender": "male",
        "diagnoses": ["chest pain", "fever"],
        "medications": ["aspirin"]
    }
    assert len(extract_entities(input_text)) == len(expected_output), "Ambiguous entities completeness test failed."

def test_completeness_real_world_data():
    """
    Real-World Data: Validate completeness using anonymized clinical narratives.
    """
    input_text = "Patient A, a 60-year-old female, was admitted with shortness of breath and diagnosed with pneumonia. She was prescribed azithromycin and underwent a chest X-ray."
    expected_output = {
        "patient_name": "Patient A",
        "age": 60,
        "gender": "female",
        "diagnoses": ["shortness of breath", "pneumonia"],
        "procedures": ["chest X-ray"],
        "medications": ["azithromycin"]
    }
    assert len(extract_entities(input_text)) == len(expected_output), "Real-world data completeness test failed."

def test_completeness_perturbed_data():
    """
    Perturbed Data: Ensure the system handles typos, abbreviations, and incomplete sentences.
    """
    input_text = "Pt. J. Smith, 67yo male, dx w/ MI and HTN. Rx: aspirin, lisinopril."
    expected_output = {
        "patient_name": "J. Smith",
        "age": 67,
        "gender": "male",
        "diagnoses": ["myocardial infarction", "hypertension"],
        "medications": ["aspirin", "lisinopril"]
    }
    assert len(extract_entities(input_text)) == len(expected_output), "Perturbed data completeness test failed."

def calculate_f1_score(expected, actual, entity_type):
    """
    Calculate precision, recall, and F1 score for a specific entity type.
    :param expected: dict, expected output
    :param actual: dict, actual output
    :param entity_type: str, the entity type to evaluate (e.g., "diagnoses")
    :return: tuple, (precision, recall, f1_score)
    """
    expected_set = set(expected.get(entity_type, []))
    actual_set = set(actual.get(entity_type, []))

    # Convert to binary format for precision/recall calculation
    all_items = list(expected_set.union(actual_set))
    expected_binary = [1 if item in expected_set else 0 for item in all_items]
    actual_binary = [1 if item in actual_set else 0 for item in all_items]

    precision = precision_score(expected_binary, actual_binary, zero_division=0)
    recall = recall_score(expected_binary, actual_binary, zero_division=0)
    f1 = f1_score(expected_binary, actual_binary, zero_division=0)

    return precision, recall, f1

def test_completeness_with_f1():
    """
    Completeness Test with F1 Score: Ensure all entities are extracted and calculate F1 scores.
    """
    test_cases = [
        {
            "input_text": "Mr. John Smith, a 67-year-old male, was admitted with chest pain and diagnosed with myocardial infarction. He was prescribed aspirin and underwent an angioplasty.",
            "expected_output": {
                "patient_name": "John Smith",
                "age": 67,
                "gender": "male",
                "diagnoses": ["myocardial infarction", "chest pain"],
                "procedures": ["angioplasty"],
                "medications": ["aspirin"]
            }
        },
        {
            "input_text": "Ms. Jane Doe, 50, was diagnosed with diabetes, hypertension, and asthma. She takes metformin, lisinopril, and albuterol. She underwent a CT scan and a lung biopsy.",
            "expected_output": {
                "patient_name": "Jane Doe",
                "age": 50,
                "gender": "female",
                "diagnoses": ["diabetes", "hypertension", "asthma"],
                "procedures": ["CT scan", "lung biopsy"],
                "medications": ["metformin", "lisinopril", "albuterol"]
            }
        }
    ]

    # Track missing entity types across runs
    missing_entity_counts = {entity: 0 for entity in ["patient_name", "age", "gender", "diagnoses", "procedures", "medications"]}

    for case in test_cases:
        input_text = case["input_text"]
        expected_output = case["expected_output"]
        actual_output = extract_entities(input_text)

        print(f"\nTesting input: {input_text}")
        for entity_type in ["patient_name", "age", "gender", "diagnoses", "procedures", "medications"]:
            precision, recall, f1 = calculate_f1_score(expected_output, actual_output, entity_type)
            print(f"Entity: {entity_type} | Precision: {precision:.2f} | Recall: {recall:.2f} | F1 Score: {f1:.2f}")

            # Check if the entity type is completely missing
            if not actual_output.get(entity_type):
                missing_entity_counts[entity_type] += 1

    # Alert if a common entity type is consistently missing
    for entity_type, count in missing_entity_counts.items():
        if count > 0:
            print(f"ALERT: Entity type '{entity_type}' is missing in {count} test cases.")
