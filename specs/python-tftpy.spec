# Tests are disabled in RHEL 9 because really old tox
# Specify --with tests to enable them.
%bcond_with tests

%global pypi_name tftpy

Name:           python-%{pypi_name}
Version:        0.8.6.2
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
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python%{python3_pkgversion}dist(tomli)
BuildRequires:  python%{python3_pkgversion}dist(wheel)
BuildRequires:  python%{python3_pkgversion}dist(setuptools)
BuildRequires:  python%{python3_pkgversion}dist(setuptools-scm[toml])
%if %{with tests}
BuildRequires:  python%{python3_pkgversion}dist(pytest)
%endif

%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

%description -n python%{python3_pkgversion}-%{pypi_name}
This module is a pure Python implementation of the TFTP protocol, RFCs 1350,
2347, 2348 and the tsize option from 2349.

%prep
%autosetup -p1 -n %{pypi_name}-%{version}

# using pyproject macros
%generate_buildrequires
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_buildrequires

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_wheel

%install
%pyproject_install

# Use -l to assert a %%license file is found (PEP 639).
# note the last argument is the top-level module directory name
%pyproject_save_files -l tftpy

%check
%pyproject_check_import
%if %{with tests}
%pytest -vv test/
%endif

%files -n python%{python3_pkgversion}-tftpy -f %{pyproject_files}
%doc README.md ChangeLog.md
%license LICENSE
%{_bindir}/*.py

%changelog
* Tue Aug 19 2025 Stephen Arnold <nerdboy@gentoo.org> - 0.8.6.2
- New upstream release
* Sat Jul 12 2025 Stephen Arnold <nerdboy@gentoo.org> - 0.8.6.1
- New package
