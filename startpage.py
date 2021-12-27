import re

importPath = r'C:\Users\Musse\Downloads\Github\Testing\content.txt'
outputPath = r'C:\Users\Musse\Downloads\Github\Testing\index.html'


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


def makeDoc(data):
    with open(outputPath, 'w') as file:
        page = '''<!DOCTYPE html>
<html lang="en">
<meta charset="UTF-8">
<title>musse@home > startpage</title>
<meta name="viewport" content="width=device-width,initial-scale=1">
<link rel="stylesheet" href="main.css">
<body>
    <p><span>musse@home &gt; </span><a href="https://app.netlify.com/sites/mussejusse/overview">startpage</a></p>
    <nav>
'''
        for category in data:
            page += '        <ul>\n'
            page += '            <li>'+category[0]+'</li>\n'
            for entry in category[1:]:
                name, link = entry.split(' | ')
                page += '                <li><a href="'+link+'">'+name+'</a></li>\n'
            page += '        </ul>\n\n'
        page += '''    </nav>

    <p><span>musse@home &gt; </span> <span id="cursor">_</span></p>
</body>

<script>
    var randomColour = "#" + ((1 << 24) * Math.random() | 0).toString(16);
    document.documentElement.style.setProperty('--bgcolour', randomColour);
</script>

</html>'''
        file.write(page)


if __name__ == "__main__":
    print('Importing data...', end="")
    data = importContent()
    print('Done.\nParsing data from import file...', end='')
    data = parseContents(data)
    print('Done.\nCreating HTML startpage...', end='')
    makeDoc(data)
    print('Done.')
    print('Finished. New startpage has been created.')
