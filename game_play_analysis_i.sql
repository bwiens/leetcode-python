# Benjamin Wiens
# Game Play Analysis I (https://leetcode.com/problems/game-play-analysis-i/)
select player_id, event_date as "first_login" from activity t1 where event_date = (select min(event_date) from activity t2 where t1.player_id = t2.player_id)
