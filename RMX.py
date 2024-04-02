import os,platform
os.system("git pull")
rmx = platform.architecture()[0]
if rmx=='64bit':
  import Fbb
elif rmx=='32bit':
  import Fbb32
