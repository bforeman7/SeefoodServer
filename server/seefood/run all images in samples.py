#!/usr/bin/python
import pexpect
## this should be the list of image locations which we want to process for food
images = ['cookies.png', 'giada.png', 'high_school_lunch.jpg', 'high_school_lunch_room.jpg', 'laska.png', 'loaded_fries.png', 'lobster.jpg', 'poodle.png']
count = 0
process = pexpect.spawn('python find_food.py', timeout = None)
result = ''
process.sendline("ready")
while True: 
	if 'Enter file path to food: ' in result:
		## print out our result once we know we have something
		print result
		result = ''
		## Here we should pop our images off the image queue
		if(count < 8):	
			print "count: "
			print count
			process.send("samples/" + images[count] + "\n")
			process.sendline("ready")
			count = count+1
		else:
			## we should really sleep here and wait for something to be added to the queue
			process.send("exit\n")
			##process.kill(3)
			##break;
	if 'closing script' in result:
		print result
		break;
	else:
		## get each piece of output from the child process
		result += process.read(1)



