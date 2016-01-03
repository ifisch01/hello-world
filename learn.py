# learning from python
def get_name():
	print 'What is your name?'
	name = raw_input('> ')
	return name

homie = get_name()
print "Hello %s" % homie
