# Tests are disabled in RHEL 9 because really old tox
# Specify --with tests to enable them.
%bcond_with tests

%global pypi_name lib4sbom

Name:           python-%{pypi_name}
Version:        0.10.4.1
Release:        1%{?dist}
Summary:        Software Bill of Material (SBOM) generator and consumer library

License:        MIT
URL:            https://github.com/VCTLabs/lib4sbom
Source0:        %{url}/releases/download/v%{version}/%{pypi_name}-%{version}.tar.gz

BuildArch:      noarch

%description
Lib4SBOM is a library to parse and generate Software Bill of Materials
(SBOMs). It supports SBOMs created in both SPDX and CycloneDX formats.
It has been developed on the assumption that having a generic
abstraction of SBOM independent of the underlying format will be useful
to developers.

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
BuildRequires:  python%{python3_pkgversion}dist(pyyaml)
BuildRequires:  python%{python3_pkgversion}dist(semantic-version)
BuildRequires:  python%{python3_pkgversion}dist(defusedxml)
BuildRequires:  python%{python3_pkgversion}dist(fastjsonschema)
BuildRequires:  python%{python3_pkgversion}dist(jsonschema)
BuildRequires:  python%{python3_pkgversion}dist(xmlschema)
BuildRequires:  python%{python3_pkgversion}dist(packageurl-python)
%if %{with tests}
BuildRequires:  python%{python3_pkgversion}dist(pytest)
%endif

%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

%description -n python%{python3_pkgversion}-%{pypi_name}
Lib4SBOM is a library to parse and generate Software Bill of Materials
(SBOMs). It supports SBOMs created in both SPDX and CycloneDX formats.
It has been developed on the assumption that having a generic
abstraction of SBOM independent of the underlying format will be useful
to developers.

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
%pyproject_save_files -l lib4sbom

%check
%pyproject_check_import -e '*.export'
%if %{with tests}
%pytest -vv test/
%endif

%files -n python%{python3_pkgversion}-lib4sbom -f %{pyproject_files}
%doc README.md CONTRIBUTING.md
%license LICENSE

%changelog
* Wed Sep 09 2026 Stephen Arnold <nerdboy@gentoo.org> - 0.10.4-1
- New package
