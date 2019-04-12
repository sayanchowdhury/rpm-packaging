# Generated by rust2rpm
%bcond_without check
%global debug_package %{nil}

%global crate pnet_sys

Name:           rust-%{crate}
Version:        0.22.0
Release:        1%{?dist}
Summary:        Access to network related system function and calls

# Upstream license specification: MIT/Apache-2.0
License:        MIT or ASL 2.0
URL:            https://crates.io/crates/pnet_sys
Source:         %{crates_source}
Patch0:		remove-windows-dependencies.patch

ExclusiveArch:  %{rust_arches}

BuildRequires:  rust-packaging
BuildRequires:  (crate(libc/default) >= 0.2.39 with crate(libc/default) < 0.3.0)

%global _description \
Access to network related system function and calls.

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%{cargo_registry}/%{crate}-%{version}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif

%changelog
* Wed Apr 10 2019 Sayan Chowdhury <sayanchowdhury@fedoraproject.org> - 0.22.0-1
- Initial package
