%{?scl:%scl_package nodejs-jsprim}
%{!?scl:%global pkg_name %{name}}
%{?nodejs_find_provides_and_requires}

%global enable_tests 0
%global npm_name jsprim

Name:       %{?scl_prefix}nodejs-%{npm_name}
Version:    1.2.2
Release:    2%{?dist}
Summary:    utilities for primitive JavaScript types
License:    MIT
URL:        https://github.com/davepacheco/node-jsprim
Source0:    http://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
BuildRequires: %{?scl_prefix}nodejs-devel
BuildArch:  noarch
ExclusiveArch: %{nodejs_arches} noarch

%description
utilities for primitive JavaScript types

%prep
%setup -q -n package

rm -rf node_modules

%nodejs_fixdep extsprintf
%nodejs_fixdep json-schema
%nodejs_fixdep verror

%build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr lib package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}
# If any binaries are included, symlink them to bindir here


%nodejs_symlink_deps

%if 0%{?enable_tests}
%check
#not running tests in RHSCL
%endif

%files
%{nodejs_sitelib}/%{npm_name}

%doc LICENSE
%doc README.md

%changelog
* Tue Sep 20 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.2.2-2
- Initial build

