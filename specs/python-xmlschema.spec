%global pypi_name xmlschema
%global debug_package %{nil}

Name:           python-%{pypi_name}
Version:        3.4.2
Release:        6%{?dist}
Summary:        A Python XML Schema validator and decoder

License:        MIT
URL:            https://github.com/brunato/xmlschema
Source0:        %{pypi_source}
BuildArch:      noarch

%?python_enable_dependency_generator

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-setuptools
BuildRequires:  python3-tomli
BuildRequires:  python3-wheel
BuildRequires:  python3-pycparser
# these are declared dependencies
BuildRequires: python%{python3_pkgversion}dist(elementpath)

%global _description %{expand:
The xmlschema library is an implementation of XML Schema for Python.

This library arises from the needs of a solid Python layer for processing XML
Schema based files for MaX (Materials design at the Exascale) European project.
A significant problem is the encoding and the decoding of the XML data files
produced by different simulation software. Another important requirement is
the XML data validation, in order to put the produced data under control.
The lack of a suitable alternative for Python in the schema-based decoding
of XML data has led to build this library. Obviously this library can be
useful for other cases related to XML Schema based processing, not only for
the original scope.}

%description %_description

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}  %_description

%prep
%autosetup -p1 -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info
%py3_shebang_fix %{pypi_name}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%files -n python%{python3_pkgversion}-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}.dist-info/
%{_bindir}/xmlschema-*

%changelog
* Wed Sep 09 2026 Stephen Arnold <nerdboy@gentoo.org> - 3.4.5-6
- Rebuilt for Python 3.9 el9
