# main.py

"""
Dynamic Data Handler - A Python script designed to dynamically process and manage data
through a series of customizable functions and operations. This serves as a basic
open-source template for handling JSON, CSV, and basic data operations.
"""

import json
import csv
from typing import List, Dict

class DataHandler:
    """
    A class used to handle data operations such as reading, writing,
    and transforming JSON and CSV files.
    """

    def __init__(self):
        """Initialize the DataHandler class."""
        print("Initializing DataHandler...")

    def load_json(self, file_path: str) -> Dict:
        """
        Load and parse a JSON file.

        Args:
            file_path (str): The path to the JSON file.

        Returns:
            Dict: The parsed JSON data.
        """
        try:
            with open(file_path, "r") as file:
                data = json.load(file)
                print(f"Successfully loaded JSON data from {file_path}.")
                return data
        except Exception as e:
            print(f"Error loading JSON file: {e}")
            return {}

    def save_json(self, file_path: str, data: Dict) -> None:
        """
        Save data to a JSON file.

        Args:
            file_path (str): The path to the JSON file.
            data (Dict): The data to be stored.
        """
        try:
            with open(file_path, "w") as file:
                json.dump(data, file, indent=4)
                print(f"Successfully saved JSON data to {file_path}.")
        except Exception as e:
            print(f"Error saving JSON file: {e}")

    def load_csv(self, file_path: str) -> List[Dict]:
        """
        Load and parse a CSV file into a list of dictionaries.

        Args:
            file_path (str): The path to the CSV file.

        Returns:
            List[Dict]: A list of rows as dictionaries.
        """
        try:
            with open(file_path, "r") as file:
                reader = csv.DictReader(file)
                data = [row for row in reader]
                print(f"Successfully loaded CSV data from {file_path}.")
                return data
        except Exception as e:
            print(f"Error loading CSV file: {e}")
            return []

    def save_csv(self, file_path: str, data: List[Dict]) -> None:
        """
        Save a list of dictionaries to a CSV file.

        Args:
            file_path (str): The path to the CSV file.
            data (List[Dict]): The data to be stored.
        """
        try:
            if data:
                with open(file_path, "w", newline="") as file:
                    writer = csv.DictWriter(file, fieldnames=data[0].keys())
                    writer.writeheader()
                    writer.writerows(data)
                    print(f"Successfully saved CSV data to {file_path}.")
            else:
                print("No data provided to save in CSV file.")
        except Exception as e:
            print(f"Error saving CSV file: {e}")

    def transform_data(self, data: List[Dict], transformations: Dict) -> List[Dict]:
        """
        Apply transformations to a list of dictionaries.

        Args:
            data (List[Dict]): The original data.
            transformations (Dict): A dictionary defining key transformations.

        Returns:
            List[Dict]: The transformed data.
        """
        transformed_data = []
        for row in data:
            transformed_row = {key: transformations.get(key, lambda x: x)(value) for key, value in row.items()}
            transformed_data.append(transformed_row)
        print("Data transformation complete.")
        return transformed_data

if __name__ == "__main__":
    # Example usage of the DataHandler class
    handler = DataHandler()

    # Example JSON operations
    json_file = "example.json"
    sample_json_data = {"name": "John Doe", "age": 30, "city": "New York"}

    handler.save_json(json_file, sample_json_data)
    loaded_json = handler.load_json(json_file)
    print("Loaded JSON Data:", loaded_json)

    # Example CSV operations
    csv_file = "example.csv"
    sample_csv_data = [
        {"name": "Alice", "age": 25, "city": "Boston"},
        {"name": "Bob", "age": 28, "city": "Seattle"},
        {"name": "Charlie", "age": 35, "city": "Denver"},
    ]

    handler.save_csv(csv_file, sample_csv_data)
    loaded_csv = handler.load_csv(csv_file)
    print("Loaded CSV Data:", loaded_csv)

    # Example transformation
    transformations = {
        "name": lambda x: x.upper(),
        "age": lambda x: int(x) + 1,
        "city": lambda x: x[::-1],
    }
    transformed_csv = handler.transform_data(loaded_csv, transformations)
    print("Transformed Data:", transformed_csv)
