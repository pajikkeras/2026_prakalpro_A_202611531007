# Name: Muhammad Rasya Fahrozi
# NIM: 2611531007
# Question 7

print("=" * 30)
print (f"{'STUDENT CARD':^30}")
print("=" * 30)

full_name = "Muhammad Rasya Fahrozi"
nim = "2611531007"

name = full_name.strip()
cek = name.find(" ")

if cek == -1:
    firstname = name
else:
    firstname = name[:cek]
     
username = full_name.strip()[:8].lower() + nim[-3:]

print("Name".ljust(10) + ":" ,name)
print("NIM".ljust(10) + ":" ,nim)
print("Username".ljust(10) + ":" ,username)
print("Intake".ljust(10) + ":","20" + nim[:2])

print("=" * 30)