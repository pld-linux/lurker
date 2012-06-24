%define		mimelib_version 3.1.1
Summary:	E-mail archiver
Summary(pl):	Archiwizator poczty elektronicznej
Name:		lurker
Version:	0.8
Release:	1
License:	GPL
Group:		Applications/Mail
Source0:	http://cesnet.dl.sourceforge.net/sourceforge/lurker/%{name}-%{version}.tar.gz
# Source0-md5:	2f3e192a1a91b898a599ef10d212328c
Source1:	http://cesnet.dl.sourceforge.net/sourceforge/lurker/mimelib-%{mimelib_version}.tar.gz
# Source1-md5:	f50d492e9bae694b449033a188afb770
Patch0:		%{name}-www_path.patch
URL:		http://sourceforge.net/projects/lurker/
BuildRequires:	jam
BuildRequires:	libxslt-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         _datadir        /home/services/httpd

%description
An archiver which can handle extremely large amounts of email.
It is fast, intuitive, and customizable.

Noteworthy features;
    - Full field *fast* searching
    - Chronological threading
    - Message threading navigation
    - File attachment support
    - Multi-lingual support
    - Cache files available directly to the web server
    - Completely customizable output

%description -l pl
Szybki i intuicyjny archiwizator potrafi�cy poradzi� sobie z du��
ilo�ci� poczty elekronicznej.

Wa�niejsze cechy:
    - Szybkie pe�notekstowe przeszukiwanie
    - W�tkowanie
    - Obs�uga za��cznik�w
    - Obs�uga wielu j�zyk�w
    - Dowolnie formatowalny format wyj�ciowy

%prep
%setup -q -a 1
%patch0 -p1

%build
%configure --with-mimelib-local
jam

%install
rm -rf $RPM_BUILD_ROOT
DESTDIR=$RPM_BUILD_ROOT jam install


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README FAQ INSTALL
%attr(755,root,root) %{_bindir}/*
%{_sysconfdir}/%{name}.conf
%dir /var/lib/%{name}/
%dir %{_datadir}/html/%{name}/
%{_datadir}/html/%{name}/
%{_datadir}/cgi-bin/*
%{_mandir}/man1/*
