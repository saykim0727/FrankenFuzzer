def ConfigParsor( Key ):
	with open(".config","r") as f :
#	with open("./.config","r") as f :
			datalist = f.readlines()
			value = ""
			for data in datalist :
				if Key in data : 
					sData = data.split("=")
					value = sData[1].rstrip().strip("\"")
					return value;
	return -1;

