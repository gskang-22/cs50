-- Keep a log of any SQL queries you execute as you solve the mystery.

-- took place on July 28, 2021 and that it took place on Humphrey Street.
--

--finding who the thief is
SELECT description
FROM crime_scene_reports
WHERE month = 7 AND day = 28 AND street = "Chamberlin Street";