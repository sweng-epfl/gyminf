# But : enlever le header "Project Gutenberg" d'un fichier .txt téléchargé sur leur site, pour usage personnel
# On détecte donc la ligne qui contient deux fois "***"

def read(path):
    with open(path, "r") as file:
        return file.read()

def write(path, text):
    with open(path, "w") as file:
        print(text, file=file)

def append(s, c):
    return s + c

def counter(c, chr, target):
    if chr == target:
        return c + 1
    return 0

def extract(name):
    text = read(name + ".txt")
    result = ""
    stars = 0
    stars_groups = 0
    header_end = False
    for c in text:
        if header_end:
            result = append(result, c)
        else:
            stars = counter(stars, c, "*")
            if stars == 3:
                stars_groups = stars_groups + 1
            if stars_groups == 2:
                header_end = True
    write(name + ".extracted.txt", result)

if __name__ == "__main__":
    extract("lupin")
