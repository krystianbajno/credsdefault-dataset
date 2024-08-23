# defcred-intel

## Process overview
### Intelligence lifecycle
- 0. Planning
- 1. Collection
- 2. Processing
- 3. Analysis
- 4. Dissemination
- 5. Feedback

### The collectors are collecting data from many sources. 
`data/collection`
Sources include PDF files, GitHub repositories, CSV files, ZIP files, websites. The collector is gathering intel.
The data is being serialized and saved in .json form in case the collection stops.

### The data is going to be processed later by processors.
`data/processing`
Each collector has it's own processor. Processors process Intel collected by the collectors and save the extracted Credentials in order to provide actionable data.

### After processing, postprocessing occurs.
The postprocessors load processed credentials, sort them, and remove duplicates.

### Result is saved in output.json.
`data/output`
The result is saved in an output JSON (`output.json`) file.

### The result is being hosted in releases
The result file is saved as a `Release` in repository to be used by other tools.

# Usage
```python3
pip3 install -r requirements.txt
python3 main.py
```