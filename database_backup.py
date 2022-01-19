import os

# os.system("/usr/local/mysql-8.0.27-macos11-arm64/bin/mysqldump --user=super_user --password=super_user_password -p WorkoutTrackerDB > bbb.sql")
# /usr/local/mysql-8.0.27-macos11-arm64/bin/mysqldump -usuper_user -p WorkoutTrackerDB > bbb.sql

os.system("/usr/local/mysql-8.0.27-macos11-arm64/bin/mysql --host=localhost --user=super_user --port=3306 -p WorkoutTrackerDB < bbb.sql")