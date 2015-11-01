# SI106Project
creating a text adventure game using python

mystery.py is a small text adventure game, which allows users to walk through the plot of the story and make choices in the game.
 
***********************************************************************************************************************

In order for this game to work, it needs:

- AVBin installed in order to decode compressed media, such as mp3 files: the file "avbin.dll" has to be in the same working directory as the game code file
#If you don't have AVBin installed:
1. You can go to this website to install AVBin: https://code.google.com/p/avbin/downloads/detail?name=avbin-win32-5.zip
2. Then move the "avbin.dll" file from the installed folder to the working directory, where you have the game. 


- "pulse.mp3" or other soundfile in mp3 format: this also has to be in the same working directory.
#Note: If you choose a soundfile other than "pulse.mp3", then you need to edit the code in in the mystery.py and replace the "pulse.mp3" with the name of the soundfile that you are going to use

*************************************************************************************************************************

This game makes use of these modules:
- pyglet 
- time
- sys
- test106 (this has to be in the same working directory)
If you don't have any of these modules, please download or install using pip. 
