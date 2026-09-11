# Tests are disabled in RHEL 9 because really old tox
# Specify --with tests to enable them.
%bcond_with tests

%global pypi_name distro2sbom

Name:           python-%{pypi_name}
Version:        0.6.0.1
Release:        1%{?dist}
Summary:        Software Bill of Material (SBOM) generator and consumer library

License:        MIT
URL:            https://github.com/VCTLabs/distro2SBOM
Source0:        %{url}/releases/download/v%{version}/%{pypi_name}-%{version}.tar.gz

BuildArch:      noarch

%description
The DISTRO2SBOM generates a SBOM (Software Bill of Materials) for
either an installed application or a complete system installation in a
number of formats including SPDX and CycloneDX. An SBOM for an
installed package will identify all of its dependent components.

%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python%{python3_pkgversion}dist(tomli)
BuildRequires:  python%{python3_pkgversion}dist(wheel)
BuildRequires:  python%{python3_pkgversion}dist(setuptools)
BuildRequires:  python%{python3_pkgversion}dist(setuptools-scm[toml])
# these are not really "extra"
BuildRequires:  python%{python3_pkgversion}dist(importlib-resources)
BuildRequires:  python%{python3_pkgversion}dist(lib4sbom)
%if %{with tests}
BuildRequires:  python%{python3_pkgversion}dist(pytest)
%endif

%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

%description -n python%{python3_pkgversion}-%{pypi_name}
The DISTRO2SBOM generates a SBOM (Software Bill of Materials) for
either an installed application or a complete system installation in a
number of formats including SPDX and CycloneDX. An SBOM for an
installed package will identify all of its dependent components.

%prep
%autosetup -p1 -n %{pypi_name}-%{version}

# using pyproject macros
%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

# Use -l to assert a %%license file is found (PEP 639).
# note the last argument is the top-level module directory name
%pyproject_save_files -l distro2sbom

%check
%pyproject_check_import -e '*.export'
%if %{with tests}
%pytest -vv test/
%endif

%files -n python%{python3_pkgversion}-distro2sbom -f %{pyproject_files}
%doc README.md CONTRIBUTING.md
%license LICENSE
%{_bindir}/*

%changelog
* Wed Sep 09 2026 Stephen Arnold <nerdboy@gentoo.org> - 0.6.0.1-1
- New package
