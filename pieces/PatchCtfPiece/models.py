from pydantic import BaseModel, Field
from typing import Optional
from enum import Enum

class OutputTypeType(str, Enum):
    """
    Output type for the result text
    """
    file = "file"
    base64_string = "base64_string"
    both = "both"
    
class InputModel(BaseModel):
    """
    Sleep Piece Input Model
    """

    input_image: str = Field(
        description='Input image from previous task',
        json_schema_extra={
            "from_upstream": "always"
        }
    )
    run_extraction_without_ctf_values: bool = Field(
        default=False,
        description='Run extraction without CTF Values?',
    )
    output_type: OutputTypeType = Field(
        default=OutputTypeType.both,
        description='Format of the output image. Options are: `file`, `base64_string`, `both`.',
    )              

class OutputModel(BaseModel):
    image_base64_string: Optional[str] = Field(
        default='',
        description='Base64 encoded string of the output image.',
    )
    image_file_path: Optional[str] = Field(
        default='',
        description='Path to the output image file.',
    )

