# Data-Engineering-Project
Here we are trying to create a ETL pipeline using Docker container, Apache airflow, AWS S3 and then analyzing it with AWS Glue studio, AWS Glue catalog, AWS Athena and Quicksight.

## Architecture of the Project:
![Data WorkFlow](https://github.com/PavansaiGundaram/Data-Engineering-Project/blob/main/Flowcharts%20(1).jpeg)

## 1. Create a Directory for Airflow
bash
Copy code
mkdir airflow-docker
•	What this does: This command creates a new directory called airflow-docker on your system. This folder will contain all the necessary files for setting up Airflow using Docker.

## 2. Navigate into the Directory
bash
Copy code
cd airflow-docker
•	What this does: This changes the current working directory to airflow-docker. All subsequent commands will be executed inside this folder.
Step 2: Open Visual Studio Code

## 3. Open the Directory in Visual Studio Code
bash
Copy code
code .
•	What this does: This opens the airflow-docker folder in Visual Studio Code (VS Code). The . refers to the current folder. Using VS Code here allows you to easily manage and edit the project files.
Step 3: Download the Docker Compose File
##4. Download the Docker Compose YAML File
bash
Copy code
curl 'https://airflow.apache.org/docs/apache-airflow/2.10.2/docker-compose.yaml' -o 'docker-compose.yaml'
•	What this does: This command uses curl, a tool to download files from the internet. It downloads the Airflow Docker Compose configuration file (docker-compose.yaml) from the official Apache Airflow documentation site.
•	Why it's important: The docker-compose.yaml file contains the configuration for Docker to set up all the necessary services for running Airflow (like the web server, scheduler, and database). This file tells Docker what images to pull and how to configure them.
Step 4: Create Necessary Directories
To store DAGs, logs, and plugins, you need to create specific folders.
## 5. Create the DAGs Directory
bash
Copy code
mkdir dags
•	What this does: This creates a dags folder where you will store your DAG Python scripts.
•	Why it's important: DAGs (Directed Acyclic Graphs) are the workflows you want Airflow to schedule and execute.
## 6. Create the Logs Directory
bash
Copy code
mkdir logs
•	What this does: This creates a logs folder where Airflow will store logs related to the execution of your tasks.
•	Why it's important: Logs are essential for debugging and monitoring the status of your tasks in Airflow.
## 7. Create the Plugins Directory
bash
Copy code
mkdir plugins
•	What this does: This creates a plugins folder where you can store custom plugins or operators for Airflow.
•	Why it's important: Plugins extend Airflow’s functionality, such as adding new operators or hooks.
Step 5: Initialize Airflow Using Docker Compose
## 8. Run Docker Compose to Initialize Airflow
-docker compose up airflow-init
•	What this does: This command initializes the Airflow environment. The airflow-init step sets up the database and any other initial configurations Airflow needs.
•	Why it's important: This initialization step is crucial because it prepares the database that Airflow uses to track DAG executions, tasks, and logs.
Step 6: Start Airflow Using Docker Compose
## 9. Start the Airflow Services
-docker compose up
•	What this does: This command starts up all the services defined in the docker-compose.yaml file. These services typically include:
o	Airflow Webserver: The UI that allows you to interact with your DAGs.
o	Airflow Scheduler: The component responsible for scheduling the DAGs and triggering tasks.
o	PostgreSQL Database: Used by Airflow to store metadata about DAG runs and tasks.
o	Redis: Acts as a broker for task queues.
•	Why it's important: This step is necessary to actually run Airflow. Without starting these services, you can't execute or monitor your workflows.
Step 7: Check If the Docker Containers Are Running
## 10. List Running Docker Containers
-docker ps
•	What this does: This command lists all running Docker containers. It shows important information like container IDs, names, status, and health.
•	Why it's important: You can use this to check if the Airflow containers (like the web server, scheduler, and database) are up and running. Look for a "healthy" status to ensure everything is working correctly.
Step 8: Access the Airflow Web Interface
## 11. Open Airflow in a Browser
•	What to do: Open any web browser and go to http://localhost:8080.
o	Why it's important: This opens the Airflow web UI, where you can manage and monitor your DAGs, check logs, trigger DAG runs, and view task statuses. The web UI is the central interface for interacting with Airflow.
________________________________________
## Summary of What Happens:
1.	You create a directory for Airflow files and open the project in Visual Studio Code.
2.	You download the Docker Compose configuration for Airflow and create necessary directories for your DAGs, logs, and plugins.
3.	You initialize Airflow using Docker Compose to set up the database and services.
4.	After the initialization, you start Airflow, which runs the web server and scheduler inside Docker containers.
5.	You verify that the containers are running and healthy by using the docker ps command.
6.	Finally, you can access the Airflow UI by going to http://localhost:8080 in your web browser to start managing your DAGs.
This setup allows you to run Airflow completely within Docker containers, making it easier to manage and scale.


