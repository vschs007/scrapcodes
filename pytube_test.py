from pytube import  YouTube
YouTube('https://www.youtube.com/watch?v=yotCyfbVmRs').streams.first().download('location')