from gtts import gTTS
import pdfplumber
from art import tprint
from pathlib import Path
import time

def pdf_to_mp3_converter(file_path='test.pdf', language='en'):
    
    if Path(file_path).is_file() and Path(file_path).suffix == '.pdf':

        print(f'[+] Original file: {Path(file_path).name}')
        print(f'[+] Start processing at {time.ctime()}')
        
        start_time = time.time()

        with pdfplumber.PDF(open(file=file_path, mode='rb')) as pdf:

            pages = [page.extract_text() for page in pdf.pages]    
        
        text = ''.join(pages)
        text = text.replace('\n', '')

        my_audio = gTTS(text=text, lang=language)
        file_name = Path(file_path).stem
        my_audio.save(f'{file_name}.mp3')

        return f'[+]Finished at {time.ctime()} in {(time.time() - start_time)} secods'\
            f'\n[+] {file_name}.mp3 saved successfully\n---Have a nice day!---'
    
    else:

        return 'File not exists, check the file path!'


def main():
    
    tprint('PDF to MP3', font='bulbhead')
    file_path = input("\nEnter a file's path: ")
    language = input("Enter a pdf file text language, for example 'en' or 'ru': ")
    print(pdf_to_mp3_converter(file_path=file_path, language=language))
    

if __name__ == '__main__':
    main()


