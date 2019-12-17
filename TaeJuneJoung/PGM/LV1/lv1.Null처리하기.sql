/*
 * [Null값 처리하기]
 * - Oracle: NVL
 * - MsSQL: ISNULL
 * - MySQL: IFNULL, COALESCE
 */

--MySQL
SELECT animal_type, IFNULL(name, 'No name') as name, sex_upon_intake
FROM animal_ins;