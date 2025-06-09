from sklearn.metrics import precision_score, recall_score, f1_score

def calculate_f1_score(expected, actual, entity_type):
    """
    Calculate precision, recall, and F1 score for a specific entity type.
    
    :param expected: dict, expected output
    :param actual: dict, actual output
    :param entity_type: str, the entity type to evaluate (e.g., "diagnoses")
    :return: tuple, (precision, recall, f1_score)
    """
    expected_set = set(expected.get(entity_type, []))
    actual_set = set(actual.get(entity_type, []))

    # Convert to binary format for precision/recall calculation
    all_items = list(expected_set.union(actual_set))
    expected_binary = [1 if item in expected_set else 0 for item in all_items]
    actual_binary = [1 if item in actual_set else 0 for item in all_items]

    precision = precision_score(expected_binary, actual_binary, zero_division=0)
    recall = recall_score(expected_binary, actual_binary, zero_division=0)
    f1 = f1_score(expected_binary, actual_binary, zero_division=0)

    return precision, recall, f1