# Automated-EMails


Both of these scripts are being run on PythonAnywhere to allow for easier automation.

The Email will connect to a DB and extract data from 5 specific fields then take those VALUES and put them into a formatted message which I use to email my superiors daily at 1500.

The Copy will take the data from the initial Database and move it to a "storage" database and truncate the original Database so that we only have the current day's unlocks and not any past. This occurs at 1515
