from pydantic import BaseModel, Field

class InputModel(BaseModel):
    """
    Import Movies Piece Input Model
    """

    movies_data_path: str = Field(
        description="Path to Movie Data Path"
    )
    gain_reference_path: str = Field(
        description="Gain Reference path"
    )    
    defect_file_path: str = Field(
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
    rotate_gain_ref: float = Field(
        default=False,
        description='Rotate gain ref?',
    )          
    raw_pixel_size_A: float = Field(
        default=False,
        description='Raw pixel size (A)',
    )    
    accelerating_voltage_kV: float = Field(
        default=False,
        description='Accelerating Voltage (kV)',
    )        
    spherical_aberration_mm: float = Field(
        default=False,
        description='Spherical Abberation (mm)',
    )
    total_exposure_dose: float = Field(
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
    override_exposure_group_id: float = Field(
        default=False,
        description='Override Exposure Group ID',
    )
    skip_header_check: bool = Field(
        default=False,
        description='Skip Header Check',
    ) 
    eer_number_of_fractions: float = Field(
        default=False,
        description='EER Number of Fractions',
    )
    eer_upsampling_factor: float = Field(
        default=False,
        description='EER Upsampling Factor',
    )        

class OutputModel(BaseModel):
    """
    Sleep Piece Output Model
    """
    base64_bytes_data: str = Field(
        description='Output data as base64 encoded string.'
    )
