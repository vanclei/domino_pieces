from domino.base_piece import BasePiece
from .models import InputModel, OutputModel
from time import sleep
import requests
import base64


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
        base64_bytes_data = base64.b64encode(response.content).decode('utf-8')
        return OutputModel(base64_bytes_data=base64_bytes_data)
