from pydub import AudioSegment

AudioSegment.from_file('video.mp4').set_channels(1).export()