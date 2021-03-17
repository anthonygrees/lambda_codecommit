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
  
#### Step 3: Add a Trigger to the Lambda Function
Add a trigger to the Lambda function you just deployed and attach it to you AWS CodeCommit repository.
  
![Trigger](https://github.com/anthonygrees/lambda_codecommit/blob/main/images/trigger.png)
  
#### Step 4: Create Environment Variables for the Lambda Function
In order for the Lambda function to send the events triggered from your code commits to you Splunk instance, it needs to know `how` to connect to the HTTP Event Collector end point.  The connection details are stored in the Lambda Environment variables.
  
![UI](https://github.com/anthonygrees/lambda_codecommit/blob/main/images/env-var.png)
  
  
