from pypsexec.client import Client

# creates an encrypted connection to the host with the username and password
c = Client("WIN-4IQVP46MK5R", username="india", password="abc",encrypt=False)

# set encrypt=False for Windows 7, Server 2008
#c = Client("WIN-4IQVP46MK5R", username="india", password="abc", encrypt=False)

# if Kerberos is available, this will use the default credentials in the
# credential cache
#c = Client("hostname")

# you can also tell it to use a specific Kerberos principal in the cache
# without a password
#c = Client("hostname", username="username@DOMAIN.LOCAL")

c.connect()
try:
    c.create_service()

    # After creating the service, you can run multiple exe's without
    # reconnecting

    # run a simple cmd.exe program with arguments
    stdout, stderr, rc = c.run_executable("cmd.exe",arguments="/c echo Hello World")

    # run whoami.exe as the SYSTEM account
   # stdout, stderr, rc = c.run_executable("whoami.exe", use_system_account=True)

    # run command asynchronously (in background), the rc is the PID of the spawned service
   # stdout, stderr, rc = c.run_executable("longrunning.exe",
    #                                      arguments="/s other args",
     #                                     asynchronous=True)

    # run whoami.exe as a specific user
    #stdout, stderr, rc = c.run_executable("whoami",
     #                                     arguments="/all",
      #                                    username="india",
       #                                   password="abc",
        #                                  run_elevated=True)
finally:
    c.remove_service()
    c.disconnect()