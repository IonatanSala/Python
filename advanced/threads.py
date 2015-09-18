# Multithreading

# Threads can be thought of a separate programs running along side each other
# However they run within one process, meaning they can share data between one another easier than actual separate programs

# The challenge of Threads is that they can be hard to manage. Esprecially when a piece of data
# is being used by more than one thread
# Thread can be used just for quick task like calculating a result from an algorithm or for 
# running slow processes in the background while the program continues

# We can also create many threads to try and find an answer faster.
# Perhaps we need to hash 100 passwords with md5. We could have 5 - 10 threads each hashing
# a password making the toal time 5 - 10 times faster

# How does it work
# We already use one thread in our programs
# The Main thread
# When we create a new thread it runs along side our main thread
# On Window it's easy to open your task manager and see how many threads programs are using

# timer Program
# A basic timer program essentially hello world for threading
# Each timer therad will output the current time
# Then wait a certain time before outputting again.

# Asynchronous Tasks
# Some tasks can take a long time. Input and output for example can talke a long time
# Some programs are required to be real time.
# So we can setup Threads to run in the background to write a file or search for items
# while the user can still interact with the interface or commandline.

# Custom Threads
# We can make our own thread subclasses
# These are useful for making task specific threads that we can simply reuse as well as add features
# to ther thread
# Can make managing harder or more simple depending on how advanced we make our threading

# AsyncWrite Program
# A basic threading program that writes a file in th background
# a custom thread class will be created to take a string and save it ot aa file in the background
# WE will make it sleep for a second so we can see it working

# Locks
# We use lock to lock access to one thread
# Because threads run simultaneously there is no guarantee that both threads wont try to use a variable at the same time

# Semaphores
# Sempahores like locks restrict access to a thread
# However semaphores can allow more than one lock to be acquired
# You may hae 10 threads running, but you only want 2 or 3 to have access to a piece of data at a time

# When to use Threading
# Threading isn't the answer to every problem
# If your program logic has to run in a sequence, then threads wont help you out.

# If you are writing a GUI, then you want at least two threads. One for the GUI and one to do all the work
# in the background.
# To avoid the Gui being unresponive.

# If the program is running on a CPU with only one core. Then there iwll be no performance imporvement
# as the threads will be time split on the one core
# It's great for servers that deal with TCP connection to be multi-Threaded as you want
# to be able to handle more than 1 request at a time.



import threading
import time


tLock = threading.Lock()

class AsyncWrite(threading.Thread):
	def __init__(self, text, out):
		threading.Thread.__init__(self)
		self.text = text
		self.out = out

	def run(self):
		f = open(self.out, 'a')
		f.write(self.text + "\n")
		f.close()
		time.sleep(2)
		print('Finished background file writing to: ' + self.out)


def timer(name, delay, repeat):
	print("Timer: " + name + " Started")
	tLock.acquire()	# this thread owns a lock now and now othre thread can aquire it yet
	print(name + " has acqured the lock")
	while repeat > 0:
		# tell the computer to wait a certain amount of time
		time.sleep(delay)
		print(name + ": " + str(time.ctime(time.time())))
		repeat -= 1
	print(name + " is releasing lock")
	tLock.release()	# release a lock
	print("Timer: " + name+ " completed")


def Main():

	# uncomment to see timer() in action
	#t1 = threading.Thread(target=timer, args=("Timer1", 1, 5));
	#t2 = threading.Thread(target=timer, args=("Timer2", 2, 5));

	## start the threads
	#t1.start()
	#t2.start()

	#print('finished main')

	message = input("Enter a string to store: ")

	background = AsyncWrite(message, 'out.txt')
	background.start()
	print("The program can contiune while it wirtes in another thread")
	print("100 + 400 = ", 100 + 400 )

	background.join()
	print("Waited until background complete");

if __name__ == '__main__':
	Main()
