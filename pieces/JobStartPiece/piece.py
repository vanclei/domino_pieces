from domino.base_piece import BasePiece
from .models import InputModel, OutputModel
import json
import requests
import os

class JobStartPiece(BasePiece):

    def piece_function(self, input_data: InputModel):

        self.logger.info(f"Job Started")
        # x = requests.get('http://domino-rest:8000/health-check')

        # self.logger.info(x.text)        
        for name, value in os.environ.items():
            self.logger.info("{0}: {1}".format(name, value))        
        

        message = input_data.model_dump(mode='json')
        self.logger.info(message)

        # Return output
        return OutputModel(
            message=json.dumps(message)
        )
