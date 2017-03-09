from transliterate import detect_language
from transliterate import translit, get_available_language_codes
from argparse import RawTextHelpFormatter
import argparse
import sys, os
import argparse

class colors:
    white = "\033[1;37m"
    normal = "\033[0;00m"
    red = "\033[1;31m"
    blue = "\033[1;34m"
    green = "\033[1;32m"
    lightblue = "\033[0;34m"
  
banner = colors.blue + r"""

                        .___ __                                     
__  _  _____________  __| _//  |_____________    ____   ____ ___.__.
\ \/ \/ /  _ \_  __ \/ __ |\   __\_  __ \__  \  /    \ /    <   |  |
 \     (  <_> )  | \/ /_/ | |  |  |  | \// __ \|   |  \   |  \___  |
  \/\_/ \____/|__|  \____ | |__|  |__|  (____  /___|  /___|  / ____|
                         \/                  \/     \/     \/\/     

"""+'\n' \
+ '\n wordtranny.py v0.1' \
+ '\n Created by: Shane Young/@x90skysn3k & Jonathan Stines/@frankenstiner' + '\n' \
+ colors.normal + '\n'

def convert_file():
    output = 'converted/' + args.outfile + ".txt"
    with open(args.file, 'r') as word_file:
        translated = []
        for word in word_file:
#            language = detect_language(u'word')
#            print language
#            break
            with open(output, 'w+') as f:
                translate = translit(word, args.language)
                translated += translate
                f.write(''.join(translated).encode('utf-8').strip())
                f.write('\n')
                
    print "\nWritten list to: " + "[" + colors.green + "+" + colors.normal + "] " + colors.green + output + colors.normal            
       

def parse_args():
    lens = get_available_language_codes()
    
    parser = argparse.ArgumentParser(formatter_class=RawTextHelpFormatter, description=\
    banner + "Usage: python wordtranny.py <OPTIONS> \n" + "Available Languages: \n" + str(lens))
    
    menu_group = parser.add_argument_group(colors.lightblue + 'Menu Options' + colors.normal)

    menu_group.add_argument('-f', '--file', help="wordlist to open", required=True)
    
    menu_group.add_argument('-l', '--language', help="language to convert to", required=True)

    menu_group.add_argument('-o', '--outfile', help="outfile to write the converted text to", required=True)
       
    args = parser.parse_args()


    output = None

    return args,output

if __name__ == "__main__":
    print(banner)
    args,output = parse_args()
    if not os.path.exists("converted/"):
        os.mkdir("converted/")
    
    convert_file() 
