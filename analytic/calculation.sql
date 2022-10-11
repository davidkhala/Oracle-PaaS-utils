
RIGHT(CONCAT('0000', CAST(CAST(RAND()*9999 AS int) AS CHAR(10))), 4) -- 4 length random digits
