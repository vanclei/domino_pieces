from domino.base_piece import BasePiece
from .models import InputModel, OutputModel
import json
import requests
import os
from util import generate_return

class JobStartPiece(BasePiece):

    def piece_function(self, input_data: InputModel):

        self.logger.info(f"Job Started")
        message = input_data.model_dump(mode='json')
        self.logger.info(message)

        result = generate_return(logger=self.logger, workflow_type='cryosparc', job_type="job_start", input_data=input_data)

        # Return output
        return OutputModel(
            job_start=json.dumps(result)
        )
