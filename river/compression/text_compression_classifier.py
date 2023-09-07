from __future__ import annotations

import zstd  # type: ignore

from river import base


class TextCompressionClassifier(base.Classifier):
    def __init__(self, compression_level=3):
        self.compression_level = compression_level
        self.label_documents = {}  # Concatenated documents for each label
        self.compression_contexts = {}  # Zstd compression contexts for each label

    def learn_one(self, x, y):
        # Convert your input 'x' to a string representation if it's not already
        # For the sake of example, let's assume 'x' is a dictionary of features
        x_str = str(x)

        # Concatenate the new example to the existing document for this label
        self.label_documents[y] = self.label_documents.get(y, "") + x_str

        # Create/Update Zstd compression context for this label
        if y not in self.compression_contexts:
            self.compression_contexts[y] = zstd.ZstdCompressor(level=self.compression_level)

        # Create a dictionary using the compressed document
        zstd_dict = zstd.ZstdCompressionDict(self.label_documents[y].encode("utf-8"))

        # Update the compression context for this label with the new dictionary
        self.compression_contexts[y].compression_dict = zstd_dict

    def predict_one(self, x):
        min_size_increase = float("inf")
        best_label = None

        # Convert your input 'x' to a string representation if it's not already
        x_str = str(x)

        for label, compressor in self.compression_contexts.items():
            # Concatenate and compress
            concatenated_doc = (self.label_documents[label] + x_str).encode("utf-8")
            compressed_size = len(compressor.compress(concatenated_doc))

            # Calculate size increase (you can define your own metric here)
            size_increase = compressed_size - len(
                compressor.compress(self.label_documents[label].encode("utf-8"))
            )

            if size_increase < min_size_increase:
                min_size_increase = size_increase
                best_label = label

        return best_label

    def test(self, arg):
        print("estou na classe !! ", arg)
