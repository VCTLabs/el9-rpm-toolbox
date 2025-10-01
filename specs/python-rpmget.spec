# Tests are disabled in RHEL 9 because really old tox
# Specify --with tests to enable them.
%bcond_with tests

%global pypi_name rpmget

Name:           python-%{pypi_name}
Version:        0.3.2
Release:        1%{?dist}
Summary:         A workflow helper to manage random sets of RPM package deps.

License:        MIT
URL:            http://github.com/sarnold/rpmget
Source0:        %{url}/releases/download/%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
RPMGet uses an ini-style config file to manage an arbitrary set of
development dependencies or releases as RPM packages. Either install
these packages in RHEL development environment or create a local
package repo.

%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python%{python3_pkgversion}dist(tomli)
BuildRequires:  python%{python3_pkgversion}dist(wheel)
BuildRequires:  python%{python3_pkgversion}dist(setuptools)
BuildRequires:  python%{python3_pkgversion}dist(setuptools-scm[toml])
# these are not really "extra"
BuildRequires:  python%{python3_pkgversion}dist(httpx)
BuildRequires:  python%{python3_pkgversion}dist(cerberus)
BuildRequires:  python%{python3_pkgversion}dist(munch)
BuildRequires:  python%{python3_pkgversion}dist(platformdirs)
BuildRequires:  python%{python3_pkgversion}dist(tqdm)
%if %{with tests}
BuildRequires:  python%{python3_pkgversion}dist(pytest)
%endif

%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

%description -n python%{python3_pkgversion}-%{pypi_name}
RPMGet uses an ini-style config file to manage an arbitrary set of
development dependencies or releases as RPM packages. Either install
these packages in RHEL development environment or create a local
package repo.

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
%pyproject_save_files -l rpmget

%check
%pyproject_check_import -e '*.export'
%if %{with tests}
%pytest -vv test/
%endif

%files -n python%{python3_pkgversion}-rpmget -f %{pyproject_files}
%doc README.rst CHANGELOG.rst
%license LICENSES REUSE.toml
%{_bindir}/*

%changelog
* Wed Oct 01 2025 Stephen Arnold <nerdboy@gentoo.org> - 0.3.2
- New package
