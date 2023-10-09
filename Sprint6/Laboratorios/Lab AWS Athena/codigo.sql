WITH RankedData AS (
  SELECT
    nome,
    SUM(total) AS totalDec,
    (ano/10)*10 AS decada,
    DENSE_RANK() OVER (PARTITION BY (ano/10)*10 ORDER BY SUM(total) DESC) AS posicao
  FROM dados
  WHERE ano >= 1950 AND ano <= 2029
  GROUP BY nome, (ano/10)*10
)

SELECT nome, totalDec, decada, posicao
FROM RankedData
WHERE posicao <= 3
ORDER BY decada, posicao, totalDec DESC;
