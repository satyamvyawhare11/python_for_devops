#1st way to make a list
a = [100,101,"sonic"]
a.append("hello")
print(a)

#2nd way to make list
clouds = list()
clouds.append("aws")
clouds.append("asure")
clouds.append("gcp")
clouds.append("utho")
print(clouds)

print("The lenght of clouds is:", len(clouds))
print("The leader of cloud service provider is:", clouds[0])
print("indian cloud service provider is:",clouds[-1])

print(dir(clouds))
print(clouds.extend.__doc__)

for cloud in clouds:
    if cloud == "aws":
        print(f"{cloud}: Market leader")
    elif cloud in ["asure","gcp"]:
        print(f"{cloud}: include in top 3")
    elif cloud == "utho":
        print(f"{cloud}: indian cloud")
    else:
        print("welcome!")