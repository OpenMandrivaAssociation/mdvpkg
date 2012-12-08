%define mandriva_datadir %{_datadir}/mandriva
%define mandriva_docdir %{_datadir}/doc/mandriva

Name:           mdvpkg
Version:        0.8.1
Release:        0

Summary:        Mandriva D-Bus packaging abstraction layer
License:        GPL
Group:          Development/Python
Url:            https://github.com/downloads/jvdm/mdvpkg/%{name}-%{version}.tar.bz2

Source0:        %{name}-%{version}.tar.bz2

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:      noarch

Requires:       python >= 2.7
Requires:       python-dbus
Requires:       python-pyinotify
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


%files
%defattr(-,root,root) 
%{_sbindir}/mdvpkgd
%{mandriva_datadir}/%{name}
%{_sysconfdir}/dbus-1/system.d/org.mandrivalinux.MdvPkg.conf
%{_datadir}/dbus-1/system-services/org.mandrivalinux.MdvPkg.service
%{_datadir}/polkit-1/actions/org.mandrivalinux.mdvpkg.policy
%doc doc/* README TODO


%changelog
* Wed Aug 17 2011 Joao Victor Duarte Martins <jvdm@mandriva.com.br> 0.8.1-0
+ Revision: 695069
- Bugfix release 0.8.1
- Do not select orphans when selecting packages to remove.
- Fix bug when parsing urpmi.cfg (#63994).
- New release 0.8.0

  + Paulo Belloni <paulo@mandriva.com>
    - Upgrades to mdvpkg 0.7.0 (github)

* Thu Jun 30 2011 Eugeni Dodonov <eugeni@mandriva.com> 0.6.3-3
+ Revision: 688392
- Revert to 0.6.3 version

* Thu Jun 30 2011 Joao Victor Duarte Martins <jvdm@mandriva.com.br> 0.7.0-0
+ Revision: 688381
- Alpha release 0.7.0

* Sun Jun 12 2011 Eugeni Dodonov <eugeni@mandriva.com> 0.6.3-2
+ Revision: 684294
- Add require on python-pyinotify.

* Sat Jun 11 2011 Joao Victor Duarte Martins <jvdm@mandriva.com.br> 0.6.3-1
+ Revision: 684290
- Use distutils generated source

* Sat Jun 11 2011 Paulo Belloni <paulo@mandriva.com> 0.6.3-0
+ Revision: 684215
- Adding version 0.6.3 with the last changes made by JVDM. Attaching the tarball.
- Adding version 0.6.3 with the last changes made by JVDM.

  + Joao Victor Duarte Martins <jvdm@mandriva.com.br>
    - 0.6.2

* Wed Jun 01 2011 Joao Victor Duarte Martins <jvdm@mandriva.com.br> 0.5.4-2
+ Revision: 682379
+ rebuild (emptylog)

* Wed Jun 01 2011 Joao Victor Duarte Martins <jvdm@mandriva.com.br> 0.5.4-1
+ Revision: 682351
- 0.5.4
- Initial release
- Created package structure for mdvpkg.

