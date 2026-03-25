import operator
from typing import Annotated, List, Dict, Optional, Any, TypedDict


#defined the compliance result
#Error report
class ComplianceIssue(TypedDict):
    category:str
    description:str # specific details of violation
    severity:str  #critical|| warning
    timestamp: Optional[str]


#define global graph state
#this defines the state that gets passed around in the agentic workflow
class VideoAudioState(TypedDict):
    '''
    Defines the data schema for langGraph execution content
    Main container:Hold all the information about the audit
    right from intial URL to the final report
    '''

    #input parameters
    video_url:str
    video_id:str

    #ingestion and extraction data
    local_file_path:Optional[str]
    video_metadata:Dict[str,Any] # {"duration":15 , "resolution":"1080p"}
    transcript:Optional[str]  # fully extracted speech to text
    ocr_text:List[str]  
    

    #analysis output
    #stores the list of all the violation found by AI
    compliance_results:Annotated[List[ComplianceIssue], operator.add]

    #final deliverables
    final_status:str  #pass or fail
    final_report:str  #markdown format

    #system obervability
    #errors: API timeout, system level errors
    #list of system level crashes
    errors:Annotated[List[str], operator.add]

