%include	/usr/lib/rpm/macros.php
%define         _class          HTML
%define         _subclass       Page
%define		_status		beta
%define		_pearname	%{_class}_%{_subclass}
%define		_ver		%{version}b4
Summary:	%{_pearname} - class for HTML page generation
Summary(pl):	%{_pearname} - klasa do generowania stron HTML
Name:		php-pear-%{_pearname}
Version:	2.0.0
Release:	0.b4
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{_ver}.tgz
# Source0-md5:	46f824abbfb9678855c08df4a75d7b92
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
