from domino.base_piece import BasePiece
from .models import InputModel, OutputModel
import json
from util import generate_return

class PatchMotionCorrectionMultiPiece(BasePiece):
    
    def piece_function(self, input_data: InputModel):

        result = generate_return(logger=self.logger, workflow_type='cryosparc', task_name="patch_motion_correction_multi", input_data=input_data.model_dump(mode='json'))
        
        micrographs = {"output": "micrographs", "result": result}
        micrographs_incomplete = {"output": "micrographs_incomplete", "result": result}

        # Return output
        return OutputModel(
            micrographs=json.dumps(micrographs),
            micrographs_incomplete=json.dumps(micrographs_incomplete)
        )      