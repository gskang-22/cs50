-- Keep a log of any SQL queries you execute as you solve the mystery.
-- took place on July 28, 2021 and that it took place on Humphrey Street.

--case description
SELECT description
FROM crime_scene_reports
WHERE year = 2021 AND month = 7 AND day = 28 AND street = "Humphrey Street";
--getting transcript of witnesses
SELECT transcript
FROM interviews
WHERE year = 2021 AND month = 7 AND day = 28 AND transcript LIKE "%bakery%";
--witness1
SELECT people.name, bakery_security_logs.license_plate, bakery_security_logs.activity
FROM bakery_security_logs
JOIN people ON bakery_security_logs.license_plate = people.license_plate
WHERE bakery_security_logs.year = 2021
AND bakery_security_logs.month = 7
AND bakery_security_logs.day = 28
AND bakery_security_logs.hour = 10
AND (bakery_security_logs.minute >= 15 AND bakery_security_logs.minute <= 25);
--witness2
SELECT people.name
FROM people
JOIN bank_accounts ON bank_accounts.person_id = people.id
JOIN atm_transactions ON atm_transactions.account_number = bank_accounts.account_number
WHERE atm_transactions.year = 2021
AND atm_transactions.month = 7
AND atm_transactions.day = 28
AND atm_transactions.atm_location = "Leggett Street"
AND atm_transactions.transaction_type = "withdraw";
--witness3
SELECT caller, receiver
FROM phone_calls
WHERE year = 2021 AND month = 7 AND day = 28
AND duration < 60;
--flight
SELECT city
FROM airports
JOIN flights ON flights.destination_airport_id = airports.id
WHERE flights.year = 2021 AND flights.month = 7 AND flights.day = 29
AND flights.origin_airport_id =
(SELECT id FROM airports WHERE city = "Fiftyville")
ORDER BY hour ASC, minute ASC
LIMIT 1;
--collate
SELECT name from 