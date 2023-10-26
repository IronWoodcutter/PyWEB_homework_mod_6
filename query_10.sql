--10 Список курсів, які певному студенту читає певний викладач
SELECT  d.name, s.fullname, t.fullname
FROM grades g
JOIN students s ON s.id = g.student_id 
JOIN disciplines d ON d.id = g.discipline_id
JOIN teachers t ON t.id = d.teacher_id 
WHERE s.id = 28 AND t.id = 4
GROUP BY d.name;