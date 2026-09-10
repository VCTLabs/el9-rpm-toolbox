%global pypi_name packageurl-python

Name:           python-%{pypi_name}
Version:        0.16.0
Release:        1%{?dist}
Summary:        Python implementation of the package url spec

License:        MIT
URL:            https://github.com/package-url/packageurl-python
Source:         %url/archive/v%{version}/%{pypi_name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python%{python3_pkgversion}dist(tomli)
BuildRequires:  python%{python3_pkgversion}dist(wheel)
BuildRequires:  python%{python3_pkgversion}dist(setuptools)
BuildRequires:  python%{python3_pkgversion}dist(setuptools-scm[toml])
BuildRequires:  python3dist(pytest)

%global common_description %{expand:
A parser and builder for purl aka. Package URLs for Python 2 and 3. See
https://github.com/package-url/purl-spec for details.}

%description %{common_description}

%package -n python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name} %{common_description}

%prep
%autosetup -p1 -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files packageurl

%check
%pytest

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc AUTHORS.rst CHANGELOG.rst CONTRIBUTING.rst README.rst
%license mit.LICENSE

%changelog
* Sun Apr 06 2025 Robert-André Mauchin <zebob.m@gmail.com> - 0.16.0-1
- Update to 0.16.0

* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.15.0-2
- Rebuilt for Python 3.13

* Wed May 22 2024 Robert-André Mauchin <zebob.m@gmail.com> - 0.15.0-1
- Update to 0.15.0

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Oct 15 2023 Robert-André Mauchin <zebob.m@gmail.com> - 0.11.2-1
- Initial import
