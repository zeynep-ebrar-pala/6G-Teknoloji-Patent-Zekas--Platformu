"""Kuzey Kıbrıs — harita boyası için basitleştirilmiş çokgen (ISO-3166-1 kodu yok)."""

# Yaklaşık kıyı / Yeşil Hat çizgisi; siyasi sınır iddiası değil, görsel doldurma içindir.
KKTC_GEOJSON = {
    "type": "FeatureCollection",
    "features": [
        {
            "type": "Feature",
            "id": "KKTC",
            "properties": {"id": "KKTC", "name": "KKTC"},
            "geometry": {
                "type": "Polygon",
                "coordinates": [
                    [
                        [32.95, 35.17],
                        [32.92, 35.28],
                        [32.96, 35.40],
                        [33.08, 35.41],
                        [33.22, 35.37],
                        [33.36, 35.34],
                        [33.50, 35.35],
                        [33.65, 35.38],
                        [33.80, 35.43],
                        [33.95, 35.48],
                        [34.12, 35.55],
                        [34.28, 35.62],
                        [34.42, 35.67],
                        [34.55, 35.695],
                        [34.58, 35.69],
                        [34.52, 35.62],
                        [34.38, 35.52],
                        [34.22, 35.40],
                        [34.05, 35.28],
                        [33.92, 35.18],
                        [33.78, 35.14],
                        [33.60, 35.145],
                        [33.40, 35.155],
                        [33.20, 35.165],
                        [33.05, 35.17],
                        [32.95, 35.17],
                    ]
                ],
            },
        }
    ],
}
