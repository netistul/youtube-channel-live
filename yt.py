import requests

def check_if_live(channel_id, channel_name, on_live, on_error):
    channel_id_url = f'https://www.youtube.com/channel/{channel_id}'

    try:
        response = requests.get(channel_id_url)
        if response.ok:
            if "hqdefault_live.jpg" in response.text:
                on_live(channel_name)
            elif "This channel does not exist" in response.text:
                on_error(channel_name, "Channel does not exist.")
            else:
                on_error(channel_name, "Channel is not live.")
        else:
            on_error(channel_name, "Failed to fetch channel data.")
    except requests.RequestException as e:
        on_error(channel_name, f"An error occurred: {e}")

def on_live(channel_name):
    print(f"The channel {channel_name} is live!")

def on_error(channel_name, error_message):
    print(f"Error for channel {channel_name}: {error_message}")

# Example usage
channel_id = "UCwUfX87V6RsbVVRrcrxmJAA"  # Replace with YouTube Channel ID. You can find or convert a YouTube channel name to a channel ID at: https://www.streamweasels.com/tools/youtube-channel-id-and-user-id-convertor/
channel_name = "CreativeMonkeyzArmy"  # Replace with any channel name

check_if_live(channel_id, channel_name, on_live, on_error)