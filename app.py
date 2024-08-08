import tkinter as tk
from tkinter import filedialog, messagebox
from moviepy.editor import VideoFileClip

class VideoToAudioConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Video to Audio Converter")
        self.root.geometry("400x200")  # Set the window size

        # Initialize the path variables
        self.video_path = None
        self.audio_path = None

        # Create and place the upload button
        self.upload_button = tk.Button(root, text="Upload Video File", command=self.upload_video)
        self.upload_button.pack(pady=10)

        # Create and place the save button
        self.save_button = tk.Button(root, text="Save Audio File", command=self.save_audio)
        self.save_button.pack(pady=10)
        self.save_button.config(state=tk.DISABLED)  # Disable until a video is uploaded

    def upload_video(self):
        try:
            # Open file dialog to select a video file
            self.video_path = filedialog.askopenfilename(filetypes=[("Video Files", "*.mp4;*.mov;*.avi")])
            
            if not self.video_path:
                return

            self.save_button.config(state=tk.NORMAL)  # Enable save button
            messagebox.showinfo("Info", "Video file uploaded successfully!")

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    def save_audio(self):
        try:
            if not self.video_path:
                messagebox.showwarning("Warning", "Please upload a video file first.")
                return

            # Load the video file
            video = VideoFileClip(self.video_path)
            
            # Extract audio
            audio = video.audio
            
            # Save audio as MP3 file
            self.audio_path = filedialog.asksaveasfilename(defaultextension=".mp3", filetypes=[("MP3 Files", "*.mp3")])
            
            if not self.audio_path:
                return
            
            audio.write_audiofile(self.audio_path)
            messagebox.showinfo("Success", "Audio successfully extracted and saved!")

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

# Create the main window
root = tk.Tk()
app = VideoToAudioConverterApp(root)

# Run the application
root.mainloop()
