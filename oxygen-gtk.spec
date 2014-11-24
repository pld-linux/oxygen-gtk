Summary:	Oxygen-Gtk - a port of the default KDE widget theme (Oxygen), to gtk
Name:		oxygen-gtk
Version:	1.4.6
Release:	1
License:	LGPL v2.1
Group:		Themes/GTK+
Source0:	ftp://ftp.kde.org/pub/kde/stable/oxygen-gtk2/%{version}/src/%{name}2-%{version}.tar.bz2
# Source0-md5:	493892fc36302bfe862604f667a6c04e
URL:		https://projects.kde.org/projects/playground/artwork/oxygen-gtk/
BuildRequires:	cairo-devel
BuildRequires:	cmake >= 2.8.0
BuildRequires:	dbus-glib-devel
BuildRequires:	gtk+2-devel >= 2.24.2
BuildRequires:	libstdc++-devel
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.600
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Oxygen-Gtk is a port of the default KDE widget theme (Oxygen), to gtk.

It's primary goal is to ensure visual consistency between gtk and
qt-based applications running under kde. A secondary objective is to
also have a stand-alone nice looking gtk theme that would behave well
on other Desktop Environments.

Unlike other attempts made to port the kde oxygen theme to gtk, this
attempt does not depend on Qt (via some Qt to Gtk conversion engine),
nor does render the widget appearance via hard coded pixmaps, which
otherwise breaks everytime some setting is changed in kde.

%prep
%setup -q -n %{name}2-%{version}

%build
install -d build
cd build
%cmake \
	../
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gtk-2.*/2.*.*/engines/liboxygen-gtk.so
%dir %{_datadir}/themes/oxygen-gtk
%dir %{_datadir}/themes/oxygen-gtk/gtk-2.*
%{_datadir}/themes/oxygen-gtk/gtk-2.*/argb-apps.conf
%{_datadir}/themes/oxygen-gtk/gtk-2.*/gtkrc
%{_datadir}/themes/oxygen-gtk/gtk-2.*/icons4
%{_datadir}/themes/oxygen-gtk/gtk-2.*/kdeglobals
%{_datadir}/themes/oxygen-gtk/gtk-2.*/oxygenrc
%dir %{_datadir}/themes/oxygen-gtk/gtk-2.*/special-icons
%{_datadir}/themes/oxygen-gtk/gtk-2.*/special-icons/standardbutton-closetab-16.png
%{_datadir}/themes/oxygen-gtk/gtk-2.*/special-icons/standardbutton-closetab-down-16.png
%{_datadir}/themes/oxygen-gtk/gtk-2.*/special-icons/standardbutton-closetab-hover-16.png
