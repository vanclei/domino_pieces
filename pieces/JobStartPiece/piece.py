from domino.base_piece import BasePiece
from .models import InputModel, OutputModel
from time import sleep


class JobStartPiece(BasePiece):

    def piece_function(self, input_data: InputModel):

        self.logger.info(f"Job Started")
        message = f"Job Executed"
        self.logger.info(message)

        # Return output
        return OutputModel(
            message=message,
        )
