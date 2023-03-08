-- script that ranks country origins of bands, ordered by the number of (non-unique) fans
-- columns: origin and nb_fans
SELECT origins, SUM(fans) AS nb_fans from metal_bands GROUP BY origins ORDER BY nb_fans DESC