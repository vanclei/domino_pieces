from domino.base_piece import BasePiece
from .models import InputModel, OutputModel
from time import sleep
from cryosparc.tools import CryoSPARC


class JobStartPiece(BasePiece):

    def piece_function(self, input_data: InputModel):

        self.logger.info(f"Job Started")
        message = f"Job Executed"
        self.logger.info(message)

        cs = CryoSPARC(
            license="ef9db022-cbbd-11ec-b0e7-7b0aa440335b",
            host="10.0.0.135",
            base_port=39000,
            email="le.tran@ovationdata.com",
            password="test"
        )

        message = f"Test CryoSparc"
        self.logger.info(message)

        assert cs.test_connection()

        message = f"Test CryoSparc PASSED"
        self.logger.info(message)

        # Return output
        return OutputModel(
            message=message,
        )
