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
        # Here you can add any library download logic if needed
        # For example, you might want to ensure that the 'datasets' library is installed
        # However, since we are already importing it, we assume it's available

    def load(self):
        """
        Load the dataset using the provided dataset ID.
        """
        print(f"Downloading libraries")
        print(f"Loading dataset with ID: {self.dataset_id}")
        return datasets.load_dataset(self.dataset_id)

# if __name__ == "__main__":
#     # Example usage
#     dataset_id = "imdb"  # Replace with your desired dataset ID
#     loader = DatasetLoader(dataset_id)
#     loader.download_libraries()
#     dataset = loader.load()
#     print(f"Dataset loaded: {dataset}")