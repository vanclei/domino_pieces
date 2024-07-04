from pydantic import BaseModel, Field
from typing import Optional

class InputModel(BaseModel):
    """
    Import Movies Piece Input Model
    """

    job_start: str = Field(
        description='Job Start',
        json_schema_extra={
            "from_upstream": "always"
        }
    )

    blob_paths: Optional[str] = Field(
        default=None,
        title="Movies data path",
        description="Absolute path, wildcard-expression (e.g. /mount/data/somewhere/*.mrcs) that will be imported. MRC (mrc, mrcs, stk) and TIFF format supported."
    )

    gainref_path: Optional[str] = Field(
        default=None,
        title="Gain reference path",
        description="Absolute path to a single gain reference for all the raw data, in MRC format. Leave blank if data is already gain-corrected."
    )

    defect_path: Optional[str] = Field(
        default=None,
        title="Defect file path",
        description="Absolute path to a defect file for all the raw data. This should be a .txt file. Leave blank if not applicable."
    )

    gainref_flip_x: bool = Field(
        default=False,
        title="Flip gain ref & defect file in X?",
        description="Flip gain ref and defect file left-to-right (in X axis)"
    )

    gainref_flip_y: bool = Field(
        default=False,
        title="Flip gain ref & defect file in Y?",
        description="Flip gain ref and defect file top-to-bottom (in Y axis)"
    )

    gainref_rotate_num: Optional[int] = Field(
        default=0,
        title="Rotate gain ref?",
        description="Rotate gain ref counter-clockwise by 90 degrees this many times"
    )

    psize_A: Optional[int] = Field(
        default=None,
        title="Raw pixel size (A)",
        description="Pixel size of the raw movie data in Angstroms"
    )

    accel_kv: Optional[int] = Field(
        default=None,
        title="Accelerating Voltage (kV)",
        description=""
    )

    cs_mm: Optional[int] = Field(
        default=None,
        title="Spherical Aberration (mm)",
        description=""
    )

    total_dose_e_per_A2: Optional[int] = Field(
        default=None,
        title="Total exposure dose (e/A^2)",
        description=""
    )

    negative_stain_data: bool = Field(
        default=False,
        title="Negative Stain Data",
        description="If Negative Stain Data is on, this indicates that there are light particles on dark background. If it's off, this indicates the movies have dark particles on light background (cryo-em data)."
    )

    phase_plate_data: bool = Field(
        default=False,
        title="Phase Plate Data",
        description=""
    )

    override_exp_group_id: Optional[int] = Field(
        default=None,
        title="Override Exposure Group ID",
        description=""
    )

    skip_header_check: bool = Field(
        default=False,
        title="Skip Header Check",
        description="Skip reading of every header file to increase import speed. WARNING: this assumes exposure shapes and extensions are consistent across the entire dataset."
    )

    eer_num_fractions: Optional[int] = Field(
        default=40,
        title="EER Number of Fractions",
        description="Number of fractions to make out of the EER input data."
    )

    eer_upsamp_factor: Optional[int] = Field(
        default=2,
        title="EER Upsampling Factor",
        description="Upsampling factor when decoding EER input data. Note that the pixel size you provide should be the raw pixel size at the nominal 4k sensor, not the pixel size after EER upsampling. "
    )
    
class OutputModel(BaseModel):
    imported_movies: Optional[str] = Field(
        title='Imported movies',
        description='Imported movies',
    )
    failed_movies: Optional[str] = Field(
        title='Failed movies',
        description='Movies that failed to import successfully.',
    )
