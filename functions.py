def select_text_on_focus(event, canvas, key, text):
    if canvas[key].get() == '':
        canvas[key].update(value=text)
    canvas[key].update(select=True)

def update_selection(canvas, key, text):
    canvas[key].Widget.bind("<FocusIn>", lambda event: select_text_on_focus(event, canvas, key, text))
    canvas[key].update(select=True)