%include	/usr/lib/rpm/macros.php
%define         _class          HTML
%define         _subclass       Page
%define		_status		beta
%define		_pearname	%{_class}_%{_subclass}
Summary:	%{_pearname} - class for HTML page generation
Summary(pl):	%{_pearname} - klasa do generowania stron HTML
Name:		php-pear-%{_pearname}
Version:	1.0
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	405ccf44f0ba499154f98e65b4807a2b
URL:		http://pear.php.net/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The %{_pearname} class provides a simple interface for generating an
HTML page framework.
- META tag support (partial)
- support for linked stylesheets and scripts
- body can be a string, object with toHtml or toString methods or an
  array (can be combined)

This class has in PEAR status: %{_status}.

%description -l pl
Klasa %{_pearname} udostêpnia prosty interfejs do generowania stron
HTML.
- wsparcie dla tagów META (czê¶ciowe)
- wsparcie dla arkuszy stylów (CSS) i skryptów
- "cia³o" strony (body) mo¿e byæ ci±giem znaków, obiektem z metodami
  toHtml lub toString, albo tablic± (mo¿e byæ ³±czone)

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

install %{_pearname}-%{version}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{php_pear_dir}/%{_class}/*.php
