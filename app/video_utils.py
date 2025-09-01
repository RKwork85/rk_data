from moviepy import VideoFileClip
import os

def split_video(input_video_path: str, segment_length: float, output_dir: str):
    """
    将视频切割为多个片段，每个片段的时长为 segment_length。
    """
    video = VideoFileClip(input_video_path)
    video_duration = video.duration
    segments = []

    os.makedirs(output_dir, exist_ok=True)

    for start_time in range(0, int(video_duration), int(segment_length)):
        end_time = min(start_time + segment_length, video_duration)
        output_path = os.path.join(output_dir, f"segment_{start_time}_{end_time}.mp4")
        
        # 剪切视频
        segment = video.subclip(start_time, end_time)
        segment.write_videofile(output_path, codec="libx264")
        
        segments.append({
            "segment_url": output_path,
            "start_time": start_time,
            "end_time": end_time
        })

    return segments
