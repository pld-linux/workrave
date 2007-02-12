#
# Conditional build:
%bcond_without	gnome		# build without GNOME support
%bcond_with	kde		# KDE support
#
Summary:	Program that assists in the recovery and prevention of RSI
Summary(pl.UTF-8):   Program pomagający w rekonwalescencji i zapobieganiu RSI
Name:		workrave
Version:	1.8.1
Release:	0.1
License:	GPL
Group:		X11/Applications
#Source0:	http://www.workrave.org/download/snapshots/20040429/workrave-src-20040429.tar.gz
Source0:	http://dl.sourceforge.net/workrave/%{name}-%{version}.tar.gz
# Source0-md5:	3a22ef8488fc2c9fe3b02f9c33b1cfb2
URL:		http://www.workrave.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	dbus-devel
BuildRequires:	doxygen
BuildRequires:	gdome2-devel
BuildRequires:	gettext-devel
BuildRequires:	gnet-devel >= 2.0.0
BuildRequires:	gtkmm-devel >= 2.4.0
%if %{with kde}
BuildRequires:	kdelibs-devel
%endif
BuildRequires:	libsigc++-devel >= 2.0.0
BuildRequires:	pkgconfig
%if %{with gnome}
BuildRequires:	GConf2-devel >= 2.4.0
BuildRequires:	ORBit2-devel >= 2.8.3
BuildRequires:	gnome-panel-devel >= 2.4.0
BuildRequires:	libbonobo-devel >= 2.4.0
BuildRequires:	libgnomeuimm-devel >= 2.8.0
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Workrave is a program that assists in the recovery and prevention of
Repetitive Strain Injury (RSI). The program frequently alerts you to
take micro-pauses, rest breaks and restricts you to your daily limit.

%description -l pl.UTF-8
Workrave to program pomagający w rekonwalescencji i zapobieganiu RSI
(Repetitive Strain Injury - dolegliwościom spowodowanym powtarzaniem
tych samych czynności, najczęściej podczas pracy przy komputerze).
Program często przypomina o konieczności robienia krótkich pauz,
przerw na odpoczynek i ogranicza dzienny limit pracy.

%prep
%setup -q

%build
rm -f missing
%{__gettextize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--%{?with_gnome:en}%{!?with_gnome:dis}able-gnome \
	--%{?with_gnome:en}%{!?with_gnome:dis}able-gconf \
	--%{?with_kde:en}%{!?with_kde:dis}able-kde \
	--enable-dbus \
	--enable-xml \
	--enable-exercises

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{_bindir}/*
%{_sysconfdir}/sound/events/*
%{_datadir}/%{name}
%{_datadir}/sounds/*
%{_pixmapsdir}/*
%if %{with gnome}
%attr(755,root,root) %{_libdir}/%{name}-applet
%{_libdir}/bonobo/servers/*
%{_datadir}/gnome-2.0/ui/*
%endif
