DELETE FROM osu_scores_high WHERE hidden!=0;

-- Saving the id of the scores we delete :
CREATE TABLE duplicate_scores(score_id int(9) PRIMARY KEY NOT NULL);
INSERT INTO duplicate_scores SELECT A.score_id FROM osu_scores_high as A WHERE EXISTS (
    SELECT * FROM osu_scores_high AS B WHERE (
        A.score_id!=B.score_id AND A.beatmap_id=B.beatmap_id AND A.enabled_mods=B.enabled_mods AND A.user_id=B.user_id
    ) AND (
        A.score<B.score OR (A.score=B.score AND A.score_id<B.score_id)
    )
);
-- Deleting the score
DELETE FROM osu_scores_high WHERE score_id IN (SELECT * FROM duplicate_scores);

-- Alternative :
-- DELETE FROM osu_scores_high WHERE score_id IN (
--     SELECT A.score_id FROM (select * from osu_scores_high) as A WHERE EXISTS (
--         SELECT * FROM (select * from osu_scores_high) as B WHERE (
--             A.score_id!=B.score_id AND A.beatmap_id=B.beatmap_id AND A.enabled_mods=B.enabled_mods AND A.user_id=B.user_id
--         ) AND (
--             A.score<B.score OR (A.score=B.score AND A.score_id<B.score_id))
--     )
-- );