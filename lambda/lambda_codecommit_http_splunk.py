import json
import urllib3
import os
import ssl
import boto3
import argparse

codecommit = boto3.client('codecommit')
region = codecommit.meta.region_name

def lambda_handler(event, context):
    #Parse URL Parameters
    http_method_a = os.environ["http_method"]
    http_method = str(http_method_a)
    url_a = os.environ["url"]
    url = str(url_a)
    port_a = os.environ["port"]
    port = str(port_a)
    token_a = os.environ["token"]
    token = str(token_a)

    #Build Full URL out of Parameters
    full_url = http_method+'://'+url+':'+port+'/services/collector/raw'
    
    #Do not check SSL certs
    cert_reqs = ssl.CERT_NONE
    urllib3.disable_warnings()
    http = urllib3.PoolManager(cert_reqs = cert_reqs)
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    
    #Log the updated references from the event
    references = { reference['ref'] for reference in event['Records'][0]['codecommit']['references'] }
    
    #Get the repository from the event and show its git clone URL
    repository = event['Records'][0]['eventSourceARN'].split(':')[5]
    region = event['Records'][0]['eventSourceARN'].split(":")[3]
    branch = event['Records'][0]['codecommit']['references'][0]['ref'].split("/")[2];
    source_version = event['Records'][0]['codecommit']['references'][0]['commit']
    commit_time = event['Records'][0]['eventTime']
    eventTriggerName = event['Records'][0]['eventTriggerName']
    userIdentityARN =  event['Records'][0]['userIdentityARN'].split(':')[5]
    ##print("*** Event is %s" % (event))
    
    try:
        response = codecommit.get_repository(repositoryName=repository)
        response1 = '{"AWSCodeCommit": "data", "Repository_HTTP": "'+response['repositoryMetadata']['cloneUrlHttp']+'", "References": "'+str(references)+'", "Region": "'+region+'", "Branch": "'+branch+'", "Source_Version": "'+source_version+'", "Commit_Time": "'+commit_time+'", "EventTriggerName": "'+eventTriggerName+'", "UserIdentityARN": "'+userIdentityARN+'"}'
        
    except Exception as e:
        print(e)
        print('Error getting repository {}. Make sure it exists and that your repository is in the same region as this function.'.format(repository))
        raise e

    #Post Event
    r = http.request('POST', full_url, body=response1, headers={'Content-Type': 'application/json', 'Authorization':'Splunk '+token})

    return {
        'statusCode': 200,
        'body':'Success'
    }
