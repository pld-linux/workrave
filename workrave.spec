Summary:	Program that assists in the recovery and prevention of RSI
Summary(pl):	Program pomagaj±cy w rekonwalescencji i zapobieganiu RSI
Name:		workrave
Version:	1.0.0
Release:	0.9
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
URL:		http://workrave.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gnet-devel
BuildRequires:	gtkmm-devel >= 2.0
BuildRequires:	libsigc++-devel
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
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
