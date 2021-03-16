# AWS CodeCommit App for Splunk
  
### Description
The app shows users code commits and branch details as events from AWS CodeCommit.  
  
![UI](https://github.com/anthonygrees/lambda_codecommit/blob/main/images/ui.png)
  
### Feeding Data
Data is sent via an Event Trigger from AWS CodeCommit.  The Event Trigger is monitored by a Lambda Function which sends the `json` output to a Splunk HEC (HTTP Event Collector) end point.  
  
### Setup the AWS CodeCommit App
The following steps will ensure the app has data:  
  
#### Step 1: Install the Application
You can install the app from the command line or from SplunkBase.  
  
To install via the CLI, run the following command.  
```bash
sudo /opt/splunk/bin/splunk install app /tmp/awscodecommit.tgz -auth user:password
```
  
#### Step 2: Deploy the Lambda Application
Navigate to the [codecommit-to-hec-splunk](https://serverlessrepo.aws.amazon.com/applications/us-east-1/457777705445/codecommit-to-splunk-hec) lambda application and click the deploy button.
  
![UI](https://github.com/anthonygrees/lambda_codecommit/blob/main/images/lambda.png)
