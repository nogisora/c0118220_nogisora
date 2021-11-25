import glob
import hashlib
import csv
import time

def hash():

  files = glob.glob("./**", recursive=True)

  list1 = list(filter(lambda s: s.endswith(".py"), files))

  a = list()
  for i in list1:
      with open(i, 'rb') as file:
          fileData = file.read()
          hash_md5 = hashlib.md5(fileData).hexdigest()
          a.append(hash_md5)

  with open("List3.csv", 'w', newline="") as file:
      spawriter = csv.writer(file)
      spawriter.writerows(zip(list1 , a))

hash()

while(True):
  time.sleep(300)
