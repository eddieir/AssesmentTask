import pytest
from src.entity_extraction import extract_entities

@pytest.mark.snapshot
def test_reliability_snapshot(snapshot):
    """
    Snapshot Test: Compare current extraction results with saved snapshots.
    """
    input_text = "Mr. John Smith, a 67-year-old male, was admitted with chest pain and diagnosed with myocardial infarction. He was prescribed aspirin and underwent an angioplasty."
    current_output = extract_entities(input_text)

    # Compare current output with the saved snapshot
    snapshot.assert_match(current_output)