#
# Conditional build:
# _without_gnome - build without GNOME support
#
Summary:	Program that assists in the recovery and prevention of RSI
Summary(pl):	Program pomagaj±cy w rekonwalescencji i zapobieganiu RSI
Name:		workrave
Version:	1.4.0
Release:	2
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	d5bd1127b533b6d613335f7f240005ad
URL:		http://workrave.sourceforge.net/
BuildRequires:	GConf2-devel
BuildRequires:	autoconf
BuildRequires:	automake
%{!?_without_gnome:Buildrequires:	gdome2-devel}
BuildRequires:	gettext-devel
%{!?_without_gnome:BuildRequires:	gnet-devel >= 2.0.0}
%{!?_without_gnome:BuildRequires:	gnome-panel-devel >= 2.0.10}
BuildRequires:	gtkmm-devel >= 2.1.0
%{!?_without_gnome:BuildRequires:	libbonobo-devel >= 2.0.0}
%{!?_without_gnome:BuildRequires:	libgnomeuimm-devel}
BuildRequires:	libsigc++-devel >= 1.2.0
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
%{?_without_gnome:	--disable-gnome} \
%{!?_without_gnome:		--enable-gconf} \
	--enable-xml \
	--enable-exercises
	
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

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
