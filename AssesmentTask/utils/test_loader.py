import yaml

def load_test_cases(filepath):
    """
    Load test cases from a YAML or JSON file.
    :param filepath: str, path to the test case file
    :return: list of test cases
    """
    with open(filepath, "r") as file:
        return yaml.safe_load(file)