import time
time = int(time.strftime('%H'))
if(time>=0 and time<12):
    print("GOOD MORNING SIR!!!")
elif(time>=12 and time<4):
    print("GOOD AFTERNOON SIR!!!")
else:
    print("GOOD NIGHT SIR!!!")