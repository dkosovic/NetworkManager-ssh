Summary: NetworkManager VPN plugin for SSH
Name: NetworkManager-ssh
Version: 1.2.6
Release: 1%{?dist}
License: GPLv2+
URL: https://github.com/danfruehauf/NetworkManager-ssh
Group: System Environment/Base
Source0: https://github.com/danfruehauf/NetworkManager-ssh/archive/1.2.6.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: autoconf
BuildRequires: gtk3-devel
BuildRequires: NetworkManager-devel
BuildRequires: NetworkManager-glib-devel >= 1:1.2.6
BuildRequires: NetworkManager-libnm-devel >= 1:1.2.6
BuildRequires: glib2-devel
BuildRequires: libtool intltool gettext
BuildRequires: libnm-gtk-devel >= 0.9.10
BuildRequires: libnma-devel >= 1.1.0
BuildRequires: libsecret-devel
BuildRequires: libtool intltool gettext
Requires: gtk3
Requires: dbus
Requires: NetworkManager >= 1:1.2.6
Requires: openssh-clients
Requires: shared-mime-info
Requires: sshpass

%global _privatelibs libnm-ssh-properties[.]so.*
%global __provides_exclude ^(%{_privatelibs})$
%global __requires_exclude ^(%{_privatelibs})$

%description
This package contains software for integrating VPN capabilities with
the OpenSSH server with NetworkManager.

%package -n NetworkManager-ssh-gnome
Summary: NetworkManager VPN plugin for SSH - GNOME files
Group: System Environment/Base
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: nm-connection-editor

%description -n NetworkManager-ssh-gnome
This package contains software for integrating VPN capabilities with
the OpenSSH server with NetworkManager (GNOME files).

%prep
%setup -q

%build
if [ ! -f configure ]; then
  autoreconf -fvi
fi
%if 0%{?rhel} == 7
CFLAGS="-DSECRET_API_SUBJECT_TO_CHANGE %{optflags}" \
%endif
%configure \
        --disable-static \
        --enable-more-warnings=yes \
        --with-dist-version=%{version}-%{release}
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} INSTALL="install -p" CP="cp -p" install

rm -f %{buildroot}%{_libdir}/NetworkManager/lib*.la

%find_lang %{name}

%files -f %{name}.lang
%{_sysconfdir}/dbus-1/system.d/nm-ssh-service.conf
%{_prefix}/lib/NetworkManager/VPN/nm-ssh-service.name
%{_libexecdir}/nm-ssh-service
%{_libexecdir}/nm-ssh-auth-dialog
%doc AUTHORS README ChangeLog NEWS
%license COPYING

%files -n NetworkManager-ssh-gnome
%{_libdir}/NetworkManager/lib*.so*
%dir %{_datadir}/gnome-vpn-properties/ssh
%{_sysconfdir}/NetworkManager/VPN/nm-ssh-service.name
%{_datadir}/gnome-vpn-properties/ssh/nm-ssh-dialog.ui
%{_datadir}/appdata/network-manager-ssh.metainfo.xml

%changelog
* Tue May 02 2017 Dan Fruehauf <malkodan@gmail.com> - 1.2.6-1
- Update to 1.2.6 release

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Sep 01 2016 Dan Fruehauf <malkodan@gmail.com> - 1.2.1-0
- Update to 1.2.1 release
- Fixed upstream #57 (Fedora #1350244) - Time out waiting for service

* Sat Apr 23 2016 Lubomir Rintel <lkundrak@v3.sk> - 1.2.0-1
- Update to 1.2.0 release

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-0.2.20151023git6a5c776
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Aug 31 2015 Lubomir Rintel <lkundrak@v3.sk> - 1.2.0-0.1.20151023git6a5c776
- Switch back to upstream source
- Fix build with the NetworkManager 1.2 snapshot

* Mon Aug 31 2015 Lubomir Rintel <lkundrak@v3.sk> - 1.2.0-0.1.20150831git2b4fb23
- Update to 1.2 git snapshot with libnm-based properties plugin

* Mon Jul 13 2015 Dan Fruehauf <malkodan@gmail.com> - 0.9.4-0.1.20150713git60f03fe
- Release 0.9.4

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.3-0.4.20140601git9d834f2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.3-0.3.20140601git9d834f2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.3-0.2.20140601git9d834f2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Jun 01 2014 Dan Fruehauf <malkodan@gmail.com> - 0.9.3-0.1.20140601git9d834f2
- Fixed GTK_STOCK deprecation errors
- Czech translation by Jiri Kilmes

* Sun Feb 09 2014 Dan Fruehauf <malkodan@gmail.com> - 0.9.2-0.2.20140209git46247c2
- Fixed upstream #25 (Fedora #1056810) - Bad strcmp usage
- Fixed upstream #27 (Fedora #1061365, #1058028) - sshpass via fd

* Sun Aug 11 2013 Dan Fruehauf <malkodan@gmail.com> - 0.9.1-0.5.20130706git6bf4649
- Added $RPM_OPT_FLAGS to CFLAGS

* Mon Aug 05 2013 Dan Fruehauf <malkodan@gmail.com> - 0.9.1-0.4.20130706git6bf4649
- Remove deprecated warning

* Fri Aug 02 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.1-0.3.20130706git6bf4649
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jul 06 2013 Dan Fruehauf <malkodan@gmail.com> - 0.9.1-0.2.20130706git6bf4649
- Depends on sshpass

* Sat Jul 06 2013 Dan Fruehauf <malkodan@gmail.com> - 0.9.1-0.1.20130706git6bf4649
- Support for password and plain key authentication 

* Tue Jun 25 2013 Dan Fruehauf <malkodan@gmail.com> - 0.0.4-0.1.20130625git241fee0
- Can choose to not set VPN as default route

* Fri Apr 19 2013 Dan Fruehauf <malkodan@gmail.com> - 0.0.3-0.8.20130419git3d5321b
- DBUS and NetworkManager files in /etc are no longer config files
- Other refactoring to conform with other NetworkManager VPN plugins

* Fri Apr 05 2013 Dan Fruehauf <malkodan@gmail.com> - 0.0.3-0.7.20130405git6ba59c4
- Added sub package for NetworkManager-ssh-gnome

* Tue Apr 02 2013 Dan Fruehauf <malkodan@gmail.com> - 0.0.3-0.6.20130402git6ba59c4
- Fixed dependencies (openssh-clients
- Added private libs

* Sat Mar 30 2013 Dan Fruehauf <malkodan@gmail.com> - 0.0.3-0.5.20130330git9afb20
- Removed macros from changelog

* Thu Mar 28 2013 Dan Fruehauf <malkodan@gmail.com> - 0.0.3-0.4.20130328gita2add30
- Fixed more issues in spec to conform with Fedora Packaging standards

* Tue Mar 26 2013 Dan Fruehauf <malkodan@gmail.com> - 0.0.3-0.3.20130326git7549f1d
- More changes to conform with Fedora packaging standards

* Fri Mar 22 2013 Dan Fruehauf <malkodan@gmail.com> - 0.0.3-0.2.20130322git8767415
- Changes to conform with Fedora packaging standards

* Wed Mar 20 2013 Dan Fruehauf <malkodan@gmail.com> - 0.0.3-0.1.20130320gitcf6c00f
- Initial spec release
