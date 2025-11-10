# Tests are disabled in RHEL 9 because really old tox
# Specify --with tests to enable them.
%bcond_with tests

%global srcname logwatcher

Name:           python-%{srcname}
Version:        0.5.3
Release:        1%{?dist}
Summary:        Real-time log file watcher supporting log rotation.

License:        MIT
URL:            https://github.com/sarnold/pylogtailer
Source0:        %{url}/releases/download/v%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires: python%{python3_pkgversion}-devel
BuildRequires: pyproject-rpm-macros
BuildRequires: python%{python3_pkgversion}dist(tomli)
BuildRequires: python%{python3_pkgversion}dist(wheel)
BuildRequires: python%{python3_pkgversion}dist(setuptools)
BuildRequires: python%{python3_pkgversion}dist(setuptools-scm[toml])
%if %{with tests}
BuildRequires:  python%{python3_pkgversion}dist(pytest)
%endif

%description
A python class that "watches" a directory and calls a user-supplied
callback(filename, lines) function every time one of the watched files
gets written to, in real time. Similar to tail, it takes care of
"watching" new files which are created after initialization and
"unwatching" those which are removed in the meantime. This means you'll
be able to "follow" and support also rotating log files.

%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}

%description -n python%{python3_pkgversion}-%{srcname}
A python class that "watches" a directory and calls a user-supplied
callback(filename, lines) function every time one of the watched files
gets written to, in real time. Similar to tail, it takes care of
"watching" new files which are created after initialization and
"unwatching" those which are removed in the meantime. This means you'll
be able to "follow" and support also rotating log files.

%prep
%autosetup -p1 -n %{srcname}-%{version}

# using pyproject macros
%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

# Use -l to assert a %%license file is found (PEP 639).
# note the last argument is the top-level module directory name
%pyproject_save_files -l logwatcher

%check
%pyproject_check_import
%if %{with tests}
%pytest -vv test/
%endif

%files -n python%{python3_pkgversion}-logwatcher -f %{pyproject_files}
%doc README.rst CHANGELOG.rst
%license LICENSES REUSE.toml

%changelog
* Sat Nov 08 2025 Stephen Arnold <nerdboy@gentoo.org> - v0.5.1
- Initial package
