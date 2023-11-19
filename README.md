# Check if a YouTube Channel is Live Without Using the YouTube API

## Overview
Simple Python script designed to check whether a YouTube channel is currently live streaming. This utility operates without the need for YouTube's API, offering an alternative approach for users.

## Disclaimer
This script is intended strictly for **educational purposes**. It is not designed to encourage or support any form of Terms of Service violation on YouTube. Users are responsible for ensuring their use of the script complies with YouTube's policies and legal regulations.

## Description
The script works by checking the YouTube channel's page for specific indicators of a live stream. It's a straightforward tool, perfect for educational insights into web scraping and basic Python scripting. 

**Note:** This method relies on parsing the HTML content of the YouTube page, which can be subject to change. Therefore, the script's effectiveness may vary over time.

## How to Use
1. **Obtain YouTube Channel ID**: First, find the YouTube channel ID you wish to check. If you only have the channel name, you can convert it to an ID using online tools like [StreamWeasels YouTube Channel ID and User ID Converter](https://www.streamweasels.com/tools/youtube-channel-id-and-user-id-convertor/).

2. **Running the Script**: Replace the `channel_id` and `channel_name` variables in the script with the respective ID and name of the YouTube channel you are checking.

3. **Execute the Script**: Run the script in a Python environment. To execute the script, navigate to the directory containing the script and run it using Python from the console:
   ```bash
   python yt.py
