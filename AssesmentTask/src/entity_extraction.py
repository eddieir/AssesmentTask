def extract_entities(input_text):
    """
    Extracts structured clinical information from unstructured medical text.
    :param input_text: str, clinical narrative
    :return: dict, extracted entities
    """
    # Mock implementation for demonstration purposes
    if "John Smith" in input_text:
        return {
            "patient_name": "John Smith",
            "age": 67,
            "gender": "male",
            "diagnoses": ["myocardial infarction", "chest pain"],
            "procedures": ["angioplasty"],
            "medications": ["aspirin"]
        }
    elif "Jane Doe" in input_text:
        return {
            "patient_name": "Jane Doe",
            "age": 50,
            "gender": "female",
            "diagnoses": ["diabetes", "hypertension"],
            "medications": ["metformin", "lisinopril"]
        }
    else:
        return {}