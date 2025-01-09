# main.py
import video_converter
import music_converter
import picture_converter
import document_converter

def main():
    print("Choose a file type to convert:")
    print("1. Video")
    print("2. Music")
    print("3. Picture")
    print("4. Document (PDF/EPUB)")
    
    choice = int(input("Enter choice (1-4): "))

    if choice == 1:
        input_file = input("Enter video file path: ")
        output_file = input("Enter output file path: ")
        output_format = input("Enter output format (e.g., avi, mp4): ")
        video_converter.convert_video(input_file, output_file, output_format)

    elif choice == 2:
        input_file = input("Enter music file path: ")
        output_file = input("Enter output file path: ")
        output_format = input("Enter output format (e.g., wav, mp3): ")
        music_converter.convert_music(input_file, output_file, output_format)

    elif choice == 3:
        input_file = input("Enter picture file path: ")
        output_file = input("Enter output file path: ")
        output_format = input("Enter output format (e.g., jpg, png): ")
        picture_converter.convert_picture(input_file, output_file, output_format)

    elif choice == 4:
        input_file = input("Enter document file path: ")
        output_file = input("Enter output file path: ")
        doc_choice = int(input("Convert: 1. PDF to EPUB or 2. EPUB to PDF? "))

        if doc_choice == 1:
            document_converter.convert_pdf_to_epub(input_file, output_file)
        elif doc_choice == 2:
            document_converter.convert_epub_to_pdf(input_file, output_file)
        else:
            print("Invalid choice.")
    else:
        print("Invalid option.")

if __name__ == "__main__":
    main()
