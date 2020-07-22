# GRAPHITE SERVER STATUS
This script will retrieve server data from the graphite link given and return corresponding status code

## Usage

  usage: main.py [-h] [-u URL] [-p METRIC] [-c CRITICAL_THRESHOLD]
               [-w WARNING_THRESHOLD]

  Server Status

  optional arguments:
    -h, --help            show this help message and exit
    
    -u URL, --url URL     enter url
    -p METRIC, --metric METRIC
                          enter metric
    -c CRITICAL_THRESHOLD, --critical_threshold CRITICAL_THRESHOLD
                          enter critical threshold
    -w WARNING_THRESHOLD, --warning_threshold WARNING_THRESHOLD
                          enter warning threshold
                        
## Results

  1 : OK
  
  2: Warning
  
  3: Critical Warining
  
  4: UNKNOWN
