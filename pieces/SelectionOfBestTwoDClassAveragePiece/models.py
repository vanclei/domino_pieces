from pydantic import BaseModel, Field


class InputModel(BaseModel):
    """
    Sleep Piece Input Model
    """

    input_image: str = Field(
        description='Input image. It should be either a path to a file, or a base64 encoded string.',
        json_schema_extra={
            "from_upstream": "always"
        }
    )


class OutputModel(BaseModel):
    image_base64_string: str = Field(
        default='',
        description='Base64 encoded string of the output image.',
    )
    image_file_path: str = Field(
        default='',
        description='Path to the output image file.',
    )
