# cracking the coding interview
# chapter 14 databases

# interview questions

# 14.1 multiple apartments
# write a sql query to get a list of tenants who are renting more than one apartment
"""
SELECT TenantName
FROM Tenants
INNER JOIN
    (SELECT TenantID FROM AptTenants GROUP BY TenantID HAVING count(*) > 1) C
ON Tenants.TenantID = C.TenantID
"""

# 14.2 open requests
# write a sql query to get a list of all buildings and the number of open requests (requests in which status equals open)
"""
SELECT BuildName, ISNULL(Count, 0) as 'Count'
FROM Buildings
LEFT JOIN
    (SELECT Apartments.BuildingID, count(*) as 'Count'
    FROM Requests INNER JOIN Apartments
    ON Requests.AptID = Apartments.AptID
    WHERE Requests.Status = 'Open'
    GROUP BY Apartments.BuildingID) ReqCounts
ON ReqCounts.BuildingID = Buildings.BuildingID
"""

# 14.3 close all requests
# building #11 is undergoing major renovation. implement a query to close all requests from apartments in this bulding
"""
UPDATE Requests
SET Status = 'Closed'
WHERE AptID in (SELECT AptID FROM Apartments WHERE Building = 11)
"""

# 14.4 joins
# what are the different types of joins? please explain how they differ and why certain types are better in certain situations
"""
Joins combine two tables that have at least 1 matching field
Inner joins only show the records that have a matching field in both tables
Outer joins show all the records of the inner joins plus those that have no matching records
    there are 3 subtypes
        left outer join aka left join
            contains all the records from the left tables and shows NULL where there are no matching records
        right outer join aka right join
            contains all the records from the right tables and shows NULL where there are no matching records
        full outer join
            basically the combination of left and right joins, shows all the records and where there is no matching
            in the left or right it shows NULL
"""

# 14.5 denormalization
# what is denormalization? explain the pros and cons
"""
denormalization is a way to optimize databases by adding redundant data
normalized data makes separate tables to decrease redundant data

cons
    updates and inserts are more expensive
    update and insert code is not as neet
    because of repetiton, data may be inconsistent
    redundancy means you need more storage

pros
    retrieving data is faster because there are fewer joins
    queries to retrieve have simpler code
"""

# 14.6 entity relationship diagram
# draw an erd for a database with companies, people, and professionals (people who work for companies)
"""
see solution book page 445
"""