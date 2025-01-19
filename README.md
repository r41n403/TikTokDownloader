# TikTok Video Downloader Instructions

## Steps:

### 1. Export TikTok Video Links
1. Open your web browser and go to the desired TikTok profile.
2. Press `F12` to open the developer console.
3. Open the console tab and paste the following code to enable continuous scrolling:
   ```javascript
   let goToBottom = setInterval(() => window.scrollBy(0, 400), 1000);
   ```
   - If prompted that the code is insecure, type `"allow pasting"` in the console and press `Enter`.
4. Copy and paste the following script into the console to extract video descriptions and URLs:
   ```javascript
   let arrayVideos = [];
   console.log('\n'.repeat(50));

   // Locate all video containers
   const videoContainers = document.querySelectorAll('.css-1uqux2o-DivItemContainerV2'); // Adjust this selector if necessary

   videoContainers.forEach((container, index) => {
       const descriptionElement = container.querySelector('img[alt]'); // Locate the <img> with description in the alt attribute
       const videoLinkElement = container.querySelector('a[href^="https://www.tiktok.com/"]'); // Locate the <a> tag with the video URL

       const description = descriptionElement ? descriptionElement.getAttribute('alt').trim() : 'No description'; // Extract description or default
       const videoURL = videoLinkElement ? videoLinkElement.href : 'No URL'; // Extract URL or default

       if (description && videoURL) {
           arrayVideos.push(`"${description}","${videoURL}"`); // Format as CSV
           console.log(`Description ${index + 1}: ${description}, URL: ${videoURL}`);
       } else {
           console.log(`Missing description or URL for video ${index + 1}.`);
       }
   });

   // Generate CSV file
   if (arrayVideos.length > 0) {
       const csvContent = "Description,URL\n" + arrayVideos.join("\n");
       const blob = new Blob([csvContent], { type: 'text/csv;charset=utf-8;' });
       const url = URL.createObjectURL(blob);
       const a = document.createElement('a');
       a.href = url;
       a.download = 'my_data.csv';
       a.click();

       console.log("CSV file created successfully.");
   } else {
       console.log("No data found to export.");
   }
   ```
5. A file named `my_data.csv` will be generated. Save it in the same directory where you plan to run the Python script.

---

### 2. Set Up the Downloader
6. Ensure that Python 3 is installed on your system.
7. Open a terminal or command prompt and install `yt-dlp` using:
   ```bash
   pip install yt-dlp
   ```

---

### 3. Run the Python Script
8. Navigate to the directory containing the `tiktok_downloader.py` script and the `my_data.csv` file using:
   ```bash
   cd /path/to/your/directory
   ```
9. Run the downloader script:
   ```bash
   python3 tiktok_downloader.py
   ```

---

### 4. Review Downloaded Files
10. The downloaded TikTok videos will be saved in a directory named `tiktok_videos`.
11. Any videos that failed to download will be logged in a file named `failed_downloads.txt` in the same directory. You can manually download these videos if necessary.

---

### Notes
- Ensure the TikTok page has fully loaded and scrolled to the bottom before running the export script.
- Adjust the CSS selectors in the script if TikTok's website layout changes.

Happy downloading! 🎥
