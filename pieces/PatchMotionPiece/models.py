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
    make_motion_diagnostics_plots: bool = Field(
        default=False,
        description='Make motion diagnostic plots',
    )    
    number_of_movies_to_plot: Optional[float] = Field(
        default=False,
        description='Number of movies do plot',
    )       
    only_process_this_many_movies: Optional[float] = Field(
        default=False,
        description='Only process this many movies',
    )
    reduce_gpu_memory_usage: bool = Field(
        default=False,
        description='Reduce GPU memory usage',
    )     
    low_memory_mode: bool = Field(
        default=False,
        description='Low-memory mode',
    )      
    maximum_alignment_resolution: Optional[float] = Field(
        default=False,
        description='Maximum alignment resolution (A)',
    )      
    b_factor_during_alignment: Optional[float] = Field(
        default=False,
        description='B-factor during alignment',
    )       
    start_frame: Optional[float] = Field(
        default=False,
        description='Start frame (included, 0-based)',
    )      
    end_frame: Optional[float] = Field(
        default=False,
        description='End frame (excluded, 0-based)',
    )
    output_f_crop_factor: Optional[float] = Field(
        default=False,
        description='Output F-crop factor',
    )    
    override_e_a: Optional[float] = Field(
        default=False,
        description='Override e/A^2',
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

