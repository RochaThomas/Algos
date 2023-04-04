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