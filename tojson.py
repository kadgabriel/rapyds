import io, json

def convert_json(genome_name):
	whole_json = {}
	with open("output/csv_"+genome_name+".csv") as f:
		for content in f:
			line = content.split("\t")
			whole_json[line[0]] = [int(x) for x in line[1].split(",")]

	with open("output/"+genome_name+'.json', 'w') as fp:
		json.dump(whole_json, fp)

if __name__ == '__main__':
	pass