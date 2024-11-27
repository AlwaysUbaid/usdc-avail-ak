-- Query to calculate daily volume for the USDC/AVAIL pair
SELECT
    DATE(block_time) AS day,
    SUM(CASE 
        WHEN token_in = LOWER('0xA0b86991c6218b36c1d19d4a2e9eb0ce3606eb48') THEN amount_in
        ELSE amount_out
    END) AS daily_volume
FROM uniswap_v3.swaps
WHERE pool_address = LOWER('0xE71F731C2b76B145354A2BD9e8216F7B0e40D555')
GROUP BY day
ORDER BY day DESC;
