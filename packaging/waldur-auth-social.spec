Name: waldur-auth-social
Summary: Waldur plugin for social authentication.
Group: Development/Libraries
Version: 0.7.2
Release: 1.el7
License: MIT
Url: http://waldur.com
Source0: %{name}-%{version}.tar.gz

Requires: waldur-core > 0.138.0

BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

BuildRequires: python-setuptools

Obsoletes: nodeconductor-auth-social

%description
Waldur plugin for social authentication.

%prep
%setup -q -n %{name}-%{version}

%build
%{__python} setup.py build

%install
rm -rf %{buildroot}
%{__python} setup.py install -O1 --root=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{python_sitelib}/*

%changelog
* Mon Jul 3 2017 Jenkins <jenkins@opennodecloud.com> - 0.7.2-1.el7
- New upstream release