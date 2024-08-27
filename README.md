# credsdefault-dataset
The dataset contains information on services, vendors, systems, OT and IoT devices, routers, and more.

## Overview of the Data Collection Process	
1. Direction and Planning	
2. Collection and Compilation	
3. Processing	
4. Analysis and Review	
5. Dissemination and Sharing	
6. Feedback and Continuous Improvement	

### Data Collection from Multiple Sources	
Collects data from various sources (PDFs, GitHub, CSVs, ZIPs, websites), saves it in JSON format to prevent data loss.

### Data Processing	
Each collected data set is processed by a corresponding processor to extract credentials.

### Post-Processing	
Refines the extracted credentials by sorting and removing duplicates.

### Saving the results	
The processed data is saved into a final JSON file (`output.json`).

### Hosting the results	
The final JSON file is hosted as a `Release`.


## Web Version
Check out the web search at [credsdefault-search](https://github.com/krystianbajno/credsdefault-search)

## CLI Version
Check out the CLI search at [credsdefault-cli](https://github.com/krystianbajno/credsdefault-cli)
