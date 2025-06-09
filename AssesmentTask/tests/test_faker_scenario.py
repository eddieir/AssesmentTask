from faker import Faker
from src.entity_extraction import extract_entities

def test_faker_scenario():
    fake = Faker()
    name = fake.name()
    age = fake.random_int(30, 80)
    text = f"{name}, a {age}-year-old, diagnosed with diabetes."
    result = extract_entities(text)
    assert result["age"] == age
    assert "diabetes" in result["diagnoses"]