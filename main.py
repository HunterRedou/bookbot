def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = ""
        file_contents = f.read()
        return file_contents
        
        
def counting(file_contents):
    words = file_contents.split()
    count = 0
    
    for word in words:
        count += 1
    
    return count
    
def main():
    print(f"{counting(get_book_text("books/frankenstein.txt"))} words found in the document")

main()