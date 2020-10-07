import configparser


# CONFIG
config = configparser.ConfigParser()
config.read('dwh.cfg')

# DROP TABLES

staging_events_table_drop = "DROP TABLE IF EXISTS staging_events"
staging_songs_table_drop = "DROP TABLE IF EXISTS staging_songs"
songplay_table_drop = "DROP TABLE IF EXISTS songplay_table_create"
user_table_drop = "DROP TABLE IF EXISTS user_table_create"
song_table_drop = "DROP TABLE IF EXISTS song_table_create"
artist_table_drop = "DROP TABLE IF EXISTS artist_table_create"
time_table_drop = "DROP TABLE IF EXISTS time_table_create"

# CREATE TABLES

staging_events_table_create= ("""
create table if not exists staging_events(
 artist VARCHAR,
 auth VARCHAR,
 firstName VARCHAR,
 gender CHAR,
 itemInSession INTEGER,
 lastName VARCHAR,
 length VARCHAR,
 level VARCHAR,
 location VARCHAR,  
 method VARCHAR,
 page VARCHAR,
 registration DECIMAL,
 sessionid INTEGER,
 song VARCHAR,
 status INTEGER,
 ts BIGINT ,
 userAgent VARCHAR,
 userId INTEGER
 )
""")

staging_songs_table_create = ("""
create table if not exists staging_songs(
    song_id VARCHAR,
    num_songs INTEGER, 
    title VARCHAR, 
    artist_name VARCHAR,
    artist_latitude DECIMAL,
    year INTEGER,
    duration DECIMAL,
    artist_id VARCHAR,
    artist_longitude DECIMAL,
    artist_location VARCHAR
    )
""")

songplay_table_create = ("""
CREATE TABLE IF NOT EXISTS songplays(
songplay_id INTEGER IDENTITY(0,1) SORTKEY DISTKEY,
start_time TIMESTAMP NOT NULL,
user_id INTEGER NOT NULL,
level VARCHAR NOT NULL,
song_id VARCHAR NOT NULL,
artist_id VARCHAR NOT NULL,
session_id INTEGER NOT NULL,
location VARCHAR NOT NULL,
user_agent VARCHAR NOT NULL
)
""")

user_table_create = ("""
CREATE TABLE IF NOT exists USERS(
user_id INTEGER IDENTITY(0,1) SORTKEY DISTKEY,
first_name VARCHAR NOT NULL,
last_name VARCHAR NOT NULL,
gender VARCHAR,
level VARCHAR
)
""")

song_table_create = ("""
CREATE TABLE IF NOT EXISTS SONGS(
song_id INTEGER IDENTITY(0,1) SORTKEY DISTKEY,
title VARCHAR,
artist_id VARCHAR,
year INTEGER,
duration DECIMAL
)
""")

artist_table_create = ("""
CREATE TABLE IF NOT EXISTS ARTISTS(
artist_id INTEGER IDENTITY(0,1) SORTKEY DISTKEY, 
name VARCHAR,
location VARCHAR,
lattitude DECIMAL,
longitude DECIMAL
)
""")

time_table_create = ("""
CREATE TABLE IF NOT EXISTS TIMES(
start_time TIMESTAMP SORTKEY,
hour INTEGER,
day INTEGER,
week INTEGER,
month INTEGER,
year INTEGER,
weekday BOOLEAN
)
""")

# STAGING TABLES

staging_events_copy = f"""copy staging_events from {config.get("S3","LOG_DATA")}
iam_role {config.get("IAM_ROLE","ARN")}
format as json {config.get("S3","LOG_JSONPATH")} region 'us-west-2'; """

staging_songs_copy = f"""copy staging_songs from {config.get("S3","SONG_DATA")}
iam_role {config.get("IAM_ROLE","ARN")}
format as json 'auto' region 'us-west-2'; """


# FINAL TABLES

songplay_table_insert = ("""
""")

user_table_insert = ("""
""")

song_table_insert = ("""
""")

artist_table_insert = ("""
""")

time_table_insert = ("""
""")

# QUERY LISTS

create_table_queries = [staging_events_table_create, staging_songs_table_create, songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [staging_events_table_drop, staging_songs_table_drop, songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]
copy_table_queries = [staging_events_copy, staging_songs_copy]
insert_table_queries = [songplay_table_insert, user_table_insert, song_table_insert, artist_table_insert, time_table_insert]
