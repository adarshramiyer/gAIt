import os

files = os.listdir('Web_Scrape_Cut')

for file in files:
    new_name = str(file)[20:]
    os.rename('.\\Web_Scrape_Cut\\' + str(file), '.\\Web_Scrape_Cut\\' + new_name)