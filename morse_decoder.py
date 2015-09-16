missed = 0
message = {}
import time
import Adafruit_BBIO.GPIO as GPIO
GPIO.setup("P8_11", GPIO.IN)
print "this be goin"
base = time.time()
x = 1
breaker = False	
while True:
	if base + .3 <= time.time() and breaker == True:
		print ""
		breaker = False
	if GPIO.input("P8_11"): 	
		while True:
			if GPIO.input("P8_11"):
					base = time.time()
					while True:
						if not GPIO.input("P8_11"):
							jj = time.time() - base
							if jj >= .29:
								message.update({x:"dash"})
								x += 1
								base = time.time()
								break
							elif jj >= .09:
								message.update({x:"dot"})
								x += 1
								base = time.time()
								break


							else:	
								missed += 1
								print "missed %r dots or dashes" % missed
								print jj
								break		
			else:
				if base + .2 <= time.time():
					if message == {1: "dot", 2: "dash"}:
						print "A"
						message = {}
						x = 1
						base = time.time()
						breaker = True
						break
					elif message == {1: "dash", 2: "dot", 3: "dot", 4: "dot"}:
						print "B"
						message = {}
						x = 1
						base = time.time()
						breaker = True
						break	
					elif message == {1: "dash", 2: "dot", 3: "dash", 4: "dot"}:
						print "C"
						message = {}
						x = 1
						base = time.time()
						breaker = True
						break
					elif message == {1: "dash", 2: "dot", 3: "dot"}:
						print "D"
						message = {}
						x = 1
						base = time.time()
						breaker = True
						break
					elif message == {1: "dot"}:
						print "E"
						message = {}
						x = 1
						base = time.time()
						breaker = True
						break
					elif message == {1: "dot", 2: "dot", 3: "dash", 4: "dot"}:
						print "F"
						message = {}
						x = 1
						base = time.time()
						breaker = True
						break
					elif message == {1: "dash", 2: "dash", 3: "dot"}:
						print "G"
						message = {}
						x = 1
						base = time.time()
						breaker = True
						break
					elif message == {1: "dot", 2: "dot", 3: "dot", 4: "dot"}:
						print "H"
						message = {}
						x = 1
						base = time.time()
						breaker = True
						break
					elif message == {1: "dot", 2: "dot"}:
						print "I"
						message = {}
						x = 1
						base = time.time()
						breaker = True
						break
					elif message == {1: "dot", 2: "dash", 3: "dash", 4: "dash"}:
						print "J"
						message = {}
						x = 1
						base = time.time()
						breaker = True
						break
					
					elif message == {1: "dash", 2: "dot", 3: "dash"}:
							print "K"
							message = {}
							x = 1
							base = time.time()
					
					elif message == {1: "dot", 2: "dash", 3: "dot", 4: "dot"}:
							print "L"
							message = {}
							x = 1
							base = time.time()
					elif message == {1: "dash", 2: "dash"}:
							print "M"
							message = {}
							x = 1
							base = time.time()

					elif message == {1: "dash", 2: "dot"}:
							print "N"
							message = {}
							x = 1
							base = time.time()

					elif message == {1: "dash", 2: "dash", 3: "dash"}:
							print "O"
							message = {}
							x = 1
							base = time.time()


					else:
						base = time.time()
						x = 1
						message = {}
						breaker = True
						break
				

