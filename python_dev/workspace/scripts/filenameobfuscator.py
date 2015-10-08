import os

if __name__ == '__main__':
	print "Files are now being renamed ..."

	for myfile in os.listdir('.'):
		if myfile.startswith ('Chapter') and myfile.endswith('.cs'):
			fn = myfile.split('_')
			fn.append('')
			fn[0] = 'ch0' + fn[0][7:]+'-'
			fn[1] = fn[1][1:]
			nn = fn[0]+fn[1]
			print "New name %s" %nn
			os.rename(myfile, nn)

	print "\nI am done renaming files.\n\n\t===> Jesus Loves you ;) <==="
