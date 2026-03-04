# Tests are disabled in RHEL 9 because really old tox
# Specify --with tests to enable them.
%bcond_with tests

%global pypi_name bitmaskfunctionalities

Name:           python-%{pypi_name}
Version:        1.2.2
Release:        1%{?dist}
Summary:        A precise and lightweight stopwatch built on top of perf_counter.

License:        MIT
URL:            https://github.com/AThieringer/BitMask
Source0:        %{pypi_source}
Patch0:         bitmask-1.2.2-rhel9.patch

BuildArch:      noarch

%description
A BitMask Python module providing a BitMask class for efficient
manipulation and representation of binary data as a fixed-length
sequence of bits. It allows initializing a bitmask with a specified
length and an optional starting value, provides methods for common
bitwise operations such as setting, resetting, and flipping individual
or all bits. Includes other useful functionalities for various
properties of the bitmask.

%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}dist(tomli)
BuildRequires:  python%{python3_pkgversion}dist(hatchling)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python%{python3_pkgversion}dist(typing-extensions)
%if %{with tests}
BuildRequires:  python%{python3_pkgversion}dist(pytest)
%endif

%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

%description -n python%{python3_pkgversion}-%{pypi_name}
A BitMask Python module providing a BitMask class for efficient
manipulation and representation of binary data as a fixed-length
sequence of bits. It allows initializing a bitmask with a specified
length and an optional starting value, provides methods for common
bitwise operations such as setting, resetting, and flipping individual
or all bits. Includes other useful functionalities for various
properties of the bitmask.

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
%pyproject_save_files -L BitMask

%check
%pyproject_check_import
%if %{with tests}
%pytest -vv test/
%endif

%files -n python%{python3_pkgversion}-bitmaskfunctionalities -f %{pyproject_files}
%doc README.md Changelog
%license LICENSE.txt

%changelog
* Tue Mar 03 2026 Stephen Arnold <nerdboy@gentoo.org> - 1.2.2
- New package
