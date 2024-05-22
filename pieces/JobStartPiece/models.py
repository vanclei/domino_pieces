from pydantic import BaseModel, Field
from enum import Enum


class PriorityType(str, Enum):
    """
    Output type for the result text
    """
    urgent = "1 - Urgent"
    high = "2 - High"
    moderated = "3 - Moderated"
    minor = "4 - Minor"
    standard = "5 - Standard"
    
class SampleTypeType(str, Enum):
    """
    Output type for the result text
    """
    type_1 = "Type 1"
    type_2 = "Type 2"    
    type_3 = "Type 3"    
    
class UserType(str, Enum):
    """
    Output type for the result text
    """
    sen_a = "Sen A"
    vanclei_p = "Vanclei P"    
    tran_l = "Tran Le"

class InputModel(BaseModel):
    priority: PriorityType = Field(
        default=PriorityType.standard,
        description='Priority',
    )
    job_number: str = Field(
        description="Job Number"
    )
    job_name: str = Field(
        description="Job Name"
    )
    sample_type: SampleTypeType = Field(
        default=SampleTypeType.type_3,
        description='Sample Type',
    )    
    project_investigator: UserType = Field(
        default=UserType.sen_a,
        description='Projct Investigator',
    )       
    project_assignment: UserType = Field(
        default=UserType.sen_a,
        description='Projct Assignment',
    )       

class OutputModel(BaseModel):
    """
    Sleep Piece Output Model
    """
    message: str = Field(
        description="Job Start Created"
    )
