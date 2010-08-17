Spotipy - A rudimentary interface to the Spotify player on OS X
===============================================================

Usage
-----
1. Install Spotipy from the Python Package Index, e.g. using easy_install:

        $ easy_install spotipy

2. Remember to activate assistive device support see <http://www.macspeech.com/extensions/faq/kb.php?article=48>

3. Use Spotipy like so:

        from spotipy import Spotipy

        spotify = Spotipy()
        
        # play/pause
        spotify.play_pause()
        
        # next/previous
        spotify.next()
        spotify.previous()
        
        # shuffle
        spotify.shuffle()
        
        # repeat
        spotify.repeat()
        
        # volume up
        spotify.volume_up()
        
        # volume down
        spotify.volume_down()
        
        # mute
        spotify.mute()
        
Inspiration
-----------
Inspired by <http://macdevcenter.com/pub/a/mac/2007/05/08/using-python-and-applescript-to-get-the-most-out-of-your-mac.html?page=2> and <http://www.jacktams.net/2009/05/15/controlling-spotify-through-applescript-quicksilver/>