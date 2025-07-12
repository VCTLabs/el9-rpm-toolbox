# Tests are disabled in RHEL 9 because really old tox
# Specify --with tests to enable them.
%bcond_with tests

%global pypi_name tftpy

Name:           python-%{pypi_name}
Version:        0.8.6.1
Release:        1%{?dist}
Summary:        A pure python TFTP library

License:        MIT
URL:            http://github.com/VCTLabs/tftpy
Source0:        %{url}/releases/download/%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
This module is a pure Python implementation of the TFTP protocol, RFCs 1350,
2347, 2348 and the tsize option from 2349.

%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}dist(wheel)
BuildRequires:  python%{python3_pkgversion}dist(setuptools)
%if %{with tests}
BuildRequires:  python%{python3_pkgversion}dist(pytest)
%endif

%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

%description -n python%{python3_pkgversion}-%{pypi_name}
This module is a pure Python implementation of the TFTP protocol, RFCs 1350,
2347, 2348 and the tsize option from 2349.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
%if %{with tests}
%pytest -vv tests/
%endif

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md ChangeLog.md
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py*.egg-info/
%{_bindir}/*.py

%changelog
* Fri Jul 11 2025 Stephen Arnold <nerdboy@gentoo.org> - 0.8.6
- New package
