from domino.base_piece import BasePiece
from .models import InputModel, OutputModel

class JobStartPiece(BasePiece):

    def piece_function(self, input_data: InputModel):

        self.logger.info(f"Job Started")
        message = f"Job Executed"
        self.logger.info(message)

        message = input_data.model_dump(mode='json')
        self.logger.info(message)

        # Return output
        return OutputModel(
            message=message,
        )
