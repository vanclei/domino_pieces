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
        description='Input image. It should be either a path to a file, or a base64 encoded string.',
        json_schema_extra={
            "from_upstream": "always"
        }
    )

    input_image: str = Field(
        description='Input image. It should be either a path to a file, or a base64 encoded string.',
        json_schema_extra={
            "from_upstream": "always"
        }
    )
    
    abinit_K: Optional[int] = Field(
        default=1,
        title="Number of Ab-Initio classes",
        description="The number of classes. Each class will be randomly initialized independently, unless an initial structure was provided, in which case each class will be a random variant of the initial structure"
    )
        

    abinit_num_particles: Optional[int] = Field(
        default=None,
        title="Num particles to use",
        description="The number of particles to use in optimization. Only this many particles will be read and classified, starting from the beginning of the particle stack. The output of this job will only contain this many particles as well."
    )
        

    abinit_max_res: Optional[float] = Field(
        default=12.0,
        title="Maximum resolution (Angstroms)",
        description="Maximum frequency to consider"
    )
        

    abinit_init_res: Optional[float] = Field(
        default=35.0,
        title="Initial resolution (Angstroms)",
        description="Starting frequency to consider"
    )
        

    abinit_num_init_iters: Optional[int] = Field(
        default=200,
        title="Number of initial iterations",
        description="Number of initial iterations before annealing starts"
    )
        

    abinit_num_final_iters: Optional[int] = Field(
        default=300,
        title="Number of final iterations",
        description="Number of final iterations after annealing ends"
    )
        

    abinit_radwn_step: Optional[float] = Field(
        default=0.04,
        title="Fourier radius step",
        description="Increase in Fourier radius a each iteration"
    )
        

    abinit_window: Optional[bool] = Field(
        default=True,
        title="Window structures in real space",
        description="Softly window the reconstructions in real space at each iteration"
    )
        

    abinit_center: Optional[bool] = Field(
        default=True,
        title="Center structures in real space",
        description="Center the reconstructions in real space at each iteration"
    )
        

    abinit_scale_mg_correct: Optional[bool] = Field(
        default=False,
        title="Correct for per-micrograph optimal scales",
        description="(Experimental) Estimate and compute optimal scales per micrograph"
    )
        

    abinit_scale_compute: Optional[bool] = Field(
        default=False,
        title="Compute per-image optimal scales",
        description="(Experimental) Estimate and compute optimal scales per image"
    )
        

    abinit_mom: Optional[int] = Field(
        default=0,
        title="SGD Momentum",
        description="Momentum for stochastic gradient descent"
    )
        

    abinit_sparsity: Optional[int] = Field(
        default=0,
        title="Sparsity prior",
        description=""
    )
        

    abinit_minisize_init: Optional[int] = Field(
        default=90,
        title="Initial minibatch size",
        description="Number of images per minibatch at the beginning. Set to zero to autotune. Autotune sets the initial minibatch size to 300 if the particle is small (box extent is less than 220A) or symmetry order is greater than 4."
    )
        

    abinit_minisize: Optional[int] = Field(
        default=300,
        title="Final minibatch size",
        description="Final number of images per minibatch. Set to zero to autotune. Autotune sets the minibatch size to 1000 if the particle is small (box extent is less than 220A) or symmetry order is greater than 4."
    )
        

    abinit_minisize_epsilon: Optional[float] = Field(
        default=0.05,
        title="Abinit minisize epsilon",
        description="Parameter that controls batch size when autotuning minibatch size. Set closer to zero for larger batches"
    )
        

    abinit_minisize_minp: Optional[float] = Field(
        default=0.01,
        title="Abinit minisize minp",
        description="Parameter that controls how the batch size adjusts to low probability classes when autotuning minibatch sizes"
    )
        

    abinit_minisize_num_init_iters: Optional[int] = Field(
        default=300,
        title="Initial minibatch size num iters",
        description="When to switch to final number of images per minibatch"
    )
        

    abinit_noise_model: Optional[str] = Field(
        default="symmetric",
        title="Noise model (white, symmetric or coloured)",
        description="Noise model to use. Valid options are white, coloured or symmetric. Symmetric is the default, meaning coloured with radial symmetry"
    )
        

    abinit_noise_priorw: Optional[int] = Field(
        default=50,
        title="Noise priorw",
        description="Weight of the prior for estimating noise (units of # of images)"
    )
        

    abinit_noise_initw: Optional[int] = Field(
        default=5000,
        title="Noise initw",
        description="Weight of the initial noise estimate (units of # of images)"
    )
        

    abinit_noise_init_sigmascale: Optional[int] = Field(
        default=None,
        title="Noise initial sigma-scale",
        description="Scale factor initially applied to the base noise estimate, set to null to auto-estimate based on ESS target"
    )
        

    abinit_class_anneal_beta: Optional[float] = Field(
        default=0.1,
        title="Class similarity",
        description="Expected similarity of structures from different classes. A number between 0 and 1. 0 means classes are independent, 1 means classes are very similar"
    )
        

    abinit_class_anneal_start: Optional[int] = Field(
        default=300,
        title="Class similarity anneal start iter",
        description="Start point for annealing the similarity factor"
    )
        

    abinit_class_anneal_end: Optional[int] = Field(
        default=350,
        title="Class similarity anneal end iter",
        description="Finish point for annealing the similarity factor"
    )
        

    abinit_target_initial_ess_fraction: Optional[float] = Field(
        default=0.011,
        title="Target 3D ESS Fraction",
        description="Fraction of poses at the first iteration that should have significant probability (used for auto-tuning initial noise sigma-scale)"
    )
        

    abinit_symmetry: Optional[str] = Field(
        default="C1",
        title="Symmetry",
        description="Symmetry enforced (C, D, I, O, T). Eg. C1, D7, C4 etc. Enforcing symmetry above C1 is not recommended for ab-initio reconstruction"
    )
        

    abinit_high_lr_duration: Optional[int] = Field(
        default=100,
        title="Initial learning rate duration",
        description="How long to apply the initial learning rate"
    )
        

    abinit_high_lr: Optional[float] = Field(
        default=0.4,
        title="Initial learning rate",
        description="Learning rate (step size) used at the start of optimization to help make rapid progress"
    )
        

    abinit_nonneg: Optional[bool] = Field(
        default=True,
        title="Enforce non-negativity",
        description="Enforce non-negativity of structures in real space during optimization. Non-negativity is recommended for ab-initio reconstruction"
    )
        

    abinit_ignore_dc: Optional[bool] = Field(
        default=True,
        title="Ignore DC component",
        description="Ignore the DC component of images. Should be true"
    )
        

    abinit_seed_init: Optional[int] = Field(
        default=None,
        title="Initial structure random seed",
        description="Random seed for generating initial structures. Set to null for each run to use a different seed based off the dataset random seed"
    )
        

    abinit_init_radwn_cutoff: Optional[int] = Field(
        default=7,
        title="Initial structure lowpass (Fourier radius)",
        description="Lowpass filter cutoff in Fourier radius for initial random structures"
    )
        

    abinit_use_engine: Optional[bool] = Field(
        default=True,
        title="Use fast codepaths",
        description=""
    )
        

    intermediate_plots: Optional[bool] = Field(
        default=True,
        title="Show plots from intermediate steps",
        description=""
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
