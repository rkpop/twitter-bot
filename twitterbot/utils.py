def sanitize_flair(flair_text):
    return flair_text.strip("[").strip("]").replace(" ", "").replace("-", "")
