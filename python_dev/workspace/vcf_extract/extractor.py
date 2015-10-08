#!/usr/bin/python

mainfile = "contacts.vcf"
stuff = []
all_tags = []


def get_all_tags(filename, delimiter=":"):
	with open(filename) as f:
		file_content = f.readlines()
	
	tags = []

	for line in file_content:
		line.strip()
		tag = line.split(delimiter)[0]
		tags.append(tag)

	tags = list(set(tags))
	return tags


def take_out_tag(tag, file_name, newfilename):
	with open(filename) as f:
		file_content = f.readlines()

	newcontent=[]
	
	line_continues = False
	for line in file_content:
		if line_continues:
			continue
		
		split_line = line.split(":")
		if line_continues and len(split_line) > 1:
			line_continues = False
		
		tags = split_line[0]
		tags = tags.strip()

		if tags.find(tag) > -1:
			line_continues = True
			continue

		newcontent.append(line)

	save_content(newfilename, newcontent)
	



def save_content(filename, content):
	with open(filename, "w") as f:
		f.write(content)		
		


		
def process_user(user):
	tags = all_tags[0:]
	processed_user = {}
	
	def get_tag_and_value(line):
		delim_pos = line.index(":")
		tag = line[:delim_pos]
		value = line[delim_pos+1:]
		
		return tag, value


	temp_user={}
	for line in user:
		tag, value = get_tag_and_value(line)
		temp_user[tag] = value

	for tag in tags:
		if temp_user.get(tag, None) is None:
			processed_user[tag] = "\t"
		else:
			processed_user[tag] = temp_user[tag]+"\t"

	
	return processed_user

		

def read_file(filename):

	with open(filename) as f:
		file_content = f.readlines()

	return file_content


def run():
	
	id = 0
	
	all_users = {}

	for line in stuff:
		line = line.strip()	
		
		if line.startswith("BEGIN"):
			user=[]						#create new user
			newuser=True
		elif line.startswith("END"):
			all_users[id] = process_user(user)		# save last processed user's details
			id += 1									# prepare for next user
		else:
			user.append(line)


	str_to_file = ""
	
	for tag in sorted(all_tags):
		str_to_file += tag +"\t"

	str_to_file+="\n"
	
	for user_id in all_users.keys():
		for user_details in sorted(all_users.get(user_id)):
			#print "%r\t" % all_users[user_id][user_details], #DEBUG		
			str_to_file += all_users[user_id][user_details]
		str_to_file+="\n"
	
	save_content("temp.csv", str_to_file)







if __name__ == '__main__':
	print "Extracting your contacts ... "

	# change mainfile to read from
	mainfile = "no_photo.vcf"
	
	stuff = read_file(mainfile)
	all_tags = get_all_tags(mainfile)
	
	run()