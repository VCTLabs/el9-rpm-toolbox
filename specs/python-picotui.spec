# Tests are disabled in RHEL 9 because really old tox
# Specify --with tests to enable them.
%bcond_with tests

%global pypi_name picotui

Name:           python-%{pypi_name}
Version:        1.2.3.1
Release:        1%{?dist}
Summary:        Lightweight, pure-Python Text User Interface (TUI) widget toolkit.

License:        LGPL-2.1-or-later
URL:            http://github.com/sarnold/picotui
Source0:        %{url}/releases/download/v%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
Picotui is a Text User Interface (TUI) widget library for Python3. It is
known to work with CPython3 and Pycopy (Unix version is officially supported
for the latter), but should work with any Python3 implementation which allows
access to the stdin/stdout file descriptors.

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
Picotui is a Text User Interface (TUI) widget library for Python3. It is
known to work with CPython3 and Pycopy (Unix version is officially supported
for the latter), but should work with any Python3 implementation which allows
access to the stdin/stdout file descriptors.

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
%pyproject_save_files -l picotui

# Use -t to only import top-level module
%check
%pyproject_check_import -t
%if %{with tests}
%pytest -vv test/
%endif

%files -n python%{python3_pkgversion}-picotui -f %{pyproject_files}
%doc README.rst CHANGELOG.rst
%license LICENSE REUSE.toml

%changelog
* Mon Jul 21 2025 Stephen Arnold <nerdboy@gentoo.org> - 1.2.3.1
- patch release for metadata fix
* Fri Jul 18 2025 Stephen Arnold <nerdboy@gentoo.org> - 1.2.3
- New package
