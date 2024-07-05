from domino.base_piece import BasePiece
from .models import InputModel, OutputModel
import json
from util import generate_return


class ImportMoviesPiece(BasePiece):

    def piece_function(self, input_data: InputModel):

        result = generate_return(logger=self.logger, workflow_type='cryosparc', task_name="import_movies", input_data=input_data.model_dump(mode='json'))
        
        imported_movies = {"output": "imported_movies", "result": result}
        failed_movies = {"output": "failed_movies", "result": result}

        # Return output
        return OutputModel(
            imported_movies=json.dumps(imported_movies),
            failed_movies=json.dumps(failed_movies)
        )        
