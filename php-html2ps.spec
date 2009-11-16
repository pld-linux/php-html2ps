Summary:	PHP LIbrary to render pages as PDF documents or PostScript files
Name:		php-html2ps
Version:	2.0.43
Release:	0.1
License:	LGPL 2.1
Group:		Development/Languages/PHP
Source0:	http://dl.sourceforge.net/project/html2ps/html2ps/html2ps-%{version}/html2ps-%{version}.zip
# Source0-md5:	2bd43d519ae7738d091dd66c41895ec4
URL:		http://www.tufat.com/html2ps.php
BuildRequires:	rpmbuild(macros) >= 1.461
BuildRequires:	unzip
Requires:	php(gd)
Requires:	php-common >= 3:4.3.0
Suggests:	php(domxml)
Suggests:	php(zlib)
Suggests:	php-activelink-xml
Suggests:	php-pecl-pdflib
Suggests:	php(iconv)
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir			%{php_data_dir}/html2ps
%define		_phpdocdir		%{_docdir}/phpdoc

%description
html2ps is a PHP equivalent of the popular Perl script by the same
name that accurately converts HTML with images, complex tables
(including rowspan/colspan), layers/divs, and CSS styles to Postscript
and PDF.

Unlike most other HTML2PS/HTML2PDF converters, it offers good CSS 2.1
support and is very tolerant to non-valid HTML.

%package phpdoc
Summary:	Online manual for %{name}
Summary(pl.UTF-8):	Dokumentacja online do %{name}
Group:		Documentation
Requires:	php-dirs

%description phpdoc
Documentation for %{name}.

%description phpdoc -l pl.UTF-8
Dokumentacja do %{name}.

%prep
%setup -q -n html2ps-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_appdir},%{_examplesdir}/%{name}-%{version},%{_phpdocdir}/%{name}}
cp -a *.php $RPM_BUILD_ROOT%{_appdir}
cp -a classes data destinations features postscript templates $RPM_BUILD_ROOT%{_appdir}
cp -a demo samples $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a help/* $RPM_BUILD_ROOT%{_phpdocdir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog TODO
%{_appdir}
%{_examplesdir}/%{name}-%{version}

%files phpdoc
%defattr(644,root,root,755)
%{_phpdocdir}/%{name}
