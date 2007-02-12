%include	/usr/lib/rpm/macros.php
%define		_class		HTML
%define		_subclass	Page
%define		_status		beta
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - base class for XHTML page generation
Summary(pl.UTF-8):   %{_pearname} - bazowa klasa do generowania stron XHTML
Name:		php-pear-%{_pearname}
Version:	2.0.0
%define		_rc RC2
%define		_rel 3
Release:	0.%{_rc}.%{_rel}
License:	PHP 3.0
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}%{_rc}.tgz
# Source0-md5:	758e8b443836bdf353d3a891c01e9b27
URL:		http://pear.php.net/package/HTML_Page/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear
Requires:	php-pear-HTML_Common >= 1.2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The PEAR::HTML_Page package provides a simple interface for generating
an XHTML compliant page.
- supports virtually all HTML doctypes, from HTML 2.0 through XHTML 1.1
  and XHTML Basic 1.0
Plus preliminary support for XHTML 2.0
- namespace support
- global language declaration for the document
- line ending styles
- full META tag support
- support for stylesheet declaration in the head section
- support for linked stylesheets and scripts
- body can be a string, object with toHtml or toString methods or an
  array (can be combined)

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Klasa PEAR::HTML_Page udostępnia prosty interfejs do generowania
zgodnych z XHTML stron.
- wspiera praktycznie wszystkie rodzaje doctype, od HTML 2.0 przez XHTML
  1.1 i XHTML Basic 1.0
Dodatkowo wstępnie wsparcie dla XHTML 2.0
- wsparcie dla namespace
- globalna deklaracja języka dla dokumentu
- rodzaje końców linii
- pełne wsparcie dla znaczników META
- wsparcie dla deklaracji arkusza stylów w sekcji HEAD
- wsparcie dla podłączonych arkuszy stylów i skryptów
- ciało dokumentu może być ciągiem znaków, obiektem z metodami toHtml
  bądź toString lub tablicą (może być mieszane)

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%doc docs/%{_pearname}/examples
%dir %{php_pear_dir}/%{_class}/%{_subclass}
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}/*.php
