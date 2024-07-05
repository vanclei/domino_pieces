from pydantic import BaseModel, Field
from typing import Optional
from enum import Enum


class FCropFactorTypeType(str, Enum):
    """
    Output type for the result text
    """
    type_1 = '1'
    type_3_4 = '3/4'    
    type_1_2 = '1/2'
    type_1_4 = '1/4'


class InputModel(BaseModel):
    """
    Sleep Piece Input Model
    """

    imported_movies: str = Field(
        title="Movies",
        description='Movies for motion correction',
        json_schema_extra={
            "from_upstream": "always"
        }
    )
    
    do_plots: bool = Field(
        default=True,
        title="Make motion diagnostic plots",
        description="Whether or not to make plots of motion trajectories. Motion trajectories can also be inspected using the 'Curate Exposures' job type after this job completes."
    )

    num_plots: Optional[int] = Field(
        default=10,
        title="Number of movies to plot",
        description="Only make plots for the first this many movies."
    )

    random_num: Optional[int] = Field(
        default=None,
        title="Only process this many movies",
        description="Randomly select this many movies to process. Helpful for tweaking params."
    )

    memoryfix2: bool = Field(
        default=False,
        title="Low-memory mode",
        description="If running out of GPU memory, this option can be used to prioritize memory use at the expense of speed (BETA). The results are unchanged."
    )

    res_max_align: Optional[int] = Field(
        default=5,
        title="Maximum alignment resolution (A)",
        description="Maximum resolution (in A) to consider when aligning frames. Generally, betwen 5A and 3A is best."
    )

    bfactor: Optional[int] = Field(
        default=500,
        title="B-factor during alignment",
        description="B-factor that blurs frames before aligning. Generally 500 to 100 is best."
    )

    frame_start: Optional[int] = Field(
        default=0,
        title="Start frame (included, 0-based)",
        description="Which frame number, starting at zero, to begin motion correction from. This value controls how many early frames are dropped from the motion corrected result. This value will also be used in local motion correction."
    )

    frame_end: Optional[int] = Field(
        default=None,
        title="End frame (excluded, 0-based) ",
        description="Which frame number, starting at zero, to not include in motion correction, also excluding all frames after this one. Generally this does not improve results, as later frames are downweighted during dose weighting in local motion correction."
    )

    output_fcrop_factor: FCropFactorTypeType = Field(
        default=FCropFactorTypeType.type_1,
        title="Output F-crop factor",
        description="Output Fourier cropping factor. 1.0 means no cropping, 1/2 means crop to 1/2 the resolution, etc."
    )

    override_total_exp: Optional[int] = Field(
        default=None,
        title="Override e/A^2",
        description="Override the dose (in total e/A^2 over the exposure) that was given at import time but can be overridden here."
    )

    variable_dose: bool = Field(
        default=False,
        title="Allow Variable Dose",
        description="Enable correct processing when frames have variable dose fractionation"
    )

    smooth_lambda_cal: Optional[float] = Field(
        default=0.5,
        title="Calibrated smoothing",
        description="Calibrated smoothing constant applied to trajectories"
    )

    override_K_Z: Optional[int] = Field(
        default=None,
        title="Override knots Z",
        description="Override automatically selected spline order for Z dimension (time)"
    )

    override_K_Y: Optional[int] = Field(
        default=None,
        title="Override knots Y",
        description="Override automatically selected spline order for Y dimension (vertical)"
    )

    override_K_X: Optional[int] = Field(
        default=None,
        title="Override knots X",
        description="Override automatically selected spline order for X dimension (horizontal)"
    )

    compute_num_gpus: Optional[int] = Field(
        default=1,
        title="Number of GPUs to parallelize",
        description="Number of GPUs over which to parallelize computation."
    )      


class OutputModel(BaseModel):
    micrographs: Optional[str] = Field(
        title='Micrographs',
        description='Micrographs full-frame aligned',
    )
    micrographs_incomplete: Optional[str] = Field(
        title='Micrographs incomplete',
        description='Incomplete Micrographs full-frame aligned',
    )

