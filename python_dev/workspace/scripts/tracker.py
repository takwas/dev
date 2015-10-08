#!/usr/bin/python


# This code finds all the paths leading from a given
# point, [the SOURCE] to another point [the DESTINATION]
# 
# The data is mapped in such a way that every point maps
# to every point that can "directly" be reached from it.
# 
# Then there is a recursive traversal over each point
# until the destination is reached and all the paths have
# been tracked.


# mapping paths to directly reacheable paths
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



# recursive function that does the magic
# params:
# 		_from:				point to start from
# 		to:					point we are trying to get to
# 		vistited_paths:		a listing of all the prreviously completed traversed paths
# 		travelled_path:		a listing of the points along the current traversal
# 		
def find_path(_from, to, visited_paths, travelled_path):
	travelled_path.append(_from)				# "travelled_path" tracks the path currenly been traversed
	
	#### DEBUG OUTPUT	
	print "\t===> G.F: [%s]\t{" %_from,		 	# "G.F" --> Going from

	routes = get_destinations(_from)			# retrieve available destinations (directly reachable points) from current source
	
	#### DEBUG OUTPUT	
	print "\b%r} <===" %(routes)


	# in case destination is among directly reacheable points
	if to in routes:
		travelled_path.append(to)					# Add destination to travelled path
		
		#### DEBUG OUTPUT
		if len(travelled_path) <= 1:
			print "Destination [%s] reached directly from [%s]" %(to, _from)
		else:
			print "Destination [%s] reached from [%s]" %(to, _from)

		show_graph(travelled_path)					#### DEBUG OUTPUT; show a map of travelled path
		visited_paths.append(travelled_path[:])		# Add new travel path to list of previous travelled paths
		travelled_path = []							# empty travel path list for a new journey
		return visited_paths



	# iterate over retrieved list of directly
	# reachable points from current point
	for route in routes:
		if route == to:										# Destination found! End here.
			travelled_path.append(route)					# Add destination to travelled path
			print "Destination '%s' reached from '%s'" %(route, _from)			#### DEBUG OUTPUT
			show_graph(travelled_path)
			visited_paths.append(travelled_path[:])			# Add new travel path to list of previous travelled paths
			travelled_path.pop()							# while recursing, we need to pop(), and move back up the tree to continue traversing
			travelled_path.pop()
			print "Going up^ a level"						#### DEBUG OUTPUT
			return

		elif route in travelled_path:		# route has been visited before in current travel path; so don't process it again
			print " Skip: [%s]" %route 		#### DEBUG OUTPUT
			continue

		else:
			# Recurse.
			# Pick current point and make it act like the
			# current source. We are still headed to the same
			# original destination								
			find_path(route, to, visited_paths, travelled_path)
			travelled_path.pop()
			print "Out of route:  [%s].\t Moving on..." %route 			#### DEBUG OUTPUT
			continue

	return visited_paths




#### UTILITY Functions ####


# retrieve list of directly reachable points from source "_from"
def get_destinations(_from):
	return paths.get(_from, [])


# shows a map of points leading to points in a traversal
def show_graph(nodes):
	for node in nodes[:-1]:
		print node, " --> ",
	print nodes[-1]
	print


# show all paths in our local database
def show_all_paths():
	print "Showing all registered paths:"
	locations = paths.keys()
	locations.sort()
	for path in locations:
		print "\t%s:\t%r" %(path, paths[path])
	print


# "visited_paths" holds a listing of traversals
# 
# Show a map for each traversal
def show_all_visited_paths(visited_paths):
	print "Showing all visited paths:\n\t",
	for path in visited_paths:
		show_graph(path)
		print "\n\t",



# run the program
def run(_from, to):
	show_all_paths()
	print "AIM:   [%s] to [%s]" %(_from, to)				#### DEBUG OUTPUT
	visited_paths = find_path(_from, to, [], [])
	
	# some extra processeing and DEBUG
	visited_paths.sort(key= len)
	print
	print "DONE CHECKING ALL ROUTES!"
	show_all_visited_paths(visited_paths)
	return visited_paths


# Python main
if __name__ == "__main__":

	import sys

	if len(sys.argv) >=3:
		_from = sys.argv[1]
		to = sys.argv[2]
	else:
		_from = "a"
		to = "f"

	run(_from, to)