import re

importPath = r"C:\\Users\\Musse\\Documents\\Github\\MusseJusse2.github.io\\content.txt"
outputPath = r"C:\\Users\\Musse\\Documents\\Github\\MusseJusse2.github.io\\index.html"
user = "musse"
main = user + "@home &gt; "
title = main + "startpage"


def importContent():
    with open(importPath, "r") as file:
        return file.read()


def parseContents(contents):
    while contents[0] == '\n':
        contents = contents[1:]
    while contents[-1] == '\n':
        contents = contents[:-1]
    contents = re.sub('\n{3,}', '\n\n', contents)
    contents = contents.split('\n\n')
    return [x.split('\n') for x in contents]


def createHTML(data):
    with open(outputPath, 'w') as file:
        page = '''<!DOCTYPE html>
<html lang="en">
<meta charset="UTF-8">
<title>'''+title+'''</title>
<meta name="viewport" content="width=device-width,initial-scale=1">
<link rel="stylesheet" href="main.css">
<script src="script.js"></script>

<body>
    <p><span>'''+main+'''</span><a href="https://app.netlify.com/sites/mussejusse/overview">startpage</a></p>
    <nav>
'''
        for category in data:
            page += '        <ul>\n'
            page += '            <li>'+category[0]+'</li>\n'
            for entry in category[1:]:
                name, link = entry.split(' | ')
                page += '            <li><a href="'+link+'">'+name+'</a></li>\n'
            page += '        </ul>\n\n'
        page += '''    </nav>

    <form action="https://www.google.com/search" class="searchform" method="get" name="searchform" target="_blank">
        <p><span>'''+main+'''</span>
            <input id="search" autocomplete="off" class="input" name="q" placeholder="" required="required"
                type="text"><button class="button" type="submit" autofocus></button>
        </p>
    </form>
</body>

</html>'''
        file.write(page)


if __name__ == "__main__":
    print('Importing data...', end='')
    data = importContent()
    print('Done.\nParsing data from import file...', end='')
    data = parseContents(data)
    print('Done.\nCreating HTML startpage...', end='')
    createHTML(data)
    print('Done.')
    print('Finished. New startpage has been created.')
