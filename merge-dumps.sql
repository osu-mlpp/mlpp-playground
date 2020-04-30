
INSERT IGNORE INTO osu_random.osu_beatmap_difficulty SELECT * FROM osu_random_03.osu_beatmap_difficulty;
INSERT IGNORE INTO osu_random.osu_beatmap_difficulty SELECT * FROM osu_random_02.osu_beatmap_difficulty;
INSERT IGNORE INTO osu_random.osu_beatmap_difficulty SELECT * FROM osu_random_01.osu_beatmap_difficulty;
INSERT IGNORE INTO osu_random.osu_beatmap_difficulty SELECT * FROM osu_random_12.osu_beatmap_difficulty;
INSERT IGNORE INTO osu_random.osu_beatmap_difficulty SELECT * FROM osu_random_11.osu_beatmap_difficulty;

INSERT IGNORE INTO osu_random.osu_beatmap_difficulty_attribs SELECT * FROM osu_random_03.osu_beatmap_difficulty_attribs;
INSERT IGNORE INTO osu_random.osu_beatmap_difficulty_attribs SELECT * FROM osu_random_02.osu_beatmap_difficulty_attribs;
INSERT IGNORE INTO osu_random.osu_beatmap_difficulty_attribs SELECT * FROM osu_random_01.osu_beatmap_difficulty_attribs;
INSERT IGNORE INTO osu_random.osu_beatmap_difficulty_attribs SELECT * FROM osu_random_12.osu_beatmap_difficulty_attribs;
INSERT IGNORE INTO osu_random.osu_beatmap_difficulty_attribs SELECT * FROM osu_random_11.osu_beatmap_difficulty_attribs;

INSERT IGNORE INTO osu_random.osu_beatmap_failtimes SELECT * FROM osu_random_03.osu_beatmap_failtimes;
INSERT IGNORE INTO osu_random.osu_beatmap_failtimes SELECT * FROM osu_random_02.osu_beatmap_failtimes;
INSERT IGNORE INTO osu_random.osu_beatmap_failtimes SELECT * FROM osu_random_01.osu_beatmap_failtimes;
INSERT IGNORE INTO osu_random.osu_beatmap_failtimes SELECT * FROM osu_random_12.osu_beatmap_failtimes;
INSERT IGNORE INTO osu_random.osu_beatmap_failtimes SELECT * FROM osu_random_11.osu_beatmap_failtimes;

INSERT IGNORE INTO osu_random.osu_beatmaps SELECT * FROM osu_random_03.osu_beatmaps;
INSERT IGNORE INTO osu_random.osu_beatmaps SELECT * FROM osu_random_02.osu_beatmaps;
INSERT IGNORE INTO osu_random.osu_beatmaps SELECT * FROM osu_random_01.osu_beatmaps;
INSERT IGNORE INTO osu_random.osu_beatmaps SELECT * FROM osu_random_12.osu_beatmaps;
-- BPM is not in the dump here :
INSERT IGNORE INTO osu_random.osu_beatmaps SELECT *,NULL FROM osu_random_11.osu_beatmaps;

INSERT IGNORE INTO osu_random.osu_beatmapsets SELECT * FROM osu_random_03.osu_beatmapsets;
INSERT IGNORE INTO osu_random.osu_beatmapsets SELECT * FROM osu_random_02.osu_beatmapsets;
INSERT IGNORE INTO osu_random.osu_beatmapsets SELECT * FROM osu_random_01.osu_beatmapsets;
INSERT IGNORE INTO osu_random.osu_beatmapsets SELECT * FROM osu_random_12.osu_beatmapsets;
INSERT IGNORE INTO osu_random.osu_beatmapsets SELECT * FROM osu_random_11.osu_beatmapsets;

INSERT IGNORE INTO osu_random.osu_scores_high SELECT * FROM osu_random_03.osu_scores_high;
INSERT IGNORE INTO osu_random.osu_scores_high SELECT * FROM osu_random_02.osu_scores_high;
INSERT IGNORE INTO osu_random.osu_scores_high SELECT * FROM osu_random_01.osu_scores_high;
INSERT IGNORE INTO osu_random.osu_scores_high SELECT * FROM osu_random_12.osu_scores_high;
INSERT IGNORE INTO osu_random.osu_scores_high SELECT * FROM osu_random_11.osu_scores_high;

INSERT IGNORE INTO osu_random.osu_user_beatmap_playcount SELECT * FROM osu_random_03.osu_user_beatmap_playcount;
INSERT IGNORE INTO osu_random.osu_user_beatmap_playcount SELECT * FROM osu_random_02.osu_user_beatmap_playcount;
INSERT IGNORE INTO osu_random.osu_user_beatmap_playcount SELECT * FROM osu_random_01.osu_user_beatmap_playcount;
INSERT IGNORE INTO osu_random.osu_user_beatmap_playcount SELECT * FROM osu_random_12.osu_user_beatmap_playcount;
INSERT IGNORE INTO osu_random.osu_user_beatmap_playcount SELECT * FROM osu_random_11.osu_user_beatmap_playcount;

INSERT IGNORE INTO osu_random.osu_user_stats SELECT * FROM osu_random_03.osu_user_stats;
INSERT IGNORE INTO osu_random.osu_user_stats SELECT * FROM osu_random_02.osu_user_stats;
INSERT IGNORE INTO osu_random.osu_user_stats SELECT * FROM osu_random_01.osu_user_stats;
INSERT IGNORE INTO osu_random.osu_user_stats SELECT * FROM osu_random_12.osu_user_stats;
INSERT IGNORE INTO osu_random.osu_user_stats SELECT * FROM osu_random_11.osu_user_stats;

INSERT IGNORE INTO osu_random.sample_users SELECT * FROM osu_random_03.sample_users;
INSERT IGNORE INTO osu_random.sample_users SELECT * FROM osu_random_02.sample_users;
INSERT IGNORE INTO osu_random.sample_users SELECT * FROM osu_random_01.sample_users;
INSERT IGNORE INTO osu_random.sample_users SELECT * FROM osu_random_12.sample_users;
INSERT IGNORE INTO osu_random.sample_users SELECT * FROM osu_random_11.sample_users;