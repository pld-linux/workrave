#
# Conditional build:
%bcond_without	gnome		# build without GNOME support
#
Summary:	Program that assists in the recovery and prevention of RSI
Summary(pl):	Program pomagaj±cy w rekonwalescencji i zapobieganiu RSI
Name:		workrave
Version:	1.6.2
Release:	1
License:	GPL
Group:		X11/Applications
#Source0:	http://www.workrave.org/download/snapshots/20040429/workrave-src-20040429.tar.gz
Source0:	http://dl.sourceforge.net/workrave/%{name}-%{version}.tar.gz
# Source0-md5:	83c96c8eebf81fed8307a56dd1ee0905
URL:		http://www.workrave.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	doxygen
BuildRequires:	gdome2-devel
BuildRequires:	gettext-devel
BuildRequires:	gnet-devel >= 2.0.0
BuildRequires:	gtkmm-devel >= 2.4.0
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

%description -l pl
Workrave to program pomagaj±cy w rekonwalescencji i zapobieganiu RSI
(Repetitive Strain Injury - dolegliwo¶ciom spowodowanym powtarzaniem
tych samych czynno¶ci, najczê¶ciej podczas pracy przy komputerze).
Program czêsto przypomina o konieczno¶ci robienia krótkich pauz,
przerw na odpoczynek i ogranicza dzienny limit pracy.

%prep
%setup -q

%build
rm -f missing
%{__gettextize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%{!?with_gnome:--disable-gnome} \
	%{?with_gnome:--enable-gconf} \
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
