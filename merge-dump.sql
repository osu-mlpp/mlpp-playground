
CREATE TABLE user_filter(user_id int(11) UNSIGNED PRIMARY KEY NOT NULL);
INSERT INTO user_filter SELECT user_id FROM osu_user_stats WHERE rank_score!=0;

INSERT IGNORE INTO osu_random.osu_beatmap_difficulty SELECT * FROM osu_beatmap_difficulty;

INSERT IGNORE INTO osu_random.osu_beatmap_difficulty_attribs SELECT * FROM osu_beatmap_difficulty_attribs;

INSERT IGNORE INTO osu_random.osu_beatmap_failtimes SELECT * FROM osu_beatmap_failtimes;

INSERT IGNORE INTO osu_random.osu_beatmaps SELECT * FROM osu_beatmaps;
-- if BPM is not in the dump :
-- INSERT IGNORE INTO osu_random.osu_beatmaps SELECT *,NULL FROM osu_beatmaps;

INSERT IGNORE INTO osu_random.osu_beatmapsets SELECT * FROM osu_beatmapsets;

INSERT IGNORE INTO osu_random.osu_scores_high SELECT A.* FROM osu_scores_high as A WHERE EXISTS (SELECT * FROM user_filter AS B WHERE A.user_id=B.user_id);

INSERT IGNORE INTO osu_random.osu_user_beatmap_playcount SELECT A.* FROM osu_user_beatmap_playcount as A WHERE EXISTS (SELECT * FROM user_filter AS B WHERE A.user_id=B.user_id);

INSERT IGNORE INTO osu_random.osu_user_stats SELECT A.* FROM osu_user_stats as A WHERE EXISTS (SELECT * FROM user_filter AS B WHERE A.user_id=B.user_id);

INSERT IGNORE INTO osu_random.sample_users SELECT A.* FROM sample_users as A WHERE EXISTS (SELECT * FROM user_filter AS B WHERE A.user_id=B.user_id);