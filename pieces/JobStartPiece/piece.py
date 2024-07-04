from domino.base_piece import BasePiece
from .models import InputModel, OutputModel
import json
import requests

class JobStartPiece(BasePiece):

    def piece_function(self, input_data: InputModel):

        self.logger.info(f"Job Started")
        x = requests.get('http://domino-rest:8000/health-check')

        self.logger.info(x.text)        
        
        

        message = input_data.model_dump(mode='json')
        self.logger.info(message)

        # Return output
        return OutputModel(
            message=json.dumps(message)
        )
