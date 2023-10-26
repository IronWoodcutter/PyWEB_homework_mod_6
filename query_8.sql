--8 Знайти середній бал, який ставить певний викладач зі своїх предметів.
SELECT ROUND(AVG(g.grade), 2) AS average_grade, t.fullname, d.name
FROM grades g
JOIN disciplines d ON d.id = g.discipline_id
JOIN teachers t ON t.id = d.teacher_id
WHERE t.id = 4
GROUP BY d.name;