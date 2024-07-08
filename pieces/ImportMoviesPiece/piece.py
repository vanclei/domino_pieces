from domino.base_piece import BasePiece
from .models import InputModel, OutputModel
import json
from util import generate_return


class ImportMoviesPiece(BasePiece):

    def piece_function(self, input_data: InputModel):

        result = generate_return(logger=self.logger, workflow_type='cryosparc', job_type="import_movies", input_data=input_data)

        # Return output
        return OutputModel(
            imported_movies=json.dumps(result),
            failed_movies=json.dumps(result)
        )        
