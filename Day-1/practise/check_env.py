env = input("Enter env: ")

if env == "prod" :
    print("Don't deploy on friday")
elif env == "stg": 
    print("take backup & test well")
elif env == "test" : 
    print("test it well")
else:
    print("safe to deploy any day")
    