
# System Design chess.com

## features required
1. personal ranking

2. 5 above and below

3. leaderboard
    - sign ups, wins and loses. redundant
    - only wins are important. consider this a score only.
    - scores table with user_id and score
    - but if you beat Magnus you will move up very high.
    - ranking table not required. can be calculated from the scores itself.
    - current scehma only has player and their scores.

4. friends also 3 above and below.


## how if 100,000 updates happen because of simultaneous scores
    - fan out problem. uses kafka to update the scores with event bus.

## how to scale this for many users
    - scores table can be sharded.
    - scores are bell curve. most people in the mid.
    - can shard based on range of scores.
    - shard key will be score ranges.

## implement privacy feature
    - user can enable privacy so that your score and ranking is not visible in the leaderboard.
    - user table has a bool for privacy. On get ranking and get scores dont show.
