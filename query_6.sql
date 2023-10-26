--6 Знайти список студентів у певній групі
SELECT s.fullname, g.name
FROM students s 
JOIN [groups] g ON g.id = s.group_id 
WHERE g.id = 3
GROUP BY s.fullname;