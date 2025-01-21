#Convert bytes into KB, MB and GB
byte = float(input("Enter number of bytes:"))
kb = byte / 1024
mb = kb / 1024
gb = mb / 1024
print("The conversion of byte into kb is:",kb)
print("The conversion of byte into mb is:",mb)
print("The conversion of byte into gb is:",gb)