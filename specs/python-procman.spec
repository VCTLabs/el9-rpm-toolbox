# Tests are disabled in RHEL 9 because really old tox
# Specify --with tests to enable them.
%bcond_with tests

%global pypi_name procman

Name:           python-%{pypi_name}
Version:        0.6.2
Release:        1%{?dist}
Summary:        Console tool for running multiple external processes and multiplexing their output

License:        LGPL-2.1-or-later
URL:            http://github.com/sarnold/procman
Source0:        %{url}/releases/download/%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
Procman is a tool for running multiple external processes and multiplexing
their output to the console. It also cleans up and stops the whole stack
if any one of the running processes stops or dies on its own.

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

# these are runtime deps BUT rpmbuild expects them during build/check
BuildRequires:  python%{python3_pkgversion}-honcho
BuildRequires:  python%{python3_pkgversion}dist(importlib-resources)
BuildRequires:  python%{python3_pkgversion}dist(munch)
BuildRequires:  python%{python3_pkgversion}dist(ruamel-yaml)

%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

%description -n python%{python3_pkgversion}-%{pypi_name}
Procman is a tool for running multiple external processes and multiplexing
their output to the console. It also cleans up and stops the whole stack
if any one of the running processes stops or dies on its own.

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
%pyproject_save_files -l procman

# Use -t to only import top-level module
%check
%pyproject_check_import -t
%if %{with tests}
%pytest -vv test/
%endif

%files -n python%{python3_pkgversion}-procman -f %{pyproject_files}
%doc README.rst CHANGELOG.rst
%license COPYING REUSE.toml
%{_bindir}/procman

%changelog
* Thu Jul 31 2025 Stephen Arnold <nerdboy@gentoo.org> - 0.6.1
- prefix update
* Mon Jul 14 2025 Stephen Arnold <nerdboy@gentoo.org> - 0.6.0
- New package
