-- Query to calculate total buy volume (USDC → AVAIL)
SELECT
    SUM(amount_in) AS total_buy_volume
FROM uniswap_v3.swaps
WHERE pool_address = LOWER('0xE71F731C2b76B145354A2BD9e8216F7B0e40D555')
  AND token_in = LOWER('0xA0b86991c6218b36c1d19d4a2e9eb0ce3606eb48');
