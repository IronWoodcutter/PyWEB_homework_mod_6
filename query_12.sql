--12 Оцінки студентів у певній групі з певного предмета на останньому занятті
SELECT g.grade, s.fullname, gr.name, d.name, g.date_of  
FROM grades g 
JOIN students s ON s.id = g.student_id
JOIN disciplines d ON d.id = g.discipline_id 
JOIN [groups] gr ON gr.id = s.group_id 
WHERE d.id = 4 AND s.group_id = 3 AND g.date_of = (
	SELECT MAX(grades.date_of)
	FROM grades
	WHERE grades.discipline_id = d.id)
ORDER BY g.grade DESC;