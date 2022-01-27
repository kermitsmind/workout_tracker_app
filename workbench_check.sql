use WorkoutTrackerDB;
show tables;

select person_id from personal_information pi
	where pi.first_name="Adam" and pi.last_name="Smith" and pi.birth_date="1998-03-12" and phone_number="123456789";
    
select * from diet;

flush privileges;

show grants for 'user_1'@'localhost';

select * from running 
	where person_id = 1
    and terrain = 'indoor';
    
select * from personal_information;

select * from running;

update running 
	set `type` = "interval"
    where person_id = 1 and running_id = 3;




