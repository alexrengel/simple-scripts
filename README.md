# Simple Scripts

> Simple scripts for pentesting and CTFs, mainly written in `bash` and `python`, that streamline Kali workflow by automating tedious manual tasks.

## Script description and usage:

### up (bash)
The script `up` creates a python Web server running in the current directory. By default it runs on port `80` using interface `eth0`. The port and inerface can be changed by using the flags `-p` and `-i` respectively, and passing the desired value ie `up -p 8080 -i tun0`. The script first tries to create the Web server using `python3`, then `python2` and finally `python`. If the computer has `Xclip` installed then it will copy the Web server address to the clipboard.

### usergen.py (python3)
The script `usergen.py` is used as `usergen.py -i file_with_first_and_last_names.lst -o file_to_be_created.lst` or by appending the `python` command at the begining. The script generates a list of possible usernames from first and last names given by line on an input file.

### get (bash)
The script `get` contains hardcoded keys and values (script names and their URLs) that can be quickly downloaded using `wget`. Usage: `get [script_name]`

## More:

Note to myself and others: 

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