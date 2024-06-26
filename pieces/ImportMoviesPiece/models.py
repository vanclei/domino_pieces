from pydantic import BaseModel, Field
from typing import Optional

class InputModel(BaseModel):
    """
    Import Movies Piece Input Model
    """

    movies_data_path: Optional[str] = Field(
        description="Path to Movie Data Path"
    )
    gain_reference_path: Optional[str] = Field(
        description="Gain Reference path"
    )    
    defect_file_path: Optional[str] = Field(
        description="Defect file path"
    )   
    flip_gain_ref_and_defect_file_in_X: bool = Field(
        default=False,
        description='Flip gain ref & defect file in X?',
    )        
    flip_gain_ref_and_defect_file_in_Y: bool = Field(
        default=False,
        description='Flip gain ref & defect file in Y?',
    )      
    rotate_gain_ref: Optional[float] = Field(
        default=False,
        description='Rotate gain ref?',
    )          
    raw_pixel_size_A: Optional[float] = Field(
        default=False,
        description='Raw pixel size (A)',
    )    
    accelerating_voltage_kV: Optional[float] = Field(
        default=False,
        description='Accelerating Voltage (kV)',
    )        
    spherical_aberration_mm: Optional[float] = Field(
        default=False,
        description='Spherical Abberation (mm)',
    )
    total_exposure_dose: Optional[float] = Field(
        default=False,
        description='Total exposure dose (e/A^2)',
    )       
    negative_stain_data: bool = Field(
        default=False,
        description='Negative Stain Data',
    )
    phase_plate_data: bool = Field(
        default=False,
        description='Phase Plate Data',
    )
    override_exposure_group_id: Optional[float] = Field(
        default=False,
        description='Override Exposure Group ID',
    )
    skip_header_check: bool = Field(
        default=False,
        description='Skip Header Check',
    ) 
    eer_number_of_fractions: Optional[float] = Field(
        default=False,
        description='EER Number of Fractions',
    )
    eer_upsampling_factor: Optional[float] = Field(
        default=False,
        description='EER Upsampling Factor',
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
