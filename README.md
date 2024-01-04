[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/_WcIwctJ)


# Reddit & 4Chan Data Collection on Sports

We are collecting data from various platforms and performing analyses. Currently this project is Implemented to collect data

<details>
<summary><b>🚀 Data Sources & Analysis</b></summary>

- **Reddit API:** Data is collected from Reddit's API.
  
- **4Chan API:** Data from 4Chan's API is also gathered.
  
- **PostgreSQL Database:** The collected data is stored in a PostgreSQL database.
  
- **Analysis:** We conduct both sentimental and competitive analyses on the stored data.
  
- **Backend Daemon:** A backend daemon is employed to fetch data from the APIs.

- **Scheduler:** We utilize Faktory as our scheduler.

</details>

<details>
<summary><b>🛠️ Commands & Execution</b></summary>

- **Directory Navigation:**  
  Navigate to the directory containing `manage.py`:  
  `cd path/to/manage.py`

- **Reddit Data Collection:**  
  `python manage.py reddit_data_collection`

- **4Chan Data Collection:**  
  `python manage.py 4chan_data_collection`

- **Job Scheduling:**  
  Initialize and run the job queue (Currently reddit and 4chan Job are added):  
  `python init_enqueue.py`
  `python worker.py`


- **Faktory Web Interface:**  
Observe the Faktory dashboard at (tunneling needed) [http://localhost:7420/](http://localhost:7420/)



