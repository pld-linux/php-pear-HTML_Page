%include	/usr/lib/rpm/macros.php
%define         _class          HTML
%define         _subclass       Page
%define		_status		beta
%define		_pearname	%{_class}_%{_subclass}
%define		_ver		%{version}RC1
Summary:	%{_pearname} - base class for XHTML page generation
Summary(pl):	%{_pearname} - bazowa klasa do generowania stron XHTML
Name:		php-pear-%{_pearname}
Version:	2.0.0
Release:	0.RC1
License:	PHP 3.0
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{_ver}.tgz
# Source0-md5:	4e8dc4c7b85f4cc46896db660624a185
URL:		http://pear.php.net/package/HTML_Page/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
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

This class has in PEAR status: %{_status}.

%description -l pl
Klasa PEAR::HTML_Page udostêpnia prosty interfejs do generowania
zgodnych z XHTML stron.
- wspiera praktycznie wszystkie rodzaje doctype, od HTML 2.0 przez XHTML
  1.1 i XHTML Basic 1.0
Dodatkowo wstêpnie wsparcie dla XHTML 2.0
- wsparcie dla namespace
- globalna deklaracja jêzyka dla dokumentu
- rodzaje koñców linii
- pe³ne wsparcie dle znaczników META
- wsparcie dla deklaracji arkusza stylów w sekcji HEAD
- wsparcie dla pod³±czonych arkuszy stylów i skryptów
- cia³o dokumentu mo¿e byæ ci±giem znaków, obiektem z metodami toHtml
  b±d¼ toString lub tablic± (mo¿e byæ mieszane)

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}

install %{_pearname}-%{_ver}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}
install %{_pearname}-%{_ver}/%{_subclass}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{_ver}/examples
%dir %{php_pear_dir}/%{_class}/%{_subclass}
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}/*.php
