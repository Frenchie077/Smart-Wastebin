import paramiko
import time

def retrieve_file():
    # Connect to the Raspberry Pi via SSH
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname='mypi7', username='grp10', password='7862')
    
    # Open an SFTP session
    sftp_client = ssh_client.open_sftp()
    
    # Download the file
    sftp_client.get('/home/grp10/Documents/image_processing.csv', 'csv/test.csv')
    print("Transfer complete")
    # Close the SFTP and SSH connection
    sftp_client.close()
    ssh_client.close()

while True:
    # Retrieve the file every 5 minutes
    retrieve_file()
    time.sleep(300)  # Sleep for 300 seconds (5 minutes)
