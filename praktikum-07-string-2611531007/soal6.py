# Name: Muhammad Rasya Fahrozi
# NIM: 2611531007
# Question 6


full_name = "Muhammad Rasya Fahrozi"
nim = "2611531007"

name = full_name.strip()
cek = name.find(" ")

if cek == -1:
    firstname = name
else:
    firstname = name[:cek]
     
username = full_name.strip()[:8].lower() + nim[-3:]

print(username)