# TODO:
# - proper webapp config
%define	mimelib_version	3.1.1
Summary:	E-mail archiver
Summary(pl.UTF-8):	Archiwizator poczty elektronicznej
Name:		lurker
Version:	2.1
Release:	0.1
License:	GPL
Group:		Applications/Mail
Source0:	http://dl.sourceforge.net/lurker/%{name}-%{version}.tar.gz
# Source0-md5:	44e73a53e84e895a8a361ae27dcda6dd
Source1:       http://dl.sourceforge.net/lurker/mimelib-%{mimelib_version}.tar.gz
# Source1-md5: f50d492e9bae694b449033a188afb770
URL:		http://lurker.sourceforge.net/
BuildRequires:	libstdc++-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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

%description -l pl.UTF-8
Szybki i intuicyjny archiwizator potrafiący poradzić sobie z dużą
ilością poczty elektronicznej.

Ważniejsze cechy:
    - Szybkie pełnotekstowe przeszukiwanie
    - Wątkowanie
    - Obsługa załączników
    - Obsługa wielu języków
    - Dowolnie formatowalny format wyjściowy

%prep
%setup -q -a1

%build
%configure \
	--with-mimelib-local \
	--with-default-www-dir=%{_datadir}/%{name}/www \
	--with-cgi-bin-dir=%{_libdir}/%{name}/cgi-bin
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install install-config \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README FAQ INSTALL
%attr(755,root,root) %{_bindir}/*
%dir %{_sysconfdir}/%{name}
%config %{_sysconfdir}/%{name}/*.conf
%dir /var/lib/%{name}
%dir %{_datadir}/%{name}
# XXX: are all those http,http really necessary???
%attr(755,http,http) %{_datadir}/%{name}/www
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/cgi-bin
%attr(755,root,root) %{_libdir}/%{name}/cgi-bin/*
%{_mandir}/man1/*
