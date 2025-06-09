import json
from deepdiff import DeepDiff
from src.entity_extraction import extract_entities

def test_snapshot_regression():
    input_text = "Jane Doe, 45, diagnosed with asthma and prescribed salbutamol."
    expected_snapshot = json.load(open("fixtures/golden_snapshot.json"))
    result = extract_entities(input_text)
    diff = DeepDiff(expected_snapshot, result, ignore_order=True)
    assert not diff, f"Regression detected: {diff}"