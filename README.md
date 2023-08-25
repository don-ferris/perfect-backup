# perfect-backup
Perfect Backup is a Python backup script that runs on a semi-air-gapped backup server. It's designed to be immune to ransomware by creating verified, immutable backups of specified directories on remote machines, storing the bsackup and key files on removable drives.

backup.py
Original backup script written to run locally with the option to specify ____ as command arguments.

verify.py
Original script created to verify the backup (created by backup.py) by extracting all files to /tmp and comparing them with the source files.

perfectbackup.py
Runs as a cron job on a remote backup server. After creating and verifying the backup file, the script makes the file immutable (using a key file) then writes the backup file, key file, and log file to an external/flash drive.

pseudocode
Using a cron job, wake up the (semi-air gapped) backup server and connect to the network
	1. Generate a fictitious password and a random 6 digit number
	2. Output the password to password.[current timestamp].[random number] (timestamp is the actual password to be used)
	3. Create a backup of the remote machine - encrypted & compressed tar file using the password (timestamp) generated in the previous step
	4. Verify the backup file using my python program (generates a log file with success/failure status)
	5. Create a key file - timestamp + random number + generated lorem ipsum text - to text file and named [(sum of) timestamp + previously generated random number].key
	6. Use the key file to encrypt the backup file (making it immutable without the key file)
	7. Copy the backup file and key file to a flash/external drive along with (if necessary?) a text file containing any additional information that might be useful
	8. Confirm that the backup and key files on the flash drive are identical to the source file (write results to the log file)
	9. Eject the flash drive
	10. Repeat steps 7-9 for a second USB drive
	11. Securely delete the backup file, key file, and temp directory used by the backup verification (python) script - but not the log file
	12. Disconnect backup server from the network
	13. Power off backup server
	14. Remove the flash/external drives - take one off-site
	15. Power the backup server back up (cron job is initialized) and put it to sleep
