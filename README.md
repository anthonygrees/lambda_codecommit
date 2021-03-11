# AWS CodeCommit to Splunk HEC Serverless Application
  
### About
This application was designed to be a generic approach for collecting AWS CodeCommit events and forwarding them onto a HEC (HTTP-Event-Collector) Endpoint in Splunk. 

Below is the current README for the serverless function. 

### CodeCommit-to-Splunk-HEC

This application will create a lambda function, with an API Gateway trigger. When deployed, you can use the API Gateway UR and "webhook-to-hec" endpoint, along with Environment Variables, to send data from AWS CodeCommit into Splunk. 

### Environment Variables defined in the Lambda Function:
 - `url` - the FQDN of your Splunk Server
 - `http_method` - whether you are running HEC with SSL enabled or not. You'll provide either http, or https.
 - `port` - the port you are running HEC on.
 - `token` - your HEC Token. 

### License

Apache License 2.0 (undefined)
