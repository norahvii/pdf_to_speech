import glob

lines_per_file = 8900
smallfile = None

file_pattern = '*.txt'
file_name_list = []

if '*' in file_pattern:
    file_name_list.extend(glob.glob(file_pattern))

for target in file_name_list:
	with open(target) as bigfile:
	    for lineno, line in enumerate(bigfile):
	        if lineno % lines_per_file == 0:
	            if smallfile:
	                smallfile.close()
	            small_filename = target.replace('.txt',' ') + str((lineno + lines_per_file)) + '.txt'
	            smallfile = open(small_filename, "w")
	        smallfile.write(line)
	    if smallfile:
	        smallfile.close()
