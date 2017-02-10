Name: python-netifaces
Version: 0.10.5
Release: 1%{?dist}
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
mkdir -p %{buildroot}/%{python2_sitearch}/
strip build/lib.*/netifaces.so
install -m755 build/lib.*/netifaces.so %{buildroot}/%{python2_sitearch}/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{python2_sitearch}/netifaces.so

%changelog
* Fri Dec 23 2016 Michal Gawlik <michal.gawlik@thalesgroup.com> 0.10.5-1
- new package built with tito

