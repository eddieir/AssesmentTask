def test_abbreviation_handling():
    input_text = "Pt. J. Smith, 67, was admitted with HTN and Rx: ASA"
    output = extract_entities(input_text)
    assert "hypertension" in output["diagnoses"]
    assert "aspirin" in output["medications"]
