A gif showing how to create a new notebook.

This was done by recording an `.mov` file and then converting using the info
available at
https://gist.github.com/SheldonWangRJT/8d3f44a35c8d1386a396b9b49b43c385:

    $ brew install ffmpeg
    $ brew install gifsicle
    $ ffmpeg -i in.mov -pix_fmt rgb8 -r 10 output.gif && gifsicle -O3 output.gif -o output.gif
