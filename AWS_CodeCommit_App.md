# AWS CodeCommit App for Splunk
  
### Description
The app shows users code commits and branch details as events from AWS CodeCommit.  
  
![UI](https://github.com/anthonygrees/lambda_codecommit/images/ui.png)
  
### Feeding Data
Data is sent via an Event Trigger from AWS CodeCommit.  The Event Trigger is monitored by a Lambda Function which sends the `json` output to a Splunk HEC (HTTP Event Collector) end point.  
  
  
