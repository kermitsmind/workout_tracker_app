use WorkoutTrackerDB;
show tables;

select person_id from personal_information pi
	where pi.first_name="Adam" and pi.last_name="Smith" and pi.birth_date="1998-03-12" and phone_number="123456789";
    
select * from mysql.user;