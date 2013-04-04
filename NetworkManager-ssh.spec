%global commit dc9b4d596a67bc812267b52c9b5c3c7343c187c3
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global checkout 20130401git%{shortcommit}

Summary: NetworkManager VPN plugin for SSH
Name: NetworkManager-ssh
Version: 0.0.3
Release: 0.6.%{checkout}%{?dist}
License: GPLv2+
URL: https://github.com/danfruehauf/NetworkManager-ssh
Group: System Environment/Base
Source0: https://github.com/danfruehauf/NetworkManager-ssh/archive/%{commit}/%{name}-%{version}-%{shortcommit}.tar.gz

BuildRequires: autoconf
BuildRequires: gtk3-devel
BuildRequires: dbus-devel
BuildRequires: NetworkManager-devel
BuildRequires: NetworkManager-glib-devel
BuildRequires: glib2-devel
BuildRequires: libgnome-keyring-devel
BuildRequires: libtool intltool gettext
Requires: gtk3
Requires: dbus
Requires: NetworkManager
Requires: openssh-clients
Requires: shared-mime-info
Requires: gnome-keyring
%if 0%{?fedora} > 17
Requires: nm-connection-editor
%else
Requires: NetworkManager-gnome
%endif

%global _privatelibs libnm-ssh-properties[.]so.*
%global __provides_exclude ^(%{_privatelibs})$
%global __requires_exclude ^(%{_privatelibs})$

%description
This package contains software for integrating VPN capabilities with
the OpenSSH server with NetworkManager and the GNOME desktop.

%prep
%setup -q -n %{name}-%{version}

%build
if [ ! -f configure ]; then
  autoreconf -fvi
fi
%configure --disable-static --disable-dependency-tracking --enable-more-warnings=yes --with-gtkver=3
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} INSTALL="install -p" CP="cp -p" install

rm -f %{buildroot}%{_libdir}/NetworkManager/lib*.la

%find_lang %{name}

%files -f %{name}.lang

%doc COPYING AUTHORS README ChangeLog
%{_libdir}/NetworkManager/lib*.so*
%config(noreplace) %{_sysconfdir}/dbus-1/system.d/nm-ssh-service.conf
%config(noreplace) %{_sysconfdir}/NetworkManager/VPN/nm-ssh-service.name
%{_libexecdir}/nm-ssh-service
%{_libexecdir}/nm-ssh-auth-dialog
%dir %{_datadir}/gnome-vpn-properties/ssh
%{_datadir}/gnome-vpn-properties/ssh/nm-ssh-dialog.ui

%changelog
* Mon Apr 01 2013 Dan Fruehauf <malkodan@gmail.com> - 0.0.3-0.6.20130401gitdc9b4d5
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
