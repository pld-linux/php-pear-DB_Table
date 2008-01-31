%include	/usr/lib/rpm/macros.php
%define		_class		DB
%define		_subclass	Table
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - automate table creation
Summary(pl.UTF-8):	%{_pearname} - automatyzacja tworzenia tabel
Name:		php-pear-%{_pearname}
Version:	1.5.0
Release:	3
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	72e3f1a3fccf18c1d038886db8b4b969
URL:		http://pear.php.net/package/DB_Table/
BuildRequires:	php-pear-PEAR >= 1:1.6.1
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear
Requires:	php-pear-DB
Requires:	php-pear-Date
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# exclude optional dependencies
%define		_noautoreq	'pear(HTML/QuickForm.*)' 'pear(DB.*)' 'pear(MDB2.*)'

%description
Builds on PEAR DB to abstract datatypes and automate table creation,
data validation, insert, update, delete, and select; combines these
with PEAR HTML_QuickForm to automatically generate input forms that
match the table column definitions.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Klasa zbudowana na PEAR DB do wyabstrahowania typów danych i
zautomatyzowania tworzenia tabel, sprawdzania poprawności danych,
wstawiania, modyfikowania, usuwania i wybierania rekordów; łączy je
z PEAR HTML_QuickForm w celu automatycznego generowania formularzy
wejściowych pasujących do definicji kolumn tabel.

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl.UTF-8):	Testy dla PEAR::%{_pearname}
Group:		Development/Languages/PHP
Requires:	%{name} = %{version}-%{release}
AutoReq:	no
AutoProv:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl.UTF-8
Testy dla PEAR::%{_pearname}.


%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ -f %{_docdir}/%{name}-%{version}/optional-packages.txt ]; then
	cat %{_docdir}/%{name}-%{version}/optional-packages.txt
fi

%files
%defattr(644,root,root,755)
%doc install.log optional-packages.txt
%doc docs/%{_pearname}/docs/*
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/*
