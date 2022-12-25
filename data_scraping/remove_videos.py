import os

input_file = open(".\\Web_Scrape_Precut\\no-content.txt", "r")
first_char = input_file.read(1)

remove_list = []

if not first_char:
    print("Failed to read file")
else:
    input_file.seek(0)
    remove_list = input_file.read().split('\n')

    for vid in remove_list:
        filepath = ".\\Web_Scrape_Precut\\WS-NL-NC-" + str(vid) + ".mp4"
        if (os.path.exists(filepath)):
            os.remove(filepath)
        else:
            print("Did not find " + str(vid))