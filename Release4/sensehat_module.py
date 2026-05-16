from sense_hat import SenseHat # Sense HAT hardware interface
import logging # Local logging system

sense = SenseHat() # Create a single Sense HAT instance for LED display and sensor access

def show_message(text, text_colour=(0, 255, 0), back_colour=(0, 0, 0)):
    """
    Display a scrolling message on the Sense HAT.
    """
    try:
        logging.info(f"Displaying message on Sense HAT: {text}") # Log the message being displayed for debugging and traceability
        sense.show_message(text, text_colour=text_colour, back_colour=back_colour, scroll_speed=0.06) # Show the scrolling message with a fixed scroll speed
    except Exception as e:
        logging.error(f"Error displaying message on Sense HAT: {e}") # Log any hardware/display errors

def clear_display():
    """
    Clear the Sense HAT LED matrix.
    """
    try:
        sense.clear() # Turn off all LEDs
        logging.info("Sense HAT display cleared.")
    except Exception as e:
        logging.error(f"Error clearing Sense HAT display: {e}") # Log any issues clearing the display
