from re import search


def sanitize_flair(flair_text):
    return (
        search(r"\[(.*?)\]", flair_text)
        .group(1)
        .replace("-", "")
        .replace(" ", "")
    )
