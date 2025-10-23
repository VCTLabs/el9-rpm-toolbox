%global pypi_name atomics

Name:           python-%{pypi_name}
Version:        1.0.3
Release:        1%{?dist}
Summary:        Atomic lock-free primitives
License:        GPL-3.0-or-later
URL:            https://github.com/doodspav/atomics
Source0:        %{pypi_source}

BuildRequires:  make
BuildRequires:  cmake
BuildRequires:  gcc

%?python_enable_dependency_generator

%description
This library implements a wrapper around the lower level patomic C
library. It exposes hardware level lock-free (and address-free) atomic
operations on a memory buffer, either internally allocated or
externally provided, via a set of atomic classes.

%package -n python3-%{pypi_name}
Summary:        Atomic lock-free primitives
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-wheel
BuildRequires:  python3-pycparser
BuildRequires:  python3-cffi
BuildRequires:  python3-GitPython
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
This library implements a wrapper around the lower level patomic C
library. It exposes hardware level lock-free (and address-free) atomic
operations on a memory buffer, either internally allocated or
externally provided, via a set of atomic classes.

%prep
%autosetup -p1 -n %{pypi_name}-%{version}

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%doc README.md ARCHITECTURE.md CHANGELOG.md
%license LICENSE.txt
%{python3_sitearch}/%{pypi_name}/
%{python3_sitearch}/dummy.*.so
%{python3_sitearch}/%{pypi_name}-%{version}-py%{python3_version}.egg-info/

%changelog
* Wed Oct 22 2025 Stephen Arnold <nerdboy@gentoo.org> - 1.0.3-1
- initial version
