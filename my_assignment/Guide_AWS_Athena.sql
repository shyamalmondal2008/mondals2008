---STEP::1
--- Create table in Athena
CREATE DATABASE assignment_sep_2022;
CREATE EXTERNAL TABLE IF NOT EXISTS playlists (
playlist_id STRING
,name STRING
,followed_by DOUBLE
,acousticness_avg DOUBLE
,acousticness_stdev DOUBLE
,artist_followers_avg DOUBLE
,artist_followers_stdev DOUBLE
,danceability_avg DOUBLE
,danceability_stdev DOUBLE
,duration_ms_avg DOUBLE
,duration_ms_stdev DOUBLE
,energy_avg DOUBLE
,energy_stdev DOUBLE
,instrumentalness_avg DOUBLE
,instrumentalness_stdev DOUBLE
,liveness_avg DOUBLE
,liveness_stdev DOUBLE
,mode_avg DOUBLE
,mode_stdev DOUBLE
,num_unique_artist_first_page DOUBLE
,speechiness_avg DOUBLE
,speechiness_stdev DOUBLE
,tempo_avg DOUBLE
,tempo_stdev DOUBLE
,valence_avg DOUBLE
,valence_stdev DOUBLE
)
ROW FORMAT DELIMITED FIELDS TERMINATED BY '\;'
STORED AS TEXTFILE
LOCATION 's3://assignment-bucket-sep-2022/';

 
 
CREATE EXTERNAL TABLE IF NOT EXISTS playlist_tracks (
playlist_id STRING
,track_id STRING
)
ROW FORMAT DELIMITED FIELDS TERMINATED BY '\;'
STORED AS TEXTFILE
LOCATION 's3://asgn-bucket-playlist-tracks-sep-2022/';


---------STEP::2
--- List of tracks belongs to playlist_id

SELECT a.track_id as track_id 
FROM playlist_tracks a
JOIN playlist_tracks b ON a.track_id=b.playlist_id;
WHERE playlist_id NOT IN ('(1022898 rows)','playlist_id')

--○ Total number of playlists
SELECT COUNT(*) as number_of_playlist
FROM
(SELECT playlist_id
FROM playlist_tracks
WHERE playlist_id NOT IN ('(1022898 rows)','playlist_id')
GROUP BY playlist_id) a;

--○ Total number of unique tracks

SELECT COUNT(*) as number_unique_tracks
FROM
(SELECT track_id 
FROM playlist_tracks
WHERE playlist_id NOT IN ('(1022898 rows)','playlist_id')
GROUP BY track_id) b;


--○ Minimum number of tracks of all playlists
SELECT tracks_count as minunum_tracks_of_all_playlists
FROM
(SELECT playlist_id,COUNT(track_id) AS tracks_count
FROM playlist_tracks
WHERE playlist_id NOT IN ('(1022898 rows)','playlist_id')
GROUP BY playlist_id) c
ORDER BY tracks_count limit 1;

--○ Average number of tracks per playlist

SELECT sum(tracks_count)/count(playlist_id) average_num_of_tracks_per_playlist
FROM
(SELECT playlist_id,COUNT(track_id) AS tracks_count
FROM playlist_tracks
WHERE playlist_id NOT IN ('(1022898 rows)','playlist_id')
GROUP BY playlist_id) d;

--○ Maximum number of tracks of all playlists


SELECT tracks_count as maximum_tracks_of_all_playlists
FROM
(SELECT playlist_id,COUNT(track_id) AS tracks_count
FROM playlist_tracks
WHERE playlist_id NOT IN ('(1022898 rows)','playlist_id')
GROUP BY playlist_id) e
ORDER BY tracks_count DESC limit 1;




----- Select multiple sub-queries data into a single query and create a new table
CREATE TABLE  playlist_tracks_stats
WITH (
format = 'TEXTFILE',
external_location = 's3://assignment-bucket-sep-2022/output/playlist_tracks_stats'
)
AS
SELECT
(SELECT COUNT(*) as number_of_playlist
FROM
(SELECT playlist_id
FROM playlist_tracks
WHERE playlist_id NOT IN ('(1022898 rows)','playlist_id')
GROUP BY playlist_id) a) AS number_of_playlist,
(SELECT COUNT(*) as number_unique_tracks
FROM
(SELECT track_id 
FROM playlist_tracks
WHERE playlist_id NOT IN ('(1022898 rows)','playlist_id')
GROUP BY track_id) b) AS number_unique_tracks,
(SELECT tracks_count as minunum_tracks_of_all_playlists
FROM
(SELECT playlist_id,COUNT(track_id) AS tracks_count
FROM playlist_tracks
WHERE playlist_id NOT IN ('(1022898 rows)','playlist_id')
GROUP BY playlist_id) c
ORDER BY tracks_count limit 1) AS minunum_tracks_of_all_playlists,
(SELECT sum(tracks_count)/count(playlist_id) average_num_of_tracks_per_playlist
FROM
(SELECT playlist_id,COUNT(track_id) AS tracks_count
FROM playlist_tracks
WHERE playlist_id NOT IN ('(1022898 rows)','playlist_id')
GROUP BY playlist_id) d) AS average_num_of_tracks_per_playlist,
(SELECT tracks_count as maximum_tracks_of_all_playlists
FROM
(SELECT playlist_id,COUNT(track_id) AS tracks_count
FROM playlist_tracks
WHERE playlist_id NOT IN ('(1022898 rows)','playlist_id')
GROUP BY playlist_id) e
ORDER BY tracks_count DESC limit 1) AS maximum_tracks_of_all_playlists
;



-------------------------matching playlist_ids-----------------

SELECT a.playlist_id AS playlist_id
FROM playlist_tracks a
INNER JOIN playlists b
ON a.playlist_id = b.playlist_id;

