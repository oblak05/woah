import os,platform
rmx = platform.architecture()[0]
if rmx=='64bit':
    import Fbb
elif rmx=='32bit':
    import Fbb32
