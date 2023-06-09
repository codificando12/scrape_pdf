import os

""" This funtion will take a directory and read all the files if there are some pdfs,
if that the case, it will return a list with the file names"""
def read_dir(dir_path):
    
    read_files = os.listdir(dir_path)
    final_files = []
    
    for file_name in read_files:
        if file_name.endswith(".pdf") or file_name.endswith(".PDF"):
            final_files.append(file_name)
        else:
            continue

    print(final_files)
    print(len(final_files))
    return final_files


if __name__ == '__main__':
    read_dir('C:/Users/eciap/Documents/GitHub/scrape_pdf/CAMBRIDGE2')