from pydantic import BaseModel
from typing import List, Optional

class EntityOutput(BaseModel):
    """
    Pydantic model for validating the output schema of the entity extraction system.
    """
    patient_name: Optional[str]
    age: Optional[int]
    gender: Optional[str]
    diagnoses: List[str]
    medications: List[str]
    procedures: List[str]