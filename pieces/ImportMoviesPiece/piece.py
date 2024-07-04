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
        
        message = input_data.model_dump(mode='json')
        self.logger.info(message)

        imported_movies = "IMPORTED MOVIE"
        failed_movies = "FAILED MOVIES"

        # Return output
        return OutputModel(
            imported_movies=imported_movies,
            failed_movies=failed_movies,
        )        
