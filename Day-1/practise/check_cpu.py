import psutil;

def check_cpu_threshold():
    cpu_threshold = int(input("Enter cpu threshold: "))
    
    current_cpu = psutil.cpu_percent(interval=1)
    print(f"current_cpu %: {current_cpu}")

    if  current_cpu >  cpu_threshold:
        print("Alert! email sent...")
    else: print("safe!")

check_cpu_threshold()