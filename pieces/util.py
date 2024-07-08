import json
import time
import requests    
import logging
import os


def generate_return(logger:logging, workflow_type:str, job_type:str, input_data):   
    
    for name, value in os.environ.items():
        print("{0}: {1}".format(name, value))
    
    workflow_unique_id = os.environ.get("AIRFLOW_CONTEXT_DAG_RUN_ID")
    r = json.dumps(os.environ.get("DOMINO_RUN_PIECE_KWARGS"))
    print(os.environ.get("DOMINO_RUN_PIECE_KWARGS"))
    print(r)
    task_params = json.loads(r)
    print(task_params)

    inputs_values = input_data.model_dump(mode='json')
    
    for key, item in input_data.model_fields.items():
        if item.json_schema_extra:
            inputs_values.update({key: json.loads(inputs_values.get(key))})

    params = {'workflow_unique_id': workflow_unique_id, 'task_params': task_params, 'workflow_type':workflow_type, 'job_type':job_type, 'params': inputs_values}
    print('params')
    print(params)

    result = requests.post('http://172.17.0.1:8000/encore/create_workflow', json=params, verify=False)
    workflow_created = result.json()
    #workflow_created = {"status":"success", "workflow_id":24}
    
    if workflow_created.get("status", "failed") == "failed":
        raise Exception("fail coming form the server")
        
    if workflow_created.get("status", "failed") == "success":
        workflow_id = workflow_created.get("workflow_id", None)
        
        if workflow_id:
            while True:
                result = requests.post('http://172.17.0.1:8000/encore/get_workflow', json={"workflow_id": workflow_id}, verify=False)
                workflow = result.json()   
                
                if workflow.get("status", "failed") == "failed":
                    raise Exception(workflow.get("message", ""))
                    
                if workflow.get("status", "failed") == "success":
                     
                    workflow = workflow.get("workflow", {})
                    
                    if workflow.get('status', "processing") == "completed":
                        result = json.loads(workflow.get('result',"{}"))
                        return result
                
                    if workflow.get("status", "failed") == "failed":
                        raise Exception("fail to complete task")    
                
                time.sleep(1)
