%define		mimelib_version 3.1.1
Summary:	email archiver
Summary(pl):	archiwizator emaili
Name:		lurker
Version:	0.8
Release:	1
License:	GPL
Group:		Applications/Mail
Source0:	http://cesnet.dl.sourceforge.net/sourceforge/lurker/%{name}-%{version}.tar.gz
Source1:	http://cesnet.dl.sourceforge.net/sourceforge/lurker/mimelib-%{mimelib_version}.tar.gz
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


%prep
%setup -q -n %{name}-%{version} -a 1
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
%doc ChangeLog README FAQ
%attr(755,root,root) %{_bindir}/*
%{_sysconfdir}/%{name}.conf
%dir /var/lib/%{name}/
%dir %{_datadir}/html/%{name}/
%{_datadir}/html/%{name}/
%{_datadir}/cgi-bin/*
%{_mandir}/man1/*

#%{_datadir}/%{name}
