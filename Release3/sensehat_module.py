from sense_hat import SenseHat
import logging

sense = SenseHat()

def show_message(text, text_colour=(0, 255, 0), back_colour=(0, 0, 0)):
    """
    Display a scrolling message on the Sense HAT.
    """
    try:
        logging.info(f"Displaying message on Sense HAT: {text}")
        sense.show_message(text, text_colour=text_colour, back_colour=back_colour, scroll_speed=0.06)
    except Exception as e:
        logging.error(f"Error displaying message on Sense HAT: {e}")

def clear_display():
    """
    Clear the Sense HAT LED matrix.
    """
    try:
        sense.clear()
        logging.info("Sense HAT display cleared.")
    except Exception as e:
        logging.error(f"Error clearing Sense HAT display: {e}")
