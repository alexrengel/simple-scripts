# pentesting-tools
Simple bash scripts that streamline my Kali workflow.
To avoid having to type `.\` before running each bash script, export the directory path to the `$PATH` variable.
This document assumes that the files are at `/opt/simple-scripts`. If they're on a different directory, please change them accordingly.


* Temporary solution:

```bash
sudo export PATH=$PATH:/opt/simple-scripts
``` 


* Permanent solution:

```bash
Assuming that we're running bash (/bin/bash)
sudo nano ~/.bashrc
#Add the following line with the correct script directory to a new line at the end of the file
export PATH=$PATH:/opt/simple-scripts
```


## up (bash)
The script `up` creates a python http server running on port 80 in the current directory. It also pulls the current `tun0` IPv4 so that the user can efficiently copy and paste it into a reverse shell script.


