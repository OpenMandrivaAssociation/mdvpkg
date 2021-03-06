%define mandriva_datadir %{_datadir}/mandriva
%define mandriva_docdir %{_datadir}/doc/mandriva

Summary:	Mandriva D-Bus packaging abstraction layer
Name:		mdvpkg
Version:	0.8.1
Release:	9
License:	GPLv2
Group:		Development/Python
Url:		https://github.com/downloads/jvdm/mdvpkg/%{name}-%{version}.tar.bz2
Source0:	%{name}-%{version}.tar.bz2
BuildArch:	noarch
Requires:	python2
Requires:	python-dbus
Requires:	python-pyinotify
Requires:	python-rpm

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
%__python2 setup.py install --root=%{buildroot}
rm -f %{buildroot}%{mandriva_datadir}/%{name}/%{name}-%{version}-py*.egg-info

%files
%{_sbindir}/mdvpkgd
%{mandriva_datadir}/%{name}
%{_sysconfdir}/dbus-1/system.d/org.mandrivalinux.MdvPkg.conf
%{_datadir}/dbus-1/system-services/org.mandrivalinux.MdvPkg.service
%{_datadir}/polkit-1/actions/org.mandrivalinux.mdvpkg.policy
%doc doc/* README TODO

