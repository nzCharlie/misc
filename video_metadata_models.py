from peewee import *

database = PostgresqlDatabase('video_metadata', **{'user': 'postgres'})
database.register_unicode = False

class BaseModel(Model):
    class Meta:
        database = database

class Actor(BaseModel):
    actor = CharField(max_length=255)
    create_date = DateTimeField(null=True)
    mapper_id = IntegerField()
    modify_date = DateTimeField(null=True)

    class Meta:
        db_table = 'actor'

class Collection(BaseModel):
    create_date = DateTimeField(null=True)
    modify_date = DateTimeField(null=True)
    title = CharField(max_length=255)
    uid = BigIntegerField()

    class Meta:
        db_table = 'collection'

class CollectionMap(BaseModel):
    collection = ForeignKeyField(db_column='collection_id', rel_model=Collection)
    create_date = DateTimeField(null=True)
    mapper_id = IntegerField()
    modify_date = DateTimeField(null=True)

    class Meta:
        db_table = 'collection_map'

class Director(BaseModel):
    create_date = DateTimeField(null=True)
    director = CharField(max_length=255)
    mapper_id = IntegerField()
    modify_date = DateTimeField(null=True)

    class Meta:
        db_table = 'director'

class Genre(BaseModel):
    create_date = DateTimeField(null=True)
    genre = CharField(db_column='gnere', max_length=255)
    mapper_id = IntegerField()
    modify_date = DateTimeField(null=True)

    class Meta:
        db_table = 'gnere'

class Library(BaseModel):
    is_public = BooleanField()
    title = CharField(max_length=255)

    class Meta:
        db_table = 'library'

class HomeVideo(BaseModel):
    create_date = DateTimeField(null=True)
    library = ForeignKeyField(db_column='library_id', null=True, rel_model=Library)
    mapper_id = IntegerField()
    modify_date = DateTimeField(null=True)
    record_time = DateTimeField(null=True)
    sort_title = CharField(max_length=255)
    title = CharField(max_length=255)

    class Meta:
        db_table = 'home_video'

class LibraryPrivilege(BaseModel):
    library = ForeignKeyField(db_column='library_id', rel_model=Library)
    uid = BigIntegerField()

    class Meta:
        db_table = 'library_privilege'

class Movie(BaseModel):
    create_date = DateTimeField(null=True)
    islock = BooleanField(null=True)
    library = ForeignKeyField(db_column='library_id', null=True, rel_model=Library)
    mapper_id = IntegerField()
    modify_date = DateTimeField(null=True)
    originally_available = DateField(null=True)
    sort_time = DateField(null=True)
    sort_title = CharField(max_length=255)
    tag_line = CharField(max_length=255)
    title = CharField(max_length=255)
    year = IntegerField(null=True)

    class Meta:
        db_table = 'movie'

class PlusInfo(BaseModel):
    create_date = DateTimeField(null=True)
    mapper_id = IntegerField()
    modify_date = DateTimeField(null=True)
    plus_info = TextField()

    class Meta:
        db_table = 'plus_info'

class Poster(BaseModel):
    create_date = DateTimeField(null=True)
    mapper_id = IntegerField()
    md5 = TextField()
    modify_date = DateTimeField(null=True)

    class Meta:
        db_table = 'poster'

class Summary(BaseModel):
    create_date = DateTimeField(null=True)
    mapper_id = IntegerField()
    modify_date = DateTimeField(null=True)
    summary = TextField()

    class Meta:
        db_table = 'summary'

class TvRecord(BaseModel):
    channel_name = CharField(max_length=255)
    create_date = DateTimeField(null=True)
    mapper_id = IntegerField()
    modify_date = DateTimeField(null=True)
    record_time = DateTimeField(null=True)
    sort_title = CharField(max_length=255)
    title = CharField(max_length=255)

    class Meta:
        db_table = 'tv_record'

class Tvshow(BaseModel):
    create_date = DateTimeField(null=True)
    islock = BooleanField(null=True)
    library = ForeignKeyField(db_column='library_id', null=True, rel_model=Library)
    mapper_id = IntegerField()
    modify_date = DateTimeField(null=True)
    originally_available = DateField(null=True)
    sort_time = DateField(null=True)
    sort_title = CharField(max_length=255)
    title = CharField(max_length=255)
    year = IntegerField(null=True)

    class Meta:
        db_table = 'tvshow'

class TvshowEpisode(BaseModel):
    create_date = DateTimeField(null=True)
    episode = IntegerField(null=True)
    islock = BooleanField(null=True)
    library = ForeignKeyField(db_column='library_id', null=True, rel_model=Library)
    mapper_id = IntegerField()
    modify_date = DateTimeField(null=True)
    originally_available = DateField(null=True)
    season = IntegerField(null=True)
    sort_time = DateField(null=True)
    tag_line = CharField(max_length=255)
    tvshow = ForeignKeyField(db_column='tvshow_id', rel_model=Tvshow)
    year = IntegerField(null=True)

    class Meta:
        db_table = 'tvshow_episode'

class VideoFile(BaseModel):
    audio_bitrate = IntegerField(null=True)
    audio_codec = CharField(max_length=255, null=True)
    channel = IntegerField(null=True)
    container_type = CharField(max_length=255, null=True)
    create_date = DateTimeField(null=True)
    display_x = IntegerField(null=True)
    display_y = IntegerField(null=True)
    duration = IntegerField()
    filesize = BigIntegerField()
    frame_bitrate = IntegerField(null=True)
    frame_rate_den = IntegerField(null=True)
    frame_rate_num = IntegerField(null=True)
    frequency = IntegerField(null=True)
    mapper_id = IntegerField()
    modify_date = DateTimeField(null=True)
    path = CharField(max_length=4096)
    resolutionx = IntegerField(null=True)
    resolutiony = IntegerField(null=True)
    updated = CharField(max_length=1, null=True)
    video_bitrate = IntegerField(null=True)
    video_codec = CharField(max_length=255, null=True)
    video_level = IntegerField(null=True)
    video_profile = IntegerField(null=True)

    class Meta:
        db_table = 'video_file'

class WatchStatus(BaseModel):
    create_date = DateTimeField(null=True)
    mapper_id = IntegerField()
    modify_date = DateTimeField(null=True)
    position = IntegerField()
    uid = BigIntegerField()
    video_file = ForeignKeyField(db_column='video_file_id', rel_model=VideoFile)

    class Meta:
        db_table = 'watch_status'

class Writer(BaseModel):
    create_date = DateTimeField(null=True)
    mapper_id = IntegerField()
    modify_date = DateTimeField(null=True)
    writer = CharField(max_length=255)

    class Meta:
        db_table = 'writer'

