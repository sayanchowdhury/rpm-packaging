# Generated by rust2rpm
%bcond_with check
%global debug_package %{nil}

%global crate erased-serde

Name:           rust-%{crate}
Version:        0.3.8
Release:        1%{?dist}
Summary:        Type-erased Serialize and Serializer traits

# Upstream license specification: MIT/Apache-2.0
License:        MIT or ASL 2.0
URL:            https://crates.io/crates/erased-serde
Source:         %{crates_source}
# Initial patched metadata
Patch0:         erased-serde-fix-metadata.diff

ExclusiveArch:  %{rust_arches}

BuildRequires:  rust-packaging
BuildRequires:  (crate(serde/default) >= 1.0.63 with crate(serde/default) < 2.0.0)
%if %{with check}
BuildRequires:  (crate(serde_cbor/default) >= 0.9.0 with crate(serde_cbor/default) < 0.10.0)
BuildRequires:  (crate(serde_derive/default) >= 1.0.0 with crate(serde_derive/default) < 2.0.0)
BuildRequires:  (crate(serde_json/default) >= 1.0.0 with crate(serde_json/default) < 2.0.0)
%endif

%global _description \
Type-erased Serialize and Serializer traits

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

%package     -n %{name}+unstable-debug-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+unstable-debug-devel %{_description}

This package contains library source intended for building other packages
which use "unstable-debug" feature of "%{crate}" crate.

%files       -n %{name}+unstable-debug-devel
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
* Mon Feb 11 2019 Sayan Chowdhury <sayanchowdhury@fedoraproject.org> - 0.3.8-1
- Initial package
