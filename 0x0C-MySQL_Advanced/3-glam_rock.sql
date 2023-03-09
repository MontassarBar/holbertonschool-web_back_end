-- script that lists all bands with Glam rock as their main style, ranked by their longevity
-- columns: band_names and lifespan
SELECT band_name, split - formed  as lifespan from metal_bands WHERE style LIKE "%Glam rock%" ORDER BY lifespan DESC