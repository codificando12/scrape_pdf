from pypdf import PdfReader
from read_folder import read_dir
from docx import Document
from tkinter import filedialog
import tkinter as tk
import unicodedata
import re


def interface():

    def get_folder_path(): #This funtion return the folder path to get the pdfs list
        global folder_path
        folder_path = filedialog.askdirectory() 
        path_label.configure(text=folder_path)
    
    def get_text():
        search_word = search_box.get()
        return search_word
    
    def file_name():
        choose_file_name = file_name_box.get()
        return choose_file_name
    
    def start_program():

        pdfs_path = get_folder_path()
        print(pdfs_path)
        file_list = read_dir(pdfs_path)
        print(len(file_list))
        lenth = len(file_list)
        print(lenth)
        book_page_paragraph = []
        word = get_text()
        compound_word = word.split(" ")
        # print(compound_word)
        file_name_choosen = file_name()
        word_document = Document()
        
        for file in range(len(file_list)):
            
            try:
                reader = PdfReader(f'{pdfs_path}/{file_list[file]}') 
                number_of_pages = len(reader.pages)
                print(file_list[file])
                print(number_of_pages)
            except:
                print(f"Error al procesar el archivo '{file_list[file]}'. La propiedad no está presente en el objeto o tiene un valor nulo.")
                continue
            
            for page_number in range(number_of_pages):

                try:    
                    page = reader.pages[page_number]
                    try:
                        text = page.extract_text()
                        text = text.lower()
                        text_normalized = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii")
                        text_normalized = text_normalized.replace("(", "( ")
                        text_normalized = text_normalized.replace("'", "' ")
                        text_normalized = text_normalized.replace("\"", "\" ")
                        text_normalized = text_normalized.replace("[", "[ ")
                        text_normalized = text_normalized.replace("{", "{ ")
                        text_normalized = text_normalized.replace(",", " ,")
                        text_normalized = text_normalized.replace(".", " .")
                        text_normalized = text_normalized.replace(";", " ;")
                        text_normalized = text_normalized.replace(":", " :")
                        paragraphs = text_normalized.split(' ')
                        # print(paragraphs)
                        
                    except:
                        continue
                except:
                    print(f"No se pudo leer las paginas en el libro '{file_list[file]}'")
                    continue
                
                # for i in range(len(paragraphs)):
                #     details = []
                                        
                #     if word in paragraphs[i]:
                #         print(paragraphs[i], i)
                #         details.append(f'PALABRA = {word}\n')
                #         details.append(f'Libro {file_list[file].upper()}')
                #         details.append(f'#####PAGINA {page_number + 1}/')
                #         details.append(f'#####PARRAFO /{"".join(paragraphs)}/')
                #         book_page_paragraph.append(details)
                #         details = []
                #         # print(book_page_paragraph)
                #         break
                
                for i in range(len(paragraphs)):
                    details = []
                    if len(compound_word) == 1 and paragraphs[i].startswith(word):
                        
                        print(compound_word[0])
                        details.append(f'PALABRA = {word}\n')
                        details.append(f'---Libro = {file_list[file].upper()} ---')
                        details.append(f'---PAGINA = {page_number + 1}/ ---')
                        sentences = paragraphs[i - 50:i + 50]
                        details.append(f'---\n/{" ".join(sentences)}/ ---')
                        print(sentences)
                        # print(details)
                        book_page_paragraph.append(details)
                        details = []
                        # print(details)


                    elif len(compound_word) > 1 and paragraphs[i].startswith(compound_word[0]) and paragraphs[i + 1].startswith(compound_word[1]):
                        print(compound_word)
                        details.append(f'PALABRA = {" ".join(compound_word)}\n')
                        details.append(f'---Libro = {file_list[file].upper()} ---')
                        details.append(f'---PAGINA = {page_number + 1}/ ---')
                        sentences = paragraphs[i - 50:i + 50]
                        details.append(f'---\n/{" ".join(sentences)}/ ---')
                        book_page_paragraph.append(details)
                        details = []
                        print(details)
                            

                    # elif len(compound_word) == 1 and paragraphs[i].startswith(compound_word[0]):
                        
                    #     print(compound_word[0])
                    #     details.append(f'PALABRA = {word}\n')
                    #     details.append(f'---Libro = {file_list[file].upper()} ---')
                    #     details.append(f'---PAGINA = {page_number + 1}/ ---')
                    #     sentences = paragraphs[i - 50:i + 50]
                    #     details.append(f'---\n/{" ".join(sentences)}/ ---')
                    #     print(sentences)
                    #     # print(details)
                    #     book_page_paragraph.append(details)
                    #     details = []
                    #     # print(details)
                
                    else:
                        continue
        # word_document = Document()

            for item in range(len(book_page_paragraph)):
                data = book_page_paragraph[item]
                joined_data = "".join(data)
                normalize_data = unicodedata.normalize("NFKD", joined_data).encode("ascii", "ignore").decode("ascii")
                clean_data = re.sub(r'[\x00-\x08\x0B\x0C\x0E-\x1F\x7F-\xFF]', '', normalize_data)
                word_document.add_paragraph(clean_data)

            word_document.save(f'{file_name_choosen}.docx')
            book_page_paragraph = []

        print("Scan completed")
    
    folder_path = "" #save the folder path that search folder path returns
    window = tk.Tk()
    window.geometry("600x600")

    title_label = tk.Label(window, text="Search the word that you want in your PDFs files \n and get a paragraph with the results")
    title_label.grid(row=0, column=1)

    folder_label = tk.Label(window, text="Folder")
    folder_label.grid(row=1, column=0)

    path_label = tk.Label(window, bg = "White", borderwidth = 1, relief = "solid" ,width = 50)
    path_label.grid(row = 1, column = 1,pady = 6)

    browse_button = tk.Button(window, text= "Browse", command = get_folder_path)
    browse_button.grid(row = 1, column = 2, padx = 6)

    search_label = tk.Label(window, text="Insert Word")
    search_label.grid(row = 2, column = 0)
    search_box = tk.Entry(window)
    search_box.grid(row = 3, column = 0)

    
    
    file_name_label = tk.Label(window, text="Choose file name")
    file_name_label.grid(row=4, column=0)

    file_name_box = tk.Entry(window)
    file_name_box.grid(row=5, column=0)

    

    submit_button = tk.Button(window, text="Submit", command=start_program)
    submit_button.grid(row=6, column=0)
    window.mainloop()

if __name__ == '__main__':
    interface()