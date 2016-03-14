#!/usr/bin/env python3
# cxhtml2.py
# Collapsible Expandable HTML Converter (Version 2).
# Single paste for automatically generating an html version of
# an allocation form.
# This is version 2 that uses bootstrap for more modern feel.
# Save this program on your computer to use.

import re

def main():
    nickname = ''
    while nickname == '':
        nickname = input("File Name (e.g, \"c4-customer3_v105\"): ")
    print('Paste the entire allocation form in a text format.')
    print('When finished, type "f" and hit <Enter>.\n')
	
    content = '<body>\n<p id="monospace">\n'
    line = escape(input())
    q = re.compile(r"INFORMATION\d?.*:")
    while q.search(line) == None:
        line = escape(line)
        content += line+'<br>\n'
        line = escape(input())
    content += '<a onclick="javascript:ShowHide(\'HiddenDiv0\')">\n'
    content += '<p id="monospace", class="ex"><b>'+line+'</b></a><br></p>\n'
    line = escape(input())
    content += '<p id="monospace">'+line+'</p>\n' # <br> removed
    # GENERAL INFORMATION section is expanded by default. Change style to "display: none;" if it should be collapsed.
    content += '<div class="mid" id="HiddenDiv0" style="display: block;">\n'    
    content += '<p id="monospace">\n'
    k = 0
    line = escape(input())
    while line != 'f':
        if q.search(line) == None:
            line = escape(line) # to properly handle spaces, <, and >
            content += line+'<br>\n'
            line = escape(input())
        else:       # Same as -->  elif: q.search(line):
            content += '<br>\n'
            content += '<br>\n'
            content += '</p>\n'
            content += '</div>\n'
            content += '\n' #End of the k-th section
            k += 1
            content += '<a onclick="javascript:ShowHide(\'HiddenDiv'+str(k)+'\')">\n'
            content += '<p id="monospace", class="ex"><b>'+line+'</b></a><br></p>\n'
            line = escape(input())
            content += '<p id="monospace">'+line+'</p>\n' #<br> removed
            content += '<div class="mid" id="HiddenDiv'+str(k)+'" style="display: none;">\n'
            content += '<p id="monospace">\n'
            line = escape(input())
    content += '<br>\n'
    content += '<br>\n'
    content += '</p>\n'
    content += '</div>\n'
    content += '\n' 
    content += '</p></body>'

    ######## Create and save the HTML source code file ########
    outfile = open(nickname+'.html', 'w')
    
    print(head(nickname), file=outfile)   # Start of <html> and the whole <head>
    print(content, file=outfile)          # Nuts and bolts of <body> 
    print(end(), file=outfile)            # End of <body> and <html>

    print('The file',nickname+'.html has been created and saved.')
    close = input('Hit <Enter> to close.')

def escape(string):
    # Converts '<' and '>' into respective html codes &#num; so '<XXXX>' won't be
    # processed as an html tag by a browser.
    # Also process whitespace as they appear on python shell or on whatever console in use
    string = string.replace(' ','&nbsp;')
    string = string.replace('<','&#60;')
    string = string.replace('>','&#62;')
    return string

def head(nickname):
    # HTML tagged form starts here.
    # 'head' is a single string but when printed linebreaks
    # appear as appropriate.
    head = '<html>\n'
    head += '<title>'+nickname+'</title>\n'
    head += '<head>\n'
    head += '<script type="text/javascript">// <![CDATA[\nfunction ShowHide(divId)\n'
    head += '{\n'
    head += 'if(document.getElementById(divId).style.display == "none")\n'
    head += '{\n'
    head += 'document.getElementById(divId).style.display="block";\n'
    head += '}\n'
    head += 'else\n'
    head += '{\n'
    head += 'document.getElementById(divId).style.display = "none";\n'
    head += '}\n'
    head += '}\n'
    head += '// ]]></script>\n'
    head += '<style type="text/css">\n'
    head += '\n'
    head += 'body {font-size: 14px;}\n'
    head += 'p {margin: 0;}\n'
    head += '\n'
    head += 'p#serif {font-family: serif;margin: 10px;}\n'
    head += 'p#sans-serif {font-family: sans-serif;margin: 10px;}\n'
    head += 'p#monospace {font-family: monospace;margin: 10px;}\n'
    head += 'p#fantasy {font-family: fantasy;margin: 10px;}\n'
    head += 'p#cursive {font-family: cursive;margin: 10px;}\n'
    head += '\n'
    head += 'p.ex {color: rgb(0,0,255);}\n'
    head += 'p.gx {color: rgb(255,0,0);}\n'
    head += '</style>\n'
    head += '<meta charset="utf-8">\n'
    head += '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
    head += '<link rel="stylesheet" href="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css">\n'
    head += '<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.0/jquery.min.js"></script>\n'
    head += '<script src="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js"></script>\n'
    head += '</head>\n'
    # HTML head section ended.
    return head

def end():
    # to conclude the HTML doc.
    # End of <body> and the entire <html>
    return '</body>\n</html>\n'

if __name__ == '__main__':
    main()

