from faker import Faker
import pytest
from src.entity_extraction import extract_entities

fake = Faker()

def generate_synthetic_input():
    """
    Generate a synthetic clinical narrative using Faker.
    """
    name = fake.name()
    age = fake.random_int(min=1, max=100)
    gender = fake.random_element(elements=["male", "female"])
    diagnosis = fake.random_element(elements=["diabetes", "hypertension", "asthma", "fever"])
    medication = fake.random_element(elements=["aspirin", "metformin", "lisinopril", "ibuprofen"])
    procedure = fake.random_element(elements=["angioplasty", "CT scan", "MRI", "biopsy"])

    input_text = f"{name}, a {age}-year-old {gender}, was diagnosed with {diagnosis} and prescribed {medication}. They underwent a {procedure}."
    expected_output = {
        "patient_name": name,
        "age": age,
        "gender": gender,
        "diagnoses": [diagnosis],
        "medications": [medication],
        "procedures": [procedure]
    }
    return input_text, expected_output

@pytest.mark.parametrize("test_case", [generate_synthetic_input() for _ in range(100)])
def test_reliability_synthetic(test_case):
    """
    Synthetic Data Test: Validate extraction on randomly generated inputs.
    """
    input_text, expected_output = test_case
    actual_output = extract_entities(input_text)
    assert actual_output == expected_output, f"Failed for input: {input_text}"