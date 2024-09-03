import random 
a=8

def pwgen():
  pw=""
  while len(pw)<a:
    rm=random.randint(65,122)
    if rm>=91 and rm<=96:
        continue
    pw+=chr(rm) 
  print("HERE THIS IS YOUR PASSWORD:",pw)
  
print ("THIS IS A PROGRAM TO GENERATE A RANDOM 8 CHARACTER PASSWORD")

def main():
	while True:
		pwgen()
		ui=input ("WOULD YOU LIKE TO GENERATE ANOTHER PASSWORD? (yes/no):\n")
		if ui.lower()=="yes":
				pass
		elif ui.lower()=="no":
				print("THANK YOU FOR USING THE PASSWORD GENERATOR. GOODBYE!")
				break
		else:
				print("SORRY I CAN'T UNDERSTAND")
				break			
				
main()		
		
	


        
    


