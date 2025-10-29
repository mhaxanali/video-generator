from moviepy import AudioFileClip, ImageClip, CompositeVideoClip, VideoFileClip, concatenate_videoclips
import os


def make_clip(line_text: str, image_path: str, audio_path: str, output_path: str) -> str:
    """
    Creates a short video segment with an image background,
    matching audio, and caption text overlay.
    """

    try:
        # Load image and audio
        audio = AudioFileClip(audio_path)
        image = ImageClip(image_path).with_duration(audio.duration)

        # Combine image + text + audio
        composite = CompositeVideoClip([image])
        composite = composite.with_audio(audio)

        # Export individual clip
        composite.write_videofile(
            output_path,
            codec='libx264',
            audio_codec='aac',
            fps=24,
            threads=4,
            logger=None
        )

        # Close resources
        composite.close()
        image.close()
        audio.close()

        return output_path

    except Exception as e:
        print(f"[ERROR] Failed to create clip: {e}")
        return ""


def combine_clips(clip_paths: list[str], final_output: str) -> None:
    """
    Combines all short clips into one continuous video.
    """
    try:
        clips = [VideoFileClip(p) for p in clip_paths if os.path.exists(p)]
        final = concatenate_videoclips(clips, method="compose")
        final.write_videofile(
            final_output,
            codec="libx264",
            audio_codec="aac",
            fps=24,
            threads=4
        )

        # Close all clips
        for clip in clips:
            clip.close()
        final.close()

    except Exception as e:
        print(f"[ERROR] Failed to combine clips: {e}")
