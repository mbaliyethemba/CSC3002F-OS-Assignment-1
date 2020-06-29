#SHNMBA004
#Mbaliyethemba Shangase
#OS Assignment 1
#2 June 2020

from random import randint
import sys

#FIFO
def FIFO(size,pages):
  frames=[]
  page_fault=0
  for i in range(size):
    frames.append(-1)
  marker=0
  i=0
  while(marker!=size and i<len(pages)):
    if (pages[i] not in frames):
      frames[marker]= pages[i]
      marker+=1
      page_fault+=1
    i+=1
  marker=0
  for i in range(i,len(pages)):
    if(pages[i] not in frames):
      page_fault+=1
      frames[marker]=pages[i]
      marker=(marker+1)%size
  frames=[]
  return page_fault

#LRU
def LRU(size,pages):
  frames,s,page_fault= [],[],0
  for i in pages:
	  if i not in frames:
		  if len(frames) < size:
			  frames.append(i)
			  s.append(len(frames)-1)
		  else:
			  ind = s.pop(0)
			  frames[ind] = i
			  s.append(ind)
		  page_fault += 1
	  else:
		  s.append(s.pop(s.index(frames.index(i)))) 
  return page_fault
  
#OPT
def OPT(size,pages):
  frames,page_fault= [],0
  occurance = [None for i in range(size)]
  for i in range(len(pages)):
	  if pages[i] not in frames:
		  if len(frames) < size:
			  frames.append(pages[i])
		  else:
			  for x in range(len(frames)):
				  if frames[x] not in pages[i+1:]:
					  frames[x] = pages[i]
					  break
				  else:
					  occurance[x] = pages[i+1:].index(frames[x])
			  else:
				  frames[occurance.index(max(occurance))] = pages[i]
		  page_fault += 1
  return page_fault
    
def main():
	pages=[]
	size = int(sys.argv[1])
	for i in range(32): 
		#reference string random generation
		pages.append(randint(0,9))
	print ("FIFO", FIFO(size,pages), "page faults.")
	print ("LRU", LRU(size,pages), "page faults.")
	print ("OPT", OPT(size,pages), "page faults.")
if __name__ == "__main__":
	if len(sys.argv) != 2:
		print ("Usage: python paging.py [number of pages]")
	else:
		main()
