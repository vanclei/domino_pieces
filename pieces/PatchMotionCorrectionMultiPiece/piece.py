from domino.base_piece import BasePiece
from .models import InputModel, OutputModel
import json
from util import generate_return

class PatchMotionCorrectionMultiPiece(BasePiece):
    
    def piece_function(self, input_data: InputModel):

        result = generate_return(logger=self.logger, workflow_type='cryosparc', job_type="patch_motion_correction_multi", input_data=input_data)

        # Return output
        return OutputModel(
            micrographs=json.dumps(result),
            micrographs_incomplete=json.dumps(result)
        )      