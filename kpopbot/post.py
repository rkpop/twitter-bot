from kpopbot import media_provider, sanitize_flair, TEMPLATES


def post_factory(praw_item):
    class_name = (
        sanitize_flair(praw_item.link_flair_text)
        if praw_item.link_flair_text is not None
        else "Misc"
    )
    return globals()[class_name](praw_item)


# Base level class.
# Never instantiate directly


class Post(object):
    _template = ""
    _with_media = False

    def __new__(cls, *args, **kwargs):
        if cls is Post:
            raise TypeError("You shouldn't do this!")
        return object.__new__(cls)

    def __init__(self, praw_item):
        self.post_id = praw_item.id
        self.title = praw_item.title

    @property
    def nice(self):
        return self._template.format(title=self.title, id=self.post_id)


class Media(Post):
    _with_media = True

    def __new__(cls, *args, **kwargs):
        if cls is Media:
            raise TypeError("You shouldn't do this!")
        return object.__new__(cls)

    def __init__(self, praw_item):
        super().__init__(praw_item)
        self.image_url = (
            media_provider(praw_item.url)
            if praw_item.is_video is False
            else None
        )
        if self.image_url is None:
            self._with_media = False


# Post level subclass


class News(Post):
    _template = TEMPLATES["News"]


class Rumor(Post):
    _template = TEMPLATES["Rumor"]


class Interview(Post):
    _template = TEMPLATES["Interview"]


class MV(Post):
    _template = TEMPLATES["MV"]


class Audio(Post):
    _template = TEMPLATES["Audio"]


class Live(Post):
    _template = TEMPLATES["Live"]


class DanceCover(Post):
    _template = TEMPLATES["Dance Cover"]


class SongCover(Post):
    _template = TEMPLATES["Song Cover"]


class DancePractice(Post):
    _template = TEMPLATES["Dance Practice"]


class Teaser(Media):
    _template = TEMPLATES["Teaser"]


class Discussion(Post):
    _template = TEMPLATES["Discussion"]


class AlbumDiscussion(Post):
    _template = TEMPLATES["Album Discussion"]


class Feature(Post):
    _template = TEMPLATES["Feature"]


class FanAccount(Post):
    _template = TEMPLATES["Fan Account"]


class Variety(Post):
    _template = TEMPLATES["Variety"]


class BehindTheScenes(Media):
    _template = TEMPLATES["Behind-The-Scenes"]


class Misc(Post):
    _template = TEMPLATES["Misc"]


class MusicShow(Post):
    _template = TEMPLATES["Music Show"]
