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

"""