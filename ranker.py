import sys
import json
import time

from operator import itemgetter

start = round(time.time() * 1000)

# Validate and store CLI areguments, create an error if the wrong number of arguments exits
if len(sys.argv) != 3:
    print("The command to run is: ranker.py <input_file> <entry_count>", file=sys.stderr)
    sys.exit(1)

# Ensure that the user supplied an integer as the second CLI argument
try:
    entries_arg = int(sys.argv[2])
except:
    print("Your second argument was not an integer. Please change and try again.", file=sys.stderr)
    sys.exit(1)

# Read each entry in the input data, create an error if the file is not valid
file_arg = sys.argv[1]
try:
    with open(file_arg, 'r') as file:
        lines = file.readlines()
except:
    print("Ensure that you have supplied a valid file and try again.", file=sys.stderr)
    sys.exit(1)

# Parse each line for ID and score, ignoring the data payload. No error handling for the contents of the file. Assuming file is structured as expected.
entries = []
for line in lines:
    score = int(line.split(':', 1)[0])
    jsonData = json.loads(line.split(':', 1)[1])
    entries.append({"score": score, "id": jsonData['id']})

# Close the file
file.close()   

# Order the list from highest score to lowest score, create JSON entries for just what is being requested
entries = sorted(entries, key=itemgetter('score'), reverse=True)
jsonOutput = json.dumps(entries[slice(entries_arg)], indent=4)

end = round(time.time() * 1000)
print(end - start)

# Print the output to stdout
print(jsonOutput)
