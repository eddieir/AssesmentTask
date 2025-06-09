import pytest
from src.entity_extraction import extract_entities
from utils.schema import NLPOutputSchema
from utils.test_loader import load_test_cases

@pytest.mark.parametrize("case", load_test_cases("fixtures/test_cases/diagnoses_cases.yaml"))
def test_diagnoses_extraction(case):
    """
    Test the extraction of diagnoses from clinical text.
    """
    result = extract_entities(case["input"])
    validated = NLPOutputSchema(**result)
    assert set(validated.diagnoses) == set(case["expected"]["diagnoses"])