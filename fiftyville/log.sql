-- Keep a log of any SQL queries you execute as you solve the mystery.

-- took place on July 28, 2021 and that it took place on Humphrey Street.
--

--finding who the thief is
SELECT description
FROM crime_scene_reports
WHERE year = 2021 AND month = 7 AND day = 28 AND street = "Humphrey Street";

SELECT transcript
FROM interviews
WHERE year = 2021 AND month = 7 AND day = 28 AND transcript LIKE "%bakery%";

SELECT people.name, bakery_security_logs.license_plate, bakery_security_logs.activity
FROM bakery_security_logs
JOIN people ON bakery_security_logs.license_plate = people.license_plate
WHERE year = 2021 AND month = 7 AND day = 28 AND hour = 10 AND (minute >= 15 AND minute <= 25);