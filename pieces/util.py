import json
import time
import requests    
import logging


def generate_return(logger:logging, workflow_type:str, task_name:str, input_data):    
    
    inputs_values = input_data
    logger.info(inputs_values)
    job_start = input_data.get('job_start')
    logger.info(job_start)
    del inputs_values['job_start']
    inputs_values.update({'workflow_type':workflow_type, 'task_name':task_name, 'job_start':job_start})
    
    inputs_values = {"body": inputs_values}

    result = requests.post('http://172.17.0.1:8000/encore/create_workflow', json=inputs_values, verify=False)
    workflow_created = result.json()
    result = {}
    
    if workflow_created.get("status", "failed") == "failed":
        raise Exception("Failed coming form the server")
        
    if workflow_created.get("status", "failed") == "success":
        workflow_id = workflow_created.get("workflow_id", None)
        
        latest_status = {}
        if workflow_id:
            inputs_values = {"body": {"workflow_id": workflow_id}}
            while True:
                result = requests.post('http://172.17.0.1:8000/encore/get_workflow', json=inputs_values, verify=False)
                workflow_status = result.json()   
                if workflow_status.get("status", "failed") in ["success", "failed"]:
                    workflow = workflow_status.get("workflow", {})
                    if workflow.get('status', "processing") in ["completed", "failed"]:
                        latest_status = workflow
                        break
                time.sleep(1)
            
            if latest_status.get('status', "completed") == "completed":
                return latest_status.get('result', {})

            if latest_status.get('status', "failed") == "failed":
                raise Exception("Failed to complete task")