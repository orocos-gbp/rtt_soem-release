Name:           ros-indigo-soem-beckhoff-drivers
Version:        0.1.1
Release:        0%{?dist}
Summary:        ROS soem_beckhoff_drivers package

Group:          Development/Libraries
License:        BSD
URL:            http://wiki.ros.org/soem_master
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-message-runtime
Requires:       ros-indigo-rtt
Requires:       ros-indigo-rtt-roscomm
Requires:       ros-indigo-soem
Requires:       ros-indigo-soem-master
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-message-generation
BuildRequires:  ros-indigo-rtt
BuildRequires:  ros-indigo-rtt-roscomm
BuildRequires:  ros-indigo-soem
BuildRequires:  ros-indigo-soem-master

%description
soem_beckhoff_drivers contains drivers for the ethercat beckhoff modules to work
together with the soem_master package, every module creates the necessary
services, dataports and properties for its own functionality.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Tue Jan 27 2015 Ruben Smits <ruben@intermodalics.eu> - 0.1.1-0
- Autogenerated by Bloom

* Mon Jan 26 2015 Ruben Smits <ruben@intermodalics.eu> - 0.1.0-0
- Autogenerated by Bloom

