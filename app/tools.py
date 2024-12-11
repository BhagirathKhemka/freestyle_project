from IPython.display import Image, display
from datetime import datetime
import pytz

def show_image(image_url):
    """Display an image from a URL."""
    display(Image(url=image_url, width=750, height=500))

def convert_to_est(published_at):
    """Convert UTC time to EST."""
    utc_time = datetime.strptime(published_at, '%Y-%m-%dT%H:%M:%S%z')
    est_tz = pytz.timezone('US/Eastern')
    est_time = utc_time.astimezone(est_tz)
    return est_time.strftime("%B %d, %Y %I:%M %p EST")
