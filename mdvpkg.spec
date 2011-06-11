%define mandriva_datadir %{_datadir}/mandriva
%define mandriva_docdir %{_datadir}/doc/mandriva

Name:           mdvpkg
Version:        0.6.3
Release:        1

Summary:        Mandriva D-Bus packaging abstraction layer
License:        GPL
Group:          Development/Python
Url:            https://github.com/downloads/jvdm/mdvpkg/%{name}-%{version}.tar.bz2

Source0:        %{name}-%{version}.tar.bz2

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:      noarch

Requires:       python >= 2.7
Requires:       python-dbus
Requires:       python-rpm


%description
mdvpkg is a layer upon mandriva urpmi database to provide
non-privileged users access to package maintenance tasks (upgrade,
installing, searching) through a DBus interface. The following
features are aimed:

* D-Bus interface allowing the creation of specialized clients (like
  an update applet, or end-users application managers)

* Privilege management using PolicyKit

* Support for urpmi input (like dep choices)

* Command line client

* Python QT/QML widgets to manage package tasks

It is inspired on ideas from PackageKit and aptdaemon.


%prep
%setup -q


%build


%install
%__python setup.py install --root=%{buildroot}
rm -f %{buildroot}%{mandriva_datadir}/%{name}/%{name}-%{version}-py*.egg-info


%preun
# Remove any pre-compiled python files in mdvpkg module
find %{mandriva_datadir}/%{name}/mdvpkg -type f \
     -print0 -name '*.pyc' | xargs -0 rm -f


%files
%defattr(-,root,root) 
%{_sbindir}/mdvpkgd
%{mandriva_datadir}/%{name}
%{_sysconfdir}/dbus-1/system.d/org.mandrivalinux.mdvpkg.conf
%{_datadir}/dbus-1/system-services/org.mandrivalinux.mdvpkg.service
%doc doc/* README TODO
