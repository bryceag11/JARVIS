# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.27

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:

# Disable VCS-based implicit rules.
% : %,v

# Disable VCS-based implicit rules.
% : RCS/%

# Disable VCS-based implicit rules.
% : RCS/%,v

# Disable VCS-based implicit rules.
% : SCCS/s.%

# Disable VCS-based implicit rules.
% : s.%

.SUFFIXES: .hpux_make_needs_suffix_list

# Command-line flag to silence nested $(MAKE).
$(VERBOSE)MAKESILENT = -s

#Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/local/lib/python3.9/dist-packages/cmake/data/bin/cmake

# The command to remove a file.
RM = /usr/local/lib/python3.9/dist-packages/cmake/data/bin/cmake -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /mnt/c/JARVIS/ydlidar

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /mnt/c/JARVIS/ydlidar/build

# Include any dependencies generated for this target.
include samples/CMakeFiles/tof_test.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include samples/CMakeFiles/tof_test.dir/compiler_depend.make

# Include the progress variables for this target.
include samples/CMakeFiles/tof_test.dir/progress.make

# Include the compile flags for this target's objects.
include samples/CMakeFiles/tof_test.dir/flags.make

samples/CMakeFiles/tof_test.dir/tof_test.cpp.o: samples/CMakeFiles/tof_test.dir/flags.make
samples/CMakeFiles/tof_test.dir/tof_test.cpp.o: /mnt/c/JARVIS/ydlidar/samples/tof_test.cpp
samples/CMakeFiles/tof_test.dir/tof_test.cpp.o: samples/CMakeFiles/tof_test.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green --progress-dir=/mnt/c/JARVIS/ydlidar/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object samples/CMakeFiles/tof_test.dir/tof_test.cpp.o"
	cd /mnt/c/JARVIS/ydlidar/build/samples && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT samples/CMakeFiles/tof_test.dir/tof_test.cpp.o -MF CMakeFiles/tof_test.dir/tof_test.cpp.o.d -o CMakeFiles/tof_test.dir/tof_test.cpp.o -c /mnt/c/JARVIS/ydlidar/samples/tof_test.cpp

samples/CMakeFiles/tof_test.dir/tof_test.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green "Preprocessing CXX source to CMakeFiles/tof_test.dir/tof_test.cpp.i"
	cd /mnt/c/JARVIS/ydlidar/build/samples && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /mnt/c/JARVIS/ydlidar/samples/tof_test.cpp > CMakeFiles/tof_test.dir/tof_test.cpp.i

samples/CMakeFiles/tof_test.dir/tof_test.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green "Compiling CXX source to assembly CMakeFiles/tof_test.dir/tof_test.cpp.s"
	cd /mnt/c/JARVIS/ydlidar/build/samples && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /mnt/c/JARVIS/ydlidar/samples/tof_test.cpp -o CMakeFiles/tof_test.dir/tof_test.cpp.s

# Object files for target tof_test
tof_test_OBJECTS = \
"CMakeFiles/tof_test.dir/tof_test.cpp.o"

# External object files for target tof_test
tof_test_EXTERNAL_OBJECTS =

tof_test: samples/CMakeFiles/tof_test.dir/tof_test.cpp.o
tof_test: samples/CMakeFiles/tof_test.dir/build.make
tof_test: libydlidar_sdk.a
tof_test: samples/CMakeFiles/tof_test.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green --bold --progress-dir=/mnt/c/JARVIS/ydlidar/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable ../tof_test"
	cd /mnt/c/JARVIS/ydlidar/build/samples && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/tof_test.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
samples/CMakeFiles/tof_test.dir/build: tof_test
.PHONY : samples/CMakeFiles/tof_test.dir/build

samples/CMakeFiles/tof_test.dir/clean:
	cd /mnt/c/JARVIS/ydlidar/build/samples && $(CMAKE_COMMAND) -P CMakeFiles/tof_test.dir/cmake_clean.cmake
.PHONY : samples/CMakeFiles/tof_test.dir/clean

samples/CMakeFiles/tof_test.dir/depend:
	cd /mnt/c/JARVIS/ydlidar/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /mnt/c/JARVIS/ydlidar /mnt/c/JARVIS/ydlidar/samples /mnt/c/JARVIS/ydlidar/build /mnt/c/JARVIS/ydlidar/build/samples /mnt/c/JARVIS/ydlidar/build/samples/CMakeFiles/tof_test.dir/DependInfo.cmake "--color=$(COLOR)"
.PHONY : samples/CMakeFiles/tof_test.dir/depend

