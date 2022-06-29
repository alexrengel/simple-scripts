# pentesting-tools
Simple bash scripts that streamline my Kali workflow.

To avoid having to type `.\` before running each bash script, export the directory path to the `$PATH` variable.
This document assumes that the scripts are in `/opt/simple-scripts`. If they're on a different directory, please change the examples below accordingly to the corresponding directory. Additionally, my bash is located at `/bin/bash`.


* Temporary solution:

```bash
sudo export PATH=$PATH:~/projects/simple-scripts:
``` 


* Permanent solution:

```bash
sudo nano ~/.bashrc
#Add the following line with the correct script directory to a new line at the end of the file
export PATH=$PATH:~/projects/simple-scripts:
```

**Also, ensure to make these files executable by running `sudo chmod +x name_of_executable`** 

If instructions aren't clear, feel free to leave me a comment.


## up (bash)
The script `up` creates a python http server running on port 8080 in the current directory. It also pulls the current `tun0` IPv4 so that the user can efficiently copy and paste it into a reverse shell script.

## usergen.py (python3)
The script `usergen.py` is used as `usergen.py -i file_with_first_and_last_names.lst -o file_to_be_created.lst` or by appending the `python` command at the begining. The script generates a list of possible usernames from first and last names given by line on an input file.