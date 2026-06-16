data=int(input("Enter the time in seceonds:"))

hours=data//3600
mineuts=(data%3600)//60
seceonds=data%60

standardtime=f"{hours:02d}:{mineuts:02d}:{seceonds:02d}"
print(f"format time: {standardtime}")
