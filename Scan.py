#!/usr/bin/env python3

import sys
import time
import queue
import threading
from telnetlib import Telnet
from termcolor import colored

with open(sys.argv[1]) as hf:
	hosts = [line.rstrip() for line in hf]
	
JoeBiden = int(sys.argv[2])
T = Telnet()
q = queue.Queue()

print(colored("[> >]Joe Biden Fights D-Link \n By: ASN \n", 'cyan'))

class DoGangShi(threading.Thread):
	def __init__(self, q):
		threading.Thread.__init__(self)
		self.q = q
	
	def run(self):
		while True:
			ip = self.q.get()
			try:
				with Telnet(ip):
				
					T.open(ip)
					print(colored(f"[+] {ip} | Connected", 'green'))
					time.sleep(1)
					#T.read_until(b' ')
					s = T.read_all().decode('ascii')
					T.read_all().decode('ascii')
					
					conv = str(s)
					f = open(f'Prompts.txt',"a")
					f.write(f"{ip} | {s} \n")
					f.close()				
					
					print(s)
			
				if ("TenGigabit Ethernet Switch" in conv):
					Model= conv.split('Command')[0].strip()
					start = 'Firmware: '
					end = 'C'
					Firmware = conv.split(start)[1].split(end)[0].strip()
					print (f"Model: {Model} \n")
					print (f"Firmware: {Firmware} \n")
					f = open(f'exp.txt',"a")
					f.write(f"{ip}\n{Model}\n{Firmware}\n")
					f.close()
					T.close()
					self.q.task_done()
				
				else:
					print(colored(f"[!] {ip} | Incorrect Device", 'yellow'))
					T.close()
					self.q.task_done()
					pass
				
			except EOFError:
				print(colored(f"[!] {ip} | EOF Error", 'red'))
				T.close()
				self.q.task_done()
				pass
				
			except TimeoutError:
				print(colored(f"[!] {ip} | Connection Timed Out", 'red'))
				T.close()
				self.q.task_done()
				pass
				
			except ConnectionResetError:
				print(colored(f"[!] {ip} | Connection Reset", 'red'))
				T.close()
				self.q.task_done()
				pass
				
			except ConnectionRefusedError:
				print(colored(f"[!] {ip} | Can't Connect", 'red'))
				T.close()
				self.q.task_done()
				pass
				
			except ConnectionError:
				print(colored(f"[!] {ip} | Connection Error", 'red'))
				T.close()
				self.q.task_done()
				pass
			except ConnectionAbortedError:
				print(colored(f"[!] {ip} | Connection Aborted", 'red'))
				T.close()
				self.q.task_done()
				pass
			except TypeError:
				print(colored(f"[!] {ip} | Attribute Error", 'red'))
				T.close()
				self.q.task_done()
				pass
			except ValueError:
				print(colored(f"[!] {ip} | Value Error", 'red'))
				T.close()
				self.q.task_done()
				pass
				
			except AttributeError:
				print(colored(f"[!] {ip} | Attribute Error", 'red'))
				T.close()
				self.q.task_done()
				pass				
		
start = time.time()

def main ():
	for i in range(JoeBiden):
		t = DoGangShi(q)
		t.setDaemon(True)
		t.start()
		
	for ip in hosts:
		q.put(ip)
	
	q.join()
	
main()
print("Elapsed Time: %s" % (time.time() - start))
