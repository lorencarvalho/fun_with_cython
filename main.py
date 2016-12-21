import pyximport
pyximport.install()

import time
import factorial


cy_start = time.time()
factorial.bench_cy()
cy_end = time.time()

print "Cython: %sms" % ((cy_end - cy_start) * 1000)


py_start = time.time()
factorial.bench_py()
py_end = time.time()

print "Python: %sms" % ((py_end - py_start) * 1000)


print "Speed-up: %s" % ((py_end - py_start) / (cy_end - cy_start))
