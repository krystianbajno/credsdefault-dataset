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
Data is gathered from a variety of sources, including PDF files, GitHub repositories, CSV files, ZIP files, and websites. The data collector retrieves this information from the internet, serializes it, and saves it in .json format to ensure preservation in case the collection process is interrupted.	

### Data Processing	
Each data collector has an associated processor. These processors analyze the information gathered by the collectors and extract relevant credentials.	

### Post-Processing	
After the initial processing, post-processors further refine the data by loading the extracted credentials, sorting them, and removing any duplicates.	

### Saving the results	
The final processed data is saved in a JSON file (`output.json`).	

### Hosting the results	
The resulting file is made available as a `Release`.
