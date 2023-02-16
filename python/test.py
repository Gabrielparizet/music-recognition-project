# We import sys which allows us to have access to the arguments passed in. 
import sys

data_to_pass_back = "Send this to node process."

input = sys.argv[1]
output = data_to_pass_back
print(output)


sys.stdout.flush()