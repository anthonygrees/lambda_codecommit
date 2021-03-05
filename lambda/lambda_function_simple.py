import json
import urllib3
import os
import ssl
import boto3

codecommit = boto3.client('codecommit')

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
    #print("*** Connected to %s as %s" % (http_method, url))
    print("*** Event details" % (event))

    #Build Full URL out of Parameters
    full_url = http_method+'://'+url+':'+port+'/services/collector/raw'
    
    cert_reqs = ssl.CERT_NONE
    urllib3.disable_warnings()
    http = urllib3.PoolManager(cert_reqs = cert_reqs)
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    
    #Log the updated references from the event
    references = { reference['ref'] for reference in event['Records'][0]['codecommit']['references'] }
    print("***References: "  + str(references))
    
    #Get the repository from the event and show its git clone URL
    repository = event['Records'][0]['eventSourceARN'].split(':')[5]
    try:
        response = codecommit.get_repository(repositoryName=repository)
        
        print("Clone URL: " +response['repositoryMetadata']['cloneUrlHttp'])
        #return response['repositoryMetadata']['cloneUrlHttp']
    except Exception as e:
        print(e)
        print('Error getting repository {}. Make sure it exists and that your repository is in the same region as this function.'.format(repository))
        raise e
    
    #Post Event
    r = http.request('POST', full_url, body=response['repositoryMetadata']['cloneUrlHttp'], headers={'Content-Type': 'application/json', 'Authorization':'Splunk '+token})
    #r = http.request('POST', full_url, body='TestMe', headers={'Content-Type': 'application/json', 'Authorization':'Splunk '+token})
    ##r = http.request('POST', full_url, body=event["body"], headers={'Content-Type': 'application/json', 'Authorization':'Splunk '+token})
    print("*** R is %s" % (r))

    return {
        'statusCode': 200,
        'body':'Success'
    }
