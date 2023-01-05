import os

def correctNum(i):
    i = str(i)
    while len(i) < 4:
        i = '0' + i
    return i

files = os.listdir('Web_Scrape_Labeled')
# print(files)

for i in range(len(files)):
    new_name = '.\\Web_Scrape_Labeled\\' + files[i][0:20] + correctNum(i) + '.mp4'
    print(new_name)
    os.rename('.\\Web_Scrape_Labeled\\' + files[i], new_name)

print("\n\nCOMPLETED\n")
