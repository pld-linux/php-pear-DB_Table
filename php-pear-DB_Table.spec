%include	/usr/lib/rpm/macros.php
%define		_class		DB
%define		_subclass	Table
%define		_status		alpha
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - automate table creation
Summary(pl):	%{_pearname} - automatyzacja tworzenia tabel
Name:		php-pear-%{_pearname}
Version:	0.22.0
Release:	2
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	33bbfc99239e4d8ab8957a9065aada86
URL:		http://pear.php.net/package/DB_Table/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Builds on PEAR DB to abstract datatypes and automate table creation,
data validation, insert, update, delete, and select; combines these
with PEAR HTML_QuickForm to automatically generate input forms that
match the table column definitions.

In PEAR status of this package is: %{_status}.

%description -l pl
Klasa zbudowana na PEAR DB do wyabstrahowania typów danych i
zautomatyzowania tworzenia tabel, sprawdzania poprawno¶ci danych,
wstawiania, modyfikowania, usuwania i wybierania rekordów; ³±czy je
z PEAR HTML_QuickForm w celu automatycznego generowania formularzy
wej¶ciowych pasuj±cych do definicji kolumn tabel.

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}

install %{_pearname}-%{version}/%{_class}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}
install %{_pearname}-%{version}/%{_class}/%{_subclass}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}/{docs,tests}
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}
