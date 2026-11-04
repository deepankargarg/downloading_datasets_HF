import datasets
class DatasetLoader:
    """
    A class to load datasets from the Hugging Face datasets library.
    """

    def __init__(self, dataset_id):
        self.dataset_id = dataset_id

    def download_libraries(self):
        """
        Download necessary libraries for dataset loading.
        """
        print("Downloading necessary libraries...")

    def load(self):
        """
        Load the dataset using the provided dataset ID.
        """
        print(f"Downloading libraries")
        print(f"Loading dataset with ID: {self.dataset_id}")
        return datasets.load_dataset(self.dataset_id)
