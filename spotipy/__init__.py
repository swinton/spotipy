#!/usr/bin/env python
import os

class Spotipy:
    """
    Provides a rudimentary interface to the Spotify player on OS X
    Supports play/pause, next/previous, shuffle, repeat, volume_up/volume_down/mute commands.
    
    Usage:
        import spotipy
        spotify = spotipy.Spotipy()
        spotify.play_pause()
        spotify.next()
        spotify.previous()
        # etc.
    
    Inspired by:
        * http://macdevcenter.com/pub/a/mac/2007/05/08/using-python-and-applescript-to-get-the-most-out-of-your-mac.html?page=2 
        -and-
        *  http://www.jacktams.net/2009/05/15/controlling-spotify-through-applescript-quicksilver/
    """
    
    __menu_items = {
        'play_pause' : 1,
        'next' : 3,
        'previous' : 4,
        'shuffle' : 6,
        'repeat' : 7,
        'volume_up' : 9,
        'volume_down' : 10,
        'mute' : 11
    }
    
    def __init__(self):
        def make_cmd(menu_item):
            cmd = """osascript<<END
tell application "Spotify" to activate
tell application "System Events"
   tell process "Spotify"
      click menu item %d of menu 1 of menu bar item 6 of menu bar 1
   end tell
end tell
END"""
            
            def do_cmd(self):
                os.system(cmd % self.__menu_items[menu_item])
            do_cmd.func_doc = "Sends the %s command to the Spotify player." % menu_item
            
            return do_cmd
            
        for key in self.__menu_items.keys():
            setattr(self.__class__, key, make_cmd(key))
            
if __name__ == "__main__":
    spotify = Spotipy()
    spotify.play_pause()