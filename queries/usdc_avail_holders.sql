-- Query to count unique AVAIL holders
SELECT
    COUNT(DISTINCT holder_address) AS num_holders
FROM ethereum.token_balances
WHERE token_address = LOWER('0xEb4dce6106aebE1a927bF3641F7Cea42685Bd68B');
