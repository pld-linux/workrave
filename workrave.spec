# TODO:
# - BRs check
#
# Conditional build:
%bcond_without	gnome		# build without GNOME support
#
Summary:	Program that assists in the recovery and prevention of RSI
Summary(pl):	Program pomagaj±cy w rekonwalescencji i zapobieganiu RSI
Name:		workrave
Version:	1.6.0
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/workrave/%{name}-%{version}.tar.gz
URL:		http://www.workrave.org/
Patch0:		workrave-libsigc20.patch
Patch1:		workrave-fakex.patch
BuildRequires:	GConf2-devel
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	GConf2-devel
BuildRequires:	gettext-devel
BuildRequires:	gtkmm-devel >= 2.1.0
BuildRequires:	libsigc++12-devel >= 1.2.0
BuildRequires:	pkgconfig
%if %{with gnome}
Buildrequires:	GConf2-devel >= 2.4.0
Buildrequires:	gdome2-devel
BuildRequires:	gnet-devel >= 2.0.0
BuildRequires:	gnome-panel-devel >= 2.4.0
BuildRequires:	libbonobo-devel >= 2.4.0
BuildRequires:	libgnomeuimm-devel >= 2.0.0
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
<<<<<<< workrave.spec
%setup -q -n workrave-1.6.0
%patch0 -p1
%patch1 -p1
=======
%setup -q
>>>>>>> 1.19

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
%attr(755,root,root) %{_libdir}/%{name}-applet
%{_libdir}/bonobo/servers/*
%{_sysconfdir}/sound/events/*
%{_datadir}/%{name}
%{_datadir}/gnome-2.0/ui/*
%{_datadir}/sounds/*
%{_pixmapsdir}/*
