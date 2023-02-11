import moviepy.editor


video = moviepy.editor.VideoFileClip('currentfilename.mp4')
audio = video.audio
audio.write_audiofile('currentfilename.mp3')
