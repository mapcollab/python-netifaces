Name: python-netifaces
Version: 0.10.5
Release: 1
Packager: builder
Summary: Portable network interface information.
License: MIT License
Group: Libraries/Net
URL: https://pypi.python.org/pypi/netifaces
Source0: %{name}-%{version}.tar.gz
BuildRequires: python-devel
Requires: python
BuildRoot: %{_tmppath}/%{name}-%{version}-root

AutoReqProv: no
%define debug_package %{nil}
%define __os_install_post %{nil}

%description
This module implements network interface information.

%prep
%setup -q -n %{name}-%{version}

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
export PYTHONPATH=$RPM_BUILD_ROOT/usr/lib64/python2.7/site-packages/
mkdir -p $PYTHONPATH
%{__python} setup.py install \
    --prefix=$RPM_BUILD_ROOT/usr \
    --record=filelist-%{name}-%{version}-%{release}-temp

cat filelist-%{name}-%{version}-%{release}-temp | \
    sed -e "s;^$RPM_BUILD_ROOT;;" | \
    grep -v "doc/" | \
    grep -v "bin/" \
    > filelist-%{name}-%{version}-%{release}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f filelist-%{name}-%{version}-%{release}
%defattr(-,root,root)
%{_libdir}/python2.7/site-packages/*

%changelog
