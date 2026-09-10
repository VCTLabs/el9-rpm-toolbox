%global pypi_name elementpath
%global debug_package %{nil}

Name:           python-%{pypi_name}
Version:        4.8.0
Release:        7%{?dist}
Summary:        XPath 1.0/2.0 parsers and selectors for ElementTree and lxml

License:        MIT
URL:            https://github.com/sissaschool/elementpath
Source0:        %{pypi_source}

%?python_enable_dependency_generator

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-wheel
BuildRequires:  python3-pycparser

%global _description %{expand:
The proposal of this package is to provide XPath 1.0, 2.0 and 3.0 selectors for
Python's ElementTree XML data structures, both for the standard ElementTree
library and for the lxml.etree library.

For lxml.etree this package can be useful for providing XPath 2.0 selectors,
because lxml.etree already has it's own implementation of XPath 1.0.}

%description %_description

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}  %_description

%prep
%autosetup -p1 -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%doc README.rst
%license LICENSE
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py*.egg-info/

%changelog
* Wed Sep 09 2026 Stephen Arnold <nerdboy@gentoo.org> - 4.8.0-7
- initial version
