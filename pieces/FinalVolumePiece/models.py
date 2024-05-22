from pydantic import BaseModel, Field
from typing import Optional
from enum import Enum

class NoiseModelType(str, Enum):
    """
    Output type for the result text
    """
    white = "white"
    symmetric = "symmetric"
    coloured = "coloured"



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
    particles: Optional[int] = Field(
        default=False,
        description='Particles',
    )
    volume: Optional[str] = Field(
        default=False,
        description='Volume',
    )
    mask: Optional[str] = Field(
        default=False,
        description='Mask',
    )    
    window_dataset_real_space: bool = Field(
        default=False,
        description='Window dataset (real-space)',
    )    
    window_inner_radius: Optional[float] = Field(
        default=False,
        description='Window inner radius',
    ) 
    window_outer_radius: Optional[float] = Field(
        default=False,
        description='Window outer radius',
    )        
    symmetry: Optional[str] = Field(
        default=False,
        description='Symmetry',
    )     
    do_symmetry_alignment: bool = Field(
        default=False,
        description='Do symmetry alignment',
    )    
    re_estimate_greyscale_level_of_input_reference: bool = Field(
        default=False,
        description='Re-estimate greyscale level of input reference',
    )     
    number_of_extra_final_passes: Optional[float] = Field(
        default=False,
        description='Number of extra final passes',
    )         
    maximum_align_resolution: Optional[float] = Field(
        default=False,
        description='Maximum align resolution (Å)',
    )    
    initial_lowpass_resolution: Optional[float] = Field(
        default=False,
        description='Initial lowpass resolution (Å)',
    )        
    GSFSC_split_resolution: Optional[float] = Field(
        default=False,
        description='GSFSC split resolution (Å)',
    )  
    force_re_do_GS_split: bool = Field(
        default=False,
        description='Force re-do GS split',
    )          
    enforce_non_negativity: bool = Field(
        default=False,
        description='Enforce non-negativity',
    )        
    window_structure_in_real_space: bool = Field(
        default=False,
        description='Window structure in real space',
    )        
    skip_interpolant_premult: bool = Field(
        default=False,
        description='Skip interpolant premult',
    )     
    ignore_DC_component: bool = Field(
        default=False,
        description='Ignore DC component',
    )     
    ignore_tilt: bool = Field(
        default=False,
        description='Ignore tilt',
    )      
    ignore_trefoil: bool = Field(
        default=False,
        description='Ignore trefoil',
    )     
    ignore_tetra: bool = Field(
        default=False,
        description='Ignore tetra',
    )     
    use_random_ordering_of_particles: bool = Field(
        default=False,
        description='Use random ordering of particles',
    )
    initial_batchsize: Optional[float] = Field(
        default=False,
        description='Initial batchsize',
    )      
    batchsize_epsilon: Optional[float] = Field(
        default=False,
        description='Batchsize epsilon',
    )   
    batchsize_snrfactor: Optional[float] = Field(
        default=False,
        description='Batchsize snrfactor',
    )      
    scale_min_use_start_iter: Optional[float] = Field(
        default=False,
        description='Scale min/use start iter',
    )         
    scale_min_use_start_iter: Optional[float] = Field(
        default=False,
        description='Scale min/use start iter',
    )         
    noise_model: NoiseModelType = Field(
        default=NoiseModelType.symmetric,
        description='Noise model',
    )    
    noise_priorw: Optional[float] = Field(
        default=False,
        description='Noise priorw',
    ) 
    noise_initw: Optional[float] = Field(
        default=False,
        description='Noise initw',
    )      
    noise_initial_sigma_scale: Optional[float] = Field(
        default=False,
        description='Noise initial sigma-scale',
    )        
    initialize_noise_model_from_images: bool = Field(
        default=False,
        description='Initialize noise model from images',
    )    
    dynamic_mask_threshold: Optional[float] = Field(
        default=False,
        description='Dynamic mask threshold (0-1)',
    )       
    dynamic_mask_near: Optional[float] = Field(
        default=False,
        description='Dynamic mask near (Å)',
    )  
    dynamic_mask_far: Optional[float] = Field(
        default=False,
        description='Dynamic mask far (Å)',
    )      
    dynamic_mask_start_resolution: Optional[float] = Field(
        default=False,
        description='Dynamic mask start resolution (A)',
    )             
    dynamic_mask_use_absolute_value: bool = Field(
        default=False,
        description='Dynamic mask use absolute value',
    )
    show_plots_from_intermediate_steps: bool = Field(
        default=False,
        description='Show plots from intermediate steps',
    )  
    GPU_batch_size_of_images: Optional[float] = Field(
        default=False,
        description='GPU batch size of images',
    )        
    optimize_per_particle_defocus: bool = Field(
        default=False,
        description='Optimize per-particle defocus',
    )                  
    num_particles_to_plot: Optional[float] = Field(
        default=False,
        description='Num. particles to plot',
    )  
    minimum_fit_res: Optional[float] = Field(
        default=False,
        description='Minimum Fit Res (Å)',
    )  
    defocus_search_range: Optional[float] = Field(
        default=False,
        description='Defocus Search Range (Å +/-)',
    )      
    defocus_GPU_batch_size_of_images: Optional[float] = Field(
        default=False,
        description='GPU batch size of images',
    )      
    optimize_per_group_CTF_params: bool = Field(
        default=False,
        description='Optimize per-group CTF params',
    )              
    num_groups_to_plot: Optional[float] = Field(
        default=False,
        description='Num. groups to plot',
    )       
    binning_to_apply_to_plots: Optional[float] = Field(
        default=False,
        description='Binning to apply to plots',
    )         
    global_minimum_fit_res: Optional[float] = Field(
        default=False,
        description='Global Minimum Fit Res (Å)',
    )
    fit_tilt: bool = Field(
        default=False,
        description='Fit Tilt',
    )
    fit_trefoil: bool = Field(
        default=False,
        description='Fit Trefoil',
    )    
    fit_spherical_aberration: bool = Field(
        default=False,
        description='Fit Spherical Aberration',
    )      
    fit_tetrafoil: bool = Field(
        default=False,
        description='Fit Tetrafoil',
    )  
    fit_anisotropic_mag: bool = Field(
        default=False,
        description='Fit Anisotropic Mag',
    ) 
    global_GPU_batch_size_of_images: Optional[float] = Field(
        default=False,
        description='Global GPU batch size of images',
    )                   
    do_EWS_correction: bool = Field(
        default=False,
        description='Do EWS correction',
    )  
    EWS_curvature_sign: Optional[str] = Field(
        default=False,
        description='EWS curvature sign',
    )
    random_seed: Optional[float] = Field(
        default=False,
        description='Random seed',
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
