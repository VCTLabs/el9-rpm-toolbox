# Tests are disabled in RHEL 9 because really old tox
# Specify --with tests to enable them.
%bcond_with tests

%global pypi_name pyprctl

Name:           python-%{pypi_name}
Version:        0.1.3
Release:        1%{?dist}
Summary:        An interface to the Linux prctl() system call and capabilities.

License:        MIT
URL:            https://pyprctl.readthedocs.io/en/latest
Source0:        %{pypi_source}
BuildArch:      noarch

%description
An interface to the Linux prctl() system call (and Linux capabilities in
general) written in pure Python using ctypes.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
An interface to the Linux prctl() system call (and Linux capabilities in
general) written in pure Python using ctypes.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
%if %{with tests}
%{__python3} setup.py test
%endif

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py*.egg-info/

%changelog
* Thu Jul 17 2025 Stephen Arnold <nerdboy@gentoo.org> - 0.1.3
- Initial package
