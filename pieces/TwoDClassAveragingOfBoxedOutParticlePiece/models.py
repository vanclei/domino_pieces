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
    inputs: str = Field(
        default=False,
        description='Inputs',
    )
    window_dataset_real_space: bool = Field(
        default=False,
        description='Window dataset (real-space)',
    )
    window_inner_radius: float = Field(
        default=False,
        description='Window inner radius',
    ) 
    window_outer_radius: float = Field(
        default=False,
        description='Window outer radius',
    )         
    number_of_2d_classes: float = Field(
        default=False,
        description='Number of 2D classes',
    )     
    maximum_resolution: float = Field(
        default=False,
        description='Maximum resolution (Å)',
    )        
    maximum_alignment_res: float = Field(
        default=False,
        description='Maximum alignment res (Å)',
    )        
    initial_classification_uncertainty_factor: float = Field(
        default=False,
        description='Initial classification uncertainty factor',
    ) 
    use_circular_mask_on_2D_classes: bool = Field(
        default=False,
        description='Use circular mask on 2D classes',
    )    
    circular_mask_diameter: float = Field(
        default=False,
        description='Circular mask diameter (Å)',
    )     
    circular_mask_diameter_outer: float = Field(
        default=False,
        description='Circular mask diameter outer (Å)',
    )              
    re_center_2D_classes: bool = Field(
        default=False,
        description='Re-center 2D classes',
    )
    re_center_mask_threshold: float = Field(
        default=False,
        description='Re-center mask threshold',
    )
    re_center_mask_binary: bool = Field(
        default=False,
        description='Re-center mask binary',
    )
    align_filament_classes_vertically: bool = Field(
        default=False,
        description='Align filament classes vertically (BETA)',
    )    
    output_filament_in_plane_rotations: bool = Field(
        default=False,
        description='Output filament in-plane rotations',
    )
    force_max_over_poses_shifts: bool = Field(
        default=False,
        description='Force Max over poses/shifts',
    )    
    cft_flip_phases_only: bool = Field(
        default=False,
        description='CTF flip phases only',
    )
    randomly_perturb_poses_radians: float = Field(
        default=False,
        description='Randomly perturb poses radians',
    )    
    number_of_final_full_iterations: float = Field(
        default=False,
        description='Number of final full iterations',
    )
    number_of_online_EM_iterations: float = Field(
        default=False,
        description='Number of online-EM iterations',
    )
    batchsize_per_class: float = Field(
        default=False,
        description='Batchsize per class',
    )      
    two_D_initial_scale: float = Field(
        default=False,
        description='2D initial scales',
    )          
    two_D_zeropad_factor: float = Field(
        default=False,
        description='2D zeropad factor',
    )  
    ignore_DC_from_image_data: bool = Field(
        default=False,
        description='Ignore DC from image data',
    )    
    min_over_scale_after_first_iteration: bool = Field(
        default=False,
        description='Min over scale after first iteration',
    )    
    enforce_non_negativity: bool = Field(
        default=False,
        description='Enforce non-negativity',
    )     
    use_clamp_solvent_to_solve_2D_classes: bool = Field(
        default=False,
        description='Use clamp-solvent to solve 2D classes',
    )   
    use_FRC_based_regularizer: bool = Field(
        default=False,
        description='Use FRC based regularizer',
    )       
    use_full_FRC: bool = Field(
        default=False,
        description='Use full FRC',
    )
    iteration_to_start_annealing_sigma: float = Field(
        default=False,
        description='Iteration to start annealing sigma',
    )      
    number_of_iteration_to_anneal_sigma: float = Field(
        default=False,
        description='Number of iteration to anneal sigma',
    )
    use_white_noise_model: bool = Field(
        default=False,
        description='Use white noise model',
    )   
    show_plots_from_intermediate_steps: bool = Field(
        default=False,
        description='Show plots from intermediate steps',
    )        
    random_seed: float = Field(
        default=False,
        description='Random seed',
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
