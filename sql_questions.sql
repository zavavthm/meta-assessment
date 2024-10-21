-- Approach:
-- I'll get the rank for image_id by score in both desc and asc order
-- then I'll individual select every 3rd row/image for both desc and asc columns. (i.e. 1st, 4th, 7th... till 10,000 rank)
-- then I'll perform a UNION ALL on all the both the CTEs. 
-- Final table will have 20K records. As the total were 1 Million, so there won't be any duplicates even if we do UNION.
-- Decided to go with UNION ALL as it won't check for duplicates and will be faster in appending and getting the final result.

WITH ranked_images AS (
    -- Rank images in descending order of score
    SELECT image_id,
           ROW_NUMBER() OVER (ORDER BY score DESC) AS posititve_rank,
           ROW_NUMBER() OVER (ORDER BY score ASC) AS negative_rank
    FROM images
),
positive_samples AS (
    -- Select every 3rd image in descending score order for positive samples
    SELECT image_id, 1 AS weak_label
    FROM ranked_images
    WHERE pos_rank % 3 = 1
    ORDER BY score DESC
    LIMIT 10000
),
negative_samples AS (
    -- Select every 3rd image in ascending score order for negative samples
    SELECT image_id, 0 AS weak_label
    FROM ranked_images
    WHERE neg_rank % 3 = 1
    ORDER BY score ASC
    LIMIT 10000
)
-- Combine both positive and negative samples and order by image_id
SELECT image_id, weak_label
FROM positive_samples
UNION ALL
SELECT image_id, weak_label
FROM negative_samples
ORDER BY image_id;