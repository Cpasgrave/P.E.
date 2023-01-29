import os

local_path = os.path.dirname(os.path.abspath(__file__))

for filename in os.listdir(local_path):
	if filename[:2] == "PE":
		new = filename[:3]+"00"+filename[3:5]+".py"
		os.rename(filename,new)


