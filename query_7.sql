--7 Знайти оцінки студентів у окремій групі з певного предмета
SELECT g.grade, s.fullname, gr.name, d.name 
FROM students s 
JOIN grades g ON s.id = g.student_id
JOIN disciplines d ON d.id = g.discipline_id 
JOIN [groups] gr ON gr.id = s.group_id 
WHERE d.id = 4 AND gr.id = 3
ORDER BY s.fullname;