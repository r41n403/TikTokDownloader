import os
import csv
import yt_dlp
import re


def sanitize_filename(filename):
    """Remove invalid characters from the filename."""
    return re.sub(r'[<>:"/\\|?*]', '_', filename)


def download_tiktok_video(url, output_dir):
    """Download a single TikTok video."""
    ydl_opts = {
        'format': 'mp4',  # Download in MP4 format
        'quiet': True,  # Suppress yt-dlp logs
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # Extract metadata
            info_dict = ydl.extract_info(url, download=False)
            title = sanitize_filename(info_dict.get('title', 'video'))  # Fallback to 'video' if no title
            output_file = os.path.join(output_dir, f"{title}.mp4")
            
            # Update output template with sanitized filename
            ydl_opts['outtmpl'] = output_file
            with yt_dlp.YoutubeDL(ydl_opts) as ydl_with_output:
                ydl_with_output.download([url])
            
            print(f"Downloaded: {url} -> {output_file}")
            return True  # Success
    except Exception as e:
        print(f"Failed to download {url}: {e}")
        return False  # Failure


def download_videos_from_csv(file_path, output_dir, failed_log_file):
    """Download TikTok videos from a list of URLs in a CSV file."""
    os.makedirs(output_dir, exist_ok=True)  # Ensure output directory exists
    failed_urls = []  # List to store failed URLs

    # Read the CSV file
    with open(file_path, 'r', encoding='utf-8') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            if 'URL' in row:  # Assumes the CSV has a column named 'URL'
                video_url = row['URL']
                success = download_tiktok_video(video_url, output_dir)
                if not success:
                    failed_urls.append(video_url)

    # Write failed URLs to the log file
    with open(failed_log_file, 'w') as failed_file:
        for url in failed_urls:
            failed_file.write(url + '\n')
    
    print(f"Failed downloads have been logged to {failed_log_file}")


# Define the input file, output directory, and failed log file
input_file = "my_data.csv"
output_directory = "./tiktok_videos"
failed_log_file = "failed_downloads.txt"

# Download videos from the CSV
download_videos_from_csv(input_file, output_directory, failed_log_file)



