--5 Знайти які курси читає певний викладач
SELECT d.name,t.fullname
FROM disciplines d
JOIN teachers t ON t.id = d.teacher_id 
WHERE t.id = 4
GROUP BY d.name;