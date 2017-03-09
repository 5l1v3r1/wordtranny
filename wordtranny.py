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

print banner
