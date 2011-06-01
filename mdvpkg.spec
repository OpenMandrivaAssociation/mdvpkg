%define mandriva_datadir %{_datadir}/mandriva
%define mandriva_docdir %{_datadir}/doc/mandriva
%define mandriva_libdir %{_libdir}/mandriva

Name:           mdvpkg
Version:        0.5.4
Release:        0

Summary:        Mandriva D-Bus packaging abstraction layer
License:        GPL
Group:          Development/Python
Url:            http://gitorious.org/%{name}

Source0:        %{name}-%{version}.tar.bz2

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot

BuildRequires:	libpython-devel
BuildRequires:	librpm-devel
Requires:       python >= 2.7
Requires:       python-dbus


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

It's inspired on ideas from PackageKit and aptdaemon.


%prep
%setup -q


%build
make build


%install
make install ROOT=%{buildroot}


%clean
rm -rf %{buildroot}


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
%{mandriva_libdir}/%{name}
%doc %{mandriva_docdir}/%{name}
