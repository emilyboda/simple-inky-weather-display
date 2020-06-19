#### INSTRUCTIONS
"""
1. Set the weather below.
2. Calibrate if part of your screen is hidden by a frame or mat.
3. Set the program to run at the frequency you wish with crontab.
"""

#### WEATHER INFO HERE
"""
Set the following equal to your dark sky API key and your location.
"""
dark_sky_api_key = "yourkeyhere"
dark_sky_coords = "37.931331,-76.187730"

#### RUN THE CALIBRATION FOR THE SCREEN
"""
This section is designed to center the display on the
part of the screen that is actually showing in a picture
frame. Most 5x7 frames will have a mat that covers up
part of the screen. Just make sure that your screen is
straight inside of the frame and then you can set the
calibration so that no part of the screen will be covered.

Run calibration.py and take a look at the numbers and boxes.
Set the following to the number line that is closest to
the edges specified.

For more instructions, see the example_calibration.png.

You can also set the following to zero to use the full display.
"""

left_edge = 49
top_edge = 46
right_edge =  579
bottom_edge = 375

