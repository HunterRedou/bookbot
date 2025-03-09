def counting(file_contents):
    words = file_contents.split()
    count = 0
    
    for word in words:
        count += 1
    
    return count