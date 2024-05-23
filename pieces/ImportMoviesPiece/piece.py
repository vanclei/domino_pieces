from domino.base_piece import BasePiece
from .models import InputModel, OutputModel
from time import sleep
import requests
import base64
from pathlib import Path
from PIL import Image
from io import BytesIO
import numpy as np


class ImportMoviesPiece(BasePiece):

    def piece_function(self, input_data: InputModel):
        
        try:        
            url = input_data.movies_data_path
            response = requests.get(url, headers={})

            self.logger.info(f" Retrieve image from {input_data.movies_data_path}")
            message = f"Image retrieved for {input_data.movies_data_path}"
            self.logger.info(message)

        except requests.RequestException as e:
            raise Exception(f"HTTP request error: {e}")

        # convert content to base64
        base64_bytes_data = base64.b64encode(response.content)
        
        image_file_path = f"{self.results_path}/modified_image.png"
        with open(image_file_path, "wb") as new_file:
            new_file.write(base64.decodebytes(base64_bytes_data))    
        
        self.display_result = {
            "file_type": "png",
            "base64_content": base64_bytes_data,
            "file_path": image_file_path
        }

        # Return output
        return OutputModel(
            image_base64_string=base64_bytes_data.decode('utf-8'),
            image_file_path=image_file_path,
        )        
