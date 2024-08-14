# Economic-Indicator-Data-Pipeline

## Overview

This repository contains an ETL (Extract, Transform, Load) pipeline designed to automate the process of
data extraction, transformation, and loading into a data warehouse in AWS S3. The pipeline is built using
Python and is orchestrated via Jenkins. The primary python script, 'etl.py', handles the ETL process, and 
the entire process is automated through a Jenkins pipeline defined in the Jenkinsfile. The pipeline serves 
as a foundation and is easily extensible, allowing for additional data sources, transformations, or destinations
to be added as needed.


## Pipeline  Features

- Automated ETL Process: The pipeline automates the extraction, transformation, and loading of data, ensuring 
timely updates and consistency across data sources.

- Virtual Environment Isolation: The ETL job is executed within a dedicated Python virtual environment
ensuring that all dependencies are properly managed and isolated from the system environment. This could 
also be done using a Docker Container. 

- Secure Environment Variables: Sensitive data such as API keys, database credentials, and other environment 
variables are securely managed using Jenkins' credentials binding feature. The environment variables are 
securely injected into the job at runtime and are not exposed in the code repository, protecting them from
unauthorized access.

- Workspace Cleanup: The pipeline includes a cleanup step to ensure that no sensitive data or unnecessary files
remain on the server after the job completes.


## Pipeline Orchestration

- Code Checkout: The pipeline begins by pulling the latest code from the specified branch of the Git repository.
This ensures that the ETL job always runs with the most up-to-date code.

- Setup Virtual Environment: A Python virtual environment (etl-venv) is created and all required Python dependencies
are installed from the requirements.txt file. This setup ensures that the ETL job runs in a controlled environment 
with all necessary libraries.

- Run ETL Script: The ETL script (etl.py) is executed within the virtual environment. The environment variables required
for the job are securely passed to the script. These variables are stored in Jenkins and are injected at runtime to 
avoid exposing sensitive information in the codebase.

- Post Deployment Actions: After the script execution, any temporary files, such as the .env file, are removed to maintain 
security and cleanliness. The pipeline cleans up the workspace, removing any residual files and deactivating the virtual 
environment after the job is executed. Success and failure notifications are logged, providing a clear indication
of the job status. The logs are then collected at a later time for dashboard creation.


## Running Pipeline

- Clone the Repository
```
git clone https://github.com/jibbs1703/Economic-Indicator-Data-Pipeline.git
cd Economic-Indicator-Data-Pipeline
```

- Install Java and Jenkins on Server/Computer.

- Setup Jenkins Pipeline on Jenkins UI.

- Create a new Jenkins Pipeline job.

- Configure the job to use the Jenkinsfile from this repository.

- Ensure that your environment variables (e.g., credentials, API keys) are securely stored in Jenkins and referenced correctly in the Jenkinsfile.

- Set up a trigger (e.g., on code changes to specified branch) to run the ETL job automatically.

- Monitor the job via the Jenkins console output to ensure it completes successfully.

