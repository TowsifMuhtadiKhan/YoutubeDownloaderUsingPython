from moviepy.editor import VideoFileClip

videoclip = VideoFileClip("file_name.mp4")
new_clip = videoclip.without_audio()
new_clip.write_videofile("new_file_name.mp4")