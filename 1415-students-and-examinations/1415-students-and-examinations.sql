# Write your MySQL query statement below
select st.student_id,
st.student_name,
su.subject_name,
count(e.student_id) as attended_exams
from students st
join subjects su
left join examinations e on e.student_id = st.student_id and su.subject_name = e.subject_name
group by st.student_id, su.subject_name, st.student_name
order by st.student_id, su.subject_name;