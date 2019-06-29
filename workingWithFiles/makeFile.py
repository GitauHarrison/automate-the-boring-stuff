import os
path = '/tmp/year/month/week/day'

access_path = 0o755

try:
    os.makedirs(path, access_path)
except OSError:
    print("Creation of the directory %s failed." % path )
else:
    print('Successfully created the directory %s ' % path)
