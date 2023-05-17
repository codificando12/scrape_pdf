from pypdf import PdfReader
from read_folder import read_dir
from docx import Document
from tkinter import filedialog
import tkinter as tk
import unicodedata
import re

def interface():

    def get_folder_path():
        folder_path = filedialog.askdirectory()
        return folder_path
    
    def start_program():

        file_list = read_dir(get_folder_path())
        print(file_list)
        lenth = len(file_list)
        book_page_paragraph = []
        word = get_text()
        file_name_choosen = file_name()

        for file in range(len(file_list)):
            
            try:
                reader = PdfReader(f'C:/Users/eciap/Documents/GitHub/scrape_pdf/pedro_pdf/{file_list[file]}') 
                number_of_pages = len(reader.pages)
                print(file_list[file])
                print(number_of_pages)
            except:
                print(f"Error al procesar el archivo '{file_list[file]}'. La propiedad no está presente en el objeto o tiene un valor nulo.")
                continue
            
            for page_number in range(number_of_pages):
                    
                page = reader.pages[page_number]
                try:
                    text = page.extract_text()
                    text = text.lower()
                    text_normalized = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii")
                    # print(text)
                    paragraphs = text_normalized.split('\n')
                except:
                    continue
                # print(paragraphs)
                
                for i in range(len(paragraphs)):
                    details = []
                                        
                    if word in paragraphs[i]:
                        details.append(f'PALABRA = {word}\n')
                        details.append(f'Libro {file_list[file].upper()}')
                        details.append(f'#####PAGINA {page_number + 1}/')
                        details.append(f'#####PARRAFO /{"".join(paragraphs)}/')
                        book_page_paragraph.append(details)
                        details = []
                        # print(book_page_paragraph)
                        break
               
        word_document = Document()

        for item in range(len(book_page_paragraph)):
            data = book_page_paragraph[item]
            joined_data = "".join(data)
            normalize_data = unicodedata.normalize("NFKD", joined_data).encode("ascii", "ignore").decode("ascii")
            clean_data = re.sub(r'[\x00-\x08\x0B\x0C\x0E-\x1F\x7F-\xFF]', '', normalize_data)
            word_document.add_paragraph(clean_data)

        word_document.save(f'{file_name_choosen}.docx')


    window = tk.Tk()
    window.geometry("400x400")

    search_label = tk.Label(window, text="Insert Word")
    search_label.pack()
    search_box = tk.Entry(window)
    search_box.pack()

    def get_text():
        search_word = search_box.get()
        return search_word
    
    file_name_label = tk.Label(window, text="Choose file name")
    file_name_label.pack()

    file_name_box = tk.Entry(window)
    file_name_box.pack()

    def file_name():
        choose_file_name = file_name_box.get()
        return choose_file_name

    submit_button = tk.Button(window, text="Submit", command=start_program)
    submit_button.pack()
    window.mainloop()

if __name__ == '__main__':
    interface()