import os

# define the input and output file paths
input_file_path = '/Users/pooja/Downloads/archive/mnist_train.csv'
shard1_file_path = 'dataset_shard1.csv'
shard2_file_path = 'dataset_shard2.csv'
shard3_file_path = 'dataset_shard3.csv'

# determine the size of the input file in bytes
file_size = os.path.getsize(input_file_path)

# calculate the size of each shard (round up to the nearest integer)
shard_size = -(-file_size // 3)  # equivalent to math.ceil(file_size / 3)

# open the input and output files
with open(input_file_path, 'r') as input_file, \
     open(shard1_file_path, 'w') as shard1_file, \
     open(shard2_file_path, 'w') as shard2_file, \
     open(shard3_file_path, 'w') as shard3_file:
    
    # initialize the current shard size to 0
    current_shard_size = 0
    
    # read each line from the input file and write it to the appropriate shard file
    for line in input_file:
        # determine which shard file to write to based on the current shard size
        if current_shard_size < shard_size:
            output_file = shard1_file
        elif current_shard_size < 2 * shard_size:
            output_file = shard2_file
        else:
            output_file = shard3_file
        
        # write the current line to the output file
        output_file.write(line)
        
        # increment the current shard size by the size of the current line
        current_shard_size += len(line)
