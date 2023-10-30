# CMake generated Testfile for 
# Source directory: /mnt/c/JARVIS/ydlidar/python
# Build directory: /mnt/c/JARVIS/ydlidar/build/python
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(ydlidar_py_test "/usr/bin/python" "/mnt/c/JARVIS/ydlidar/python/test/pytest.py")
set_tests_properties(ydlidar_py_test PROPERTIES  ENVIRONMENT "PYTHONPATH=:/mnt/c/JARVIS/ydlidar/build/python" _BACKTRACE_TRIPLES "/mnt/c/JARVIS/ydlidar/python/CMakeLists.txt;42;add_test;/mnt/c/JARVIS/ydlidar/python/CMakeLists.txt;0;")
subdirs("examples")
