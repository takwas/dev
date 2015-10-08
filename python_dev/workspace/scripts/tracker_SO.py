#!/usr/bin/python


# mapping paths
paths = {	\
	"a" : [ "b", "c", "d" ],		\
	"b" : [ "a", "e", "f" ],		\
	"c" : [ "a", "e", "f" ],		\
	"d" : [ "a", "g", "h" ],		\
	"e" : [ "b", "c", "f", "i" ],	\
	"f" : [ "b", "c", "e", "i" ],	\
	"g" : [ "d", "i", "j" ],		\
	"h" : [ "d", "j" ],				\
	"i" : [ "e", "f", "g", "j" ],	\
	"j" : [ "g", "h", "i" ]			\
}


def find_path(_from, to, visited_paths, travelled_path):
	travelled_path.append(_from)			# "travelled_path" tracks the path currenly been traversed
	print "\t===> G.F: [%s]\t{" %_from,		 	# "G.F" --> Going from

	routes = get_destinations(_from)		# retrieve available destinations from current source
	print "\b%r} <===" %(routes)


	# in case destination is found along the way
	# if to in routes:
	# 	travelled_path.append(to)					# Add destination to travelled path
	
	# 	if len(travelled_path) <= 1:
	# 		print "Destination [%s] reached directly from [%s]" %(to, _from)
	# 	else:
	# 		print "Destination [%s] reached from [%s]" %(to, _from)
	# 	show_graph(travelled_path)
	# 	visited_paths.append(travelled_path[:])		# Add new travel path to list of previous travelled paths
	# 	travelled_path = []
	# 	return visited_paths


	for route in routes:
		if route == to:									# Destination found! End here.
			travelled_path.append(route)					# Add destination to travelled path
			print "Destination '%s' reached from '%s'" %(route, _from)
			show_graph(travelled_path)
			visited_paths.append(travelled_path[:])		# Add new travel path to list of previous travelled paths
			travelled_path.pop()
			travelled_path.pop()
			print "Going up^ a level"
			return

		elif route in travelled_path:		# route has been visited before in current travel path; so don't process it again
			print " Skip: [%s]" %route
			continue

		else:
			find_path(route, to, visited_paths, travelled_path)
			travelled_path.pop()
			print "Out of route:  [%s].\t Moving on..." %route
			continue

	return visited_paths



def get_destinations(_from):
	return paths.get(_from, [])


def show_graph(nodes):
	for node in nodes[:-1]:
		print node, " --> ",
	print nodes[-1]
	print


def show_all_paths():
	print "Showing all registered paths:"
	locations = paths.keys()
	locations.sort()
	for path in locations:
		print "\t%s:\t%r" %(path, paths[path])
	print


def show_all_visited_paths(visited_paths):
	print "Showing all visited paths:\n\t",
	for path in visited_paths:
		show_graph(path)
		print "\n\t",

def run(_from, to):
	show_all_paths()
	print "AIM:   [%s] to [%s]" %(_from, to)
	visited_paths = find_path(_from, to, [], [])
	visited_paths.sort(key= len)

	print
	print "DONE CHECKING ALL ROUTES!"
	show_all_visited_paths(visited_paths)
	return visited_paths


if __name__ == "__main__":

	import sys

	if len(sys.argv) >=3:
		_from = sys.argv[1]
		to = sys.argv[2]
	else:
		_from = "a"
		to = "f"

	run(_from, to)