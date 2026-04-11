WITH
days as (
  select generate_series(date_trunc('day',date '2025-03-27') , now(), '1 day') as "date"
  ORDER BY "date"
),
running as (
SELECT
            MIN("timestamp"::date) as "date",
            SUM("distance")/1000 as "total_kilometers",
            SUM("duration")/60 as "total_minutes",
					  MIN("elevation") as "elevation_min",
					  MAX("elevation") as "elevation_max"
            FROM public_running_coordinates
            WHERE "timestamp">='2025-03-27'
            GROUP BY "timestamp"::date
            ORDER BY date DESC
  ),
running_elevation as (
  	SELECT
  	"timestamp",
		("elevation" - lag("elevation") over (order by "timestamp", "run_id")),
    case when ("elevation" - lag("elevation") over (order by "timestamp", "run_id")) >= 0 then ("elevation" - lag("elevation") over (order by "timestamp", "run_id")) end as "positive",
    case when ("elevation" - lag("elevation") over (order by "timestamp", "run_id")) < 0 then ("elevation" - lag("elevation") over (order by "timestamp", "run_id")) end as "negative"
		FROM public_running_coordinates
  ),
  elev as (
  	SELECT
    MIN("timestamp"::date) as "date",
   	SUM("positive") as "elevation_gain",
    SUM("negative") as "elevation_loss"
    from running_elevation
    GROUP BY "timestamp"::date
    )

 SELECT
 days."date",
 coalesce(running."total_kilometers",0) as "distance [ km ]",
 coalesce(running."total_minutes",0)/60 as "duration [ hours ]",
 elev."elevation_gain"/1000 as "elevation_gain [ km ]",
 elev."elevation_loss"/1000 as "elevation_loss [ km ]"
 /*--CASE WHEN (coalesce(running."total_kilometers",0) > 0 THEN (elev."elevation_gain"/1000) / (coalesce(running."total_kilometers",0)) ELSE 0 END as "elevation [ %% of run ]"
 --(elev."elevation_gain"/1000) / (coalesce(running."total_kilometers",0)) as "elevation [ %% of run ]"
 */
 FROM days
 LEFT JOIN running ON days."date" = running."date"
 LEFT JOIN elev ON days."date" = elev."date"
 --WHERE coalesce(running."total_kilometers",0) > 0
 ORDER BY days."date"

