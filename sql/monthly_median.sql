WITH monthly_data AS (
    SELECT DATE_TRUNC('month', created_at) AS month,
        price,
        LAG(price) OVER (
            PARTITION BY DATE_TRUNC('month', created_at)
            ORDER BY created_at
        ) AS prev_month_price,
        LEAD(price) OVER (
            PARTITION BY DATE_TRUNC('month', created_at)
            ORDER BY created_at
        ) AS next_month_price
    FROM fixed
)
SELECT month,
    percentile_cont(0.5) WITHIN GROUP (
        ORDER BY price
    ) AS monthly_median
FROM monthly_data
WHERE prev_month_price IS NOT NULL
    AND next_month_price IS NOT NULL
GROUP BY month
ORDER BY month;