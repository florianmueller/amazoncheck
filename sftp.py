import pysftp

##ftp credentials:
myHostname = "your ftp server ip"
myUsername = "your ftp user"
myPassword = "your ftp pass"

with pysftp.Connection(host=myHostname, username=myUsername, password=myPassword) as sftp:
    print ("Connection succesfully stablished ... ")

    # Define the file that you want to upload from your local directorty
    # or absolute "C:\Users\sdkca\Desktop\TUTORIAL2.txt"
    localFilePath = './availability.log'

    # Define the remote path where the file will be uploaded
    remoteFilePath = '/availability.log'

    sftp.put(localFilePath, remoteFilePath)

# connection closed automatically at the end of the with-block
