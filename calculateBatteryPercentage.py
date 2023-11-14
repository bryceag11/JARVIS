import subprocess # runs an external c++ program and captures/processes the output

def calculate_battery_percentage():
    try:
        output = subprocess.check_output(['./PATHTOC++EXE'], stderr=subprocess.STDOUT) # runs external c++ program and returns calculated battery percentage, also redirects standard error to standard output to capture any c++ error msgs
        battery_percent = output.decode('utf-8').strip() # output variable contains output of c++ program (bytes) and then uses utf-8 to decode the bytes
        return float(battery_percent) # Convert battery_percentage string to float if necessary
    except subprocess.CalledProcessError as e:
        print("Error: ", e)
        return None # Handle errors/exceptions