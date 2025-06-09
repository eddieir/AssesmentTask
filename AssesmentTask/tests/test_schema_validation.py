from pydantic import BaseModel
from typing import List, Optional

class EntityOutput(BaseModel):
    patient_name: Optional[str]
    age: Optional[int]
    gender: Optional[str]
    diagnoses: List[str]
    medications: List[str]
    procedures: List[str]

# filepath: /tests/test_schema_validation.py
from utils.schema import EntityOutput
from src.entity_extraction import extract_entities

def test_valid_schema():
    result = extract_entities("John Smith, 67, admitted for chest pain.")
    validated = EntityOutput(**result)
    assert validated.age == 67