# A plugin for [Sublime Text 2][1] which centers the window around the cursor

## Background

This plugin implements the Emacs command Ctrl-l, which centers the current
view vertically around the cursor.

I can’t remember where I found this or who originally wrote it, but  I
am putting it up here so that more people can benefit from it. Hope that’s 
OK with the original author.

## Usage

Copy CenterSelectionInVisibleAreaCommand.py to your Packages/User folder, 
then add a key-binding for the new command, like so:

    { "keys": ["ctrl+l"], "command": "center_selection_in_visible_area" },


[1]: http://www.sublimetext.com/2
