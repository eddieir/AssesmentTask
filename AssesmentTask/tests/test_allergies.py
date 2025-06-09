import pytest
from src.entity_extraction import extract_entities
from utils.schema import NLPOutputSchema
from utils.test_loader import load_test_cases

@pytest.mark.parametrize("case", load_test_cases("fixtures/test_cases/allergies_cases.yaml"))
def test_allergies_extraction(case):
    """
    Test the extraction of allergies from clinical text.
    """
    result = extract_entities(case["input"])
    validated = NLPOutputSchema(**result)
    assert set(validated.allergies) == set(case["expected"]["allergies"])