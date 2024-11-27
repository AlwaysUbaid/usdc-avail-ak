-- Query to calculate total sell volume (AVAIL → USDC)
SELECT
    SUM(amount_out) AS total_sell_volume
FROM uniswap_v3.swaps
WHERE pool_address = LOWER('0xE71F731C2b76B145354A2BD9e8216F7B0e40D555')
  AND token_out = LOWER('0xA0b86991c6218b36c1d19d4a2e9eb0ce3606eb48');
